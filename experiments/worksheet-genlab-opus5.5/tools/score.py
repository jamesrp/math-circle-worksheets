#!/usr/bin/env python3
"""Aggregate eval results (EVAL-v1). Prints tables; writes analysis/scores.json.

Primary metric: organizer edit minutes per packet = sum over bands of edit minutes,
recomputed from each audit's edit list, averaged over audit replicates.
"""
import glob, json, os, re, sys, collections, statistics as st

ROOT = "/home/claude/genlab"
BANDS = ["k-1", "grades-2-3", "grades-4-5"]
CATS = ["SLOP", "MATH", "CLARITY", "CONCRETENESS", "LEVEL", "SCAFFOLDING", "VOLUME", "LAYOUT", "FORMAT"]
DIMS = ["math_substance", "concreteness", "level_fit", "clarity", "human_voice", "volume", "layout", "readiness"]

def bmap():
    return json.load(open(f"{ROOT}/eval/private/blind-map.json"))

def load_audits(pid, include_pilot=False):
    out = []
    for f in sorted(glob.glob(f"{ROOT}/eval/results/{pid}/audit-*.json")):
        if "pilot" in f and not include_pilot:
            continue
        try:
            out.append((os.path.basename(f), json.load(open(f))))
        except Exception as e:
            print("BAD JSON", f, e, file=sys.stderr)
    return out

def audit_summary(a):
    s = {"bands": {}, "total_minutes": 0, "cat_minutes": collections.Counter(), "n_edits": 0}
    for b in BANDS:
        v = a["bands"][b]
        mins = sum(int(e.get("minutes", 0)) for e in v["edits"])
        cats = collections.Counter()
        for e in v["edits"]:
            cats[e.get("category", "?").upper()] += int(e.get("minutes", 0))
        s["bands"][b] = {"minutes": mins, "n_edits": len(v["edits"]), "cats": dict(cats),
                         "quick": v.get("minutes_quick_child"), "typical": v.get("minutes_typical_child"),
                         "scores": v.get("scores", {}), "problems": v.get("problems"), "pages": v.get("pages")}
        s["total_minutes"] += mins
        s["cat_minutes"].update(cats)
        s["n_edits"] += len(v["edits"])
    s["readiness_overall"] = a.get("overall", {}).get("readiness")
    return s

def packet_summary(pid):
    auds = load_audits(pid)
    if not auds:
        return None
    sums = [audit_summary(a) for _, a in auds]
    r = {"pid": pid, "n_audits": len(sums),
         "minutes": [s["total_minutes"] for s in sums],
         "minutes_mean": st.mean(s["total_minutes"] for s in sums),
         "cat_minutes_mean": {c: st.mean(s["cat_minutes"].get(c, 0) for s in sums) for c in CATS},
         "bands": {}}
    for b in BANDS:
        bb = [s["bands"][b] for s in sums]
        r["bands"][b] = {
            "minutes_mean": st.mean(x["minutes"] for x in bb),
            "quick_mean": st.mean(x["quick"] or 0 for x in bb),
            "typical_mean": st.mean(x["typical"] or 0 for x in bb),
            "scores_mean": {d: st.mean(x["scores"].get(d, 0) for x in bb) for d in DIMS},
            "problems": [x["problems"] for x in bb], "pages": bb[0]["pages"],
        }
    r["readiness_mean"] = st.mean(r["bands"][b]["scores_mean"]["readiness"] for b in BANDS)
    r["AQI"] = st.mean(r["bands"][b]["scores_mean"][d] for b in BANDS for d in DIMS)
    r["AQI_each"] = [round(st.mean(audit_summary(a)["bands"][b]["scores"][d] for b in BANDS for d in DIMS), 2) for _, a in auds]
    SUB = ["math_substance", "concreteness", "level_fit", "clarity", "volume", "layout"]
    r["substance"] = st.mean(r["bands"][b]["scores_mean"][d] for b in BANDS for d in SUB)
    r["slop_edits"] = st.mean(sum(1 for b in BANDS for e in a["bands"][b]["edits"] if e.get("category","").upper()=="SLOP") for _, a in auds)
    r["math_edits"] = st.mean(sum(1 for b in BANDS for e in a["bands"][b]["edits"] if e.get("category","").upper()=="MATH") for _, a in auds)
    r["human_voice_mean"] = st.mean(r["bands"][b]["scores_mean"]["human_voice"] for b in BANDS)
    r["math_mean"] = st.mean(r["bands"][b]["scores_mean"]["math_substance"] for b in BANDS)
    r["quick_k1"] = r["bands"]["k-1"]["quick_mean"]
    return r

