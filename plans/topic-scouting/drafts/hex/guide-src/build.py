"""Build the Hex facilitator guide.

Run inside this folder:  python3 build.py
Runs the answer checks, writes the figures, compiles facilitator.tex twice with
pdfLaTeX and writes ../facilitator.pdf.  Fails on any check failure, LaTeX
error or overfull box.
"""
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "facilitator.pdf")


def run(cmd):
    r = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout[-4000:], r.stderr[-2000:])
        raise SystemExit("failed: " + " ".join(cmd))
    return r.stdout


if __name__ == "__main__":
    out = run([sys.executable, "check_guide.py"])
    print(out.strip().splitlines()[-1])
    run([sys.executable, "figs.py"])
    for _ in range(2):
        run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "facilitator.tex"])
    log = open(os.path.join(HERE, "facilitator.log"), encoding="latin-1").read()
    bad = re.findall(r"^(Overfull|Underfull) .*$", log, re.M)
    if bad:
        print("\n".join(bad))
        raise SystemExit("box warnings in facilitator.log")
    shutil.move(os.path.join(HERE, "facilitator.pdf"), OUT)
    for ext in (".aux", ".log", ".out"):
        try:
            os.remove(os.path.join(HERE, "facilitator" + ext))
        except FileNotFoundError:
            pass
    print("built", OUT)
