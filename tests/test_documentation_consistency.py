from pathlib import Path
import tempfile
import unittest

from scripts.audit_documentation_consistency import (
    ARCHIVE_BANNER,
    audit_repository,
    is_historical,
)


class DocumentationConsistencyTests(unittest.TestCase):
    def test_repository_wide_audit_passes_on_current_tree(self):
        result = audit_repository(Path(__file__).resolve().parents[1])
        self.assertEqual(result["errors"], [])
        self.assertGreater(result["tracked_files"], 100)
        self.assertGreater(result["active_text_files"], 40)
        self.assertGreater(result["historical_files"], 5)

    def test_historical_scope_is_contextual(self):
        self.assertTrue(is_historical("docs/historical/superseded/old-prompt.md"))
        self.assertFalse(is_historical("docs/DECISIONS.md"))
        self.assertFalse(is_historical("design/owner-controlled-kit-v2/README.md"))

    def test_historical_visual_html_is_explicitly_non_operative(self):
        root = Path(__file__).resolve().parents[1]
        paths = (
            "docs/historical/visual-proposals/m1-territory-study.html",
            "docs/historical/visual-proposals/reference-led-directions.html",
            "docs/historical/visual-proposals/visual-directions.html",
        )
        for relative in paths:
            with self.subTest(path=relative):
                source = (root / relative).read_text(encoding="utf-8")
                self.assertIn(ARCHIVE_BANNER, source[:700])

    def test_archival_banner_is_explicit(self):
        self.assertIn("HISTORICAL", ARCHIVE_BANNER)
        self.assertIn("DO NOT IMPLEMENT", ARCHIVE_BANNER)


if __name__ == "__main__":
    unittest.main()
