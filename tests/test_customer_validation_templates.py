from pathlib import Path
import csv
import unittest

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "templates" / "research"

EXPECTED_HEADERS = {
    "participant-screener.csv": [
        "participant_code", "eligibility_status", "market_context",
        "relevant_purchase_context", "recent_relevant_purchase",
        "online_shopping_context", "english_interface_comprehension",
        "recruitment_source_code", "consent_status", "reviewer_notes",
    ],
    "research-session-notes.csv": [
        "session_id", "participant_code", "study_stage", "context_summary",
        "recent_purchase_story", "product_discovery_path", "decision_factors",
        "product_information_needed", "trust_questions", "cross_border_questions",
        "payment_concerns", "delivery_or_returns_questions",
        "english_comprehension_observations", "purchase_or_enquiry_context",
        "deidentified_quote_or_paraphrase", "quote_permission_status",
        "evidence_reference", "follow_up_notes",
    ],
    "task-observations.csv": [
        "session_id", "participant_code", "task_id", "device_context",
        "task_prompt", "task_outcome", "observed_behaviour", "hesitation_or_error",
        "information_missing", "participant_feedback_paraphrase", "impact",
        "severity", "confidence", "evidence_reference", "follow_up_needed",
    ],
    "finding-synthesis.csv": [
        "finding_id", "theme", "evidence_references", "supporting_sessions",
        "contradicting_sessions", "participant_count", "sample_denominator",
        "evidence_type", "confidence", "implication", "proposed_response",
        "owner_decision_required", "status",
    ],
}

FORBIDDEN_IDENTIFIER_FIELDS = {
    "name", "full_name", "email", "phone", "telephone", "address",
    "date_of_birth", "birth_date", "income", "payment_card", "password",
}


class CustomerValidationTemplateTests(unittest.TestCase):
    def test_all_research_csv_templates_are_blank_and_match_the_contract(self):
        for filename, expected_headers in EXPECTED_HEADERS.items():
            with self.subTest(filename=filename):
                path = TEMPLATE_DIR / filename
                self.assertTrue(path.is_file())
                with path.open(encoding="utf-8", newline="") as handle:
                    rows = list(csv.reader(handle))
                self.assertEqual(rows, [expected_headers])
                self.assertEqual(len(rows), 1)

    def test_research_templates_do_not_request_direct_identifier_fields(self):
        for filename, headers in EXPECTED_HEADERS.items():
            with self.subTest(filename=filename):
                self.assertTrue(FORBIDDEN_IDENTIFIER_FIELDS.isdisjoint(headers))

    def test_playbook_preserves_owner_and_research_gates(self):
        playbook = (ROOT / "docs" / "22-CUSTOMER-VALIDATION-PLAYBOOK.md").read_text(encoding="utf-8")
        self.assertIn("research-ready, not research-complete", playbook)
        self.assertIn("M1-B", playbook)
        self.assertIn("No participant recruitment", playbook)
        self.assertIn("owner-approved identity inputs", playbook)
        self.assertIn("not statistically representative", playbook)
        self.assertIn("English-only", playbook)

    def test_stage_b_requires_owner_authorization_and_verified_real_sample(self):
        guide = (TEMPLATE_DIR / "prototype-usability-guide.md").read_text(encoding="utf-8")
        self.assertIn("not permission to start M2", guide)
        self.assertIn("owner-approved identity inputs", guide)
        self.assertIn("representative product/photo sample has been privately verified", guide)

    def test_recording_is_separately_optional(self):
        consent = (TEMPLATE_DIR / "session-opening-and-consent.md").read_text(encoding="utf-8").lower()
        self.assertIn("voluntary", consent)
        self.assertIn("recording is optional", consent)
        self.assertIn("separately", consent)
        self.assertIn("explicit permission", consent)

    def test_discovery_guide_uses_past_behaviour_and_avoids_promises(self):
        guide = (TEMPLATE_DIR / "discovery-interview-guide.md").read_text(encoding="utf-8")
        self.assertIn("most recent time", guide)
        self.assertIn("Do not suggest that DAG currently supports", guide)
        self.assertIn("Do not frame enquiry as the preferred", guide)


if __name__ == "__main__":
    unittest.main()
