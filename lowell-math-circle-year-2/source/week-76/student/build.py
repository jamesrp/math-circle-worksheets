#!/usr/bin/env python3
"""Build the student packet with Python's standard library and pdfLaTeX."""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True, type=Path, help="Directory for students.pdf")
    args = parser.parse_args()
    source = Path(__file__).resolve().parent
    output = args.out.resolve()
    output.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, str(source / "check_math.py")], check=True)
    latex = shutil.which("pdflatex")
    if latex is None:
        raise SystemExit("Install a normal TeX Live distribution with pdfLaTeX, TikZ, fancyhdr, geometry and Latin Modern.")
    with tempfile.TemporaryDirectory(prefix="substitution-build-", dir=output) as tmp:
        work = Path(tmp)
        shutil.copy2(source / "students.tex", work / "students.tex")
        command = [latex, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "students.tex"]
        for _ in range(2):
            result = subprocess.run(command, cwd=work, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if result.returncode:
                (output / "build-error.log").write_text(result.stdout)
                raise SystemExit(f"pdfLaTeX failed; see {output / 'build-error.log'}")
        log = (work / "students.log").read_text(errors="replace")
        if "Overfull" in log:
            (output / "build-error.log").write_text(log)
            raise SystemExit(f"Overfull TeX box; see {output / 'build-error.log'}")
        shutil.copy2(work / "students.pdf", output / "students.pdf")
    print(output / "students.pdf")


if __name__ == "__main__":
    main()
