#!/usr/bin/env python3
"""Validate a local/private DAG prototype before owner review.

The validator is intentionally a gate, not a renderer or approval mechanism.
It never reads or writes catalogue/photo data outside the supplied prototype
root except for the owner decision register and proposal hash in this repo.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_NAME = "prototype-manifest.json"
PROPOSAL_PATH = Path("docs/27-M2-A-REFERENCE-LED-VISUAL-PROPOSAL.md")
ROUTES = (
    "index.html",
    "pages/shop.html",
    "pages/collection.html",
    "pages/product.html",
    "pages/about.html",
    "pages/makers.html",
    "pages/journal.html",
    "pages/article.html",
    "pages/contact.html",
)
AREA_ROUTES = {
    "Homepage": ("index.html",),
    "Shop and Collections": ("pages/shop.html", "pages/collection.html"),
    "Product Detail": ("pages/product.html",),
    "About and Makers": ("pages/about.html", "pages/makers.html"),
    "Journal and Stories": ("pages/journal.html", "pages/article.html"),
    "Contact and Support": ("pages/contact.html",),
}
PLACEHOLDER_LABELS = {
    "ILLUSTRATIVE IMAGE FRAME — DAG PHOTOGRAPH PENDING",
    "LAYOUT PLACEHOLDER — NOT A DAG PRODUCT",
}
IMAGE_SUFFIXES = {".avif", ".gif", ".jpg", ".jpeg", ".png", ".svg", ".webp"}
NETWORK_PATTERNS = (
    ("fetch/XHR", re.compile(r"\bfetch\s*\(|\bXMLHttpRequest\b", re.I)),
    ("WebSocket/EventSource", re.compile(r"\bWebSocket\s*\(|\bEventSource\s*\(", re.I)),
    ("beacon submission", re.compile(r"\bsendBeacon\s*\(", re.I)),
    ("dynamic code loading", re.compile(r"\bimport\s*\(", re.I)),
    ("browser persistence/cookie access", re.compile(r"\bdocument\.cookie\b|\blocalStorage\b|\bsessionStorage\b", re.I)),
    ("form submission API", re.compile(r"\.(?:submit|requestSubmit)\s*\(", re.I)),
    ("dynamic code execution", re.compile(r"\beval\s*\(|\bnew\s+Function\s*\(", re.I)),
)
TRANSACTION_TARGET = re.compile(
    r"(?:^|[/#?._-])(cart|checkout|payment|payments|orders?|purchase|shipping|"
    r"fulfilment|fulfillment|tax|refunds?|wishlist|account|inventory)(?:[/#?._=-]|$)",
    re.I,
)
CSS_URL = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.I)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")


class PageParser(HTMLParser):
    """Collect the source properties needed for a conservative static audit."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.lang: str | None = None
        self.title_count = 0
        self.title_text: list[str] = []
        self.h1_count = 0
        self.main_count = 0
        self.images: list[tuple[str, str, str]] = []
        self.links: list[str] = []
        self.stylesheets: list[str] = []
        self.scripts: list[str] = []
        self.inline_scripts: list[str] = []
        self.inline_styles: list[str] = []
        self.base_hrefs: list[str] = []
        self.meta_refresh: list[str] = []
        self.embedded_content: list[str] = []
        self.forms: list[dict[str, object]] = []
        self.form_stack: list[dict[str, object]] = []
        self.controls: list[dict[str, object]] = []
        self.text: list[str] = []
        self._in_title = False
        self._in_script = False
        self._in_style = False
        self._script_buffer: list[str] = []
        self._style_buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value for key, value in attrs}
        if tag == "base":
            self.base_hrefs.append(values.get("href") or "")
        elif tag == "meta" and (values.get("http-equiv") or "").lower() == "refresh":
            self.meta_refresh.append(values.get("content") or "")
        elif tag in {"iframe", "object", "embed", "video", "audio"}:
            self.embedded_content.append(tag)
        elif tag == "html":
            self.lang = values.get("lang")
        elif tag == "title":
            self.title_count += 1
            self._in_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "main":
            self.main_count += 1
        elif tag == "img":
            self.images.append((values.get("src") or "", values.get("alt") or "", values.get("srcset") or ""))
        elif tag == "a":
            self.links.append(values.get("href") or "")
        elif tag == "link" and "stylesheet" in (values.get("rel") or "").lower().split():
            self.stylesheets.append(values.get("href") or "")
        elif tag == "script":
            src = values.get("src")
            if src:
                self.scripts.append(src)
            else:
                self._in_script = True
                self._script_buffer = []
        elif tag == "style":
            self._in_style = True
            self._style_buffer = []
        elif tag == "form":
            form = {
                "action": values.get("action") or "",
                "method": (values.get("method") or "get").lower(),
                "controls": [],
            }
            self.forms.append(form)
            self.form_stack.append(form)
        elif tag in {"button", "input", "select", "textarea"}:
            control = {
                "tag": tag,
                "disabled": "disabled" in values,
                "type": (values.get("type") or "").lower(),
            }
            self.controls.append(control)
            if self.form_stack:
                self.form_stack[-1]["controls"].append(control)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_script:
            self.inline_scripts.append("".join(self._script_buffer))
            self._in_script = False
        elif tag == "style" and self._in_style:
            self.inline_styles.append("".join(self._style_buffer))
            self._in_style = False
        elif tag == "form" and self.form_stack:
            self.form_stack.pop()

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.text.append(data.strip())
        if self._in_title:
            self.title_text.append(data)
        if self._in_script:
            self._script_buffer.append(data)
        if self._in_style:
            self._style_buffer.append(data)


