#!/usr/bin/env python3
"""Build the original standalone guide; write every intermediate under output."""
from pathlib import Path
import shutil
import subprocess
import sys

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 build.py OUTPUT_DIRECTORY")
    src = Path(__file__).resolve().parent
    out = Path(sys.argv[1]).resolve()
    build = out / "build"
    build.mkdir(parents=True, exist_ok=True)
    cmd = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
           "-file-line-error", f"-output-directory={build}", str(src / "facilitator.tex")]
    with (build / "console.log").open("w") as log:
        for _ in range(2):
            subprocess.run(cmd, cwd=src, stdout=log, stderr=subprocess.STDOUT, check=True)
    shutil.copyfile(build / "facilitator.pdf", out / "facilitator.pdf")
    print(out / "facilitator.pdf")

if __name__ == "__main__":
    main()
