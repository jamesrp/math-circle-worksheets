#!/usr/bin/env python3
"""Build materials.pdf (the letter tiles) with only Python's standard library and pdfLaTeX."""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True, help="Directory for materials.pdf")
    args = parser.parse_args()
    source = Path(__file__).resolve().parent
    output = args.out.resolve()
    output.mkdir(parents=True, exist_ok=True)
    latex = shutil.which("pdflatex")
    if latex is None:
        raise SystemExit("Install TeX Live or MacTeX with pdfLaTeX and the packages listed in README.md.")
    with tempfile.TemporaryDirectory(prefix="substitution-materials-", dir=output) as temp:
        work = Path(temp)
        shutil.copy2(source / "materials.tex", work / "materials.tex")
        for _ in range(2):
            result = subprocess.run([latex, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "materials.tex"], cwd=work, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if result.returncode:
                (output / "build-error.log").write_text(result.stdout)
                raise SystemExit(f"pdfLaTeX failed; see {output / 'build-error.log'}")
        log = (work / "materials.log").read_text(errors="replace")
        if "Overfull" in log:
            (output / "build-error.log").write_text(log)
            raise SystemExit(f"Overfull TeX box; see {output / 'build-error.log'}")
        shutil.copy2(work / "materials.pdf", output / "materials.pdf")
    print(output / "materials.pdf")


if __name__ == "__main__":
    main()
