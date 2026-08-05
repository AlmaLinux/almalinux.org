#!/usr/bin/env python3
"""Unit tests for tools/generate_design_colors.py."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import generate_design_colors as gdc  # noqa: E402

SAMPLE_SCSS = """\
// Fonts
$al-font-color: #fefefe;
$al-font-base-size: 16px;

// Base colors
$al-body-background: #0f4266; // @usage Default page background
$al-link-color: #c4e1ff; // @usage Inline text links

// Brand colors
$al-c-brand-primary: #0069da; // @usage Primary buttons

// Sizing
$al-page-readable-max-width: 680px;
"""


class TestParseColors(unittest.TestCase):
    def test_only_color_groups_included(self):
        labels = [label for label, _ in gdc.parse_colors(SAMPLE_SCSS)]
        self.assertEqual(labels, ["Base colors", "Brand colors"])

    def test_font_and_sizing_excluded(self):
        groups = gdc.parse_colors(SAMPLE_SCSS)
        names = [c["name"] for _, colors in groups for c in colors]
        self.assertNotIn("al-font-color", names)
        self.assertNotIn("al-page-readable-max-width", names)

    def test_parses_hex_and_usage(self):
        groups = dict(gdc.parse_colors(SAMPLE_SCSS))
        primary = groups["Brand colors"][0]
        self.assertEqual(primary["name"], "al-c-brand-primary")
        self.assertEqual(primary["hex"], "#0069da")
        self.assertEqual(primary["usage"], "Primary buttons")


class TestRenderTable(unittest.TestCase):
    def test_table_structure(self):
        group = [
            {"name": "al-c-brand-primary", "hex": "#0069da", "usage": "Primary buttons"},
            {"name": "al-link-color", "hex": "#c4e1ff", "usage": "Links"},
        ]
        lines = gdc.render_table(group).split("\n")
        self.assertEqual(len(lines), 4)  # header + separator + 2 rows
        self.assertEqual(len({len(ln) for ln in lines}), 1)  # prettier alignment
        self.assertTrue(set(lines[1]) <= set("-| "))  # separator row
        self.assertIn("`$al-c-brand-primary`", lines[2])
        self.assertIn("`#0069da`", lines[2])
        self.assertIn("Primary buttons", lines[2])

    def test_empty_usage_renders_blank_cell(self):
        # Spec: a variable with no @usage renders an empty Usage cell.
        # No em-dash placeholder (house style forbids em-dashes).
        table = gdc.render_table([{"name": "x", "hex": "#fff", "usage": ""}])
        self.assertNotIn("\u2014", table)  # no em-dash placeholder
        row = table.split("\n")[2]
        self.assertTrue(row.rstrip().endswith("|"))  # trailing Usage cell is blank


class TestRenderBlock(unittest.TestCase):
    def test_block_has_group_headings_and_tables(self):
        groups = gdc.parse_colors(SAMPLE_SCSS)
        block = gdc.render_block(groups)
        self.assertIn("### Base colors", block)
        self.assertIn("### Brand colors", block)
        self.assertIn("| Variable", block)
        self.assertIn("`$al-c-brand-primary`", block)


class TestReplaceBlock(unittest.TestCase):
    def test_replaces_between_sentinels(self):
        doc = f"intro\n{gdc.BEGIN_MARKER}\nOLD\n{gdc.END_MARKER}\noutro\n"
        out = gdc.replace_block(doc, "NEW")
        self.assertIn("NEW", out)
        self.assertNotIn("OLD", out)
        self.assertIn("intro", out)
        self.assertIn("outro", out)
        self.assertEqual(out.count(gdc.BEGIN_MARKER), 1)
        self.assertEqual(out.count(gdc.END_MARKER), 1)

    def test_missing_sentinels_raises(self):
        with self.assertRaises(ValueError):
            gdc.replace_block("no markers here", "NEW")


class TestMainAndCheck(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        gdc.SCSS_PATH = self.tmp / "variables.scss"
        gdc.DESIGN_PATH = self.tmp / "DESIGN.md"
        gdc.SCSS_PATH.write_text(SAMPLE_SCSS)

    def test_generate_then_check_in_sync(self):
        gdc.DESIGN_PATH.write_text(
            f"# Doc\n\n{gdc.BEGIN_MARKER}\n{gdc.END_MARKER}\n"
        )
        self.assertEqual(gdc.main([]), 0)            # write mode
        self.assertEqual(gdc.main(["--check"]), 0)   # now in sync

    def test_check_fails_when_stale(self):
        gdc.DESIGN_PATH.write_text(
            f"# Doc\n\n{gdc.BEGIN_MARKER}\nstale\n{gdc.END_MARKER}\n"
        )
        self.assertEqual(gdc.main(["--check"]), 1)

    def test_missing_sentinels_returns_error(self):
        gdc.DESIGN_PATH.write_text("# Doc with no markers\n")
        self.assertEqual(gdc.main([]), 1)


if __name__ == "__main__":
    unittest.main()
