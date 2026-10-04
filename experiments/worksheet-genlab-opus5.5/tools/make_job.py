#!/usr/bin/env python3
"""Build a judge job file from the frozen eval prompt templates.

Usage:
  make_job.py audit PID OUTLINE K        -> eval/jobs/audit-PID-K/JOB.md, output eval/results/PID/audit-K.json
  make_job.py pair  PIDX PIDY OUTLINE    -> eval/jobs/pair-PIDX-PIDY/JOB.md, output eval/results/pairs/PIDX__PIDY.json
Prints the job path. Appends to eval/jobs/index.jsonl.
"""
import hashlib, json, os, sys, datetime

ROOT = "/home/claude/genlab"
P = f"{ROOT}/eval/prompts"
OUTLINES = {"A": "outline-A-tiling.md", "B": "outline-B-games.md"}

def read(p):
    return open(p).read().strip()

def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()[:12]

def common(outline):
    return {
        "{{STANDARD}}": read(f"{P}/judge-standard.md"),
        "{{OUTLINE}}": read(f"{ROOT}/inputs/{OUTLINES[outline]}"),
        "{{CONTEXT}}": read(f"{ROOT}/inputs/context.md"),
    }

def fill(tmpl, subs):
    for k, v in subs.items():
        tmpl = tmpl.replace(k, v)
    assert "{{" not in tmpl, tmpl[tmpl.index("{{"):tmpl.index("{{") + 40]
    return tmpl

def main():
    kind = sys.argv[1]
    if kind == "audit":
        pid, outline, k = sys.argv[2], sys.argv[3], sys.argv[4]
        tmpl = read(f"{P}/AUDIT.md")
        out = f"{ROOT}/eval/results/{pid}/audit-{k}.json"
        subs = common(outline) | {"{{PID}}": pid, "{{BUNDLE}}": f"{ROOT}/eval/bundles/{pid}", "{{OUT}}": out}
        job = f"{ROOT}/eval/jobs/audit-{pid}-{k}"
        pids = [pid]
    elif kind == "pair":
        x, y, outline = sys.argv[2], sys.argv[3], sys.argv[4]
        tmpl = read(f"{P}/PAIR.md")
        out = f"{ROOT}/eval/results/pairs/{x}__{y}.json"
        subs = common(outline) | {"{{PID_X}}": x, "{{PID_Y}}": y, "{{BUNDLE_X}}": f"{ROOT}/eval/bundles/{x}",
                                  "{{BUNDLE_Y}}": f"{ROOT}/eval/bundles/{y}", "{{OUT}}": out}
        job = f"{ROOT}/eval/jobs/pair-{x}-{y}"
        pids = [x, y]
    else:
        raise SystemExit("kind?")
    os.makedirs(job, exist_ok=True)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    text = fill(tmpl, subs)
    open(f"{job}/JOB.md", "w").write(text + "\n")
    rec = {"job": os.path.basename(job), "kind": kind, "pids": pids, "outline": outline, "out": out,
           "template_sha": sha(tmpl), "standard_sha": sha(read(f"{P}/judge-standard.md")),
           "created": datetime.datetime.now().isoformat(timespec="seconds")}
    with open(f"{ROOT}/eval/jobs/index.jsonl", "a") as f:
        f.write(json.dumps(rec) + "\n")
    print(f"{job}/JOB.md")

if __name__ == "__main__":
    main()
