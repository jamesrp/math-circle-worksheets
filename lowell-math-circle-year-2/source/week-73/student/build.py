#!/usr/bin/env python3
"""Build a self-contained student PDF. Requires Python 3 and pdflatex/TikZ."""
import argparse
import pathlib
import os
import shutil
import subprocess
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
p = argparse.ArgumentParser()
p.add_argument("--out", type=pathlib.Path, default=HERE.parent)
a = p.parse_args()
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
