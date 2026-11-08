from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
ROUTES = (
    "index.html", "pages/shop.html", "pages/collection.html",
    "pages/product.html", "pages/about.html", "pages/makers.html",
    "pages/journal.html", "pages/article.html", "pages/contact.html",
)
EXPECTED_DISPOSITIONS = {
    "M2-A": "blocked on owner input",
    "M2-B": "recommendation prepared",
    "M2-C": "blocked on sample/evidence",
    "M2-D": "execution matrix implemented",
    "M2-E": "authorized for bounded structural review only",
}


class M2PrototypeReadinessTests(unittest.TestCase):
    def test_m2_pack_uses_the_nine_page_d014_scope(self):
        pack = (ROOT / "docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md").read_text(encoding="utf-8")
        self.assertIn("D-014", pack)
        for route in ROUTES:
            with self.subTest(route=route):
                self.assertIn(route, pack)

    def test_five_gate_dispositions_match_owner_inputs_and_d015(self):
        pack = (ROOT / "docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md").read_text(encoding="utf-8")
        for gate, disposition in EXPECTED_DISPOSITIONS.items():
            row = next((line for line in pack.splitlines() if line.startswith(f"| {gate}")), "")
            with self.subTest(gate=gate):
                self.assertTrue(row, f"missing gate row {gate}")
                self.assertIn(disposition, row.lower())
        self.assertIn("D-015", pack)
        self.assertIn("bounded structural review", pack.lower())

    def test_m2_a_and_c_remain_explicitly_blocked_on_owner_evidence(self):
        pack = (ROOT / "docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md").read_text(encoding="utf-8").lower()
        self.assertIn("no brand tokens or identity assets have been supplied", pack)
        self.assertIn("no original product sample/export/photo set is present", pack)

    def test_production_and_unlisted_interactions_are_excluded(self):
        pack = (ROOT / "docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md").read_text(encoding="utf-8").lower()
        self.assertIn("no production application development", pack)
        self.assertIn("disabled controls", pack)


if __name__ == "__main__":
    unittest.main()
