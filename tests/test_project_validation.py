from pathlib import Path
import unittest

from scripts.validate_project import REQUIRED, ROUTES, validate_project

ROOT = Path(__file__).resolve().parents[1]


class ProjectValidationTests(unittest.TestCase):
    def test_v2_governance_paths_are_present(self):
        self.assertTrue(all((ROOT / path).is_file() for path in REQUIRED))

    def test_exact_nine_route_inventory_is_complete(self):
        inventory = (ROOT / "docs/PAGE-INVENTORY.md").read_text(encoding="utf-8")
        for route in ROUTES:
            with self.subTest(route=route):
                self.assertIn(route, inventory)

    def test_documentation_authority_is_consistent(self):
        self.assertEqual(validate_project(ROOT), [])


if __name__ == "__main__":
    unittest.main()
