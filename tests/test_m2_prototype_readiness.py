from pathlib import Path
import csv
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md"
TEMPLATE = ROOT / "templates" / "prototypes" / "prototype-review.csv"


class M2PrototypeReadinessTests(unittest.TestCase):
    def test_entry_pack_keeps_m2_blocked_until_owner_inputs_are_recorded(self):
        content = DOC.read_text(encoding="utf-8")
        for gate in ["M2-A", "M2-B", "M2-C", "M2-D", "M2-E"]:
            with self.subTest(gate=gate):
                self.assertIn(gate, content)
        self.assertIn("no visual selection, no production-style prototype", content.lower())
        self.assertIn("M2 has not started", content)
        self.assertIn("owner explicitly", content.lower())
        self.assertIn("do not recruit or spend", content.lower())

    def test_entry_pack_covers_six_first_routes_and_five_viewports(self):
        content = DOC.read_text(encoding="utf-8")
        for route in [
            "Homepage", "Shop / Category / Collection", "Product detail",
            "About / Makers", "Journal / Stories", "Contact / Support",
        ]:
            with self.subTest(route=route):
                self.assertIn(route, content)
        for width in ["390 px", "430 px", "768 px", "1280 px", "1440 px"]:
            with self.subTest(width=width):
                self.assertIn(width, content)

    def test_cart_and_checkout_remain_non_transactional_concepts(self):
        content = DOC.read_text(encoding="utf-8").lower()
        self.assertIn("non-transactional concept", content)
        self.assertIn("no payment submission", content)
        self.assertIn("u-001–u-008", content)

    def test_prototype_review_template_is_blank_and_does_not_request_direct_identifiers(self):
        with TEMPLATE.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle))
        self.assertEqual(len(rows), 1)
        headers = set(rows[0])
        self.assertTrue(headers.isdisjoint({
            "name", "full_name", "email", "phone", "telephone",
            "address", "date_of_birth", "birth_date", "password",
        }))
        self.assertTrue({
            "route", "journey_id", "viewport_width_px", "expected_result",
            "observed_result", "status", "evidence_reference", "reviewed_at",
        }.issubset(headers))


if __name__ == "__main__":
    unittest.main()
