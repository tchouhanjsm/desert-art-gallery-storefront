#!/usr/bin/env python3
"""Validate DAG foundation and owner-controlled visual exploration (stdlib only)."""
from __future__ import annotations
import re, sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
 ".github/ISSUE_TEMPLATE/.gitkeep",".github/workflows/.gitkeep",".github/workflows/project-quality.yml",
 "AGENTS.md","README.md","design/README.md","design/approved/.gitkeep","design/explorations/.gitkeep",
 "design/explorations/visual-directions.html","design/prototypes/.gitkeep",
 "docs/00-PROJECT-CHARTER.md","docs/01-DESIGN-PHILOSOPHY.md","docs/02-BRAND-IDENTITY.md",
 "docs/03-CREATIVE-DIRECTION.md","docs/04-VISUAL-DESIGN-SYSTEM.md","docs/05-ART-DIRECTION-AND-PHOTOGRAPHY.md",
 "docs/06-CONTENT-STRATEGY.md","docs/07-INFORMATION-ARCHITECTURE.md","docs/08-TECHNICAL-ARCHITECTURE.md",
 "docs/09-QUALITY-AND-ACCEPTANCE.md","docs/10-ROADMAP.md","docs/11-CUSTOMER-AND-MERCHANDISING-STRATEGY.md",
 "docs/12-MERCHANT-OPERATIONS.md","docs/13-DESIGN-REVIEW-PROTOCOL.md","docs/14-OWNER-CONTROLLED-VISUAL-DIRECTION.md",
 "docs/15-CREATIVE-DIRECTION-OPTIONS.md","docs/15-FOUR-VISUAL-DIRECTION-SPECIFICATIONS.md","docs/ADR-TEMPLATE.md",
 "docs/AI-BOOTSTRAP-PROMPT.md","docs/AI-WORKING-PROTOCOL.md","docs/DECISIONS.md",
 "docs/OWNER-INPUT-REGISTER.md","docs/REFERENCE-RESEARCH-LOG.md","docs/UPDATE-VISUAL-OWNER-GATE-PROMPT.md",
 "scripts/validate_project.py","tests/test_project_validation.py"]
OPTIONS=["Graphic Atelier","Future Relics","Living Garden","Modern Folk Pop"]
FONTS=["Inter","Noto Sans Display","PT Mono","EB Garamond","Lato","Comfortaa"]
RENDERS=[f"design/explorations/rendered/{name}-{device}.svg"
 for name in ["graphic-atelier","future-relics","living-garden","modern-folk-pop"] for device in ["desktop","mobile"]]
LINK=re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HEADING=re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
HEX=re.compile(r"#[0-9A-Fa-f]{6}\b")

def heading_slug(value: str) -> str:
 value=re.sub(r"[\x60*_]","",value.strip().lower())
 value=re.sub(r"[^a-z0-9\- ]","",value)
 return re.sub(r"\s+","-",value).strip("-")

def markdown_links(source: str) -> list[str]:
 return [m.group(1).strip() for m in LINK.finditer(source)]

def check_markdown_file(path: Path, root: Path=ROOT) -> list[str]:
 errors=[]; content=path.read_text(encoding="utf-8"); last=0
 for no,line in enumerate(content.splitlines(),1):
  h=HEADING.match(line)
  if h:
   level=len(h.group(1))
   if last and level>last+1: errors.append(f"{path.relative_to(root)}:{no}: heading jump H{last} to H{level}")
   last=level
 for target in markdown_links(content):
  u=urlsplit(target)
  if u.scheme or u.netloc or target.startswith(("mailto:","tel:")): continue
  dest=(path.parent/unquote(u.path)).resolve() if u.path else path.resolve()
  if not dest.exists(): errors.append(f"{path.relative_to(root)}: broken link {target}"); continue
  if u.fragment and dest.is_file() and dest.suffix.lower()==".md":
   anchors={heading_slug(m.group(2)) for line in dest.read_text(encoding="utf-8").splitlines() if (m:=HEADING.match(line))}
   if unquote(u.fragment).lower() not in anchors: errors.append(f"{path.relative_to(root)}: broken anchor {target}")
 return errors

