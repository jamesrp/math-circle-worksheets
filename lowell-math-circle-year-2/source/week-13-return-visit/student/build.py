#!/usr/bin/env python3
"""Build the return-visit PDF from this folder, with no repository dependencies."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

here = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--out", type=Path, default=here.parent / "return-visit.pdf")
parser.add_argument("--pdflatex", default=os.environ.get("PDFLATEX", "pdflatex"))
args = parser.parse_args()
engine = shutil.which(args.pdflatex)
if engine is None and Path(args.pdflatex).is_file():
    engine = str(Path(args.pdflatex).resolve())
if engine is None:
    raise SystemExit("pdflatex is required; put it on PATH or pass --pdflatex /path/to/pdflatex")
out = args.out.resolve()
out.parent.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory(prefix="return-visit-build-", dir=out.parent) as temp:
    command = [engine, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
               "-output-directory", temp, str(here / "return-visit.tex")]
    result = subprocess.run(command, cwd=here, text=True, capture_output=True)
    if result.returncode:
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(result.returncode)
    warnings = [line for line in result.stdout.splitlines()
                if "Overfull" in line or "Underfull" in line]
    if warnings:
        print("\n".join(warnings))
    shutil.copyfile(Path(temp) / "return-visit.pdf", out)
print(out)
