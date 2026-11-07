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
 "design/explorations/visual-directions.html","design/explorations/reference-led-directions.html","design/prototypes/.gitkeep",
 "docs/00-PROJECT-CHARTER.md","docs/01-DESIGN-PHILOSOPHY.md","docs/02-BRAND-IDENTITY.md",
 "docs/03-CREATIVE-DIRECTION.md","docs/04-VISUAL-DESIGN-SYSTEM.md","docs/05-ART-DIRECTION-AND-PHOTOGRAPHY.md",
 "docs/06-CONTENT-STRATEGY.md","docs/07-INFORMATION-ARCHITECTURE.md","docs/08-TECHNICAL-ARCHITECTURE.md",
 "docs/09-QUALITY-AND-ACCEPTANCE.md","docs/10-ROADMAP.md","docs/11-CUSTOMER-AND-MERCHANDISING-STRATEGY.md",
 "docs/12-MERCHANT-OPERATIONS.md","docs/13-DESIGN-REVIEW-PROTOCOL.md","docs/14-OWNER-CONTROLLED-VISUAL-DIRECTION.md","docs/15-REFERENCE-TO-DAG-IMPLEMENTATION-SPEC.md",
 "docs/15-CREATIVE-DIRECTION-OPTIONS.md","docs/15-FOUR-VISUAL-DIRECTION-SPECIFICATIONS.md","docs/17-REFERENCE-LED-DESIGN-BRIEF.md","docs/18-REFERENCE-LED-DIRECTION-SPECIFICATIONS.md","docs/19-PHOTO-LIBRARY-AUDIT.md","docs/20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md","docs/21-ETSY-SOURCE-EXPORT-MAPPING-AND-RECONCILIATION.md","docs/ADR-TEMPLATE.md",
 "docs/AI-BOOTSTRAP-PROMPT.md","docs/AI-WORKING-PROTOCOL.md","docs/DECISIONS.md",
 "docs/OWNER-INPUT-REGISTER.md","docs/REFERENCE-RESEARCH-LOG.md","docs/UPDATE-VISUAL-OWNER-GATE-PROMPT.md",
 "scripts/validate_project.py","scripts/audit_photo_library.py","scripts/validate_catalogue_intake.py","scripts/preview_etsy_export.py","tests/test_project_validation.py","tests/test_photo_library_audit.py","tests/test_catalogue_intake.py","tests/test_etsy_export_preview.py","templates/catalogue/README.md","templates/catalogue/products.csv","templates/catalogue/product-facts.csv","templates/catalogue/product-images.csv","templates/catalogue/product-source-records.csv","templates/catalogue/etsy-image-sources.csv"]
