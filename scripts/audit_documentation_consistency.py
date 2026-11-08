#!/usr/bin/env python3
"""Context-aware repository-wide DAG documentation and instruction audit.

Scans tracked files across the whole repository. Historical material is checked
for an archival banner and excluded from active-instruction pattern matching.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HISTORICAL_PREFIXES = (
    "docs/historical/",
)
TEXT_SUFFIXES = {
    ".md", ".html", ".htm", ".css", ".js", ".mjs", ".cjs", ".py",
    ".yml", ".yaml", ".txt", ".sh",
}
ARCHIVE_BANNER = "HISTORICAL — NOT ACTIVE — DO NOT IMPLEMENT"

# Patterns are deliberately limited to stale active directives/state, not
# mere mentions of retired concepts in decision registers or audit reports.
ACTIVE_STALE_PATTERNS = (
    ("old kit materialization blocker", re.compile(r"(?:once|when) the owner[- ]supplied archive is materialized", re.I)),
    ("old kit materialization blocker", re.compile(r"source[- ]materialization blocker", re.I)),
    ("old kit materialization instruction", re.compile(r"verify that the files are actually present before claiming installation", re.I)),
    ("AI visual-option workflow", re.compile(r"(?:create|prepare|present) at least four (?:materially )?different (?:creative )?territor(?:y|ies|ies)", re.I)),
    ("AI visual-option workflow", re.compile(r"ask the owner which (?:territory|option) to choose, combine or reject", re.I)),
    ("AI visual-option workflow", re.compile(r"current alternatives are.{0,120}(?:Graphic Atelier|Future Relics|Living Garden|Modern Folk Pop)", re.I)),
    ("legacy palette directive", re.compile(r"(?:default to|must use|use as the primary palette).{0,80}(?:beige|ivory|sand|terracotta)", re.I)),
    ("legacy typography directive", re.compile(r"(?:must use|use the).{0,80}(?:old|legacy).{0,40}(?:font|typeface|pairing)", re.I)),
    ("Japanese UI directive", re.compile(r"(?:must|should|required to) (?:use|include|publish|provide).{0,100}(?:Japanese[- ]language|Japanese UI|bilingual storefront)", re.I)),
    ("fabricated catalogue example directive", re.compile(r"(?:use|insert|publish).{0,100}(?:fictional|invented|fabricated) (?:product|maker|business)", re.I)),
)

def tracked_paths(root: Path = ROOT) -> list[str]:
    """Use Git's tracked-file index so untracked/generated files are excluded."""
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=root,
            check=True,
            capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise RuntimeError(f"cannot enumerate tracked paths with git ls-files: {exc}") from exc
    return sorted(p.decode("utf-8", errors="strict") for p in result.stdout.split(b"\0") if p)


def is_historical(path: str) -> bool:
    return any(path.startswith(prefix) for prefix in HISTORICAL_PREFIXES)


def audit_repository(root: Path = ROOT) -> dict:
    paths = tracked_paths(root)
    errors: list[str] = []
    warnings: list[str] = []
    historical_paths = [p for p in paths if is_historical(p)]
    active_text_paths = [
        p for p in paths
        if not is_historical(p) and Path(p).suffix.lower() in TEXT_SUFFIXES
    ]

    for path in historical_paths:
        if Path(path).suffix.lower() not in {".md", ".html", ".htm"}:
            continue
        content = (root / path).read_text(encoding="utf-8", errors="replace")
        if ARCHIVE_BANNER not in content[:700]:
            errors.append(f"{path}: historical artifact lacks the mandatory non-operative banner")

    for path in active_text_paths:
        content = (root / path).read_text(encoding="utf-8", errors="replace")
        for number, line in enumerate(content.splitlines(), start=1):
            # Do not flag a line whose purpose is explicitly to say the phrase
            # is retired, historical, superseded, or not an instruction.
            lower = line.lower()
            if any(word in lower for word in ("historical", "not active", "do not revive", "superseded", "rejected", "non-operative", "not a default", "not authorized")):
                continue
            for label, pattern in ACTIVE_STALE_PATTERNS:
                if pattern.search(line):
                    errors.append(f"{path}:{number}: possible active stale instruction ({label}): {line.strip()[:180]}")

    required = (
        "AGENTS.md",
        "README.md",
        "HANDOFF-PROMPT.md",
        "docs/DECISIONS.md",
        "docs/DESIGN-AUTHORITY.md",
        "docs/DOCUMENTATION-SOURCE-OF-TRUTH.md",
        "docs/PAGE-INVENTORY.md",
        "docs/COMPONENT-INVENTORY.md",
        "docs/DOCUMENTATION-RECONCILIATION-MATRIX.md",
        "docs/DOCUMENTATION-RECONCILIATION-REPORT.md",
        "docs/DOCUMENTATION-RECONCILIATION-CHECKLIST.md",
        "docs/DOCUMENTATION-CHANGELOG.md",
    )
    missing = [p for p in required if p not in paths]
    for path in missing:
        errors.append(f"required governance file is not tracked: {path}")

    source_path = root / "docs/DOCUMENTATION-SOURCE-OF-TRUTH.md"
    if source_path.is_file():
        source = source_path.read_text(encoding="utf-8")
        hierarchy = [
            "Explicit owner-approved decisions",
            "Root `AGENTS.md`",
            "`docs/DESIGN-AUTHORITY.md`",
            "This document",
            "Owner-approved design specifications",
            "Current page and component inventories",
            "Technical and implementation documentation",
            "Historical documents",
        ]
        # Order check is robust to formatting details but exact to the required
        # authority sequence.
        positions = [source.find(item) for item in hierarchy]
        if any(pos < 0 for pos in positions) or positions != sorted(positions):
            errors.append("source-of-truth document does not state the required eight-level authority hierarchy in order")

    return {
        "tracked_files": len(paths),
        "historical_files": len(historical_paths),
        "active_text_files": len(active_text_paths),
        "errors": errors,
        "warnings": warnings,
        "historical_paths": historical_paths,
        "active_text_paths": active_text_paths,
    }


def main() -> int:
    try:
        result = audit_repository()
    except RuntimeError as exc:
        print(f"Repository documentation audit: FAILED — {exc}")
        return 2

    if result["errors"]:
        print(f"Repository documentation audit: FAILED ({len(result['errors'])} finding(s))")
        print(f"- Tracked files: {result['tracked_files']}")
        print(f"- Active text files scanned: {result['active_text_files']}")
        print(f"- Historical files checked: {result['historical_files']}")
        for error in result["errors"]:
            print(f"- {error}")
        return 1

    print("Repository documentation audit: PASS")
    print(f"- Tracked files enumerated: {result['tracked_files']}")
    print(f"- Active text/source files scanned: {result['active_text_files']}")
    print(f"- Historical paths checked for non-operative labels: {result['historical_files']}")
    print("- Retired concepts may remain in decision/audit context; live stale directives are checked separately.")
    print("- Required governance paths are tracked and the eight-level authority hierarchy is ordered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
