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

--bands k-1 (or any comma-separated subset of k-1, grades-2-3, grades-4-5)
asks for those packets only, for example K-1 pages for a week whose other
bands already exist. The default asks for all three, with the tested text.
"""
import argparse, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

def read(*parts):
    return open(os.path.join(HERE, *parts)).read().strip()

BANDS = ["k-1", "grades-2-3", "grades-4-5"]
NAMES = {"k-1": "K–1", "grades-2-3": "grades 2–3", "grades-4-5": "grades 4–5"}
COUNT = {1: "", 2: "two "}

def sub(text, old, new):
    if old not in text:
        sys.exit(f"make_prompts.py: expected text not found, so --bands cannot be applied: {old!r}")
    return text.replace(old, new)

def narrow(name, text, bands):
    """Rewrite one stage file for a subset of the three bands."""
    if bands == BANDS:
        return text
    n = len(bands)
    pdfs = lambda d: "".join(f"  {{{{RUN_DIR}}}}/{d}/{b}.pdf\n" for b in bands)
    all_pdfs = lambda d: "".join(f"  {{{{RUN_DIR}}}}/{d}/{b}.pdf\n" for b in BANDS)
    paths = "PDF at exactly this path" if n == 1 else f"{COUNT[n]}PDFs at exactly these paths"
    reply = "the PDF path and its page count" if n == 1 else f"the {COUNT[n]}PDF paths and their page counts"
    draft = ", ".join(f"draft/{b}.pdf" for b in bands)
    if name == "spec-ask":
        ones = [f"one PDF for {NAMES[b]}" if i == 0 else f"one for {NAMES[b]}" for i, b in enumerate(bands)]
        text = sub(text, "one PDF for K–1, one for grades 2–3, and one for grades 4–5", " and ".join(ones))
    if name == "harness":
        text = sub(text, "the three finished PDFs at exactly these paths", "the finished " + paths)
        text = sub(text, all_pdfs("draft"), pdfs("draft"))
        text = sub(text, "reply with the three PDF paths and their page counts", "reply with " + reply)
    if name in ("critic", "critic-math", "reviser"):
        text = sub(text, "draft/k-1.pdf, draft/grades-2-3.pdf, draft/grades-4-5.pdf: the author's draft.", draft + ": the author's draft.")
    if name == "critic-math":
        scope = f"For every problem in the {NAMES[bands[0]]} packet:" if n == 1 else "For every problem in every band (" + ", ".join(NAMES[b] for b in bands) + "):"
        text = sub(text, "For every problem in every band (K–1, grades 2–3, grades 4–5):", scope)
    if name == "reviser":
        text = sub(text, "build the three PDFs at exactly these paths", "build the " + paths)
        text = sub(text, all_pdfs("final"), pdfs("final"))
        text = sub(text, "Reply with the three PDF paths and their page counts", "Reply with " + reply)
    return text

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outline", required=True, help="outline file (see outlines/TEMPLATE.md)")
    ap.add_argument("--run", required=True, help="run folder to create, e.g. tmp/worksheet-runs/week-03-v1")
    ap.add_argument("--context", default=os.path.join(HERE, "context.md"), help="session context file")
    ap.add_argument("--bands", default=",".join(BANDS), help="packets to write: a comma-separated subset of " + ", ".join(BANDS))
    a = ap.parse_args()
    bands = [b for b in BANDS if b in a.bands.split(",")]
    if not bands or sorted(bands) != sorted(set(a.bands.split(","))):
        sys.exit("--bands must be a comma-separated subset of " + ", ".join(BANDS))

    run = os.path.abspath(a.run)
    if os.path.exists(os.path.join(run, "PROMPT.md")):
        sys.exit(f"{run} already has a PROMPT.md; use a new run folder.")
    os.makedirs(os.path.join(run, "draft", "src"), exist_ok=True)
    os.makedirs(os.path.join(run, "final"), exist_ok=True)

    outline = open(a.outline).read().strip()
    context = open(a.context).read().strip()
    writer = "\n\n\n".join([
        narrow("spec-ask", read("blocks", "spec-ask.md"), bands),
        "=== Activity outline ===\n\n" + outline,
        "=== Session context ===\n\n" + context,
        read("blocks", "spec.md"),
        read("blocks", "neg.md"),
        read("blocks", "exemplars.md"),
        narrow("harness", read("blocks", "harness.md"), bands),
    ]).replace("{{RUN_DIR}}", run) + "\n"
    stage = lambda f: narrow(f, read("stages", f + ".md"), bands).replace("{{RUN_DIR}}", run) + "\n"
    files = {
        "PROMPT.md": writer,
        "CRITIC.md": stage("critic"),
        "CRITIC-MATH.md": stage("critic-math"),
        "REVISE.md": stage("reviser"),
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