OPTIONS=["Graphic Atelier","Future Relics","Living Garden","Modern Folk Pop"]
REFERENCE_OPTIONS=["Porcelain Index","Bordeaux Editions","Blue Current","Citron Signal"]
REFERENCE_FONTS=["Cormorant Garamond","Manrope","Fraunces","DM Sans","Newsreader","Work Sans","Space Grotesk","IBM Plex Mono"]
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
 def __init__(self):
  super().__init__(convert_charrefs=True)
  self.stack=[]; self.errors=[]; self.cards=0; self.viewport=False; self.lang_en=False
  self.main_count=0; self.main_ids=[]; self.skip_links=[]; self.h1_count=0; self.h2_ids=set()
  self.option_labels=[]; self.preview_groups=[]; self.ids=set(); self.duplicate_ids=[]; self.images_missing_alt=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=="html" and a.get("lang","").lower()=="en": self.lang_en=True
  if tag=="meta" and a.get("name","").lower()=="viewport": self.viewport=True
  if a.get("id"):
   if a["id"] in self.ids: self.duplicate_ids.append(a["id"])
   self.ids.add(a["id"])
  if tag=="main":
   self.main_count+=1
   if a.get("id"): self.main_ids.append(a["id"])
  if tag=="a" and "skip-link" in a.get("class","").split():
   self.skip_links.append(a.get("href",""))
  if tag=="h1": self.h1_count+=1
  if tag=="h2" and a.get("id"): self.h2_ids.add(a["id"])
  if tag=="article" and "option" in a.get("class","").split():
   self.cards+=1
   self.option_labels.append(a.get("aria-labelledby",""))
  if a.get("role")=="group": self.preview_groups.append(a.get("aria-label",""))
  if tag=="img" and "alt" not in a: self.images_missing_alt.append(a.get("src","(missing src)"))
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
 if "D-008" not in docs.get("docs/DECISIONS.md","") or "My DAG visual direction decision: reject." not in docs.get("docs/DECISIONS.md",""): errors.append("decision register missing explicit owner rejection D-008")
 if "D-009" not in docs.get("docs/DECISIONS.md","") or "pojstudio.com" not in docs.get("docs/DECISIONS.md","") or "shop.macaro-ni.jp" not in docs.get("docs/DECISIONS.md",""): errors.append("decision register missing reference decision D-009")
 if "D-010" not in docs.get("docs/DECISIONS.md","") or "Status: CONFIRMED" not in docs.get("docs/DECISIONS.md","") or "DAG's reference fidelity is BLEND" not in docs.get("docs/DECISIONS.md",""): errors.append("decision register missing confirmed D-010 reference hierarchy")
 spec15 = root/"docs/15-REFERENCE-TO-DAG-IMPLEMENTATION-SPEC.md"
 if spec15.exists():
  st=spec15.read_text(encoding="utf-8")
  for term in ["POJ Studio leads","Macaroni Shoten informs","M2 prototype gate","Responsive and interaction matrix","CSS and frontend architecture","Owner-approved reference hierarchy"]:
   if term not in st: errors.append(f"reference implementation specification missing {term}")
  for page in ["Homepage","Shop / All Products","Category landing page","Collection page","Product detail page","Search results","Cart","Checkout","Maker / Artisan profile","About DAG","Journal / Stories index","Journal / Story article","Contact / Customer support","Curated collection","Account","Wishlist","Shipping","Legal"]:
   if page.lower() not in st.lower(): errors.append(f"reference implementation specification missing page {page}")
 else: errors.append("missing reference-to-DAG implementation specification")
 if "15-REFERENCE-TO-DAG-IMPLEMENTATION-SPEC.md" not in docs.get("README.md",""): errors.append("README does not link reference-to-DAG implementation specification")
 if "P-015" not in docs.get("docs/DECISIONS.md","") or "Status: REJECTED" not in docs.get("docs/DECISIONS.md",""): errors.append("decision register must mark P-015 rejected")
 brief = root/"docs/17-REFERENCE-LED-DESIGN-BRIEF.md"
 if brief.exists():
  bt=brief.read_text(encoding="utf-8").lower()
  for term in ["poj studio","macaroni shoten","pixel-for-pixel","at least four","jaisalmer"]:
   if term not in bt: errors.append(f"reference-led brief missing {term}")
 else: errors.append("missing reference-led design brief")

 if "P-015" not in docs.get("docs/DECISIONS.md","") or "no winner" not in docs.get("docs/DECISIONS.md","").lower(): errors.append("decision register missing no-winner proposal P-015")
 if "no option is recommended" not in docs.get("docs/M1-OWNER-REVIEW.md","").lower() or "rejected" not in docs.get("docs/M1-OWNER-REVIEW.md","").lower(): errors.append("owner review must record rejection and preserve no-recommendation rule")
 reference_spec=root/"docs/18-REFERENCE-LED-DIRECTION-SPECIFICATIONS.md"
 if reference_spec.exists():
  rt=reference_spec.read_text(encoding="utf-8")
  for n in REFERENCE_OPTIONS:
   if n not in rt: errors.append(f"reference-led specification missing {n}")
  for f in REFERENCE_FONTS:
   if f not in rt: errors.append(f"reference-led specification missing font {f}")
  if len(set(HEX.findall(rt)))<24: errors.append("reference-led specification requires 24+ exact HEX values")
  if "none is recommended" not in rt.lower(): errors.append("reference-led specification must state no option is recommended")
 else: errors.append("missing reference-led direction specifications")
 reference_board=root/"design/explorations/reference-led-directions.html"
 if reference_board.exists():
  rt=reference_board.read_text(encoding="utf-8"); rp=BoardParser(); rp.feed(rt); rp.close(); errors.extend(rp.errors)
  if rp.stack: errors.append(f"unclosed reference board HTML tags: {rp.stack[-8:]}")
  if rp.cards!=4: errors.append(f"expected four reference-led option cards, found {rp.cards}")
  if not rp.viewport or not rp.lang_en: errors.append("reference board missing English lang or viewport metadata")
  if rp.main_count != 1 or len(rp.main_ids) != 1: errors.append("reference board must expose one main landmark with an id")
  elif f"#{rp.main_ids[0]}" not in rp.skip_links: errors.append("reference board skip link must target the main landmark")
  if rp.h1_count != 1: errors.append(f"reference board must contain one page H1, found {rp.h1_count}")
  if len(rp.option_labels) != 4 or any(label not in rp.h2_ids for label in rp.option_labels): errors.append("each reference option must be labelled by its own H2")
  if rp.preview_groups.count("Desktop layout preview") != 4 or rp.preview_groups.count("Mobile layout preview") != 4: errors.append("each reference option must expose labelled desktop and mobile preview groups")
  if rp.duplicate_ids: errors.append(f"reference board contains duplicate ids: {sorted(set(rp.duplicate_ids))}")
  if rp.images_missing_alt: errors.append(f"reference board contains images without alt text: {rp.images_missing_alt}")
  if ":focus-visible" not in rt: errors.append("reference board is missing a visible keyboard focus style")
  for n in REFERENCE_OPTIONS+REFERENCE_FONTS:
   if n not in rt: errors.append(f"reference board missing {n}")
  if "Desktop layout preview" not in rt or "Mobile layout preview" not in rt: errors.append("reference board missing labelled desktop/mobile layout previews")
  if "not dag products" not in rt.lower(): errors.append("reference board must label placeholders as not DAG products")
  if "max-width:900px" not in rt: errors.append("reference board missing responsive breakpoint")
 else: errors.append("missing reference-led visual board")

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
 print(f"- {len(RENDERS)} archived desktop/mobile SVG previews and four fresh reference-led previews present")
 print("- Markdown UTF-8, internal links and heading hierarchy pass")
 print("- owner-control gate, explicit P-015 rejection, new reference decision and no-clone boundary pass")
 print("- reference-led owner-review board landmarks, keyboard access and preview labels pass")
 print("- archived rejection and fresh four-option palettes, fonts and responsive render board pass")
 print("- D-010 reference hierarchy and page-by-page responsive implementation specification pass")
 print("- photo inventory and draft catalogue intake tools are documented; no app/framework/database/hosting scaffold introduced")
 return 0

if __name__=="__main__": sys.exit(main())
