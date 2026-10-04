"""Build both original Week 59 PDFs; all intermediates stay in OUTPUT/.build."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
sys.dont_write_bytecode=True
from make_assets import make_all


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("output",type=Path)
    args=ap.parse_args()
    out=args.output.resolve()
    out.mkdir(parents=True,exist_ok=True)
    work=out/".build"
    work.mkdir(exist_ok=True)
    src=Path(__file__).resolve().parent
    make_all(work)
    env=dict(os.environ)
    env["SOURCE_DATE_EPOCH"]="1791072000"
    env["FORCE_SOURCE_DATE"]="1"
    for name in ["students","materials"]:
        shutil.copy2(src/(name+".tex"),work/(name+".tex"))
        command=["pdflatex","-interaction=nonstopmode","-halt-on-error","-file-line-error",name+".tex"]
        for _ in range(2):
            done=subprocess.run(command,cwd=work,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            (work/(name+"-console.txt")).write_text(done.stdout)
            if done.returncode:
                print(done.stdout)
                raise SystemExit(done.returncode)
        log=(work/(name+".log")).read_text()
        if "Overfull" in log:
            print("Layout warning in",name)
            print("\n".join(x for x in log.splitlines() if "Overfull" in x))
            raise SystemExit(2)
        shutil.copy2(work/(name+".pdf"),out/(name+".pdf"))
        print(out/(name+".pdf"))


if __name__=="__main__":
    main()
