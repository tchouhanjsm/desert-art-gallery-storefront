from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
ROUTES = (
    "index.html", "pages/shop.html", "pages/collection.html",
    "pages/product.html", "pages/about.html", "pages/makers.html",
    "pages/journal.html", "pages/article.html", "pages/contact.html",
)
EXPECTED_DISPOSITIONS = {
    "M2-A": "proposal prepared; owner visual approval pending",
    "M2-B": "cohort approved as a plan; fieldwork authorization pending",
    "M2-C": "placeholder approach approved; sample pending",
    "M2-D": "priority approved; automation passed; human review pending",
    "M2-E": "conditionally authorized after visual approval",
}


class M2PrototypeReadinessTests(unittest.TestCase):
    def test_m2_pack_preserves_the_nine_page_d014_inventory(self):
        pack = (ROOT / "docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md").read_text(encoding="utf-8")
        inventory = (ROOT / "docs/PAGE-INVENTORY.md").read_text(encoding="utf-8")
        self.assertIn("D-014", pack)
        for route in ROUTES:
            with self.subTest(route=route):
                self.assertIn(route, pack)
                self.assertIn(route, inventory)

    def test_five_gate_dispositions_match_d016(self):
        pack = (ROOT / "docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md").read_text(encoding="utf-8")
        for gate, disposition in EXPECTED_DISPOSITIONS.items():
            row = next((line for line in pack.splitlines() if line.startswith(f"| {gate}")), "")
            with self.subTest(gate=gate):
                self.assertTrue(row, f"missing owner gate row {gate}")
                self.assertIn(disposition, row.lower())
        self.assertIn("D-016", pack)
        self.assertIn("only after the owner explicitly approves", pack.lower())

    def test_visual_proposal_is_not_an_approval_or_applied_theme(self):
        proposal = (ROOT / "docs/27-M2-A-REFERENCE-LED-VISUAL-PROPOSAL.md").read_text(encoding="utf-8")
        tokens = (ROOT / "docs/OWNER-TOKEN-INPUT.md").read_text(encoding="utf-8")
        self.assertIn("NOT APPROVED", proposal)
        self.assertIn("#174F6B", proposal)
        self.assertIn("PENDING OWNER APPROVAL", tokens)
        kit_tokens = (ROOT / "design/owner-controlled-kit-v2/styles/tokens-layout-only.css").read_text(encoding="utf-8")
        self.assertNotIn("#174F6B", kit_tokens)

    def test_private_prototype_uses_six_areas_and_no_production_transaction(self):
        decisions = (ROOT / "docs/DECISIONS.md").read_text(encoding="utf-8").lower()
        walkthrough = (ROOT / "docs/26-M2-OWNER-REVIEW-WALKTHROUGHS.md").read_text(encoding="utf-8")
        for area in ("Homepage", "Shop and Collections", "Product Detail", "About and Makers", "Journal and Stories", "Contact and Support"):
            self.assertIn(area, decisions)
            self.assertIn(area, walkthrough)
        self.assertIn("non-transactional", decisions)
        self.assertIn("outside the public repository", decisions)
        self.assertIn("no public deployment", decisions)

    def test_research_cohort_is_approved_but_no_fieldwork_is_authorized(self):
        research = (ROOT / "docs/28-M2-B-RESEARCH-OPERATIONS-PLAN.md").read_text(encoding="utf-8").lower()
        for phrase in ("3 home/interior", "2 craft/material", "1 trade/design", "gift", "no recruitment", "no external contact", "no spending"):
            self.assertIn(phrase, research)

    def test_product_and_photo_evidence_remains_pending_and_placeholders_are_labelled(self):
        pack = (ROOT / "docs/25-M2-DECISION-AND-REVIEW-PACK.md").read_text(encoding="utf-8")
        intake = (ROOT / "docs/20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md").read_text(encoding="utf-8")
        self.assertIn("sample pending", pack.lower())
        self.assertIn("ILLUSTRATIVE IMAGE FRAME", intake)
        self.assertIn("LAYOUT PLACEHOLDER", intake)
        self.assertIn("no full-library migration", pack.lower())

    def test_automation_is_not_human_usability_validation(self):
        review = (ROOT / "docs/26-M2-OWNER-REVIEW-WALKTHROUGHS.md").read_text(encoding="utf-8")
        self.assertIn("not participant usability research", review.lower())
        self.assertIn("human usability acceptance", review.lower())

    def test_unapproved_commerce_and_production_behaviour_remains_excluded(self):
        pack = (ROOT / "docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md").read_text(encoding="utf-8").lower()
        self.assertIn("no production", pack)
        self.assertIn("remain disabled", pack)
        self.assertIn("no public deployment", pack)


if __name__ == "__main__":
    unittest.main()
