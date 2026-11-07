#!/usr/bin/env python3
"""Check local Markdown links in active DAG documentation and kit files."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")


def active_markdown_files(root: Path = ROOT) -> list[Path]:
    files = []
    for path in root.rglob("*.md"):
        relative = path.relative_to(root).as_posix()
        if relative.startswith("docs/historical/"):
            continue
        if any(part in {".git", "node_modules", "vendor"} for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def audit_links(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for source in active_markdown_files(root):
        text = source.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            destination = match.group(1).strip()
            if not destination:
                continue
            # Markdown permits optional titles after the destination.
            destination = destination.split(maxsplit=1)[0]
            destination = destination.strip("<>")
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc:
                continue
            if not parsed.path:
                continue
            target = (source.parent / unquote(parsed.path)).resolve()
            try:
                target.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{source.relative_to(root)}: link escapes repository: {destination}")
                continue
            if not target.exists():
                errors.append(f"{source.relative_to(root)}: missing local target: {destination}")
    return errors


def main() -> int:
    files = active_markdown_files()
    errors = audit_links()
    if errors:
        print(f"Documentation link audit: FAILED ({len(errors)} issue(s), {len(files)} files scanned)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Documentation link audit: PASS ({len(files)} active Markdown files scanned)")
    print("- All local inline Markdown links resolve to repository paths.")
    print("- Historical archives are retained as read-only evidence and excluded from active-link enforcement.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
