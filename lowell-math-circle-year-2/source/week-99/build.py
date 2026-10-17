#!/usr/bin/env python3
"""Build the owned Week 99 family; the source ZIP needs no checkout or network."""
import argparse, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
WEEK=99

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,default=ROOT/'out')
    ap.add_argument('--work',type=Path)
    args=ap.parse_args()
    out=args.out.resolve(); out.mkdir(parents=True,exist_ok=True)
    repo=ROOT.parents[2] if len(ROOT.parents)>2 else ROOT
    work=(args.work or (repo/'tmp/pdf-builds' if (repo/'AGENTS.md').exists() else ROOT/'tmp')).resolve()
    work.mkdir(parents=True,exist_ok=True)
    latex=shutil.which('pdflatex')
    if not latex:
        raise SystemExit('Install TeX Live with pdfLaTeX, TikZ, geometry, fancyhdr, lmodern and standard math packages.')
    env=dict(os.environ,SOURCE_DATE_EPOCH='1792195200',FORCE_SOURCE_DATE='1')
    check=subprocess.run([sys.executable,str(ROOT/'check_math.py')],cwd=work,env=env,text=True,capture_output=True)
    (work/f'week-{WEEK}-math.txt').write_text(check.stdout+check.stderr)
    if check.returncode:raise SystemExit(check.stdout+check.stderr)
    targets=json.loads((ROOT/'build-targets.json').read_text())
    with tempfile.TemporaryDirectory(prefix=f'week-{WEEK}-',dir=work) as temp:
        for ix,target in enumerate(targets):
            sources=[ROOT/p for p in target.get('sources',[target.get('source')])]
            folder=Path(temp)/str(ix)
            shutil.copytree(sources[0].parent,folder,ignore=shutil.ignore_patterns('*.pdf','*.aux','*.log','*.out','__pycache__'))
            pdfs=[]
            for source in sources:
                if source.parent != sources[0].parent: raise SystemExit('A multipart target must share one source folder.')
                for _ in range(2):
                    run=subprocess.run([latex,'-interaction=nonstopmode','-halt-on-error',source.name],cwd=folder,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                    (work/f"week-{WEEK}-{source.stem}.log").write_text(run.stdout)
                    if run.returncode:raise SystemExit(run.stdout[-6000:])
                if 'Overfull' in run.stdout:raise SystemExit('Overfull content in '+source.name+'; inspect the build log.')
                pdfs.append(folder/(source.stem+'.pdf'))
            if len(pdfs)==1:
                shutil.copy2(pdfs[0],out/target['output'])
            else:
                try: from pypdf import PdfReader,PdfWriter
                except ImportError: raise SystemExit('This mixed-orientation packet also requires pypdf: python3 -m pip install pypdf')
                writer=PdfWriter()
                for pdf in pdfs:
                    for page in PdfReader(pdf).pages:writer.add_page(page)
                writer.add_metadata({'/Title':f"Week {WEEK} / "+target['output'],'/Creator':'Bellingham Math Circle'})
                with (out/target['output']).open('wb') as f:writer.write(f)
    print(f'PASS: Week {WEEK}; {len(targets)} PDFs; mathematical checks passed.')
if __name__=='__main__':main()