class BoardParser(HTMLParser):
 VOID={"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}
 def __init__(self): super().__init__(convert_charrefs=True); self.stack=[]; self.errors=[]; self.cards=0; self.viewport=False; self.lang_en=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=="html" and a.get("lang","").lower()=="en": self.lang_en=True
  if tag=="meta" and a.get("name","").lower()=="viewport": self.viewport=True
  if tag=="article" and "option" in a.get("class","").split(): self.cards+=1
  if tag not in self.VOID: self.stack.append(tag)
 def handle_endtag(self,tag):
  if tag in self.VOID:return
  if not self.stack or self.stack[-1]!=tag:self.errors.append(f"unexpected or mismatched </{tag}>")
  else:self.stack.pop()

def validate_project(root: Path=ROOT) -> list[str]:
 errors=[]
 for p in REQUIRED+RENDERS:
  if not (root/p).is_file(): errors.append(f"missing required file: {p}")
 for md in sorted(root.rglob("*.md")):
  try: md.read_text(encoding="utf-8"); errors.extend(check_markdown_file(md,root))
  except UnicodeDecodeError as exc: errors.append(f"invalid UTF-8 {md.relative_to(root)}: {exc}")
 names=["AGENTS.md","README.md","docs/03-CREATIVE-DIRECTION.md","docs/04-VISUAL-DESIGN-SYSTEM.md",
 "docs/09-QUALITY-AND-ACCEPTANCE.md","docs/14-OWNER-CONTROLLED-VISUAL-DIRECTION.md",
 "docs/AI-WORKING-PROTOCOL.md","docs/DECISIONS.md","docs/10-ROADMAP.md","docs/M1-OWNER-REVIEW.md"]
 docs={n:(root/n).read_text(encoding="utf-8") for n in names if (root/n).exists()}
 for n in names[:7]:
  t=docs.get(n,"")
  if not all(x in t for x in ["THE AI PROPOSES","THE OWNER CHOOSES","THE AI IMPLEMENTS"]): errors.append(f"{n}: missing owner-control rule")
 if "Japan-first" not in docs.get("AGENTS.md","") or "English-only" not in docs.get("AGENTS.md",""): errors.append("AGENTS.md missing confirmed Japan-first/English-only principles")
 if "14-OWNER-CONTROLLED-VISUAL-DIRECTION.md" not in docs.get("README.md",""): errors.append("README does not link owner-control policy")
 if "not a default" not in docs.get("docs/AI-WORKING-PROTOCOL.md","").lower(): errors.append("AI protocol does not retire prior synthesis as default")
 if "D-007" not in docs.get("docs/DECISIONS.md","") or "CONFIRMED" not in docs.get("docs/DECISIONS.md",""): errors.append("decision register missing confirmed D-007")
 if "P-015" not in docs.get("docs/DECISIONS.md","") or "no winner" not in docs.get("docs/DECISIONS.md","").lower(): errors.append("decision register missing no-winner proposal P-015")
 if "no option is recommended" not in docs.get("docs/M1-OWNER-REVIEW.md","").lower(): errors.append("owner review must say no option is recommended")
 if "four" not in docs.get("docs/10-ROADMAP.md","").lower() or "owner" not in docs.get("docs/10-ROADMAP.md","").lower(): errors.append("roadmap missing four-option owner gate")
 spec=root/"docs/15-FOUR-VISUAL-DIRECTION-SPECIFICATIONS.md"
 if spec.exists():
  t=spec.read_text(encoding="utf-8")
  for n in OPTIONS:
   if n not in t: errors.append(f"specification missing {n}")
  if len(set(HEX.findall(t)))<20: errors.append("specification requires 20+ exact HEX values")
  for f in FONTS:
   if f not in t: errors.append(f"specification missing font {f}")
  if "no option is recommended" not in t.lower(): errors.append("specification must state no option is recommended")
 board=root/"design/explorations/visual-directions.html"
 if board.exists():
  t=board.read_text(encoding="utf-8"); p=BoardParser(); p.feed(t); p.close(); errors.extend(p.errors)
  if p.stack: errors.append(f"unclosed HTML tags: {p.stack[-8:]}")
  if p.cards!=4: errors.append(f"expected four option cards, found {p.cards}")
  if not p.viewport or not p.lang_en: errors.append("board missing English lang or viewport metadata")
  if len(set(HEX.findall(t)))<20: errors.append("board must show 20+ HEX values")
  for n in OPTIONS+FONTS:
   if n not in t: errors.append(f"board missing {n}")
  for bp in ["max-width:900px","max-width:520px"]:
   if bp not in t: errors.append(f"board missing breakpoint {bp}")
  if "not dag product" not in t.lower(): errors.append("board must label abstract placeholders as not DAG product")
  for cls in ["o1","o2","o3","o4"]:
   match=re.search(rf'<article class="option {cls}">(.*?)</article>',t,re.S)
   if not match: errors.append(f"board option {cls} missing")
   elif re.search(r"recommended|preferred|winner|best direction",match.group(1),re.I): errors.append(f"board option {cls} contains winner language")
 for forbidden in ["package.json","package-lock.json","pnpm-lock.yaml","yarn.lock","composer.json","Dockerfile","docker-compose.yml","docker-compose.yaml"]:
  if (root/forbidden).exists(): errors.append(f"out-of-scope app/infrastructure file: {forbidden}")
 return errors

def main() -> int:
 errors=validate_project()
 if errors:
  print(f"DAG governance validation: FAILED ({len(errors)} issue(s))")
  for e in errors: print(f"- {e}")
  return 1
 print("DAG governance validation: PASS")
 print(f"- {len(REQUIRED)} foundation/governance paths present")
 print(f"- {len(RENDERS)} desktop/mobile SVG direction previews present")
 print("- Markdown UTF-8, internal links and heading hierarchy pass")
 print("- owner-control gate, no-winner rule and historical-default retirement pass")
 print("- four territories, exact HEX palettes, typography and responsive board pass")
 print("- no app/framework/database/hosting scaffold introduced")
 return 0

if __name__=="__main__": sys.exit(main())
