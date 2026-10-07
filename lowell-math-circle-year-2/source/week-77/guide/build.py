#!/usr/bin/env python3
"""Build facilitator.pdf from this standalone folder with Python and pdfLaTeX."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def run(command, cwd, env):
    result = subprocess.run(command, cwd=cwd, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if result.returncode:
        raise RuntimeError(result.stdout[-14000:])
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    source = Path(__file__).resolve().parent
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, str(source / "check_math.py")], check=True)
    if shutil.which("pdflatex") is None:
        raise SystemExit("Install TeX Live or MacTeX with pdflatex, geometry, fancyhdr, amsmath and url.")
    with tempfile.TemporaryDirectory(prefix="week77-guide-", dir=out) as temp:
        work = Path(temp)
        shutil.copy2(source / "facilitator.tex", work / "facilitator.tex")
        env = os.environ.copy()
        # Minimal TeX images may have no filename database or initialized format.
        # Discover their installed trees, enable disk search, and initialize a
        # temporary format from the distribution. No runtime files are packaged.
        if shutil.which("kpsewhich"):
            fmt = subprocess.run(["kpsewhich", "pdflatex.fmt"], env=env,
                                 stdout=subprocess.PIPE, text=True).stdout.strip()
            if not fmt:
                if "TEXMF" not in env:
                    trees = run(["kpsewhich", "-var-value=TEXMF"], work, env).strip()
                    env["TEXMF"] = trees.replace("!!", "")
                log = run(["pdftex", "-ini", "-etex", "-jobname=pdflatex",
                           "-interaction=nonstopmode", "-halt-on-error", "pdflatex.ini"],
                          work, env)
                (out / "format-build.log").write_text(log, encoding="utf-8")
                env["TEXFORMATS"] = str(work) + os.pathsep + env.get("TEXFORMATS", "")
        try:
            log = run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                       "-file-line-error", "facilitator.tex"], work, env)
        except RuntimeError as error:
            (out / "build.log").write_text(str(error), encoding="utf-8")
            raise SystemExit(str(error))
        (out / "build.log").write_text(log, encoding="utf-8")
        if "Overfull" in log:
            raise SystemExit("Overfull TeX box: inspect build.log before delivery.")
        shutil.copy2(work / "facilitator.pdf", out / "facilitator.pdf")
    print(out / "facilitator.pdf")


if __name__ == "__main__":
    main()
