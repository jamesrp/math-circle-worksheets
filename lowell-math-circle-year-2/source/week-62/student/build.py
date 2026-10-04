#!/usr/bin/env python3
"""Build the PDF in an explicit output directory, keeping TeX artifacts there."""
from pathlib import Path
import argparse, subprocess, sys
p=argparse.ArgumentParser()
p.add_argument("--out",required=True,type=Path)
a=p.parse_args()
src=Path(__file__).resolve().parent
out=a.out.resolve()
out.mkdir(parents=True,exist_ok=True)
subprocess.run([sys.executable,str(src/"make_source.py"),"--out",str(out)],check=True)
subprocess.run(["pdflatex","-interaction=nonstopmode","-halt-on-error",f"-output-directory={out}",str(out/"students.tex")],check=True,cwd=out,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
print(out/"students.pdf")
