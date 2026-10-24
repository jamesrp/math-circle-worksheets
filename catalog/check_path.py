#!/usr/bin/env python3
"""Check the six-year path in catalog/path.toml against the catalog.

    python3 catalog/check_path.py            # check and print a short summary
    python3 catalog/check_path.py --tables   # also print the year tables for plans/six-year-path.md

The builder (catalog/build.py) runs the same check and stops on any failure. The check
fails on: unknown ids; a concept appearing before a concept it requires (root concepts
are everyday background; [[waiver]] entries list the exceptions); the same theme twice in
a year; more than two sessions in a row from one area; a year with fewer than five areas;
a revisit closer than one year (twenty sessions), including a catalog "revisits" link
between two path entries; three heavy kits in a row; a session with no K–1 entry; and a
week or atlas family that is neither on the path nor in a [[left_out]] group.
"""
import argparse
import json
import re
import sys
import tomllib
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAT = ROOT / "catalog"
YEAR2 = ROOT / "lowell-math-circle-year-2"
INVENTORY = ROOT / "plans" / "bonus-return-visits-delivery-inventory.json"

BANDS = ["K-1", "2-3", "4-5"]
KITS = ["light", "medium", "heavy"]
SESSION_FIELDS = {"year", "id", "hours", "move", "kit", "kit_note", "revisits", "note", "k1"}
YEAR_GAP = 20          # a revisit must come at least one year of sessions later
MAX_RUN = 2            # at most two sessions in a row from one area
MIN_AREAS = 5
AREA_SHORT = {"networks": "Networks", "games": "Games", "chance": "Chance and infinity", "number": "Number",
              "symmetry": "Symmetry", "shape": "Shape", "logic": "Logic", "counting": "Counting"}
MOVE_SHORT = {
    "invariant": "invariant", "monovariant": "monovariant", "colouring": "colouring argument",
    "copying": "copy the opponent", "work-backward": "work backward", "pair-up": "pair up",
    "double-count": "count two ways", "pigeonhole": "pigeonhole", "extremal": "look at extremes",
    "smaller-cases": "smaller cases", "every-case": "every case", "construct": "construct",
    "certificate": "example plus proof", "counterexample": "counterexample", "unfold": "unfold",
    "greedy": "greedy", "up-to-symmetry": "up to symmetry", "limit": "follow it forever",
    "coordinates": "coordinates", "simulate": "simulate",
}
ATLAS_BOOK_STEMS = {
    "algebra-discrete": "atlas-algebra-discrete", "geometry-analysis": "atlas-geometry-analysis",
    "applied-probability": "atlas-probability-applications", "random-ten": "atlas-random-ten",
}


def week_num(wid):
    m = re.fullmatch(r"(\d+)(e?)", wid)
    return (int(m.group(1)), m.group(2)) if m else None


def week_slug(wid):
    n, e = week_num(wid)
    return f"week-{n:02d}" + ("-encore" if e else "")


def return_visits():
    """The return-visit and bonus companions for Weeks 1–51, keyed 'rv-N'."""
    out = {}
    for w in json.loads(INVENTORY.read_text())["weeks"]:
        inv = []
        for i in w["investigations"]:
            t = i["suitable_bands_and_readiness"].replace("-", "–")
            inv.append({"title": i["title"], "bands": t})
        out[f"rv-{w['week']}"] = {"week": str(w["week"]), "theme": w["theme"], "investigations": inv,
                                  "student": "lowell-math-circle-year-2/" + w["paths"]["student"],
                                  "guide": "lowell-math-circle-year-2/" + w["paths"]["adult"],
                                  "source": "lowell-math-circle-year-2/" + w["paths"]["build_instructions"]}
    return out


def rv_bands(rv):
    text = " | ".join(i["bands"] for i in rv["investigations"])
    k1 = bool(re.search(r"K–1|K–5|K–\d|younger|oral K", text))
    b23 = bool(re.search(r"2–|K–5|third grader|younger", text))
    return {"K-1": "rv" if k1 else "base", "2-3": "rv" if b23 else "base", "4-5": "rv"}


