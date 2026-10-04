#!/usr/bin/env python3
"""Assemble the stage prompts for one run of the worksheet workflow.

Usage:
  python3 worksheet-workflow/make_prompts.py --outline worksheet-workflow/outlines/week-03-x.md --run tmp/worksheet-runs/week-03-v1

Writes into the run folder:
  PROMPT.md       writer: outline + context + standard + do-not list + examples + technical notes
  CRITIC.md       generic adversarial review   -> review.md
  CRITIC-MATH.md  optional correctness check   -> review-math.md
  REVISE.md       revision                     -> final/*.pdf
Each stage is meant for a fresh agent. See worksheet-workflow/README.md.
"""
import argparse, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

def read(*parts):
    return open(os.path.join(HERE, *parts)).read().strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outline", required=True, help="outline file (see outlines/TEMPLATE.md)")
    ap.add_argument("--run", required=True, help="run folder to create, e.g. tmp/worksheet-runs/week-03-v1")
    ap.add_argument("--context", default=os.path.join(HERE, "context.md"), help="session context file")
    a = ap.parse_args()

    run = os.path.abspath(a.run)
    if os.path.exists(os.path.join(run, "PROMPT.md")):
        sys.exit(f"{run} already has a PROMPT.md; use a new run folder.")
    os.makedirs(os.path.join(run, "draft", "src"), exist_ok=True)
    os.makedirs(os.path.join(run, "final"), exist_ok=True)

    outline = open(a.outline).read().strip()
    context = open(a.context).read().strip()
    writer = "\n\n\n".join([
        read("blocks", "spec-ask.md"),
        "=== Activity outline ===\n\n" + outline,
        "=== Session context ===\n\n" + context,
        read("blocks", "spec.md"),
        read("blocks", "neg.md"),
        read("blocks", "exemplars.md"),
        read("blocks", "harness.md"),
    ]).replace("{{RUN_DIR}}", run) + "\n"
    files = {
        "PROMPT.md": writer,
        "CRITIC.md": read("stages", "critic.md").replace("{{RUN_DIR}}", run) + "\n",
        "CRITIC-MATH.md": read("stages", "critic-math.md").replace("{{RUN_DIR}}", run) + "\n",
        "REVISE.md": read("stages", "reviser.md").replace("{{RUN_DIR}}", run) + "\n",
    }
    for name, text in files.items():
        with open(os.path.join(run, name), "w") as f:
            f.write(text)
    print(f"Run folder: {run}")
    print("Next, each in a fresh agent:")
    print(f"  1. {run}/PROMPT.md       (writer -> draft/*.pdf)")
    print(f"  2. {run}/CRITIC.md       (review -> review.md)")
    print(f"     {run}/CRITIC-MATH.md  (optional, for enumeration-heavy weeks -> review-math.md)")
    print(f"  3. {run}/REVISE.md       (revision -> final/*.pdf)")

if __name__ == "__main__":
    main()
