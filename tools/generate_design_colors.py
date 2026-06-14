#!/usr/bin/env python3
"""Generate the brand-colors table in DESIGN.md from assets/scss/variables.scss.

The brand-colors section of DESIGN.md lives between sentinel comments and is
fully generated from variables.scss, the single source of truth for both the
hex value and (via `// @usage` comments) the intended use of each color.

Usage:
    python3 tools/generate_design_colors.py            # rewrite DESIGN.md
    python3 tools/generate_design_colors.py --check    # exit 1 if stale
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCSS_PATH = ROOT / "assets" / "scss" / "variables.scss"
DESIGN_PATH = ROOT / "DESIGN.md"

BEGIN_MARKER = "<!-- BEGIN GENERATED: brand-colors -->"
END_MARKER = "<!-- END GENERATED: brand-colors -->"

# Only these SCSS section comments contribute to the palette table, in order.
COLOR_GROUPS = ["Base colors", "Brand colors", "Brand palette"]

GROUP_RE = re.compile(r"^//\s*(?P<label>.+?)\s*$")
VAR_RE = re.compile(
    r"^\$(?P<name>[\w-]+):\s*(?P<value>#[0-9a-fA-F]{3,6})\s*;"
    r"(?:\s*//\s*@usage\s*(?P<usage>.*?)\s*)?$"
)


def parse_colors(scss_text):
    """Return an ordered list of (group_label, [{name, hex, usage}, ...]).

    Only variables under a COLOR_GROUPS section comment that hold a hex value
    are included. Groups are returned in COLOR_GROUPS order.
    """
    groups = {}
    current = None
    for raw in scss_text.splitlines():
        line = raw.strip()
        group_match = GROUP_RE.match(line)
        if group_match:
            label = group_match.group("label")
            current = label if label in COLOR_GROUPS else None
            if current:
                groups.setdefault(current, [])
            continue
        if current is None:
            continue
        var_match = VAR_RE.match(line)
        if var_match:
            groups[current].append({
                "name": var_match.group("name"),
                "hex": var_match.group("value").lower(),
                "usage": (var_match.group("usage") or "").strip(),
            })
    return [(label, groups[label]) for label in COLOR_GROUPS if label in groups]


def render_table(group):
    """Render one color group as a prettier-formatted markdown table.

    Columns are left-aligned and padded to the widest cell, matching
    prettier's default markdown table formatting so regeneration never
    fights the lint-staged prettier hook. A color with no `@usage` comment
    renders an empty Usage cell (no placeholder).
    """
    headers = ["Variable", "Hex", "Usage"]
    rows = [
        [f"`${c['name']}`", f"`{c['hex']}`", c["usage"]]
        for c in group
    ]
    widths = [
        max(len(headers[i]), *(len(r[i]) for r in rows)) if rows else len(headers[i])
        for i in range(3)
    ]

    def fmt(cells):
        return "| " + " | ".join(cells[i].ljust(widths[i]) for i in range(3)) + " |"

    lines = [fmt(headers), fmt(["-" * w for w in widths])]
    lines.extend(fmt(r) for r in rows)
    return "\n".join(lines)


def render_block(groups):
    """Render the full generated block (content between, not incl. markers)."""
    parts = []
    for label, colors in groups:
        parts.append(f"### {label}")
        parts.append("")
        parts.append(render_table(colors))
        parts.append("")
    return "\n".join(parts).rstrip()


def replace_block(design_text, block):
    """Return design_text with the content between the sentinels replaced.

    Raises ValueError if either sentinel is missing.
    """
    begin = design_text.find(BEGIN_MARKER)
    end = design_text.find(END_MARKER)
    if begin == -1 or end == -1 or end < begin:
        raise ValueError("DESIGN.md is missing the brand-colors sentinels")
    before = design_text[: begin + len(BEGIN_MARKER)]
    after = design_text[end:]
    return f"{before}\n\n{block}\n\n{after}"


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate the brand-colors table in DESIGN.md."
    )
    parser.add_argument(
        "--check", action="store_true",
        help="Exit 1 if DESIGN.md is out of sync; do not write.",
    )
    args = parser.parse_args(argv)

    if not SCSS_PATH.exists():
        print(f"Missing SCSS file: {SCSS_PATH}", file=sys.stderr)
        return 1
    if not DESIGN_PATH.exists():
        print(f"Missing DESIGN.md: {DESIGN_PATH}", file=sys.stderr)
        return 1

    groups = parse_colors(SCSS_PATH.read_text())
    block = render_block(groups)
    current = DESIGN_PATH.read_text()
    try:
        updated = replace_block(current, block)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.check:
        if updated != current:
            print(
                "DESIGN.md brand-colors table is out of sync with "
                "variables.scss. Run: npm run generate:design-colors",
                file=sys.stderr,
            )
            return 1
        print("DESIGN.md brand-colors table is in sync.")
        return 0

    if updated != current:
        DESIGN_PATH.write_text(updated)
        print("Updated DESIGN.md brand-colors table.")
    else:
        print("DESIGN.md brand-colors table already in sync.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
