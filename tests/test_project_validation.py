from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_project import OPTIONS, heading_slug, markdown_links, validate_project  # noqa: E402


class OwnerControlledVisualGovernanceTests(unittest.TestCase):
    def test_complete_project_validation_passes(self):
        self.assertEqual(validate_project(ROOT), [])

    def test_heading_slug_is_deterministic(self):
        self.assertEqual(
            heading_slug("M1 — Owner-Controlled Visual Direction"),
            "m1-owner-controlled-visual-direction",
        )

    def test_markdown_link_extraction(self):
        self.assertEqual(
            markdown_links("[Roadmap](10-ROADMAP.md) and [site](https://example.com)"),
            ["10-ROADMAP.md", "https://example.com"],
        )

    def test_four_distinct_option_names_are_defined(self):
        self.assertEqual(
            OPTIONS,
            ["Graphic Atelier", "Future Relics", "Living Garden", "Modern Folk Pop"],
        )

    def test_previous_synthesis_is_historical_only(self):
        protocol = (ROOT / "docs/AI-WORKING-PROTOCOL.md").read_text(encoding="utf-8").lower()
        history = (ROOT / "docs/15-CREATIVE-DIRECTION-OPTIONS.md").read_text(encoding="utf-8").lower()
        self.assertIn("not a default", protocol)
        self.assertIn("historical ai proposal only", history)


if __name__ == "__main__":
    unittest.main()