def _inside(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def _safe_local_path(raw: str, source: Path, root: Path, errors: list[str], label: str) -> Path | None:
    value = raw.strip()
    if not value or value.startswith("#"):
        return None
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc:
        errors.append(f"{label}: external or non-file URL is not allowed: {value[:160]}")
        return None
    if value.startswith("//") or value.startswith("\\"):
        errors.append(f"{label}: absolute/network path is not allowed: {value[:160]}")
        return None
    decoded = unquote(parsed.path)
    if not decoded:
        return None
    relative = decoded.lstrip("/") if decoded.startswith("/") else decoded
    candidate = (root / relative if decoded.startswith("/") else source.parent / relative).resolve()
    if not _inside(candidate, root):
        errors.append(f"{label}: reference escapes the private prototype root: {value[:160]}")
        return None
    if not candidate.is_file():
        errors.append(f"{label}: referenced local file is missing: {candidate.relative_to(root).as_posix()}")
        return None
    if candidate.is_symlink():
        errors.append(f"{label}: symlinked local asset is not allowed: {candidate.relative_to(root).as_posix()}")
        return None
    return candidate


def _normalise_asset_reference(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _asset_references_from_srcset(srcset: str) -> list[str]:
    references: list[str] = []
    for candidate in srcset.split(","):
        candidate = candidate.strip()
        if candidate:
            references.append(candidate.split()[0])
    return references


def _audit_owner_approval(manifest: dict[str, object], repo_root: Path, errors: list[str]) -> None:
    if manifest.get("base_decision_ref") != "D-016":
        errors.append("manifest base_decision_ref must be D-016")
    if manifest.get("prototype_mode") != "private-local-nontransactional":
        errors.append("prototype_mode must be private-local-nontransactional")

    approval = manifest.get("owner_visual_approval")
    if not isinstance(approval, dict):
        errors.append("owner_visual_approval object is required")
        return
    if approval.get("status") != "approved":
        errors.append("owner visual approval is not recorded as approved; M2-A must be explicitly approved before prototype build")
        return

    decision_ref = approval.get("decision_ref")
    if not isinstance(decision_ref, str) or not re.fullmatch(r"D-\d{3}", decision_ref):
        errors.append("approved visual direction must reference a numbered owner decision (for example D-017)")
        return

    decision_register = repo_root / "docs/DECISIONS.md"
    if not decision_register.is_file():
        errors.append("repository docs/DECISIONS.md is missing; owner decision cannot be cross-checked")
    else:
        content = decision_register.read_text(encoding="utf-8")
        match = re.search(
            rf"^### {re.escape(decision_ref)}\b([\s\S]*?)(?=^### |\Z)",
            content,
            re.MULTILINE,
        )
        if not match:
            errors.append(f"owner decision register does not contain {decision_ref}")
        else:
            section = match.group(1).lower()
            if "m2-a" not in section or "visual" not in section or "approved" not in section:
                errors.append(f"{decision_ref} does not explicitly record approved M2-A visual direction")

    digest = approval.get("approved_proposal_sha256")
    proposal = repo_root / PROPOSAL_PATH
    if not proposal.is_file():
        errors.append("M2-A visual proposal source is missing from repository")
    elif not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
        errors.append("approved_proposal_sha256 must be a 64-character lowercase SHA-256")
    else:
        actual = hashlib.sha256(proposal.read_bytes()).hexdigest()
        if actual != digest:
            errors.append("approved proposal SHA-256 does not match the current M2-A proposal; approval must be renewed after changes")

    approved_at = approval.get("approved_at")
    if not isinstance(approved_at, str) or not DATE_RE.fullmatch(approved_at):
        errors.append("owner approval date must use YYYY-MM-DD")


def _audit_asset_ledger(
    manifest: dict[str, object],
    root: Path,
    image_refs_by_page: dict[str, set[str]],
    page_text: dict[str, str],
    errors: list[str],
) -> None:
    ledger = manifest.get("asset_ledger")
    if not isinstance(ledger, dict):
        errors.append("asset_ledger object is required, including an entry for each referenced image")
        return

    referenced = set().union(*image_refs_by_page.values()) if image_refs_by_page else set()
    ledger_paths = set(ledger)
    for missing in sorted(referenced - ledger_paths):
        errors.append(f"image asset is missing from asset_ledger: {missing}")
    for unused in sorted(ledger_paths - referenced):
        errors.append(f"asset_ledger contains an unreferenced image: {unused}")

    for rel, metadata in ledger.items():
        if not isinstance(rel, str) or not isinstance(metadata, dict):
            errors.append(f"invalid asset_ledger entry: {rel!r}")
            continue
        candidate = (root / rel).resolve()
        if not _inside(candidate, root) or not candidate.is_file() or candidate.is_symlink():
            errors.append(f"asset_ledger path is missing, unsafe or symlinked: {rel}")
            continue
        if candidate.suffix.lower() not in IMAGE_SUFFIXES:
            errors.append(f"asset_ledger entry must reference an image file: {rel}")
        kind = metadata.get("kind")
        if kind in {"illustrative_frame", "layout_placeholder"}:
            required_label = (
                "ILLUSTRATIVE IMAGE FRAME — DAG PHOTOGRAPH PENDING"
                if kind == "illustrative_frame"
                else "LAYOUT PLACEHOLDER — NOT A DAG PRODUCT"
            )
            if metadata.get("label") != required_label:
                errors.append(f"{rel}: placeholder must use its exact approved label: {required_label}")
            associated_pages = [page for page, refs in image_refs_by_page.items() if rel in refs]
            if not any(required_label in page_text.get(page, "") for page in associated_pages):
                errors.append(f"{rel}: exact placeholder label must be visible on every page where it is used")
        elif kind == "genuine_dag_photo":
            if metadata.get("rights_status") != "cleared" or not metadata.get("rights_evidence_ref"):
                errors.append(f"{rel}: genuine DAG photo requires cleared rights and rights evidence")
            if metadata.get("prototype_use_status") != "approved" or not metadata.get("prototype_use_evidence_ref"):
                errors.append(f"{rel}: genuine DAG photo requires separate private prototype-use approval evidence")
            if not metadata.get("product_record_ref"):
                errors.append(f"{rel}: genuine DAG photo must map to a verified product record")
        else:
            errors.append(f"{rel}: unsupported asset kind {kind!r}")


def validate_private_prototype(prototype_root: Path, repo_root: Path = ROOT) -> dict[str, object]:
    """Validate a completed prototype stored outside the public Git repository."""
    errors: list[str] = []
    repo = repo_root.resolve()
    if prototype_root.is_symlink():
        return {"ok": False, "errors": ["prototype root must not be a symlink"], "routes_checked": 0, "images_checked": 0}

    try:
        root = prototype_root.expanduser().resolve(strict=True)
    except (OSError, RuntimeError):
        return {"ok": False, "errors": ["prototype root does not exist or cannot be resolved"], "routes_checked": 0, "images_checked": 0}

    if not root.is_dir():
        errors.append("prototype root must be a directory")
    if _inside(root, repo):
        errors.append("prototype root must be outside the public repository directory")
    if errors:
        return {"ok": False, "errors": errors, "routes_checked": 0, "images_checked": 0}

    for path in root.rglob("*"):
        if path.is_symlink():
            errors.append(f"symlink is not allowed in private prototype: {path.relative_to(root).as_posix()}")

    manifest_path = root / MANIFEST_NAME
    if not manifest_path.is_file():
        errors.append(f"missing {MANIFEST_NAME}")
        manifest: dict[str, object] = {}
    else:
        try:
            parsed = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest = parsed if isinstance(parsed, dict) else {}
            if not isinstance(parsed, dict):
                errors.append("prototype manifest must contain a JSON object")
        except (OSError, json.JSONDecodeError) as exc:
            manifest = {}
            errors.append(f"prototype manifest is invalid JSON: {exc.__class__.__name__}")

    _audit_owner_approval(manifest, repo, errors)

    declared_routes = manifest.get("routes")
    if not isinstance(declared_routes, list) or tuple(declared_routes) != ROUTES:
        errors.append("manifest routes must equal the exact nine D-014 routes in their approved order")
    expected_areas = {name: list(routes) for name, routes in AREA_ROUTES.items()}
    areas = manifest.get("areas")
    if areas != expected_areas:
        errors.append("manifest areas must equal the exact six D-016 groupings mapped to the nine D-014 routes")

    actual_html = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*.html")
        if path.is_file()
    }
    if actual_html != set(ROUTES):
        missing = sorted(set(ROUTES) - actual_html)
        extra = sorted(actual_html - set(ROUTES))
        if missing:
            errors.append("missing D-014 HTML route(s): " + ", ".join(missing))
        if extra:
            errors.append("unapproved HTML route(s): " + ", ".join(extra))

    image_refs_by_page: dict[str, set[str]] = {}
    page_text: dict[str, str] = {}
    all_assets: set[str] = set()
    for route in ROUTES:
        path = root / route
        if not path.is_file():
            continue
        source = path.read_text(encoding="utf-8", errors="replace")
        parser = PageParser()
        try:
            parser.feed(source)
            parser.close()
        except Exception as exc:
            errors.append(f"{route}: HTML parser error ({exc.__class__.__name__})")
            continue
        text = " ".join(parser.text)
        page_text[route] = text
        if parser.lang != "en":
            errors.append(f"{route}: customer-facing prototype must declare lang='en'")
        if parser.title_count != 1 or not "".join(parser.title_text).strip():
            errors.append(f"{route}: exactly one non-empty title is required")
        if parser.h1_count != 1:
            errors.append(f"{route}: exactly one h1 is required")
        if parser.main_count != 1:
            errors.append(f"{route}: exactly one main landmark is required")

        page_refs: set[str] = set()
        if parser.base_hrefs:
            errors.append(f"{route}: base href is not permitted in a private prototype")
        if parser.meta_refresh:
            errors.append(f"{route}: meta refresh navigation is not permitted")
        if parser.embedded_content:
            errors.append(f"{route}: embedded/remote media elements are not permitted: {', '.join(sorted(set(parser.embedded_content)))}")
        for href in parser.links:
            if not href:
                errors.append(f"{route}: anchor has an empty href")
                continue
            parsed_href = urlsplit(href)
            if parsed_href.scheme in {"mailto", "tel"}:
                continue
            if TRANSACTION_TARGET.search(parsed_href.path):
                errors.append(f"{route}: transactional destination is not allowed: {href[:160]}")
            _safe_local_path(href, path, root, errors, f"{route} link")

        for image_src, alt, srcset in parser.images:
            if not alt.strip():
                errors.append(f"{route}: every image must have a non-empty alt attribute")
            candidates = [image_src] + _asset_references_from_srcset(srcset)
            for raw in candidates:
                if not raw:
                    errors.append(f"{route}: image is missing a local src")
                    continue
                asset = _safe_local_path(raw, path, root, errors, f"{route} image")
                if asset:
                    if asset.suffix.lower() not in IMAGE_SUFFIXES:
                        errors.append(f"{route}: referenced img/srcset file is not a supported image: {raw}")
                    else:
                        rel = _normalise_asset_reference(asset, root)
                        page_refs.add(rel)
                        all_assets.add(rel)

        stylesheet_sources: list[tuple[Path, str]] = []
        for href in parser.stylesheets:
            sheet = _safe_local_path(href, path, root, errors, f"{route} stylesheet")
            if sheet:
                stylesheet_sources.append((sheet, sheet.read_text(encoding="utf-8", errors="replace")))
        for style in parser.inline_styles:
            stylesheet_sources.append((path, style))
        for sheet_path, css in stylesheet_sources:
            for imported in re.finditer(r"""@import\s+(?:url\(\s*)?['"]?([^'")\s;]+)""", css, re.I):
                _safe_local_path(imported.group(1), sheet_path, root, errors, f"{route} CSS import")
            for match in CSS_URL.finditer(css):
                raw = match.group(2).strip()
                if not raw or raw.startswith("data:") or raw.startswith("#"):
                    if raw.startswith("data:"):
                        errors.append(f"{route}: embedded data URI assets are not allowed")
                    continue
                asset = _safe_local_path(raw, sheet_path, root, errors, f"{route} CSS asset")
                if asset and asset.suffix.lower() in IMAGE_SUFFIXES:
                    rel = _normalise_asset_reference(asset, root)
                    page_refs.add(rel)
                    all_assets.add(rel)

        script_sources = [(path, code) for code in parser.inline_scripts]
        for src in parser.scripts:
            script = _safe_local_path(src, path, root, errors, f"{route} script")
            if script:
                script_sources.append((script, script.read_text(encoding="utf-8", errors="replace")))
        for script_path, code in script_sources:
            for label, pattern in NETWORK_PATTERNS:
                if pattern.search(code):
                    errors.append(f"{route}: disallowed {label} capability in {script_path.name}")
            for match in re.finditer(r"""(?:href|src|location(?:\.href)?)\s*=\s*['"]([^'"]+)['"]""", code, re.I):
                if TRANSACTION_TARGET.search(urlsplit(match.group(1)).path):
                    errors.append(f"{route}: transactional destination in script: {match.group(1)[:120]}")

        for form in parser.forms:
            action = str(form["action"])
            if action and action != "#":
                errors.append(f"{route}: forms must not have an action endpoint")
            if form["method"] != "get":
                errors.append(f"{route}: forms must not use POST or another write method")
        for form_match in re.finditer(r"<form\\b[^>]*>([\\s\\S]*?)</form\\s*>", source, re.I):
            for control_match in re.finditer(r"<(?:button|input|select|textarea)\\b([^>]*)>", form_match.group(1), re.I):
                if not re.search(r"(?:^|\\s)disabled(?:\\s|=|/?>)", control_match.group(1), re.I):
                    errors.append(f"{route}: every control inside a prototype form must remain disabled")
                    break

        for control in parser.controls:
            if control["tag"] == "button" and control["type"] == "submit" and not control["disabled"]:
                errors.append(f"{route}: submit buttons must remain disabled")

        image_refs_by_page[route] = page_refs

    _audit_asset_ledger(manifest, root, image_refs_by_page, page_text, errors)

    return {
        "ok": not errors,
        "errors": errors,
        "routes_checked": sum(1 for route in ROUTES if (root / route).is_file()),
        "images_checked": len(all_assets),
        "prototype_root_is_private_to_repo": not _inside(root, repo),
        "areas_checked": len(AREA_ROUTES),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the D-016 private, non-transactional prototype entry gates."
    )
    parser.add_argument(
        "--prototype-root",
        required=True,
        type=Path,
        help="absolute or relative path to the prototype directory outside this public repository",
    )
    args = parser.parse_args()
    result = validate_private_prototype(args.prototype_root)
    print("DAG private prototype validation: " + ("PASS" if result["ok"] else "FAIL"))
    print(f"- Routes checked: {result['routes_checked']}/9")
    print(f"- D-016 areas checked: {result.get('areas_checked', 0)}/6")
    print(f"- Image assets checked: {result['images_checked']}")
    print("- Prototype source remains outside the public repository.")
    for error in result["errors"]:
        print(f"- {error}")
    if result["ok"]:
        print("- Owner M2-A approval reference, proposal hash and asset evidence are present.")
        print("- No external resources, active transactions, form endpoints or network APIs were detected.")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
