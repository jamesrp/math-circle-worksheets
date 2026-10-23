#!/usr/bin/env python3
"""Build the stride-strip materials page using Python 3 and an ordinary pdflatex installation."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--out", type=Path, default=HERE.parent)
args = parser.parse_args()
out = args.out.resolve()
out.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory(prefix="ggt-materials-") as temp:
    env = os.environ.copy()
    env["TEXMFVAR"] = str(Path(temp) / "texmf-var")
    env["TEXMFCONFIG"] = str(Path(temp) / "texmf-config")
    result = subprocess.run([
        "pdflatex", "-halt-on-error", "-interaction=nonstopmode",
        "-output-directory", temp, str(HERE / "materials.tex")
    ], cwd=HERE, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log = result.stdout.decode(errors="replace")
    if result.returncode:
        print(log)
        raise SystemExit(result.returncode)
    if "Overfull" in log:
        print(log)
        raise SystemExit("Overfull TeX box: inspect and correct before release.")
    shutil.copyfile(Path(temp) / "materials.pdf", out / "materials.pdf")
print(out / "materials.pdf")
