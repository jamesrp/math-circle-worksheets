#!/usr/bin/env python3
"""Full analysis: per-packet metrics, all pairwise results, reliability. Writes analysis/*.json|csv|md."""
import json, glob, os, csv, statistics as st, collections, itertools, sys
sys.path.insert(0, os.path.dirname(__file__))
from score import load_audits, audit_summary, BANDS, DIMS

G = "/home/claude/genlab"
m = json.load(open(f"{G}/eval/private/blind-map.json"))
SUB = ["math_substance", "concreteness", "level_fit", "clarity", "volume", "layout"]

def label(pid):
    s = m[pid]["source"]
    return s.split(":", 1)[1]

rows = []
for pid in m:
    auds = load_audits(pid)
    if not auds:
        continue
    S = [audit_summary(a) for _, a in auds]
    lint = json.load(open(f"{G}/eval/lint/{pid}.json"))["total"] if os.path.exists(f"{G}/eval/lint/{pid}.json") else {}
    aqi_each = [st.mean(s["bands"][b]["scores"][d] for b in BANDS for d in DIMS) for s in S]
    r = {
        "packet": label(pid), "pid": pid, "n_audits": len(S),
        "AQI": round(st.mean(aqi_each), 3), "AQI_each": [round(x, 2) for x in aqi_each],
        "substance": round(st.mean(st.mean(s["bands"][b]["scores"][d] for b in BANDS for d in SUB) for s in S), 3),
        "human_voice": round(st.mean(st.mean(s["bands"][b]["scores"]["human_voice"] for b in BANDS) for s in S), 2),
        "readiness": round(st.mean(st.mean(s["bands"][b]["scores"]["readiness"] for b in BANDS) for s in S), 2),
        "edit_min": round(st.mean(s["total_minutes"] for s in S), 1),
        "slop_edits": round(st.mean(s["cat_minutes"].get("SLOP", 0) and sum(1 for b in BANDS for e in a["bands"][b]["edits"] if e["category"].upper() == "SLOP") for s, (_, a) in zip(S, auds)), 1),
        "math_edits": round(st.mean(sum(1 for b in BANDS for e in a["bands"][b]["edits"] if e["category"].upper() == "MATH") for _, a in auds), 1),
        "n_edits": round(st.mean(s["n_edits"] for s in S), 1),
    }
    for b in BANDS:
        r[f"quick_{b}"] = round(st.mean(s["bands"][b]["quick"] or 0 for s in S), 1)
        r[f"AQI_{b}"] = round(st.mean(st.mean(s["bands"][b]["scores"][d] for d in DIMS) for s in S), 2)
    r["pages"] = lint.get("pages"); r["words"] = lint.get("words"); r["tells_per_100w"] = lint.get("tells_per_100w")
    rows.append(r)
rows.sort(key=lambda r: -r["AQI"])

# pairwise
pairs = collections.defaultdict(list)
for f in glob.glob(f"{G}/eval/results/pairs/*.json"):
    d = json.load(open(f)); x, y = d["x"], d["y"]
    ov = d.get("overall") or d["bands"].get("overall")
    w = lambda s: x if s.strip().upper() == "X" else y if s.strip().upper() == "Y" else "tie"
    pairs[tuple(sorted([x, y]))].append({"x": x, "y": y, "overall": w(ov["winner"]), "s": ov.get("strength"),
                                         "bands": {b: w(d["bands"][b]["winner"]) for b in BANDS}})
pair_rows = []
consistent = 0; total_pairs = 0
for (a, b), recs in sorted(pairs.items(), key=lambda kv: (label(kv[0][0]), label(kv[0][1]))):
    sc = lambda win: 1.0 if win == a else 0.0 if win == b else 0.5
    ov = st.mean(sc(r["overall"]) for r in recs)
    bands = {bb: st.mean(sc(r["bands"][bb]) for r in recs) for bb in BANDS}
    if len(recs) == 2:
        total_pairs += 1
        consistent += recs[0]["overall"] == recs[1]["overall"]
    pair_rows.append({"A": label(a), "B": label(b), "n": len(recs), "A_score": ov, **{f"A_{k}": v for k, v in bands.items()},
                      "strengths": [r["s"] for r in recs]})

# reliability across packets with 2 audits
def icc(vals):
    vals = [v for v in vals if len(v) == 2]
    means = [st.mean(v) for v in vals]
    msb = 2 * st.variance(means); msw = st.mean(st.variance(v) for v in vals)
    return (msb - msw) / (msb + msw)
rel = {}
for key in ["AQI_each"]:
    rel["AQI"] = round(icc([r["AQI_each"] for r in rows]), 3)

os.makedirs(f"{G}/analysis", exist_ok=True)
json.dump({"packets": rows, "pairs": pair_rows, "reliability": rel,
           "pair_order_consistency": f"{consistent}/{total_pairs}"}, open(f"{G}/analysis/results.json", "w"), indent=1)
with open(f"{G}/analysis/packets.csv", "w", newline="") as f:
    wr = csv.DictWriter(f, fieldnames=[k for k in rows[0].keys() if k != "AQI_each"])
    wr.writeheader()
    for r in rows:
        wr.writerow({k: v for k, v in r.items() if k != "AQI_each"})

print(f"{'packet':12} {'AQI':>5} {'each':>12} {'subst':>5} {'voice':>5} {'ready':>5} {'slopN':>5} {'mathN':>5} {'edit':>6} {'K1q':>4} {'23q':>4} {'45q':>4} {'pg':>3} {'words':>5} {'tells':>5}")
for r in rows:
    print(f"{r['packet']:12} {r['AQI']:5.2f} {str(r['AQI_each']):>12} {r['substance']:5.2f} {r['human_voice']:5.2f} {r['readiness']:5.2f} {r['slop_edits']:5.1f} {r['math_edits']:5.1f} {r['edit_min']:6.1f} {r['quick_k-1']:4.0f} {r['quick_grades-2-3']:4.0f} {r['quick_grades-4-5']:4.0f} {r['pages'] or 0:3} {r['words'] or 0:5} {r['tells_per_100w'] or 0:5}")
print("\nPairs (A_score = share of both-order judgments won by A; 0.5 = tie/split):")
for p in pair_rows:
    print(f"  {p['A']:14} vs {p['B']:14} n={p['n']} A={p['A_score']:.2f}  K1={p['A_k-1']:.2f} 23={p['A_grades-2-3']:.2f} 45={p['A_grades-4-5']:.2f} str={p['strengths']}")
print("\nReliability:", rel, "pair order consistency (overall winner identical in both orders):", f"{consistent}/{total_pairs}")
