#!/usr/bin/env python3
"""Check the activity catalog and build the explorer and the catalog page.

Reads catalog/concepts.toml and catalog/weeks/*.toml, finds each week's current
print files, and writes explorer/index.html and CATALOG.md.

    python3 catalog/build.py            # check and build
    python3 catalog/build.py --check    # check only
    python3 catalog/build.py --fragment out.html   # also write the page body alone
"""
import argparse
import html
import json
import math
import random
import re
import sys
import tomllib
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAT = ROOT / "catalog"
YEAR2 = ROOT / "lowell-math-circle-year-2"
REPO_URL = "https://github.com/jamesrp/math-circle-worksheets/blob/main/"

BANDS = ["K-1", "2-3", "4-5"]
STATUSES = ["piloted", "organizer-approved", "unpiloted"]
VERDICTS = ["keep", "revise", "revised", "rework", "merge", "none"]
APP_DECISIONS = ["in app", "not porting", "open"]
KINDS = ["leads-to", "revisits", "same-theorem", "same-object", "contrast"]
REQUIRED = ["week", "title", "hook", "math", "concepts", "mechanisms", "bands",
            "reading", "arithmetic", "materials", "status", "verdict", "app", "app_decision"]
OPTIONAL = ["discover", "gem", "uses", "prep", "verdict_note", "related", "proposed_concepts"]

# Collections the library was built in, by week number.
SERIES = [
    (1, 10, "Fall 2026 core weeks"),
    (11, 51, "Generated library"),
    (52, 63, "New themes"),
    (64, 65, "Octagon surfaces"),
    (66, 75, "Geometric group theory"),
    (76, 78, "Frontier prototypes"),
    (79, 84, "Infinity and knowledge"),
    (85, 91, "Seven reserved families"),
    (92, 97, "Analysis, inference and number theory"),
    (98, 100, "Final breadth"),
]

# Print-file roles, by filename suffix after "week-NN-".
FILE_ROLES = [
    ("k-1.pdf", "K–1 packet"),
    ("grades-2-3.pdf", "Grades 2–3 packet"),
    ("grades-4-5.pdf", "Grades 4–5 packet"),
    ("grades-3-5.pdf", "Grades 3–5 packet"),
    ("students.pdf", "Shared student packet"),
    ("shared.pdf", "Shared student packet"),
    ("upper.pdf", "Upper packet"),
    ("line.pdf", "Line packet"),
    ("shared-catalog.pdf", "Compact catalog"),
    ("shared-catalog-upper.pdf", "Compact catalog, upper"),
    ("shared-catalog-boards.pdf", "Compact catalog boards"),
    ("shared-catalog-facilitator.pdf", "Compact catalog adult guide"),
    ("facilitator.pdf", "Adult guide"),
    ("materials.pdf", "Materials to print"),
    ("extra-rhombi.pdf", "Paper rhombi"),
    ("return-visit.pdf", "Return visit"),
    ("return-visit-facilitator.pdf", "Return visit guide"),
    ("bonus.pdf", "Bonus"),
    ("bonus-facilitator.pdf", "Bonus guide"),
    ("bonus-challenges.pdf", "Bonus challenges"),
    ("extensions.pdf", "Extensions"),
    ("extensions-facilitator.pdf", "Extensions guide"),
]
STUDENT_ROLES = {"K–1 packet", "Grades 2–3 packet", "Grades 4–5 packet", "Grades 3–5 packet",
                 "Shared student packet", "Upper packet", "Line packet", "Compact catalog",
                 "Compact catalog, upper"}


class CatalogError(Exception):
    pass


def week_key(w):
    """Sort key and canonical id for a week label such as '9' or '1e'."""
    m = re.fullmatch(r"(\d+)(e?)", str(w))
    if not m:
        raise CatalogError(f"bad week label {w!r}")
    return (int(m.group(1)), m.group(2))


def week_id(w):
    n, e = week_key(w)
    return f"{n}{e}"


def week_slug(w):
    n, e = week_key(w)
    return f"week-{n:02d}" + ("e" if e else "")


def series_of(w):
    n, e = week_key(w)
    if e:
        return "Fall 2026 core weeks"
    for lo, hi, name in SERIES:
        if lo <= n <= hi:
            return name
    return ""


