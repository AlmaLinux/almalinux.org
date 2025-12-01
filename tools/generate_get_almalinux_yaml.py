#!/usr/bin/env python3
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

SPEC_PATH = DATA_DIR / "get_almalinux_spec.yaml"
CHECKSUMS_PATH = DATA_DIR / "get_almalinux_checksums.yaml"
OUTPUT_PATH = DATA_DIR / "get_almalinux.yaml"

# Optional, human-friendly labels for known arches. Falls back to ID when missing.
ARCH_LABELS = {
    "x86_64": "x86_64",
    "x86_64_v2": "x86_64 v2",
    "aarch64": "aarch64",
    "s390x": "s390x",
    "ppc64le": "ppc64le",
}


def load_yaml(path):
    if not path.exists():
        print(f"Missing YAML file: {path}", file=sys.stderr)
        sys.exit(1)
    return yaml.safe_load(path.read_text())


def deep_merge_dict(base: dict, override: dict) -> dict:
    """Recursively merge two dicts, with override winning on conflicts.

    Values from ``override`` take precedence. Nested dicts are merged
    recursively; all other values are replaced wholesale.
    """

    if not isinstance(base, dict):
        base = {}
    if not isinstance(override, dict):
        return dict(base)

    result: dict = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge_dict(result[key], value)
        else:
            result[key] = value
    return result


def get_pattern_arches(pattern_cfg):
    """Return normalized list of arches for a pattern or None if not restricted.

    Patterns (and some nested providers) may declare an "arches" list. When present,
    we only enable that pattern for matching arches.
    """

    if not isinstance(pattern_cfg, dict):
        return None
    arches = pattern_cfg.get("arches")
    if not arches:
        return None
    return [str(a) for a in arches]


def enabled_for_arch(cfg: dict | None, arch_value: str) -> bool:
    """Return True if this provider/pattern should be shown for the given arch."""

    if not isinstance(cfg, dict) or not cfg:
        return False
    arches = get_pattern_arches(cfg)
    if arches is None:
        return True
    return str(arch_value) in arches


def per_arch_url(config: dict, url_key: str, arch_value: str) -> str:
    """Return the Azure marketplace URL appropriate for this arch.

    Supports either a single top-level "url_key" or a mapping of per-arch
    entries under "url_keys".
    """

    if not isinstance(config, dict):
        return ""
    per_arch = config.get(url_key, {})
    if isinstance(per_arch, dict):
        url = per_arch.get(str(arch_value))
        if url:
            return url
    # Fallback to shared url_key if defined
    return config.get(url_key, "")