def load_pairs():
    """Return dict (pidA,pidB) sorted -> list of per-order results."""
    res = collections.defaultdict(list)
    for f in glob.glob(f"{ROOT}/eval/results/pairs/*.json"):
        try:
            d = json.load(open(f))
        except Exception as e:
            print("BAD JSON", f, e, file=sys.stderr); continue
        x, y = d["x"], d["y"]
        key = tuple(sorted([x, y]))
        def who(w):
            w = (w or "").strip().upper()
            return x if w == "X" else y if w == "Y" else "tie"
        ov = d.get("overall") or d["bands"].get("overall")
        rec = {"x": x, "y": y, "overall": who(ov["winner"]), "overall_strength": ov.get("strength"),
               "bands": {b: who(d["bands"][b]["winner"]) for b in BANDS},
               "band_strength": {b: d["bands"][b].get("strength") for b in BANDS}}
        res[key].append(rec)
    return res

def pair_outcome(recs, a, b, field="overall", band=None):
    """Score for a vs b in [0,1] combining both orders; inconsistent -> 0.5 each order."""
    vals = []
    for r in recs:
        w = r["overall"] if band is None else r["bands"][band]
        vals.append(1.0 if w == a else 0.0 if w == b else 0.5)
    return st.mean(vals) if vals else None

if __name__ == "__main__":
    m = bmap()
    rows = []
    for pid, info in m.items():
        s = packet_summary(pid)
        if s:
            s["source"] = info["source"]
            rows.append(s)
    rows.sort(key=lambda r: -r["AQI"])
    print(f"{'source':22} {'pid':6} {'AQI':>5} {'(each)':>12} {'subst':>5} {'voice':>5} {'slopN':>5} {'mathN':>5} {'ready':>5} {'edit_min':>8} {'k1q':>4} {'23q':>4} {'45q':>4}  top edit-minute categories")
    for r in rows:
        cats = sorted(r["cat_minutes_mean"].items(), key=lambda kv: -kv[1])[:3]
        print(f"{r['source']:22} {r['pid']:6} {r['AQI']:5.2f} {str(r['AQI_each']):>12} {r['substance']:5.2f} {r['human_voice_mean']:5.2f} {r['slop_edits']:5.1f} {r['math_edits']:5.1f} {r['readiness_mean']:5.2f} {r['minutes_mean']:8.1f} {r['quick_k1']:4.0f} {r['bands']['grades-2-3']['quick_mean']:4.0f} {r['bands']['grades-4-5']['quick_mean']:4.0f}  " +
              ", ".join(f"{c}:{v:.0f}" for c, v in cats))
    pairs = load_pairs()
    print("\nPairs (overall score for first, both orders combined; per-band):")
    for (a, b), recs in sorted(pairs.items()):
        sa = pair_outcome(recs, a, b)
        bands = {bb: pair_outcome(recs, a, b, band=bb) for bb in BANDS}
        print(f"  {m[a]['source']:20} vs {m[b]['source']:20} n={len(recs)} overall={sa:.2f} bands=" +
              " ".join(f"{k}:{v:.2f}" for k, v in bands.items()) +
              "  raw=" + "; ".join(f"[{m[r['x']]['source'][-8:]} as X] {m[r['overall']]['source'][-8:] if r['overall']!='tie' else 'tie'}" for r in recs))
    os.makedirs(f"{ROOT}/analysis", exist_ok=True)
    json.dump({"packets": rows}, open(f"{ROOT}/analysis/scores.json", "w"), indent=1)
