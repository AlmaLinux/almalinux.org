#!/usr/bin/env python3
"""
Script to generate get_almalinux_checksums.yaml by fetching and parsing ISO and cloud image checksum files.
"""
import re
from pathlib import Path
from typing import Dict, Optional, Tuple

import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
SPEC_FILE = DATA_DIR / "get_almalinux_spec.yaml"
OUTPUT_FILE = DATA_DIR / "get_almalinux_checksums.yaml"

VERSION_REGEX = r"[0-9.]+"

def build_filename_pattern(template: str, replacements: Dict[str, str], version_regex: str) -> str:
    """
    Escape the template, then replace placeholders and {full} with regex.
    Args:
        template: The filename template string (e.g. from iso_base or image_url_tpl)
        replacements: Dict of placeholder replacements (e.g. {arch}, {major}, {variant})
        version_regex: Regex string to use for {full}
    Returns:
        Regex pattern string for matching filenames
    """
    for key, value in replacements.items():
        template = template.replace(f"{{{key}}}", value)
    pat = re.escape(template)
    pat = pat.replace(re.escape("{full}"), version_regex)
    return pat

def parse_iso_checksum(content: str, filename_patterns: Dict[str, str]) -> Tuple[Dict[str, str], Optional[str]]:
    """
    Parse ISO checksum file content and extract checksums and version.
    Args:
        content: The text content of the checksum file
        filename_patterns: Dict of variant to regex pattern
    Returns:
        (checksums dict, extracted version or None)
    """
    checksums = {}
    extracted_version = None
    for line in content.splitlines():
        m = re.match(r"SHA256 \(([^)]+)\) = ([a-f0-9]{64})", line)
        if m:
            fname, sha = m.groups()
            for variant, pattern in filename_patterns.items():
                if re.fullmatch(pattern, fname):
                    checksums[variant] = sha
                    # Only extract version for accepted files
                    ver_match = re.match(rf".*-({VERSION_REGEX})-[^-]+-[^-]+\.iso$", fname)
                    if ver_match:
                        extracted_version = ver_match.group(1)
    return checksums, extracted_version

def parse_cloud_checksum(content: str, filename_patterns: Dict[str, str]) -> Dict[str, str]:
    """
    Parse cloud image checksum file content and extract checksums.
    Args:
        content: The text content of the checksum file
        filename_patterns: Dict of image type to regex pattern
    Returns:
        checksums dict
    """
    checksums = {}
    for line in content.splitlines():
        m = re.match(r"([a-f0-9]{64})\s+([^.\s]+.*)", line)
        if m:
            sha, fname = m.groups()
            for image_type, pattern in filename_patterns.items():
                if re.fullmatch(pattern, fname):
                    checksums[image_type] = sha
    return checksums

def get_checksum_file(url: str) -> str:
    """
    Fetch the checksum file from the given URL.
    Args:
        url: The URL to fetch
    Returns:
        The text content of the checksum file
    Raises:
        Exception if the request fails
    """
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"Error fetching {url}: {e}", flush=True)
        raise

def main():
    with open(SPEC_FILE) as f:
        spec = yaml.safe_load(f)

    output = {"versions": {}}
    common = spec["common"]

    for version in spec["versions"]:
        vid = version["id"]
        output["versions"][vid] = {}
        # Make sure fullVersion ends up at the top
        output["versions"][vid]["fullVersion"] = None
        arches = version.get("arches", [])
        sections = version.get("sections", {})
        # ISO section
        iso_section = sections.get("iso")
        if iso_section is None:
            iso_section = {}
        iso_common = common["iso"]
        iso_base = iso_section.get("base", iso_common["base"])
        iso_checksum_url_tpl = iso_section.get("checksumUrl", iso_common["checksumUrl"])
        iso_variants = iso_section.get("variants", iso_common["variants"])
        for arch in arches:
            if arch not in output["versions"][vid]:
                output["versions"][vid][arch] = {}
            # Compose checksum URL
            iso_checksum_url = iso_checksum_url_tpl.format(major=vid, full=vid, arch=arch)
            try:
                content = get_checksum_file(iso_checksum_url)
            except Exception:
                continue
            # Build filename patterns for each variant using the base template
            filename_patterns = {}
            iso_base_filename = Path(iso_base).name
            for variant in iso_variants:
                replacements = {"major": vid, "arch": arch, "variant": variant}
                fname_pat = build_filename_pattern(iso_base_filename, replacements, VERSION_REGEX)
                filename_patterns[variant] = fname_pat
            checksums, extracted_version = parse_iso_checksum(content, filename_patterns)
            if checksums:
                output["versions"][vid][arch]["iso"] = checksums
            if extracted_version:
                output["versions"][vid]["fullVersion"] = extracted_version

        # Remove fullVersion if not set
        if not output["versions"][vid]["fullVersion"]:
            del output["versions"][vid]["fullVersion"]

        # Cloud section
        cloud_section = sections.get("cloud")
        if cloud_section is None:
            cloud_section = {}
        cloud_common = common["cloud"]
        for cloud_type in ["genericCloud", "openNebula"]:
            csec = cloud_section.get(cloud_type, cloud_common.get(cloud_type, {}))
            if not csec:
                continue
            arches = cloud_section.get("arches", arches)
            checksum_url_tpl = csec.get("checksumUrl", cloud_common[cloud_type]["checksumUrl"])
            image_url_tpl = csec.get("imageUrl", cloud_common[cloud_type]["imageUrl"])
            for arch in arches:
                checksum_url = checksum_url_tpl.format(major=vid, arch=arch)
                try:
                    content = get_checksum_file(checksum_url)
                except Exception:
                    continue
                # Build filename patterns
                patterns = {}
                image_base_filename = Path(image_url_tpl).name
                replacements = {"major": vid, "arch": arch}
                fname_pat = build_filename_pattern(image_base_filename, replacements, VERSION_REGEX)
                patterns[cloud_type] = fname_pat
                checksums = parse_cloud_checksum(content, patterns)
                if checksums:
                    if "cloud" not in output["versions"][vid][arch]:
                        output["versions"][vid][arch]["cloud"] = {}
                    output["versions"][vid][arch]["cloud"].update(checksums)

    with open(OUTPUT_FILE, "w") as f:
        # We'll output the yaml to a string first so we can replace the
        # single quotes for double quotes just like Prettier wants it.
        yaml_str = yaml.dump(output, sort_keys=False)
        yaml_str = yaml_str.replace("'", '"')
        f.write(yaml_str)
    print(f"Wrote {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