def check(areas, mechanisms, concepts, weeks, atlas, path_file=None):
    """Return (path data for the explorer, errors, summary lines, entries)."""
    errors = []
    doc = tomllib.loads(Path(path_file or CAT / "path.toml").read_text())
    rvs = return_visits()
    per_year = doc.get("sessions_per_year", 20)
    years = {y["year"]: y for y in doc.get("year", [])}

    # ------------------------------------------------------------ entries
    entries = []
    seen_ids = set()
    slot = 0
    for i, s in enumerate(doc.get("session", [])):
        where = f"session {i + 1} ({s.get('id', '?')})"
        for k in s:
            if k not in SESSION_FIELDS:
                errors.append(f"{where}: unknown field {k!r}")
        sid = str(s.get("id", ""))
        if sid in seen_ids:
            errors.append(f"{where}: {sid} appears twice on the path")
        seen_ids.add(sid)
        if sid in weeks:
            kind, theme, rec = "week", sid, weeks[sid]
        elif sid in rvs and rvs[sid]["week"] in weeks:
            kind, theme, rec = "rv", rvs[sid]["week"], weeks[rvs[sid]["week"]]
        elif sid in atlas:
            kind, theme, rec = "atlas", sid, atlas[sid]
        else:
            errors.append(f"{where}: unknown id {sid!r} (not a week, a return visit rv-N for Weeks 1–51, or an atlas family)")
            continue
        hours = s.get("hours", 1)
        if hours not in (1, 2):
            errors.append(f"{where}: hours must be 1 or 2")
            hours = 1
        year = s.get("year")
        if year not in years:
            errors.append(f"{where}: year {year!r} has no [[year]] entry")
            continue
        move = s.get("move", "")
        if move not in mechanisms:
            errors.append(f"{where}: unknown move {move!r}")
        elif kind != "rv" and move not in rec["mechanisms"]:
            errors.append(f"{where}: move {move!r} is not one of the record's mechanisms {rec['mechanisms']}")
        if s.get("kit") not in KITS:
            errors.append(f"{where}: kit must be one of {KITS}")
        start = slot + 1
        slot += hours
        e = {"id": sid, "kind": kind, "theme": theme, "rec": rec, "year": year, "start": start, "hours": hours,
             "move": move, "kit": s.get("kit", ""), "kit_note": s.get("kit_note", ""), "note": s.get("note", ""),
             "k1": s.get("k1", ""), "revisits": [str(r) for r in s.get("revisits", [])],
             "area": concepts[rec["concepts"][0]]["area"],
             "concepts": list(rec["concepts"]), "uses": list(rec.get("uses", []))}
        if kind == "week":
            e["title"] = rec["title"]
        elif kind == "rv":
            e["title"] = f"{rec['title']}: return visit"
        else:
            e["title"] = (rec["_pages"][3] if rec.get("_pages") else "") or rec["_family"]["title"]
        entries.append(e)
    by_id = {e["id"]: e for e in entries}

    # ------------------------------------------------------------ year structure
    for y in years:
        ys = [e for e in entries if e["year"] == y]
        n = sum(e["hours"] for e in ys)
        if n != per_year:
            errors.append(f"Year {y}: {n} sessions, not {per_year}")
    order = [e["year"] for e in entries]
    if order != sorted(order):
        errors.append("sessions must be listed year by year")
    for e in entries:
        lo = (e["year"] - 1) * per_year + 1
        if not (lo <= e["start"] and e["start"] + e["hours"] - 1 <= lo + per_year - 1):
            errors.append(f"{e['id']}: does not fit inside Year {e['year']} (check the session counts)")
    for e in entries:
        e["pos"] = e["start"] - (e["year"] - 1) * per_year

    def at(e):
        return f"Y{e['year']}·{e['pos']}"

    def name(e):
        if e["kind"] == "week":
            return f"Week {e['id']}"
        if e["kind"] == "rv":
            return f"Week {e['theme']} return visit"
        return f"Atlas {e['id']}"

    # ------------------------------------------------------------ bands and the K–1 table
    for e in entries:
        if e["kind"] == "rv":
            e["bands"] = rv_bands(rvs[e["id"]])
        else:
            e["bands"] = {b: ("pages" if b in e["rec"]["bands"] else None) for b in BANDS}
            if not e["bands"]["K-1"] and e["k1"]:
                e["bands"]["K-1"] = "route"
        if not e["bands"]["K-1"]:
            errors.append(f"{name(e)} ({at(e)}): no K–1 entry; give a k1 route or choose another theme")
        if not e["bands"]["2-3"]:
            errors.append(f"{name(e)} ({at(e)}): no Grades 2–3 entry")

    # ------------------------------------------------------------ concept order
    reqs = {c: concepts[c].get("requires", []) for c in concepts}

    def closure(c, acc=None):
        acc = set() if acc is None else acc
        for r in reqs.get(c, []):
            if r not in acc:
                acc.add(r)
                closure(r, acc)
        return acc

    first_seen, first_taught = {}, {}
    for e in entries:
        for c in e["concepts"] + e["uses"]:
            first_seen.setdefault(c, e)
        for c in e["concepts"]:
            first_taught.setdefault(c, e)
    waivers = {}
    for w in doc.get("waiver", []):
        key = (str(w.get("session", "")), w.get("concept", ""))
        if key[0] not in by_id:
            errors.append(f"waiver: session {key[0]!r} is not on the path")
        if key[1] not in concepts:
            errors.append(f"waiver: unknown concept {key[1]!r}")
        if not w.get("reason"):
            errors.append(f"waiver {key}: give a reason")
        waivers[key] = {"used": False, "reason": w.get("reason", "")}
    waived = []
    for e in entries:
        for c in e["concepts"] + e["uses"]:
            for r in sorted(closure(c)):
                if not reqs[r]:
                    continue  # a root concept: everyday background
                f = first_seen.get(r)
                if f and f["start"] > e["start"]:
                    key = (e["id"], r)
                    if key in waivers:
                        if not waivers[key]["used"]:
                            waived.append(f"{name(e)} ({at(e)}) before {concepts[r]['name'].lower()} ({name(f)}, {at(f)})")
                        waivers[key]["used"] = True
                    else:
                        errors.append(f"{name(e)} ({at(e)}): {concepts[c]['name'].lower()} needs "
                                      f"{concepts[r]['name'].lower()}, first met in {name(f)} ({at(f)})")
        for u in e["uses"]:
            f = first_taught.get(u)
            if reqs.get(u) and f and f["start"] > e["start"]:
                if (e["id"], u) in waivers:
                    waivers[(e["id"], u)]["used"] = True
                else:
                    errors.append(f"{name(e)} ({at(e)}) assumes {concepts[u]['name'].lower()}, "
                                  f"which the path only takes up in {name(f)} ({at(f)})")
    for key, w in waivers.items():
        if not w["used"]:
            errors.append(f"waiver {key}: nothing to waive; remove it")

    # ------------------------------------------------------------ same theme twice in a year
    for y in years:
        cnt = Counter(e["theme"] for e in entries if e["year"] == y)
        for t, n in cnt.items():
            if n > 1:
                errors.append(f"Year {y}: theme {t} appears {n} times")

    # ------------------------------------------------------------ area runs and year variety
    slots = []
    for e in entries:
        slots += [e] * e["hours"]
    run = 1
    for i in range(1, len(slots) + 1):
        if i < len(slots) and slots[i]["area"] == slots[i - 1]["area"]:
            run += 1
            continue
        if run > MAX_RUN:
            first = slots[i - run]
            errors.append(f"{run} {AREA_SHORT[first['area']].lower()} sessions in a row from {at(first)}")
        run = 1
    area_count = {}
    for y in years:
        c = Counter()
        for e in entries:
            if e["year"] == y:
                c[e["area"]] += e["hours"]
        area_count[y] = c
        if len(c) < MIN_AREAS:
            errors.append(f"Year {y}: only {len(c)} areas ({', '.join(sorted(c))})")

    # ------------------------------------------------------------ revisits
    def related(a, b):
        """Is there a catalog link between the themes of entries a and b?"""
        ta, tb = a["theme"], b["theme"]
        if ta == tb:
            return True
        for x, y in ((a, b), (b, a)):
            for rel in x["rec"].get("related", []):
                if str(rel["week"]) == y["theme"]:
                    return True
        return False

    links = []
    for e in entries:
        targets = list(e["revisits"])
        if e["kind"] == "rv" and e["theme"] not in targets:
            targets.insert(0, e["theme"])
        e["revisitIds"] = []
        for t in targets:
            o = by_id.get(t)
            if o is None:
                errors.append(f"{name(e)} ({at(e)}): revisits {t!r}, which is not on the path")
                continue
            if o["start"] >= e["start"]:
                errors.append(f"{name(e)} ({at(e)}): revisits {name(o)}, which comes later ({at(o)})")
                continue
            if not related(e, o):
                errors.append(f"{name(e)} ({at(e)}): revisits {name(o)} without a catalog link between them")
            gap = e["start"] - o["start"]
            if gap < YEAR_GAP:
                errors.append(f"{name(e)} ({at(e)}) revisits {name(o)} ({at(o)}) only {gap} sessions later")
            e["revisitIds"].append(o["id"])
            links.append((o, e))
    # catalog links of kind "revisits" between two path entries count too
    for e in entries:
        for rel in e["rec"].get("related", []):
            if rel["kind"] != "revisits":
                continue
            for o in entries:
                if o is e or o["theme"] != str(rel["week"]) or o["kind"] == "rv":
                    continue
                if e["kind"] == "rv" and o["theme"] == e["theme"]:
                    continue
                gap = abs(e["start"] - o["start"])
                if gap < YEAR_GAP:
                    errors.append(f"{name(e)} ({at(e)}) and {name(o)} ({at(o)}): the catalog calls one a revisit "
                                  f"of the other, but they are only {gap} sessions apart")
    for e in entries:
        e["revisitedBy"] = [x["id"] for (o, x) in links if o is e]

    # ------------------------------------------------------------ kits
    heavy_run = 0
    for e in entries:
        heavy_run = heavy_run + 1 if e["kit"] == "heavy" else 0
        if heavy_run >= 3:
            errors.append(f"three heavy kits in a row, ending at {name(e)} ({at(e)})")

    # ------------------------------------------------------------ left out
    left = {}
    for g in doc.get("left_out", []):
        if not g.get("group") or not g.get("reason"):
            errors.append("each [[left_out]] group needs a group name and a reason")
        for i in g.get("ids", []):
            i = str(i)
            if i not in weeks and i not in atlas:
                errors.append(f"left_out: unknown id {i!r}")
            if i in by_id:
                errors.append(f"left_out: {i} is on the path")
            if i in left:
                errors.append(f"left_out: {i} is in two groups")
            left[i] = g.get("group", "")
    on_path = {e["id"] for e in entries}
    for wid in weeks:
        if wid not in on_path and wid not in left:
            errors.append(f"Week {wid} is neither on the path nor in a [[left_out]] group")
    for aid in atlas:
        if aid not in on_path and aid not in left:
            errors.append(f"Atlas {aid} is neither on the path nor in a [[left_out]] group")
    unused_rv = sorted((k for k in rvs if k not in on_path), key=lambda k: int(k[3:]))

    # ------------------------------------------------------------ summary
    n_kind = Counter(e["kind"] for e in entries)
    summary = [f"Six-year path: {len(slots)} sessions in {len(entries)} entries: {n_kind['week']} weeks, "
               f"{n_kind['rv']} return visits, {n_kind['atlas']} atlas families; "
               f"{sum(1 for e in entries if e['hours'] == 2)} themes take two sessions."]
    for y in sorted(years):
        c = area_count[y]
        kits = Counter(e["kit"] for e in entries if e["year"] == y)
        rv_n = sum(1 for e in entries if e["year"] == y and e["revisitIds"])
        summary.append(f"Year {y} ({years[y].get('label', '')}): {len(c)} areas ("
                       + ", ".join(f"{AREA_SHORT[a].lower()} {c[a]}" for a in areas if c[a])
                       + f"); kits {kits['light']} light, {kits['medium']} medium, {kits['heavy']} heavy; "
                       f"{rv_n} entries return to earlier ones")
    # themes a K-start child meets at K–1 (Years 1–2) and when they come back
    early = [e for e in entries if e["year"] <= 2 and e["kind"] != "rv"]
    back, not_back = [], []
    for e in early:
        later = [x for (o, x) in links if o is e and 1 <= x["year"] - e["year"] <= 3]
        (back if later else not_back).append(e)
    summary.append(f"Revisits: {len(links)} links, all at least a year apart. Themes first met in Years 1–2 that "
                   f"come back one to three years later: {len(back)} of {len(early)}"
                   + (f" (not: {', '.join(name(e) for e in not_back)})" if not_back else "") + ".")
    k1 = Counter(e["bands"]["K-1"] for e in entries)
    summary.append(f"K–1 table: {k1['pages']} entries with K–1 pages, {k1['rv']} return visits with a K–1 entry, "
                   f"{k1['route']} adult-led routes in a guide, {k1['base']} using the base week's K–1 packet.")
    if waived:
        summary.append("Waived: " + "; ".join(waived) + ".")
    lw = sum(1 for i in left if i in weeks)
    summary.append(f"Left out: {lw} weeks and {len(left) - lw} atlas families in "
                   f"{len(doc.get('left_out', []))} groups; {len(unused_rv)} return visits unused.")

    # ------------------------------------------------------------ explorer data
    data = {"title": doc.get("title", ""), "status": doc.get("status", ""), "perYear": per_year,
            "years": [{"year": y, "label": years[y].get("label", ""), "note": years[y].get("note", "")} for y in sorted(years)],
            "sessions": [], "leftOut": doc.get("left_out", []), "unusedReturnVisits": unused_rv,
            "areaShort": AREA_SHORT, "moveShort": MOVE_SHORT}
    for e in entries:
        d = {"id": e["id"], "kind": e["kind"], "theme": e["theme"], "title": e["title"], "area": e["area"],
             "year": e["year"], "pos": e["pos"], "start": e["start"], "hours": e["hours"], "move": e["move"],
             "kit": e["kit"], "kitNote": e["kit_note"], "note": e["note"], "k1": e["k1"], "bands": e["bands"],
             "revisits": e["revisitIds"], "revisitedBy": e["revisitedBy"],
             "status": e["rec"]["status"] if e["kind"] == "week" else "unpiloted"}
        if e["kind"] == "rv":
            rv = rvs[e["id"]]
            d["rv"] = {"theme": rv["theme"], "investigations": rv["investigations"], "student": rv["student"],
                       "guide": rv["guide"], "source": rv["source"]}
        data["sessions"].append(d)
    return data, errors, summary, entries


