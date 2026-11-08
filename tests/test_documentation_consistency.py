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

    def test_archival_banner_is_explicit(self):
        self.assertIn("HISTORICAL", ARCHIVE_BANNER)
        self.assertIn("DO NOT IMPLEMENT", ARCHIVE_BANNER)


if __name__ == "__main__":
    unittest.main()
