from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_project import heading_slug, markdown_links, validate_project  # noqa: E402


class ProjectValidationTests(unittest.TestCase):
    def test_full_project_validation_passes(self):
        self.assertEqual(validate_project(ROOT), [])

    def test_heading_slug_is_stable(self):
        self.assertEqual(heading_slug("M1 — Customer & Brand Strategy"), "m1-customer-brand-strategy")

    def test_markdown_link_extraction(self):
        self.assertEqual(
            markdown_links("[Roadmap](10-ROADMAP.md) and [site](https://example.com)"),
            ["10-ROADMAP.md", "https://example.com"],
        )


if __name__ == "__main__":
    unittest.main()