def load():
    concepts_doc = tomllib.loads((CAT / "concepts.toml").read_text())
    areas = concepts_doc["areas"]
    mechanisms = concepts_doc["mechanisms"]
    concepts = concepts_doc["concepts"]
    errors = []
    for cid, c in concepts.items():
        for field in ("name", "area", "about"):
            if field not in c:
                errors.append(f"concept {cid}: missing {field}")
        if c.get("area") not in areas:
            errors.append(f"concept {cid}: unknown area {c.get('area')!r}")
        for r in c.get("requires", []):
            if r not in concepts:
                errors.append(f"concept {cid}: requires unknown concept {r!r}")
    # cycle check
    state = {}

    def visit(cid, stack):
        if state.get(cid) == 1:
            errors.append("concept cycle: " + " -> ".join(stack + [cid]))
            return
        if state.get(cid) == 2:
            return
        state[cid] = 1
        for r in concepts[cid].get("requires", []):
            if r in concepts:
                visit(r, stack + [cid])
        state[cid] = 2

    for cid in concepts:
        visit(cid, [])

    weeks = {}
    for path in sorted((CAT / "weeks").glob("week-*.toml")):
        try:
            rec = tomllib.loads(path.read_text())
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"{path.name}: {exc}")
            continue
        where = path.name
        for field in REQUIRED:
            if field not in rec:
                errors.append(f"{where}: missing {field}")
        for field in rec:
            if field not in REQUIRED and field not in OPTIONAL:
                errors.append(f"{where}: unknown field {field!r}")
        if "week" not in rec:
            continue
        try:
            wid = week_id(rec["week"])
        except CatalogError as exc:
            errors.append(f"{where}: {exc}")
            continue
        if path.stem != week_slug(wid):
            errors.append(f"{where}: file name should be {week_slug(wid)}.toml")
        for cid in rec.get("concepts", []) + rec.get("uses", []):
            if cid not in concepts:
                errors.append(f"{where}: unknown concept {cid!r}")
        if not 1 <= len(rec.get("concepts", [])) <= 4:
            errors.append(f"{where}: concepts should list 1 to 4 ids")
        for mid in rec.get("mechanisms", []):
            if mid not in mechanisms:
                errors.append(f"{where}: unknown mechanism {mid!r}")
        for b in rec.get("bands", []):
            if b not in BANDS:
                errors.append(f"{where}: unknown band {b!r}")
        if rec.get("status") not in STATUSES:
            errors.append(f"{where}: status must be one of {STATUSES}")
        if rec.get("verdict") not in VERDICTS:
            errors.append(f"{where}: verdict must be one of {VERDICTS}")
        if rec.get("app_decision") not in APP_DECISIONS:
            errors.append(f"{where}: app_decision must be one of {APP_DECISIONS}")
        if not isinstance(rec.get("materials", []), list):
            errors.append(f"{where}: materials must be a list")
        for rel in rec.get("related", []):
            if rel.get("kind") not in KINDS:
                errors.append(f"{where}: related kind {rel.get('kind')!r} is not one of {KINDS}")
            if "note" not in rel or "week" not in rel:
                errors.append(f"{where}: each related entry needs week, kind and note")
        rec["id"] = wid
        weeks[wid] = rec
    for wid, rec in weeks.items():
        for rel in rec.get("related", []):
            try:
                other = week_id(rel.get("week", ""))
            except CatalogError:
                errors.append(f"{week_slug(wid)}.toml: bad related week {rel.get('week')!r}")
                continue
            if other not in weeks and not (1 <= week_key(other)[0] <= 100):
                errors.append(f"{week_slug(wid)}.toml: related week {other} does not exist")
            if other == wid:
                errors.append(f"{week_slug(wid)}.toml: relates to itself")
    if errors:
        raise CatalogError("\n".join(errors))
    return areas, mechanisms, concepts, weeks


