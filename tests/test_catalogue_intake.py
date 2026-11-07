from __future__ import annotations

import csv
import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_catalogue_intake import HEADERS, validate_catalogue_directory, main  # noqa: E402


def write_package(root: Path, products=None, facts=None, images=None):
    root.mkdir(parents=True, exist_ok=True)
    datasets = {
        "products.csv": products or [],
        "product-facts.csv": facts or [],
        "product-images.csv": images or [],
    }
    for filename, rows in datasets.items():
        with (root / filename).open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=HEADERS[filename])
            writer.writeheader()
            writer.writerows(rows)


def product_row(**overrides):
    row = {key: "" for key in HEADERS["products.csv"]}
    row.update({
        "product_id": "p-001",
        "title_en": "Sample title",
        "publication_status": "draft",
        "availability_status": "not_verified",
    })
    row.update(overrides)
    return row


def fact_row(**overrides):
    row = {key: "" for key in HEADERS["product-facts.csv"]}
    row.update({
        "product_id": "p-001",
        "fact_key": "material",
        "fact_value": "Cotton",
        "verification_status": "unverified",
        "public_approval": "not_reviewed",
    })
    row.update(overrides)
    return row


def image_row(**overrides):
    row = {key: "" for key in HEADERS["product-images.csv"]}
    row.update({
        "product_id": "p-001",
        "asset_id": "asset-001",
        "source_relative_path": "products/p-001/image-01.jpg",
        "image_role": "primary",
        "sort_order": "1",
        "rights_status": "unknown",
        "publication_status": "pending",
    })
    row.update(overrides)
    return row


