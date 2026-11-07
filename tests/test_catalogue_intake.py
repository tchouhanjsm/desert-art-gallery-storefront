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


def write_package(root: Path, products=None, facts=None, images=None, sources=None, etsy_images=None):
    root.mkdir(parents=True, exist_ok=True)
    datasets = {
        "products.csv": products or [],
        "product-facts.csv": facts or [],
        "product-images.csv": images or [],
        "product-source-records.csv": sources or [],
        "etsy-image-sources.csv": etsy_images or [],
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



def source_record_row(**overrides):
    row = {key: "" for key in HEADERS["product-source-records.csv"]}
    row.update({
        "product_id": "p-001",
        "source_system": "etsy",
        "source_file_sha256": "a" * 64,
        "source_data_row_number": "1",
        "source_record_ref": "etsy:" + ("a" * 64) + ":row:1",
        "source_record_id": "",
        "source_sku_raw": "",
        "source_title_raw": "Original source title",
        "source_price_raw": "149.00",
        "source_currency_raw": "USD",
        "source_quantity_raw": "1",
        "source_materials_raw": "Cotton",
        "source_tags_raw": "textile,handmade",
        "source_variations_raw": "",
        "reconciliation_status": "not_reviewed",
    })
    row.update(overrides)
    return row


def etsy_image_source_row(**overrides):
    row = {key: "" for key in HEADERS["etsy-image-sources.csv"]}
    row.update({
        "product_id": "p-001",
        "source_record_ref": "etsy:" + ("a" * 64) + ":row:1",
        "source_image_field": "IMAGE1",
        "source_image_url": "https://i.etsystatic.com/123456/photo.jpg",
        "local_asset_id": "",
        "rights_status": "unknown",
        "download_status": "not_attempted",
        "owner_review_status": "pending",
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

    def test_source_snapshot_preserves_duplicate_raw_skus_without_using_them_as_catalogue_skus(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            hash_value = "b" * 64
            p1 = "etsy:" + hash_value + ":row:1"
            p2 = "etsy:" + hash_value + ":row:2"
            write_package(
                root,
                products=[
                    product_row(product_id="p-001", source_record_ref=p1, sku=""),
                    product_row(product_id="p-002", source_record_ref=p2, sku=""),
                ],
                sources=[
                    source_record_row(source_file_sha256=hash_value, source_record_ref=p1, source_sku_raw="DUP-SKU"),
                    source_record_row(product_id="p-002", source_file_sha256=hash_value, source_data_row_number="2", source_record_ref=p2, source_sku_raw="DUP-SKU"),
                ],
            )
            self.assertEqual(validate_catalogue_directory(root), [])

    def test_source_record_reference_must_bind_file_hash_and_data_row(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_package(
                root,
                products=[product_row(source_record_ref="etsy:hash-mismatch:row:1")],
                sources=[source_record_row(source_file_sha256="wrong", source_record_ref="etsy:hash-mismatch:row:1")],
            )
            messages = [str(issue) for issue in validate_catalogue_directory(root)]
            self.assertTrue(any("lowercase 64-character SHA-256" in item for item in messages))
            self.assertTrue(any("source_record_ref must equal" in item for item in messages))

    def test_etsy_source_image_url_must_use_exact_https_host(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = source_record_row()
            write_package(
                root,
                products=[product_row(source_record_ref=source["source_record_ref"])],
                sources=[source],
                etsy_images=[etsy_image_source_row(source_image_url="https://images.example.com/photo.jpg")],
            )
            messages = [str(issue) for issue in validate_catalogue_directory(root)]
            self.assertTrue(any("exact i.etsystatic.com host" in item for item in messages))

    def test_etsy_downloaded_image_must_map_to_a_local_asset(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = source_record_row()
            write_package(
                root,
                products=[product_row(source_record_ref=source["source_record_ref"])],
                sources=[source],
                etsy_images=[etsy_image_source_row(
                    local_asset_id="asset-local-1",
                    rights_status="cleared",
                    download_status="downloaded",
                    owner_review_status="accepted",
                )],
            )
            messages = [str(issue) for issue in validate_catalogue_directory(root)]
            self.assertTrue(any("local_asset_id must match" in item for item in messages))
            self.assertTrue(any("accepted source image requires" in item for item in messages))

    def test_etsy_downloaded_image_passes_when_linked_to_local_image_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = source_record_row()
            write_package(
                root,
                products=[product_row(source_record_ref=source["source_record_ref"])],
                sources=[source],
                images=[image_row(asset_id="asset-local-1")],
                etsy_images=[etsy_image_source_row(
                    local_asset_id="asset-local-1",
                    rights_status="cleared",
                    download_status="downloaded",
                    owner_review_status="accepted",
                )],
            )
            self.assertEqual(validate_catalogue_directory(root), [])

    def test_etsy_image_source_requires_matching_etsy_source_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_package(
                root,
                products=[product_row()],
                etsy_images=[etsy_image_source_row()],
            )
            messages = [str(issue) for issue in validate_catalogue_directory(root)]
            self.assertTrue(any("does not exist in product-source-records.csv" in item for item in messages))

    def test_image_reference_must_point_to_existing_product(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_package(root, products=[product_row()], images=[image_row(product_id="missing")])
            messages = [str(issue) for issue in validate_catalogue_directory(root)]
            self.assertTrue(any("does not exist in products.csv" in item for item in messages))


if __name__ == "__main__":
    unittest.main()
