#!/usr/bin/env python3
"""Build the student PDF. Requires Python 3.11+ and pdflatex/TikZ.

students.tex is written from the problem files by regenerate.py, which this script
runs first unless --no-regenerate is given (the package's root build.py regenerates
in place, then builds a copy)."""
import argparse
import pathlib
import os
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
p = argparse.ArgumentParser()
p.add_argument("--out", type=pathlib.Path, default=HERE.parent)
p.add_argument("--no-regenerate", action="store_true", help="compile students.tex as it is")
a = p.parse_args()
if not a.no_regenerate:
    subprocess.run([sys.executable, str(HERE / "regenerate.py")], check=True)
a.out.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory(prefix="worksheet-") as tmp:
    env = os.environ.copy()
    env["TEXMFVAR"] = str(pathlib.Path(tmp) / "texmf-var")
    env["TEXMFCONFIG"] = str(pathlib.Path(tmp) / "texmf-config")
    result = subprocess.run(["pdflatex", "-halt-on-error", "-interaction=nonstopmode", "-output-directory", tmp, str(HERE / "students.tex")], cwd=HERE, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if result.returncode:
        print(result.stdout.decode(errors="replace"))
        raise SystemExit(result.returncode)
    shutil.copy2(pathlib.Path(tmp) / "students.pdf", a.out / "students.pdf")
print(a.out / "students.pdf")
