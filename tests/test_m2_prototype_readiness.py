from pathlib import Path
import csv
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md"
TEMPLATE = ROOT / "templates" / "prototypes" / "prototype-review.csv"
DECISION_TEMPLATE = ROOT / "templates" / "prototypes" / "m2-owner-entry-decision.md"


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
        for term in ["japan-first customer-segment focus", "home and interior buyers", "craft and material enthusiasts", "gift and considered-purchase buyers", "trade and design professionals", "shared global shell", "responsive primary and category navigation", "search entry/disclosure", "global footer", "reusable presentation components", "mixed product/photo evidence", "rights/permissions", "mobile is a required test dimension across every selected journey"]:
            with self.subTest(term=term):
                self.assertIn(term, content.lower())
        self.assertNotIn("mobile recovery", content.lower())

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

    def test_owner_entry_worksheet_captures_all_gates_without_preselecting_options(self):
        content = DECISION_TEMPLATE.read_text(encoding="utf-8")
        for gate in ["M2-A", "M2-B", "M2-C", "M2-D", "M2-E"]:
            with self.subTest(gate=gate):
                self.assertIn(gate, content)
        for proposal in ["Porcelain Index", "Bordeaux Editions", "Blue Current", "Citron Signal"]:
            with self.subTest(proposal=proposal):
                self.assertIn(proposal, content)
        self.assertIn("No option is preselected, recommended or approved", content)
        self.assertIn("M2 has not started", content)
        self.assertIn("BLOCKED until every applicable gate", content)
        self.assertIn("Recruitment, incentives and other spending remain unauthorized", content)
        self.assertIn("Do not commit populated catalogue data", content)
        self.assertIn("non-production prototype only", content.lower())
        for term in ["initial customer segments (japan-first)", "home and interior buyers", "craft and material enthusiasts", "gift and considered-purchase buyers", "trade and design professionals", "mixed genuine-photo and placeholder evidence", "mobile is a required test dimension", "responsive primary/category navigation", "global footer"]:
            with self.subTest(term=term):
                self.assertIn(term, content.lower())
        self.assertNotIn("mobile recovery", content.lower())
        self.assertNotIn("[x]", content.lower())

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
