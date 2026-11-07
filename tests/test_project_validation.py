from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_project import OPTIONS, REFERENCE_OPTIONS, REFERENCE_FONTS, heading_slug, markdown_links, validate_project  # noqa: E402
from validate_catalogue_intake import HEADERS as CATALOGUE_HEADERS  # noqa: E402


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

    def test_owner_rejection_and_reference_led_decision_are_recorded(self):
        decisions = (ROOT / "docs/DECISIONS.md").read_text(encoding="utf-8")
        brief = (ROOT / "docs/17-REFERENCE-LED-DESIGN-BRIEF.md").read_text(encoding="utf-8")
        review = (ROOT / "docs/M1-OWNER-REVIEW.md").read_text(encoding="utf-8")
        self.assertIn("D-008", decisions)
        self.assertIn("D-009", decisions)
        self.assertIn("Status: REJECTED", decisions)
        self.assertIn("shop.macaro-ni.jp", decisions)
        self.assertIn("pojstudio.com", decisions)
        self.assertIn("pixel-for-pixel", brief)
        self.assertIn("rejected", review.lower())

    def test_fresh_reference_led_options_are_rendered_and_specified(self):
        spec = (ROOT / "docs/18-REFERENCE-LED-DIRECTION-SPECIFICATIONS.md").read_text(encoding="utf-8")
        board = (ROOT / "design/explorations/reference-led-directions.html").read_text(encoding="utf-8")
        for option in REFERENCE_OPTIONS:
            self.assertIn(option, spec)
            self.assertIn(option, board)
        for font in REFERENCE_FONTS:
            self.assertIn(font, spec)
            self.assertIn(font, board)
        self.assertIn("Desktop composition", board)
        self.assertIn("Mobile composition", board)
        self.assertIn("not DAG products", board)


    def test_photo_audit_is_included_and_documented_as_read_only(self):
        script = (ROOT / "scripts/audit_photo_library.py").read_text(encoding="utf-8")
        guide = (ROOT / "docs/19-PHOTO-LIBRARY-AUDIT.md").read_text(encoding="utf-8")
        self.assertIn("read-only", script.lower())
        self.assertIn("never renames", script.lower())
        self.assertIn("SHA-256", guide)
        self.assertIn("bulk migration", guide)

    def test_catalogue_intake_templates_are_header_only_and_match_contract(self):
        template_dir = ROOT / "templates/catalogue"
        self.assertTrue((template_dir / "README.md").is_file())
        for filename, expected_headers in CATALOGUE_HEADERS.items():
            content = (template_dir / filename).read_text(encoding="utf-8").splitlines()
            self.assertEqual(content, [",".join(expected_headers)])
        self.assertIn("draft", (ROOT / "docs/20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md").read_text(encoding="utf-8"))
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8").lower()
        self.assertIn("must not be committed to git", agents)
        self.assertIn("owner verification", agents)

    def test_previous_synthesis_is_historical_only(self):
        protocol = (ROOT / "docs/AI-WORKING-PROTOCOL.md").read_text(encoding="utf-8").lower()
        history = (ROOT / "docs/15-CREATIVE-DIRECTION-OPTIONS.md").read_text(encoding="utf-8").lower()
        self.assertIn("not a default", protocol)
        self.assertIn("historical ai proposal only", history)


if __name__ == "__main__":
    unittest.main()
