#!/usr/bin/env python3
"""Build the original student PDF with standard pdflatex; no network needed."""
from pathlib import Path
import argparse
import shutil
import subprocess

p = argparse.ArgumentParser()
p.add_argument("output_dir", type=Path)
a = p.parse_args()
source = Path(__file__).resolve().parent / "students.tex"
out = a.output_dir.resolve()
if out == source.parent or source.parent in out.parents:
    p.error("output directory must be outside the editable source directory")
build = out / ".build"
build.mkdir(parents=True, exist_ok=True)
command = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
           f"-output-directory={build}", str(source)]
for _ in range(2):
    subprocess.run(command, cwd=source.parent, check=True, stdout=subprocess.PIPE,
                   stderr=subprocess.STDOUT)
shutil.copy2(build / "students.pdf", out / "students.pdf")
print(out / "students.pdf")
