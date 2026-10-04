#!/usr/bin/env python3
"""Set up multi-stage (wave 2+) runs and write their stage prompt files.

  make_stage.py post RUN_ID BASE_RUN_ID            # copy base draft into runs/RUN_ID (base/, src/, BRIEF.md)
  make_stage.py critic RUN_ID TYPE                 # TYPE in generic|checklist|sim|math -> runs/RUN_ID/CRITIC.md
  make_stage.py reviser RUN_ID TYPE [REVIEW_FILE]  # TYPE in generic|min -> runs/RUN_ID/REVISE.md
  make_stage.py designer RUN_ID OUTLINE            # -> runs/RUN_ID/DESIGN-PROMPT.md
  make_stage.py writer-design RUN_ID OUTLINE       # -> runs/RUN_ID/PROMPT.md (A3 prompt + design note)
"""
import hashlib, json, os, shutil, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from make_prompt import build, blk, inp, OUTLINES

ROOT = "/home/claude/genlab"
S = f"{ROOT}/prompts/stages"

def st(name):
    return open(f"{S}/{name}.md").read().strip()

def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()[:12]

def record(run, name, text, extra=None):
    meta = {"file": name, "sha12": sha(text.replace(run, "{{RUN_DIR}}")), "words": len(text.split()),
            "created": datetime.datetime.now().isoformat(timespec="seconds")} | (extra or {})
    with open(f"{run}/STAGES.jsonl", "a") as f:
        f.write(json.dumps(meta) + "\n")
    print(json.dumps(meta))

ISOLATION = ("Work only inside {{RUN_DIR}}: do not read any file outside it, do not use web search or fetch, "
             "and do not use remote-device, computer, or browser tools.")

def files_block(run):
    return st("common-files").replace("{{RUN_DIR}}", run)

def main():
    cmd, rid = sys.argv[1], sys.argv[2]
    run = f"{ROOT}/runs/{rid}"
    if cmd == "post":
        base = f"{ROOT}/runs/{sys.argv[3]}"
        os.makedirs(run, exist_ok=True)
        shutil.copytree(f"{base}/final", f"{run}/base", dirs_exist_ok=True)
        shutil.copytree(f"{base}/src", f"{run}/src", dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns("png", "__pycache__", "*.aux", "*.log"))
        os.makedirs(f"{run}/final", exist_ok=True)
        os.makedirs(f"{run}/scratch", exist_ok=True)
        brief = open(f"{base}/PROMPT.md").read().replace(base, run).replace(f"runs/{sys.argv[3]}", run)
        open(f"{run}/BRIEF.md", "w").write(brief)
        record(run, "BRIEF.md", brief, {"base_run": sys.argv[3]})
    elif cmd == "critic":
        t = st(f"critic-{sys.argv[3]}").replace("{{FILES}}", files_block(run)).replace("{{RUN_DIR}}", run)
        open(f"{run}/CRITIC.md", "w").write(t + "\n")
        record(run, "CRITIC.md", t, {"critic": sys.argv[3]})
    elif cmd == "reviser":
        t = st(f"reviser-{sys.argv[3]}").replace("{{FILES}}", files_block(run)).replace("{{RUN_DIR}}", run)
        if len(sys.argv) > 4:
            t = t.replace("review.md", sys.argv[4])
        open(f"{run}/REVISE.md", "w").write(t + "\n")
        record(run, "REVISE.md", t, {"reviser": sys.argv[3]})
    elif cmd == "designer":
        outline = sys.argv[3]
        os.makedirs(f"{run}/design-checks", exist_ok=True)
        ocs = "\n\n\n".join([f"=== Activity outline ===\n\n{inp(OUTLINES[outline])}",
                             f"=== Session context ===\n\n{inp('context.md')}", blk("spec")])
        t = (st("designer").replace("{{OUTLINE_CONTEXT_SPEC}}", ocs)
             .replace("{{ISOLATION}}", ISOLATION).replace("{{RUN_DIR}}", run))
        open(f"{run}/DESIGN-PROMPT.md", "w").write(t + "\n")
        record(run, "DESIGN-PROMPT.md", t, {"outline": outline})
    elif cmd == "writer-design":
        outline = sys.argv[3]
        os.makedirs(f"{run}/src", exist_ok=True); os.makedirs(f"{run}/final", exist_ok=True)
        base = build("A3", outline, run)
        note = st("writer-from-design").replace("{{RUN_DIR}}", run)
        ask_end = base.index("\n\n\n")  # after the opening ask paragraph
        t = base[:ask_end] + "\n\n" + note + base[ask_end:]
        t = t.replace(f"Do not read any file outside {run}", f"Do not read any file outside {run}")
        open(f"{run}/PROMPT.md", "w").write(t)
        record(run, "PROMPT.md", t, {"outline": outline, "base_arm": "A3+design"})
    else:
        raise SystemExit(cmd)

if __name__ == "__main__":
    main()