def md_link(e):
    if e["kind"] == "week":
        n, x = week_num(e["id"])
        label = f"Week {e['id']}: {e['rec']['title']}"
        return f"[{label}](../lowell-math-circle-year-2/source/{week_slug(e['id'])}/README.md)"
    if e["kind"] == "rv":
        rv = return_visits()[e["id"]]
        return f"[Week {e['theme']} return visit: {e['rec']['title']}](../{rv['student']})"
    pages = e["rec"].get("_pages")
    stem = ATLAS_BOOK_STEMS[pages[0]] if pages else ""
    return (f"[Atlas {e['id']}: {e['title']}](../lowell-math-circle-year-2/combined/{stem}-student-worksheets.pdf)"
            + (f", pp. {pages[1]}" if pages else ""))


def tables(entries, per_year):
    out = []
    by_id = {e["id"]: e for e in entries}
    for y in sorted({e["year"] for e in entries}):
        out += [f"| # | Theme | Area | Main move | Returns to · what it revisits or prepares | Kit |",
                "|---|---|---|---|---|---|"]
        for e in (x for x in entries if x["year"] == y):
            num = str(e["pos"]) if e["hours"] == 1 else f"{e['pos']}–{e['pos'] + 1}"
            ret = ", ".join(f"Y{by_id[r]['year']}·{by_id[r]['pos']}" for r in e["revisitIds"])
            note = (f"↩ {ret}. " if ret else "") + e["note"]
            kit = e["kit"] if e["kit"] != "heavy" else "**heavy**"
            if e["hours"] == 2:
                kit += ", two hours"
            if e["bands"]["K-1"] == "route":
                kit += "; K–1 by adult-led route"
            elif e["bands"]["K-1"] == "base":
                kit += f"; K–1 uses the Week {e['theme']} K–1 packet"
            out.append(f"| {num} | {md_link(e)} | {AREA_SHORT[e['area']]} | {MOVE_SHORT[e['move']]} | "
                       f"{note.replace('|', '/')} | {kit} |")
        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tables", action="store_true", help="print the year tables in Markdown")
    ap.add_argument("--file", help="check another path file (for testing the check)")
    args = ap.parse_args()
    sys.path.insert(0, str(CAT))
    import build
    try:
        areas, mechanisms, concepts, weeks, atlas = build.load()
    except build.CatalogError as exc:
        print("The catalog has problems:\n" + str(exc), file=sys.stderr)
        sys.exit(1)
    data, errors, summary, entries = check(areas, mechanisms, concepts, weeks, atlas, args.file)
    if errors:
        print("The six-year path has problems:\n" + "\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print("\n".join(summary))
    print("All path checks pass.")
    if args.tables:
        print()
        print(tables(entries, data["perYear"]))


if __name__ == "__main__":
    main()