def print_files(wid):
    n, e = week_key(wid)
    folder = YEAR2 / (f"week-{n:02d}-encore" if e else f"week-{n:02d}")
    prefix = f"week-{n:02d}-encore-" if e else f"week-{n:02d}-"
    files = []
    if folder.is_dir():
        for pdf in sorted(folder.glob("*.pdf")):
            if not pdf.name.startswith(prefix):
                continue
            suffix = pdf.name[len(prefix):]
            role = next((r for s, r in FILE_ROLES if suffix == s), None)
            if role is None:
                role = suffix.removesuffix(".pdf").replace("-", " ").capitalize()
            files.append({"role": role, "path": str(pdf.relative_to(ROOT)),
                          "student": role in STUDENT_ROLES})
    order = {r: i for i, (_, r) in enumerate(FILE_ROLES)}
    files.sort(key=lambda f: order.get(f["role"], 99))
    views = []
    bv = YEAR2 / "band-views" / f"week-{n:02d}"
    if not e and bv.is_dir():
        for pdf in sorted(bv.glob("*.pdf")):
            suffix = pdf.name[len(f"week-{n:02d}-"):]
            label = {"k-1.pdf": "K–1 pages", "grades-2-3.pdf": "Grades 2–3 pages",
                     "grades-4-5.pdf": "Grades 4–5 pages", "menu.pdf": "One-page menu"}.get(
                suffix, suffix.removesuffix(".pdf"))
            views.append({"role": label, "path": str(pdf.relative_to(ROOT))})
    links = []
    src = YEAR2 / "source" / (f"week-{n:02d}-encore" if e else f"week-{n:02d}") / "README.md"
    if src.exists():
        links.append({"role": "Source and build notes", "path": str(src.relative_to(ROOT))})
    card = ROOT / "plans" / "review" / (f"week-{n:02d}e.md" if e else f"week-{n:02d}.md")
    if card.exists():
        links.append({"role": "Review card", "path": str(card.relative_to(ROOT))})
    return files, views, links


def concept_depths(concepts):
    depth = {}

    def d(cid):
        if cid not in depth:
            reqs = concepts[cid].get("requires", [])
            depth[cid] = 0 if not reqs else 1 + max(d(r) for r in reqs)
        return depth[cid]

    for cid in concepts:
        d(cid)
    return depth


def layout_concepts(concepts, depth, areas, shown):
    """Area lanes, read left to right by prerequisite depth.

    Each area gets a horizontal lane; inside it a concept sits in the column of
    its depth, so columns line up across lanes. Concepts in a cell are ordered by
    the average height of their prerequisites to keep arrows short.
    """
    col_w, row_h = 214, 30
    pos, lanes = {}, []
    y = 16
    for a in areas:
        cs = [c for c in concepts if concepts[c]["area"] == a and c in shown]
        if not cs:
            continue
        cells = defaultdict(list)
        for c in cs:
            cells[depth[c]].append(c)
        top = y
        y0 = y + 30
        rows = max(len(v) for v in cells.values())
        for d in sorted(cells):
            def bary(c):
                ys = [pos[r][1] for r in concepts[c].get("requires", []) if r in pos]
                return (sum(ys) / len(ys)) if ys else y0 + rows * row_h / 2
            cell = sorted(cells[d], key=lambda c: (bary(c), concepts[c]["name"]))
            offset = 0
            for i, c in enumerate(cell):
                pos[c] = (40 + d * col_w, y0 + offset + i * row_h + 11)
        y = y0 + rows * row_h + 18
        lanes.append({"area": a, "y": top, "h": y - top - 8})
    width = 40 + (max(depth[c] for c in shown) + 1) * col_w
    return pos, width, y, lanes


def layout_weeks(weeks, edges, areas):
    """Force-directed layout of weeks, seeded by area sectors, deterministic."""
    rnd = random.Random(7)
    ids = sorted(weeks, key=week_key)
    area_list = list(areas)
    pos = {}
    for wid in ids:
        a = weeks[wid]["_area"]
        ang = 2 * math.pi * area_list.index(a) / len(area_list)
        pos[wid] = [math.cos(ang) * 300 + rnd.uniform(-60, 60), math.sin(ang) * 300 + rnd.uniform(-60, 60)]
    adj = defaultdict(set)
    for e in edges:
        adj[e["a"]].add(e["b"])
        adj[e["b"]].add(e["a"])
    k = 88.0
    temp = 60.0
    for it in range(400):
        disp = {w: [0.0, 0.0] for w in ids}
        for i, u in enumerate(ids):
            for v in ids[i + 1:]:
                dx = pos[u][0] - pos[v][0]
                dy = pos[u][1] - pos[v][1]
                dist = math.hypot(dx, dy) or 0.01
                f = k * k / dist
                if weeks[u]["_area"] == weeks[v]["_area"]:
                    f *= 0.6
                disp[u][0] += dx / dist * f
                disp[u][1] += dy / dist * f
                disp[v][0] -= dx / dist * f
                disp[v][1] -= dy / dist * f
        for e in edges:
            u, v = e["a"], e["b"]
            dx = pos[u][0] - pos[v][0]
            dy = pos[u][1] - pos[v][1]
            dist = math.hypot(dx, dy) or 0.01
            f = dist * dist / k
            disp[u][0] -= dx / dist * f
            disp[u][1] -= dy / dist * f
            disp[v][0] += dx / dist * f
            disp[v][1] += dy / dist * f
        for u in ids:
            # gentle pull toward the area's sector keeps regions readable
            a = weeks[u]["_area"]
            ang = 2 * math.pi * area_list.index(a) / len(area_list)
            disp[u][0] += (math.cos(ang) * 320 - pos[u][0]) * 0.05
            disp[u][1] += (math.sin(ang) * 320 - pos[u][1]) * 0.05
            dx, dy = disp[u]
            d = math.hypot(dx, dy) or 0.01
            pos[u][0] += dx / d * min(d, temp)
            pos[u][1] += dy / d * min(d, temp)
        temp = max(2.0, temp * 0.985)
    xs = [p[0] for p in pos.values()]
    ys = [p[1] for p in pos.values()]
    minx, miny = min(xs), min(ys)
    for w in pos:
        pos[w] = (round(pos[w][0] - minx + 40, 1), round(pos[w][1] - miny + 40, 1))
    width = max(xs) - minx + 80
    height = max(ys) - miny + 80
    return pos, round(width), round(height)


