from __future__ import annotations
import csv
import sys
import tempfile
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_etsy_review_bundle import build_private_review_bundle  # noqa: E402
from create_etsy_reconciliation_worklist import WORKLIST_FIELDS, create_reconciliation_worklist, main  # noqa: E402

HEADERS = [
    "TITLE", "DESCRIPTION", "PRICE", "CURRENCY_CODE", "QUANTITY",
    "SKU", "MATERIALS", "TAGS", "IMAGE1", "IMAGE2",
    "VARIATION 1 TYPE", "VARIATION 1 NAME", "VARIATION 1 VALUES",
]

def create_bundle(root: Path) -> Path:
    source_dir = root / "source"
    source_dir.mkdir()
    source = source_dir / "etsy.csv"
    with source.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(HEADERS)
        writer.writerow([
            "Repeated title", "Multiline\nsource description", "120", "USD", "1",
            "SKU-A", "Cotton", "textile,handwoven",
            "https://i.etsystatic.com/a.jpg", "https://images.example.com/review.jpg",
            "Material", "Size", "Large",
        ])
        writer.writerow([
            "Repeated title", "Another description", "125", "USD", "1",
            "sku-a", "Wool", "object", "", "", "", "", "",
        ])
    bundle = root.parent / (root.name + "-bundle")
    build_private_review_bundle(source, bundle)
    return bundle

class EtsyReconciliationWorklistTests(unittest.TestCase):
    def test_worklist_preserves_source_keys_and_leaves_product_decisions_blank(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundle = create_bundle(root)
            output = root.parent / (root.name + "-worklist.csv")
            result = create_reconciliation_worklist(bundle, output)
            self.assertEqual(result["source_rows"], 2)
            self.assertEqual(result["image_reference_rows"], 2)
            with output.open("r", encoding="utf-8-sig", newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 2)
            self.assertEqual(list(rows[0]), WORKLIST_FIELDS)
            self.assertEqual(rows[0]["source_data_row_number"], "1")
            self.assertEqual(rows[0]["source_title_raw"], "Repeated title")
            self.assertEqual(rows[0]["source_sku_raw"], "SKU-A")
            self.assertEqual(rows[0]["source_sku_duplicate"], "True")
            self.assertEqual(rows[0]["title_occurrences"], "2")
            self.assertEqual(rows[0]["source_materials_raw"], "Cotton")
            self.assertEqual(rows[0]["source_tags_raw"], "textile,handwoven")
            self.assertEqual(rows[0]["image_source_count"], "2")
            self.assertEqual(rows[0]["source_variations_raw"], '{"VARIATION 1 NAME": "Size", "VARIATION 1 TYPE": "Material", "VARIATION 1 VALUES": "Large"}')
            self.assertEqual(rows[0]["proposed_dag_product_id"], "")
            self.assertEqual(rows[0]["identity_match_basis"], "")
            self.assertEqual(rows[0]["identity_evidence_reference"], "")
            self.assertEqual(rows[0]["owner_reconciliation_status"], "unreviewed")
            self.assertEqual(rows[1]["proposed_dag_product_id"], "")
            self.assertEqual(rows[1]["source_sku_duplicate"], "True")

    def test_worklist_cli_reports_creation_and_refuses_existing_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundle = create_bundle(root)
            output = root.parent / (root.name + "-worklist.csv")
            self.assertEqual(main([str(bundle), str(output)]), 0)
            self.assertEqual(main([str(bundle), str(output)]), 2)

    def test_worklist_output_must_be_outside_bundle(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundle = create_bundle(root)
            with self.assertRaises(ValueError):
                create_reconciliation_worklist(bundle, bundle / "worklist.csv")

    def test_worklist_output_must_be_outside_git_worktree(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundle = create_bundle(root)
            repository = root / "repository"
            repository.mkdir()
            (repository / ".git").mkdir()
            with self.assertRaises(ValueError):
                create_reconciliation_worklist(bundle, repository / "worklist.csv")

    def test_worklist_rejects_symlinked_destination(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundle = create_bundle(root)
            real = root.parent / (root.name + "-real.csv")
            real.write_text("existing", encoding="utf-8")
            link = root.parent / (root.name + "-link.csv")
            try:
                link.symlink_to(real)
            except OSError:
                self.skipTest("symlinks are not available on this runner")
            with self.assertRaises(ValueError):
                create_reconciliation_worklist(bundle, link)

    def test_worklist_rejects_unverified_or_modified_bundle(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundle = create_bundle(root)
            with (bundle / "README.txt").open("a", encoding="utf-8") as handle:
                handle.write("tamper\n")
            with self.assertRaises(ValueError):
                create_reconciliation_worklist(bundle, root.parent / (root.name + "-worklist.csv"))

    def test_worklist_contains_no_description_or_image_url_dump(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundle = create_bundle(root)
            output = root.parent / (root.name + "-worklist.csv")
            create_reconciliation_worklist(bundle, output)
            content = output.read_text(encoding="utf-8-sig")
            self.assertNotIn("Multiline", content)
            self.assertNotIn("https://", content)

if __name__ == "__main__":
    unittest.main()
