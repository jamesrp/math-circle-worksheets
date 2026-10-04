#!/usr/bin/env python3
"""Standalone builder; source stays clean and TeX intermediates are temporary."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
sys.dont_write_bytecode = True
from generate_figures import generate


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", required=True)
    args = p.parse_args()
    root = Path(__file__).resolve().parent
    output = Path(args.output_dir).resolve()
    output.mkdir(parents=True, exist_ok=True)
    if not shutil.which("pdflatex"):
        raise SystemExit("pdflatex is required (standard TeX Live/MacTeX).")
    with tempfile.TemporaryDirectory(prefix="week57-build-", dir=output) as working:
        work = Path(working)
        shutil.copy2(root / "students.tex", work / "students.tex")
        generate(work / "figures.tex")
        env = dict(os.environ, SOURCE_DATE_EPOCH="1791072000", FORCE_SOURCE_DATE="1")
        for _ in range(2):
            run = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "students.tex"], cwd=work, env=env, capture_output=True, text=True)
            output.joinpath("compile.log").write_text(run.stdout + run.stderr)
            if run.returncode:
                raise SystemExit("LaTeX failed; see " + str(output / "compile.log"))
        log = work.joinpath("students.log").read_text()
        output.joinpath("tex.log").write_text(log)
        if "Overfull" in log or "LaTeX Error" in log:
            raise SystemExit("Layout/LaTeX error; see " + str(output / "tex.log"))
        shutil.copy2(work / "students.pdf", output / "students.pdf")
    print(output / "students.pdf")


if __name__ == "__main__":
    main()
