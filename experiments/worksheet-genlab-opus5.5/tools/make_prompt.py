#!/usr/bin/env python3
"""Assemble a frozen single-agent writer prompt for an arm and write it into a run directory.

Usage: make_prompt.py ARM OUTLINE RUN_DIR [--out NAME]
  ARM     one of the keys in ARMS below
  OUTLINE A (tiling) or B (games)
"""
import hashlib, os, sys, json, datetime

ROOT = "/home/claude/genlab"
B = f"{ROOT}/prompts/blocks"
INP = f"{ROOT}/inputs"

def blk(name):
    return open(f"{B}/{name}.md").read().strip()

def inp(name):
    return open(f"{INP}/{name}").read().strip()

OUTLINES = {"A": "outline-A-tiling.md", "B": "outline-B-games.md"}

# Each arm = ordered list of (section title or None, source)
ARMS = {
    "A0": [(None, "blk:naive-ask"), ("Activity outline", "outline"), ("Session context", "inp:context.md"), (None, "harness")],
    "A1": [(None, "blk:naive-ask"), ("Activity outline", "outline"), ("Session context", "inp:context.md"), (None, "blk:neg"), (None, "harness")],
    "A2": [(None, "blk:spec-ask"), ("Activity outline", "outline"), ("Session context", "inp:context.md"), (None, "blk:spec"), (None, "harness")],
    "A3": [(None, "blk:spec-ask"), ("Activity outline", "outline"), ("Session context", "inp:context.md"), (None, "blk:spec"), (None, "blk:neg"), (None, "blk:exemplars"), (None, "harness")],
}

def build(arm, outline, run_dir):
    parts = []
    for title, src in ARMS[arm]:
        if src == "outline":
            text = inp(OUTLINES[outline])
        elif src == "harness":
            text = inp("harness.md").replace("{{RUN_DIR}}", run_dir)
        elif src.startswith("blk:"):
            text = blk(src[4:])
        elif src.startswith("inp:"):
            text = inp(src[4:])
        else:
            raise ValueError(src)
        if title:
            text = f"=== {title} ===\n\n{text}"
        parts.append(text)
    return "\n\n\n".join(parts) + "\n"

if __name__ == "__main__":
    arm, outline, run_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    name = sys.argv[5] if len(sys.argv) > 5 and sys.argv[4] == "--out" else "PROMPT.md"
    os.makedirs(f"{run_dir}/src", exist_ok=True)
    os.makedirs(f"{run_dir}/final", exist_ok=True)
    text = build(arm, outline, run_dir)
    path = f"{run_dir}/{name}"
    open(path, "w").write(text)
    h = hashlib.sha256(text.replace(run_dir, "{{RUN_DIR}}").encode()).hexdigest()[:12]
    meta = {"arm": arm, "outline": outline, "prompt_file": name, "prompt_sha12": h,
            "words": len(text.split()), "created": datetime.datetime.now().isoformat(timespec="seconds")}
    open(f"{run_dir}/{name}.meta.json", "w").write(json.dumps(meta, indent=1))
    print(json.dumps(meta))