class CatalogueIntakeTests(unittest.TestCase):
    def test_header_only_templates_are_valid(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for filename, headers in HEADERS.items():
                (root / filename).write_text(",".join(headers) + "\n", encoding="utf-8")
            self.assertEqual(validate_catalogue_directory(root), [])

    def test_rejects_duplicate_product_ids_and_skus(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_package(root, products=[
                product_row(sku="SKU-1"),
                product_row(product_id="p-002", sku="sku-1"),
                product_row(sku="SKU-2"),
            ])
            messages = [str(issue) for issue in validate_catalogue_directory(root)]
            self.assertTrue(any("duplicate product_id" in item for item in messages))
            self.assertTrue(any("duplicates row" in item for item in messages))

    def test_price_requires_amount_currency_and_evidence_together(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_package(root, products=[product_row(price_amount="1200")])
            messages = [str(issue) for issue in validate_catalogue_directory(root)]
            self.assertTrue(any("must be supplied together" in item for item in messages))

    def test_valid_price_pair_accepts_explicit_currency_and_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_package(root, products=[product_row(
                price_amount="1200.00",
                price_currency="INR",
                price_evidence_reference="private-source:listing-001",
            )])
            self.assertEqual(validate_catalogue_directory(root), [])

    def test_public_fact_requires_owner_verification_and_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_package(root, products=[product_row()], facts=[fact_row(public_approval="approved")])
            messages = [str(issue) for issue in validate_catalogue_directory(root)]
            self.assertTrue(any("public approval requires owner_verified" in item for item in messages))

    def test_image_publication_requires_cleared_rights_and_alt_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_package(root, products=[product_row()], images=[image_row(publication_status="approved")])
            messages = [str(issue) for issue in validate_catalogue_directory(root)]
            self.assertTrue(any("rights_status=cleared" in item for item in messages))
            self.assertTrue(any("alt_text_en" in item for item in messages))

    def test_published_product_requires_approved_primary_image(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_package(root, products=[product_row(publication_status="published")])
            messages = [str(issue) for issue in validate_catalogue_directory(root)]
            self.assertTrue(any("no approved primary image" in item for item in messages))

    def test_approved_primary_image_makes_published_product_ready(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_package(
                root,
                products=[product_row(publication_status="published")],
                images=[image_row(rights_status="cleared", publication_status="approved", alt_text_en="Folded textile detail")],
            )
            self.assertEqual(validate_catalogue_directory(root), [])

    def test_rejects_unsafe_image_relative_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_package(root, products=[product_row()], images=[
                image_row(source_relative_path="../../private/photo.jpg")
            ])
            messages = [str(issue) for issue in validate_catalogue_directory(root)]
            self.assertTrue(any("normalized relative path" in item for item in messages))

    def write_photo_audit(self, tmp_path, rows, summary_overrides=None):
        csv_path = tmp_path / "photo-audit.csv"
        with csv_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=[
                "relative_path", "detected_format", "status", "sha256", "duplicate_group"
            ])
            writer.writeheader()
            writer.writerows(rows)
        summary = {
            "image_candidates": len(rows),
            "read_only": True,
            "scan_complete": True,
            "directory_traversal_errors": 0,
        }
        summary.update(summary_overrides or {})
        summary_path = tmp_path / "photo-audit-summary.json"
        summary_path.write_text(json.dumps(summary), encoding="utf-8")
        return csv_path, summary_path

    def test_photo_audit_cross_check_accepts_matching_approved_image(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalogue"
            write_package(
                root,
                products=[product_row(publication_status="published")],
                images=[image_row(rights_status="cleared", publication_status="approved", alt_text_en="Textile detail")],
            )
            csv_path, summary_path = self.write_photo_audit(Path(tmp), [{
                "relative_path": "products/p-001/image-01.jpg",
                "detected_format": "JPEG", "status": "ok", "sha256": "a" * 64, "duplicate_group": "",
            }])
            self.assertEqual(validate_catalogue_directory(root, csv_path, summary_path), [])

    def test_photo_audit_cross_check_rejects_missing_source_image(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalogue"
            write_package(root, products=[product_row()], images=[image_row()])
            csv_path, summary_path = self.write_photo_audit(Path(tmp), [{
                "relative_path": "products/other/image.jpg",
                "detected_format": "JPEG", "status": "ok", "sha256": "b" * 64, "duplicate_group": "",
            }])
            messages = [str(issue) for issue in validate_catalogue_directory(root, csv_path, summary_path)]
            self.assertTrue(any("was not found in the completed photo-audit inventory" in item for item in messages))

    def test_photo_audit_requires_complete_scan_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalogue"
            write_package(root, products=[product_row()], images=[image_row()])
            csv_path, summary_path = self.write_photo_audit(Path(tmp), [{
                "relative_path": "products/p-001/image-01.jpg",
                "detected_format": "JPEG", "status": "ok", "sha256": "c" * 64, "duplicate_group": "",
            }], {"scan_complete": False, "directory_traversal_errors": 1})
            messages = [str(issue) for issue in validate_catalogue_directory(root, csv_path, summary_path)]
            self.assertTrue(any("photo audit is incomplete" in item for item in messages))

    def test_approved_image_rejects_review_or_duplicate_audit_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalogue"
            write_package(
                root,
                products=[product_row()],
                images=[image_row(rights_status="cleared", publication_status="approved", alt_text_en="Textile detail")],
            )
            csv_path, summary_path = self.write_photo_audit(Path(tmp), [{
                "relative_path": "products/p-001/image-01.jpg",
                "detected_format": "JPEG", "status": "review", "sha256": "d" * 64, "duplicate_group": "dup-123",
            }])
            messages = [str(issue) for issue in validate_catalogue_directory(root, csv_path, summary_path)]
            self.assertTrue(any("photo-audit status=ok" in item for item in messages))
            self.assertTrue(any("byte-identical" in item for item in messages))

    def test_cli_requires_photo_audit_csv_and_summary_as_a_pair(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_package(root)
            with self.assertRaises(SystemExit) as raised:
                main([str(root), "--photo-audit-csv", str(root / "missing.csv")])
            self.assertEqual(raised.exception.code, 2)

    def test_image_reference_must_point_to_existing_product(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_package(root, products=[product_row()], images=[image_row(product_id="missing")])
            messages = [str(issue) for issue in validate_catalogue_directory(root)]
            self.assertTrue(any("does not exist in products.csv" in item for item in messages))


if __name__ == "__main__":
    unittest.main()