def main() -> int:
    spec = load_yaml(SPEC_PATH)
    checksums = load_yaml(CHECKSUMS_PATH)

    versions_out = []

    versions_spec = spec.get("versions", [])
    common_cfg = spec.get("common", {}) or {}
    versions_checks = checksums.get("versions", {})

    for v in versions_spec:
        # Merge common defaults into the version definition so any keys under
        # ``common`` become the baseline for all versions. Per-version values
        # always win over shared defaults.
        v_merged = deep_merge_dict(common_cfg, v)

        vid = str(v_merged["id"])
        v_checks = versions_checks.get(vid, {}) or {}

        # fullVersion now lives in the checksums file so there's a single
        # place to bump when a new point release comes out.
        full = str(v_checks.get("fullVersion", vid))
        label = v_merged.get("label", f"AlmaLinux {full}")
        major = vid

        patterns = v_merged.get("sections", {})

        arches_out = []
        for arch in v_merged.get("arches", []):
            arch_str = str(arch)
            a_checks = v_checks.get(arch_str, {})
            iso_hashes = a_checks.get("iso", {})
            cloud_hashes = a_checks.get("cloud", {})

            sections = []

            # Build sections in the order patterns are defined. For each
            # section we start from any shared/per-version defaults that were
            # merged into ``v_merged`` under a matching key, and then layer the
            # section-specific pattern config on top. This allows
            # ``common.<section_key>`` (and per-version overrides) to define
            # defaults for any section, not just containers.
            for section_key, pattern_cfg in patterns.items():
                section_defaults = v_merged.get(section_key, {}) or {}
                section_cfg = deep_merge_dict(section_defaults, pattern_cfg or {})
                # If a pattern declares an explicit list of arches, skip others.
                if enabled_for_arch(section_cfg, arch_str) is False:
                    continue
                if section_key == "iso":
                    iso_pat = section_cfg
                    # ISO blocks
                    blocks = []
                    base = iso_pat.get("base", "")
                    variants_cfg = iso_pat.get("variants", [])

                    for name in variants_cfg:
                        name = str(name)
                        variant = name
                        url = base.format(major=major, full=full, arch=arch_str, variant=variant)
                        block = {
                            "id": name,
                            "variant": name.capitalize(),
                            "url": url,
                            "sha256": iso_hashes.get(name, ""),
                        }
                        blocks.append(block)

                    mirrors_url_tmpl = iso_pat.get("mirrorsUrl", "")
                    torrent_url_tmpl = iso_pat.get("torrentUrl", "")
                    checksum_url_tmpl = iso_pat.get("checksumUrl", "")

                    iso_section = {
                        "id": "iso_images",
                        "anchorPrefix": "ISO_Images",
                        "title": "ISO Images",
                        "blocks": blocks,
                    }

                    if mirrors_url_tmpl:
                        iso_section["mirrorsUrl"] = mirrors_url_tmpl.format(
                            major=major, full=full, arch=arch_str
                        )
                    if torrent_url_tmpl:
                        iso_section["torrentUrl"] = torrent_url_tmpl.format(
                            major=major, full=full, arch=arch_str
                        )
                    if checksum_url_tmpl:
                        iso_section["checksumUrl"] = checksum_url_tmpl.format(
                            major=major, full=full, arch=arch_str
                        )
                    sections.append(iso_section)

                elif section_key == "cloud":
                    cloud_pat = section_cfg
                    # Cloud section (structure driven by spec patterns, arch-specific where needed).
                    aws = cloud_pat.get("aws", {})
                    generic = cloud_pat.get("genericCloud", {})
                    google = cloud_pat.get("googleCloud", {})
                    azure = cloud_pat.get("azure", {})
                    openneb = cloud_pat.get("openNebula", {})
                    oci = cloud_pat.get("oci", {})

                    cloud_section = {
                        "id": "cloud_images",
                        "anchorPrefix": "Cloud_Images",
                        "title": "Cloud Images",
                        "aws": {
                            "sellerProfileUrl": aws.get("sellerProfileUrl", ""),
                            "marketplaceUrl": per_arch_url(aws, "marketplaceUrls", arch_str),
                        } if enabled_for_arch(aws, arch_str) else {},
                        "genericCloud": {
                            "imageUrl": generic.get("imageUrl", "").format(major=major, full=full, arch=arch_str),
                            "checksumUrl": generic.get("checksumUrl", "").format(major=major, full=full, arch=arch_str),
                            "sha256": cloud_hashes.get("genericCloud", ""),
                        } if enabled_for_arch(generic, arch_str) else {},
                        "googleCloud": {
                            "marketplaceBrowseUrl": google.get("marketplaceBrowseUrl", ""),
                            "productUrl": google.get("productUrl", "").format(major=major, full=full, arch=arch_str),
                        } if enabled_for_arch(google, arch_str) else {},
                        "azure": {
                            "marketplaceUrl": per_arch_url(azure, "marketplaceUrls", arch_str),
                        } if enabled_for_arch(azure, arch_str) else {},
                        "openNebula": {
                            "imageUrl": openneb.get("imageUrl", "").format(major=major, full=full, arch=arch_str),
                            "checksumUrl": openneb.get("checksumUrl", "").format(major=major, full=full, arch=arch_str),
                            "sha256": cloud_hashes.get("openNebula", ""),
                        } if enabled_for_arch(openneb, arch_str) else {},
                        "oci": {
                            "marketplaceUrl": per_arch_url(oci, "marketplaceUrls", arch_str),
                            "partnerListingUrl": oci.get("partnerListingUrl", ""),
                        } if enabled_for_arch(oci, arch_str) else {},
                    }
                    # Remove empty providers (any keys with empty dicts)
                    cloud_section = {k: v for k, v in cloud_section.items() if v != {}}
                    sections.append(cloud_section)

                elif section_key == "container":
                    container_pat = section_cfg
                    # Containers are generally available for all arches, but allow
                    # an optional "arches" list for future restriction.
                    if enabled_for_arch(container_pat, arch_str) is False:
                        continue

                    bootc_pat = container_pat.get("bootc", {}) or {}
                    bootc = {}
                    if enabled_for_arch(bootc_pat, arch_str):
                        bootc = {
                            "repoUrl": bootc_pat.get("repoUrl", ""),
                        }

                    container_section = {
                        "id": "container_images",
                        "anchorPrefix": "Container_Images",
                        "title": "Container Images",
                        "platformImages": container_pat.get("platformImages", {}),
                        "ubiAlternatives": container_pat.get("ubiAlternatives", {}),
                        "bootc": bootc,
                    }
                    sections.append(container_section)

                elif section_key == "live":
                    live_pat = section_cfg
                    # Live media variants (e.g. GNOME, GNOME Mini, KDE, XFCE, MATE)
                    variants_out = []
                    for key, cfg in (live_pat.get("variants", {}) or {}).items():
                        url_tmpl = cfg.get("url", "")
                        if not url_tmpl:
                            continue
                        variants_out.append({
                            "id": str(key),
                            "label": cfg.get("label", str(key)),
                            "url": url_tmpl.format(major=major, full=full, arch=arch_str),
                        })

                    live = {
                        "variants": variants_out,
                        "checksumUrl": live_pat.get("checksumUrl", "").format(major=major, full=full, arch=arch_str),
                    }
                    live_section = {
                        "id": "live_media",
                        "anchorPrefix": "Live_Media",
                        "title": "Live Media",
                        "live": live,
                    }
                    sections.append(live_section)

                elif section_key == "vagrant":
                    vagrant_pat = section_cfg
                    vagrant = {
                        "registryUrl": per_arch_url(vagrant_pat, "registryUrls", arch_str).format(major=major, full=full, arch=arch_str)
                    }
                    vagrant_section = {
                        "id": "vagrant_boxes",
                        "anchorPrefix": "Vagrant_Boxes",
                        "title": "Vagrant Boxes",
                        "vagrant": vagrant,
                    }
                    sections.append(vagrant_section)

                elif section_key == "incusLxc":
                    incus_pat = section_cfg
                    # Incus/LXC images: URLs are specified per arch in the spec
                    urls = incus_pat.get("urls", {}) if isinstance(incus_pat, dict) else {}
                    base_url_tmpl = urls.get(arch_str, "")
                    base_url = base_url_tmpl.format(major=major) if base_url_tmpl else ""

                    incus_section = {
                        "id": "incus_lxc",
                        "anchorPrefix": "Incus-LXC",
                        "title": "Incus and LXC",
                        "url": base_url,
                    }
                    sections.append(incus_section)

                elif section_key == "wsl":
                    wsl_pat = section_cfg
                    wsl_section = {
                        "id": "wsl",
                        "anchorPrefix": "WSL",
                        "title": "WSL",
                        "storeUrl": wsl_pat.get("storeUrl", "").format(major=major, full=full, arch=arch_str),
                    }
                    sections.append(wsl_section)

                elif section_key == "raspberrypi":
                    rpi_pat = section_cfg
                    rpi_section = {
                        "id": "raspberry_pi",
                        "anchorPrefix": "Raspberry_Pi",
                        "title": "Raspberry Pi",
                        "url": rpi_pat.get("url", "").format(major=major, full=full, arch=arch_str),
                    }
                    sections.append(rpi_section)

            arch_node = {
                "id": arch_str,
                # Human-friendly label; keep existing IDs but allow nicer labels later.
                "label": ARCH_LABELS.get(arch_str, arch_str.replace("_", " ")),
                "sections": sections,
            }
            arches_out.append(arch_node)

        versions_out.append({
            "id": vid,
            "label": label,
            "fullVersion": full,
            "arches": arches_out,
        })

    # The output is now a straight list of versions; any shared configuration
    # from ``common`` has already been merged into each version above.
    output = {
        "versions": versions_out,
    }

    OUTPUT_PATH.write_text(
        yaml.safe_dump(output, sort_keys=False, default_flow_style=False)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