def build_data(areas, mechanisms, concepts, weeks):
    depth = concept_depths(concepts)
    concept_weeks = defaultdict(list)
    concept_uses = defaultdict(list)
    for wid, rec in weeks.items():
        for i, cid in enumerate(rec["concepts"]):
            concept_weeks[cid].append(wid)
        for cid in rec.get("uses", []):
            concept_uses[cid].append(wid)
        rec["_area"] = concepts[rec["concepts"][0]]["area"]
        rec["_depth"] = max(depth[c] for c in rec["concepts"])

    # relations: keep leads-to directed, merge symmetric duplicates
    edges = {}
    for wid, rec in weeks.items():
        for rel in rec.get("related", []):
            other = week_id(rel["week"])
            if other not in weeks:
                continue
            kind = rel["kind"]
            if kind == "leads-to":
                key = (wid, other, kind)
            else:
                a, b = sorted([wid, other], key=week_key)
                key = (a, b, kind)
            if key in edges:
                if rel["note"] not in edges[key]["notes"]:
                    edges[key]["notes"].append(rel["note"])
            else:
                edges[key] = {"a": key[0], "b": key[1], "kind": kind, "notes": [rel["note"]],
                              "from": wid}
    edge_list = list(edges.values())

    # Show concepts that some theme is about or builds on, with their prerequisites.
    shown = set()

    def keep(cid):
        if cid not in shown:
            shown.add(cid)
            for r in concepts[cid].get("requires", []):
                keep(r)

    for cid in concepts:
        if concept_weeks[cid] or concept_uses[cid]:
            keep(cid)
    cpos, cw, ch, lanes = layout_concepts(concepts, depth, areas, shown)
    wpos, ww, wh = layout_weeks(weeks, edge_list, areas)

    out_weeks = []
    for wid in sorted(weeks, key=week_key):
        rec = weeks[wid]
        files, views, links = print_files(wid)
        out_weeks.append({
            "id": wid,
            "slug": week_slug(wid),
            "title": rec["title"],
            "hook": rec["hook"],
            "math": rec["math"],
            "discover": rec.get("discover", ""),
            "gem": rec.get("gem", ""),
            "concepts": rec["concepts"],
            "uses": rec.get("uses", []),
            "mechanisms": rec["mechanisms"],
            "bands": [b for b in BANDS if b in rec["bands"]],
            "reading": rec["reading"],
            "arithmetic": rec["arithmetic"],
            "materials": rec["materials"],
            "prep": rec.get("prep", ""),
            "status": rec["status"],
            "verdict": rec["verdict"],
            "verdictNote": rec.get("verdict_note", ""),
            "app": rec["app"],
            "appDecision": rec["app_decision"],
            "area": rec["_area"],
            "depth": rec["_depth"],
            "series": series_of(wid),
            "files": files,
            "views": views,
            "links": links,
            "x": wpos[wid][0],
            "y": wpos[wid][1],
        })
    out_concepts = []
    for cid, c in concepts.items():
        if cid not in shown:
            continue
        out_concepts.append({
            "id": cid,
            "name": c["name"],
            "area": c["area"],
            "about": c["about"],
            "requires": [r for r in c.get("requires", []) if r in shown],
            "depth": depth[cid],
            "weeks": sorted(concept_weeks[cid], key=week_key),
            "usedBy": sorted(concept_uses[cid], key=week_key),
            "x": cpos[cid][0],
            "y": cpos[cid][1],
        })
    return {
        "repo": REPO_URL,
        "areas": areas,
        "mechanisms": mechanisms,
        "bands": BANDS,
        "kinds": KINDS,
        "concepts": out_concepts,
        "weeks": out_weeks,
        "edges": edge_list,
        "conceptMap": {"width": cw, "height": ch, "lanes": lanes},
        "weekMap": {"width": ww, "height": wh},
    }


