from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.private_prototype_browser_review import run_private_review
from scripts.validate_private_prototype import (
    AREA_ROUTES,
    PROPOSAL_PATH,
    ROOT,
    ROUTES,
    validate_private_prototype,
)


class PrivatePrototypeValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="dag-private-prototype-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / "repo"
        self.proto = self.base / "private-prototype"
        (self.repo / "docs").mkdir(parents=True)
        (self.proto / "pages").mkdir(parents=True)
        proposal = self.repo / PROPOSAL_PATH
        proposal.parent.mkdir(parents=True, exist_ok=True)
        proposal.write_text("owner visual proposal fixture\n", encoding="utf-8")
        self.proposal_hash = hashlib.sha256(proposal.read_bytes()).hexdigest()
        (self.repo / "docs/DECISIONS.md").write_text(
            "### D-017 — Owner approves M2-A visual proposal\n"
            "Status: CONFIRMED\n"
            "The M2-A visual direction and visual proposal are approved.\n",
            encoding="utf-8",
        )
        for route in ROUTES:
            page = self.proto / route
            page.parent.mkdir(parents=True, exist_ok=True)
            page.write_text(
                '<!doctype html><html lang="en"><head><title>DAG review</title></head>'
                '<body><main><h1>Owner review</h1><p>Review placeholder copy.</p></main></body></html>',
                encoding="utf-8",
            )
        self.write_manifest()

    def write_manifest(self, **overrides):
        manifest = {
            "schema_version": 1,
            "base_decision_ref": "D-016",
            "prototype_mode": "private-local-nontransactional",
            "routes": list(ROUTES),
            "areas": {name: list(routes) for name, routes in AREA_ROUTES.items()},
            "owner_visual_approval": {
                "status": "approved",
                "decision_ref": "D-017",
                "approved_proposal_sha256": self.proposal_hash,
                "approved_at": "2026-11-09",
            },
            "asset_ledger": {},
        }
        manifest.update(overrides)
        (self.proto / "prototype-manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def validate(self):
        return validate_private_prototype(self.proto, self.repo)

    def test_valid_private_prototype_passes(self):
        result = self.validate()
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual(result["routes_checked"], 9)
        self.assertEqual(result["areas_checked"], 6)

    def test_prototype_root_inside_repository_is_rejected(self):
        inside = self.repo / "private-prototype"
        inside.mkdir()
        result = validate_private_prototype(inside, self.repo)
        self.assertFalse(result["ok"])
        self.assertTrue(any("outside the public repository" in error for error in result["errors"]))

    def test_unapproved_visual_direction_is_rejected(self):
        manifest = json.loads((self.proto / "prototype-manifest.json").read_text())
        manifest["owner_visual_approval"]["status"] = "pending"
        (self.proto / "prototype-manifest.json").write_text(json.dumps(manifest))
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("not recorded as approved" in error for error in result["errors"]))

    def test_owner_decision_reference_must_exist_and_approve_m2a(self):
        manifest = json.loads((self.proto / "prototype-manifest.json").read_text())
        manifest["owner_visual_approval"]["decision_ref"] = "D-099"
        (self.proto / "prototype-manifest.json").write_text(json.dumps(manifest))
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("does not contain D-099" in error for error in result["errors"]))

    def test_approved_proposal_hash_must_match_current_proposal(self):
        manifest = json.loads((self.proto / "prototype-manifest.json").read_text())
        manifest["owner_visual_approval"]["approved_proposal_sha256"] = "0" * 64
        (self.proto / "prototype-manifest.json").write_text(json.dumps(manifest))
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("SHA-256 does not match" in error for error in result["errors"]))

    def test_exact_nine_routes_and_six_area_mapping_are_required(self):
        manifest = json.loads((self.proto / "prototype-manifest.json").read_text())
        manifest["routes"] = ["index.html"]
        manifest["areas"].pop("Journal and Stories")
        (self.proto / "prototype-manifest.json").write_text(json.dumps(manifest))
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("exact nine D-014 routes" in error for error in result["errors"]))
        self.assertTrue(any("exact six D-016 groupings" in error for error in result["errors"]))

    def test_unapproved_extra_html_route_is_rejected(self):
        (self.proto / "pages/promo.html").write_text("<html></html>", encoding="utf-8")
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("unapproved HTML route" in error for error in result["errors"]))

    def test_missing_semantic_landmarks_are_rejected(self):
        (self.proto / "pages/shop.html").write_text(
            "<html lang='en'><head><title>x</title></head><body><h1>one</h1><h1>two</h1></body></html>",
            encoding="utf-8",
        )
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("exactly one main landmark" in error for error in result["errors"]))
        self.assertTrue(any("exactly one h1" in error for error in result["errors"]))

    def test_external_image_and_stylesheet_urls_are_rejected(self):
        (self.proto / "pages/shop.html").write_text(
            '<html lang="en"><head><title>x</title><link rel="stylesheet" href="https://cdn.example/x.css"></head>'
            '<body><main><h1>x</h1><img src="https://cdn.example/product.jpg" alt="x"></main></body></html>',
            encoding="utf-8",
        )
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("external or non-file URL" in error for error in result["errors"]))

    def test_placeholder_requires_ledger_entry_and_visible_exact_label(self):
        (self.proto / "assets").mkdir()
        (self.proto / "assets/frame.svg").write_text("<svg xmlns='http://www.w3.org/2000/svg'></svg>")
        (self.proto / "pages/product.html").write_text(
            '<html lang="en"><head><title>x</title></head><body><main><h1>x</h1>'
            '<img src="../assets/frame.svg" alt="Illustrative empty image"></main></body></html>',
            encoding="utf-8",
        )
        self.write_manifest(asset_ledger={
            "assets/frame.svg": {
                "kind": "illustrative_frame",
                "label": "ILLUSTRATIVE IMAGE FRAME — DAG PHOTOGRAPH PENDING",
            }
        })
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("exact placeholder label must be visible" in error for error in result["errors"]))

    def test_genuine_photo_requires_rights_product_mapping_and_prototype_use(self):
        (self.proto / "assets").mkdir()
        (self.proto / "assets/item.jpg").write_bytes(b"not-a-real-jpeg-but-a-file")
        (self.proto / "pages/product.html").write_text(
            '<html lang="en"><head><title>x</title></head><body><main><h1>x</h1>'
            '<img src="../assets/item.jpg" alt="Verified product photograph"></main></body></html>',
            encoding="utf-8",
        )
        self.write_manifest(asset_ledger={
            "assets/item.jpg": {"kind": "genuine_dag_photo", "rights_status": "cleared"}
        })
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("prototype-use approval evidence" in error for error in result["errors"]))
        self.assertTrue(any("verified product record" in error for error in result["errors"]))

    def test_active_form_controls_and_post_methods_are_rejected(self):
        (self.proto / "pages/contact.html").write_text(
            '<html lang="en"><head><title>x</title></head><body><main><h1>x</h1>'
            '<form method="post" action="https://api.example/contact">'
            '<input name="email"><button type="submit">Send</button></form></main></body></html>',
            encoding="utf-8",
        )
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("forms must not have an action endpoint" in error for error in result["errors"]))
        self.assertTrue(any("POST" in error for error in result["errors"]))
        self.assertTrue(any("every control inside a prototype form must remain disabled" in error for error in result["errors"]))

    def test_transactional_destination_and_network_api_are_rejected(self):
        (self.proto / "pages/shop.html").write_text(
            '<html lang="en"><head><title>x</title></head><body><main><h1>x</h1>'
            '<a href="pages/checkout.html">Checkout</a><script>fetch("/api/orders")</script>'
            '</main></body></html>',
            encoding="utf-8",
        )
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("transactional destination" in error for error in result["errors"]))
        self.assertTrue(any("disallowed fetch/XHR" in error for error in result["errors"]))

    def test_symlinks_are_rejected(self):
        target = self.proto / "pages/shop.html"
        link = self.proto / "pages/shop-copy.html"
        try:
            link.symlink_to(target)
        except OSError:
            self.skipTest("symlinks are not supported in this environment")
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("symlink is not allowed" in error for error in result["errors"]))


    def test_placeholder_asset_passes_with_visible_exact_label_and_ledger(self):
        (self.proto / "assets").mkdir()
        (self.proto / "assets/frame.svg").write_text(
            "<svg xmlns='http://www.w3.org/2000/svg'></svg>", encoding="utf-8"
        )
        (self.proto / "pages/product.html").write_text(
            '<html lang="en"><head><title>x</title></head><body><main><h1>x</h1>'
            '<img src="../assets/frame.svg" alt="Illustrative image placeholder">'
            '<p>ILLUSTRATIVE IMAGE FRAME — DAG PHOTOGRAPH PENDING</p>'
            '</main></body></html>',
            encoding="utf-8",
        )
        self.write_manifest(asset_ledger={
            "assets/frame.svg": {
                "kind": "illustrative_frame",
                "label": "ILLUSTRATIVE IMAGE FRAME — DAG PHOTOGRAPH PENDING",
            }
        })
        result = self.validate()
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual(result["images_checked"], 1)

    def test_local_browser_review_stops_before_playwright_without_visual_approval(self):
        manifest = json.loads((self.proto / "prototype-manifest.json").read_text())
        manifest["owner_visual_approval"]["status"] = "pending"
        (self.proto / "prototype-manifest.json").write_text(json.dumps(manifest))
        output = self.base / "owner-review-output"
        result = run_private_review(self.proto, output)
        self.assertFalse(result["ok"])
        self.assertEqual(result["checks"], 0)
        self.assertTrue(any("entry validation failed" in error for error in result["errors"]))
        self.assertFalse(output.exists())


    def test_manifest_schema_and_template_remain_pending_by_default(self):
        schema = json.loads((ROOT / "schemas/private-prototype-manifest.schema.json").read_text())
        template = json.loads(
            (ROOT / "templates/private-prototype-manifest.template.json").read_text()
        )
        self.assertEqual(schema["properties"]["base_decision_ref"]["const"], "D-016")
        self.assertEqual(template["owner_visual_approval"]["status"], "pending")
        self.assertEqual(template["routes"], list(ROUTES))
        self.assertEqual(
            template["areas"],
            {name: list(routes) for name, routes in AREA_ROUTES.items()},
        )


    def test_picture_source_and_inline_css_external_assets_are_rejected(self):
        (self.proto / "pages/shop.html").write_text(
            '<html lang="en"><head><title>x</title></head><body><main><h1>x</h1>'
            '<picture><source srcset="https://cdn.example/alt.webp"><img src="missing.jpg" alt="x"></picture>'
            '<div style="background-image:url(https://cdn.example/bg.jpg)">x</div>'
            '</main></body></html>',
            encoding="utf-8",
        )
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("picture source: external or non-file URL" in error for error in result["errors"]))
        self.assertTrue(any("CSS asset: external or non-file URL" in error for error in result["errors"]))

    def test_external_script_navigation_is_rejected(self):
        (self.proto / "pages/shop.html").write_text(
            '<html lang="en"><head><title>x</title></head><body><main><h1>x</h1>'
            '<script>window.location.assign("https://checkout.example/")</script>'
            '</main></body></html>',
            encoding="utf-8",
        )
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("external script navigation is not allowed" in error for error in result["errors"]))

    def test_missing_manifest_and_nonexistent_root_are_reported(self):
        (self.proto / "prototype-manifest.json").unlink()
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("missing prototype-manifest.json" in error for error in result["errors"]))
        missing = validate_private_prototype(self.base / "missing", self.repo)
        self.assertFalse(missing["ok"])


    def test_inline_event_handler_attributes_are_rejected(self):
        (self.proto / "pages/about.html").write_text(
            '<html lang="en"><head><title>x</title></head><body><main><h1>x</h1>'
            "<button onclick=\"fetch('/api/orders')\">Explore</button>"
            '</main></body></html>',
            encoding="utf-8",
        )
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("inline event-handler attributes are not allowed" in error for error in result["errors"]))

    def test_background_workers_and_form_override_attributes_are_rejected(self):
        (self.proto / "pages/contact.html").write_text(
            '<html lang="en"><head><title>x</title></head><body><main><h1>x</h1>'
            '<button type="submit" form="remote-form" formaction="/checkout">Continue</button>'
            '<a href="mailto:help@example.com" ping="https://tracker.example/">Email</a>'
            '<script>navigator.serviceWorker.register("/worker.js")</script>'
            '</main></body></html>',
            encoding="utf-8",
        )
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("form/network override attributes" in error for error in result["errors"]))
        self.assertTrue(any("background worker registration" in error for error in result["errors"]))
        self.assertTrue(any("ping" in error for error in result["errors"]))

    def test_malformed_manifest_types_fail_closed_without_crashing(self):
        manifest = json.loads((self.proto / "prototype-manifest.json").read_text())
        manifest["schema_version"] = True
        manifest["owner_visual_approval"]["status"] = []
        (self.proto / "assets").mkdir()
        (self.proto / "assets/missing.jpg").write_bytes(b"not-a-real-jpeg")
        manifest["asset_ledger"] = {"assets/missing.jpg": {"kind": []}}
        self.write_manifest(**manifest)
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("schema_version must be integer 1" in error for error in result["errors"]))
        self.assertTrue(any("status must be pending or approved" in error for error in result["errors"]))
        self.assertTrue(any("asset kind must be a string" in error for error in result["errors"]))

    def test_asset_ledger_rejects_non_normalized_paths(self):
        (self.proto / "assets").mkdir()
        (self.proto / "assets/frame.svg").write_text(
            "<svg xmlns='http://www.w3.org/2000/svg'></svg>", encoding="utf-8"
        )
        (self.proto / "pages/product.html").write_text(
            '<html lang="en"><head><title>x</title></head><body><main><h1>x</h1>'
            '<img src="../assets/frame.svg" alt="Illustrative image placeholder">'
            '<p>ILLUSTRATIVE IMAGE FRAME — DAG PHOTOGRAPH PENDING</p>'
            '</main></body></html>',
            encoding="utf-8",
        )
        self.write_manifest(asset_ledger={
            "assets/../assets/frame.svg": {
                "kind": "illustrative_frame",
                "label": "ILLUSTRATIVE IMAGE FRAME — DAG PHOTOGRAPH PENDING",
            }
        })
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("normalized relative POSIX path" in error for error in result["errors"]))

    def test_asset_ledger_rejects_unknown_metadata_fields(self):
        (self.proto / "assets").mkdir()
        (self.proto / "assets/frame.svg").write_text(
            "<svg xmlns='http://www.w3.org/2000/svg'></svg>", encoding="utf-8"
        )
        (self.proto / "pages/product.html").write_text(
            '<html lang="en"><head><title>x</title></head><body><main><h1>x</h1>'
            '<img src="../assets/frame.svg" alt="Illustrative image placeholder">'
            '<p>ILLUSTRATIVE IMAGE FRAME — DAG PHOTOGRAPH PENDING</p>'
            '</main></body></html>',
            encoding="utf-8",
        )
        self.write_manifest(asset_ledger={
            "assets/frame.svg": {
                "kind": "illustrative_frame",
                "label": "ILLUSTRATIVE IMAGE FRAME — DAG PHOTOGRAPH PENDING",
                "owner_note": "unrecognised field",
            }
        })
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("unsupported asset ledger field" in error for error in result["errors"]))

    def test_owner_approval_rejects_unknown_fields(self):
        manifest = json.loads((self.proto / "prototype-manifest.json").read_text())
        manifest["owner_visual_approval"]["approval_comment"] = "not part of the signed gate"
        (self.proto / "prototype-manifest.json").write_text(
            json.dumps(manifest), encoding="utf-8"
        )
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("unsupported field(s)" in error for error in result["errors"]))

    def test_invalid_calendar_date_is_rejected(self):
        manifest = json.loads((self.proto / "prototype-manifest.json").read_text())
        manifest["owner_visual_approval"]["approved_at"] = "2026-99-99"
        (self.proto / "prototype-manifest.json").write_text(
            json.dumps(manifest), encoding="utf-8"
        )
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("valid calendar date" in error for error in result["errors"]))

    def test_browser_runner_rejects_symlink_prototype_root(self):
        link = self.base / "prototype-link"
        try:
            link.symlink_to(self.proto, target_is_directory=True)
        except OSError:
            self.skipTest("directory symlinks are not supported in this environment")
        output = self.base / "owner-review-output"
        result = run_private_review(link, output)
        self.assertFalse(result["ok"])
        self.assertTrue(any("root must not be a symlink" in error for error in result["errors"]))
        self.assertFalse(output.exists())

    def test_browser_runner_reports_missing_root_without_traceback(self):
        output = self.base / "owner-review-output"
        result = run_private_review(self.base / "missing-prototype", output)
        self.assertFalse(result["ok"])
        self.assertTrue(any("does not exist or cannot be resolved" in error for error in result["errors"]))
        self.assertFalse(output.exists())


    def test_inline_svg_external_image_and_symbol_references_are_rejected(self):
        (self.proto / "pages/about.html").write_text(
            '<html lang="en"><head><title>x</title></head><body><main><h1>x</h1>'
            '<svg xmlns="http://www.w3.org/2000/svg">'
            '<image href="https://cdn.example/photo.jpg"/>'
            '<use href="https://cdn.example/symbols.svg#mark"/>'
            '</svg></main></body></html>',
            encoding="utf-8",
        )
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("inline SVG image: external or non-file URL" in error for error in result["errors"]))
        self.assertTrue(any("inline SVG symbol: external or non-file URL" in error for error in result["errors"]))

    def test_image_type_submit_controls_are_rejected(self):
        (self.proto / "pages/contact.html").write_text(
            '<html lang="en"><head><title>x</title></head><body><main><h1>x</h1>'
            '<input type="image" src="submit.png" alt="Submit">'
            '</main></body></html>',
            encoding="utf-8",
        )
        result = self.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("image-type submit controls are not allowed" in error for error in result["errors"]))


if __name__ == "__main__":
    unittest.main()
