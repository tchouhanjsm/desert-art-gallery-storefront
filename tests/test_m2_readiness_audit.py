import unittest
from scripts.audit_m2_readiness import audit_m2_readiness


class M2ReadinessAuditTests(unittest.TestCase):
    def test_all_owner_gates_are_consistent_and_open(self):
        result = audit_m2_readiness()
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["overall"], "BLOCKED")
        self.assertEqual(result["open_gates"], ["M2-A", "M2-B", "M2-C", "M2-D", "M2-E"])


if __name__ == "__main__":
    unittest.main()