def write_catalog_md(data, path):
    areas = data["areas"]
    concepts = {c["id"]: c for c in data["concepts"]}
    weeks = data["weeks"]
    by_area = defaultdict(list)
    for w in weeks:
        by_area[w["area"]].append(w)
    lines = [
        "# Activity catalog",
        "",
        f"Every theme in the library, {len(weeks)} in all, grouped by the area of its central idea. "
        "Built from [catalog/](catalog/README.md) by `python3 catalog/build.py`; edit the records there, not this page. "
        "The explorer (`explorer/index.html`; download it and open it in a browser, or see the published copy linked from the "
        "[catalog README](catalog/README.md)) shows the same records with filters, the concept map and the links between activities.",
        "",
        "Bands are entry points by prerequisites, not age limits. Status: piloted means a classroom report exists; "
        "organizer-approved means the organizer reviewed and promoted it; everything else is unpiloted.",
        "",
    ]
    for a, name in areas.items():
        ws = by_area.get(a, [])
        if not ws:
            continue
        lines += [f"## {name}", "", "| Week | Theme | What children do | Bands | Status | Print |", "|---|---|---|---|---|---|"]
        for w in sorted(ws, key=lambda w: week_key(w["id"])):
            student = [f for f in w["files"] if f["student"]]
            guide = next((f for f in w["files"] if f["role"] == "Adult guide"), None)
            prints = []
            for f in student[:4]:
                prints.append(f"[{f['role'].replace(' packet', '')}]({f['path']})")
            if guide:
                prints.append(f"[guide]({guide['path']})")
            bands = ", ".join(b.replace("-", "–") for b in w["bands"])
            status = w["status"]
            if w["verdict"] not in ("keep", "none"):
                status += f"; card: {w['verdict']}"
            hook = w["hook"].replace("|", "\\|")
            title = w["title"].replace("|", "\\|")
            lines.append(f"| {w['id']} | {title} | {hook} | {bands} | {status} | {' · '.join(prints)} |")
        lines.append("")
    lines += ["## Concepts", "", "Each concept with the themes about it. A concept's prerequisites are in [catalog/concepts.toml](catalog/concepts.toml).", ""]
    for a, name in areas.items():
        cs = [c for c in data["concepts"] if c["area"] == a]
        items = []
        for c in sorted(cs, key=lambda c: (c["depth"], c["name"])):
            if c["weeks"]:
                items.append(f"{c['name']} ({', '.join(c['weeks'])})")
        if items:
            lines.append(f"- **{name}:** " + "; ".join(items) + ".")
    lines.append("")
    path.write_text("\n".join(lines))


def write_explorer(data, out_html, fragment_path=None):
    template = (CAT / "explorer_template.html").read_text()
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    body = template.replace("/*__DATA__*/null", payload)
    if fragment_path:
        Path(fragment_path).write_text(body)
    doc = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
           "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
           "</head>\n<body>\n" + body + "\n</body>\n</html>\n")
    out_html.parent.mkdir(parents=True, exist_ok=True)
    out_html.write_text(doc)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="check the records only")
    ap.add_argument("--fragment", help="also write the page body without the document wrapper")
    args = ap.parse_args()
    try:
        areas, mechanisms, concepts, weeks = load()
    except CatalogError as exc:
        print("The catalog has problems:\n" + str(exc), file=sys.stderr)
        sys.exit(1)
    print(f"{len(weeks)} week records, {len(concepts)} concepts: all checks pass")
    if args.check:
        return
    data = build_data(areas, mechanisms, concepts, weeks)
    write_explorer(data, ROOT / "explorer" / "index.html", args.fragment)
    write_catalog_md(data, ROOT / "CATALOG.md")
    print("Wrote explorer/index.html and CATALOG.md")


if __name__ == "__main__":
    main()
