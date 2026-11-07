from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
ROUTES = (
    "index.html", "pages/shop.html", "pages/collection.html",
    "pages/product.html", "pages/about.html", "pages/makers.html",
    "pages/journal.html", "pages/article.html", "pages/contact.html",
)


class M2PrototypeReadinessTests(unittest.TestCase):
    def test_m2_pack_uses_the_nine_page_d014_scope(self):
        pack = (ROOT / "docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md").read_text(encoding="utf-8")
        self.assertIn("D-014", pack)
        for route in ROUTES:
            with self.subTest(route=route):
                self.assertIn(route, pack)

    def test_all_five_owner_gates_remain_open(self):
        pack = (ROOT / "docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md").read_text(encoding="utf-8")
        for gate in ("M2-A", "M2-B", "M2-C", "M2-D", "M2-E"):
            row = next((line for line in pack.splitlines() if line.startswith(f"| {gate}")), "")
            with self.subTest(gate=gate):
                self.assertIn("Open", row)

    def test_production_and_unlisted_interactions_are_excluded(self):
        pack = (ROOT / "docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md").read_text(encoding="utf-8").lower()
        self.assertIn("no production application development", pack)
        self.assertIn("disabled controls", pack)


if __name__ == "__main__":
    unittest.main()
