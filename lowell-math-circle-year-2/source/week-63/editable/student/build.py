#!/usr/bin/env python3
"""Portable two-PDF build. No generated files are written into this source folder."""
import argparse
import os
from pathlib import Path
import subprocess

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    src = Path(__file__).resolve().parent
    out = args.out.resolve()
    if out == src or src in out.parents:
        parser.error("--out must be outside the authored source folder")
    out.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["SOURCE_DATE_EPOCH"] = "946684800"
    env["FORCE_SOURCE_DATE"] = "1"
    for stem in ("students", "materials"):
        log = out / f"{stem}-build.log"
        with log.open("w") as stream:
            subprocess.run(
                ["pdflatex", "-halt-on-error", "-interaction=nonstopmode",
                 "-file-line-error", f"-output-directory={out}", f"{stem}.tex"],
                cwd=src, env=env, stdout=stream, stderr=subprocess.STDOUT, check=True, timeout=60)
        print(out / f"{stem}.pdf")

if __name__ == "__main__":
    main()
