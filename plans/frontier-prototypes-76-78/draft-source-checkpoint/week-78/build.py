#!/usr/bin/env python3
"""Build the original Week 78 packet with Python's standard library and TeX."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys

import data

HERE = Path(__file__).resolve().parent

def run(args, *, cwd, env, log):
    result = subprocess.run(args, cwd=cwd, env=env, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True)
    log.write_text(result.stdout)
    if result.returncode:
        print(result.stdout[-12000:], file=sys.stderr)
        raise SystemExit(f"Command failed; see {log}")

def point_macro(kind, xy, label):
    return rf"\{kind}{{{xy[0]}}}{{{xy[1]}}}{{{label}}}"

def boards(pairs, scale, kind, columns=2):
    chunks=[]
    for row_start in range(0,len(pairs),columns):
        row=[]
        for pair in pairs[row_start:row_start+columns]:
            labels = ('A','B') if kind == 'junction' else ('P','Q')
            commands=[point_macro(kind,p,labels[i]) for i,p in enumerate(pair)]
            commands+=['']*(2-len(commands))
            row.append(rf"\board{{{scale}}}{{{commands[0]}}}{{{commands[1]}}}")
        chunks.append(r"\noindent " + r"\hfill ".join(row))
    return "\n\\par\\vspace{7pt}\n".join(chunks)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',required=True,type=Path)
    args=parser.parse_args()
    out=args.out.expanduser().resolve()
    out.mkdir(parents=True,exist_ok=True)
    build=out/'.build'
    build.mkdir(exist_ok=True)
    env=os.environ.copy()
    env.update({'TEXMFVAR':str(build/'texmf-var'),
                'TEXMFCONFIG':str(build/'texmf-config'),
                'TEXMFOUTPUT':str(build)})
    # A normal TeX install needs no special setup. Some minimal containers ship
    # all TeX files but omit databases and formats. Read-only disk search and a
    # format generated inside --out make that case reproducible too.
    kpse=shutil.which('kpsewhich')
    if not shutil.which('pdflatex') or not kpse:
        raise SystemExit('Install a TeX distribution with pdflatex, TikZ, and Latin Modern.')
    cls=subprocess.run([kpse,'article.cls'],env=env,capture_output=True,text=True)
    if not cls.stdout.strip():
        roots=subprocess.check_output([kpse,'-var-value=TEXMF'],env=env,text=True).strip()
        env['TEXMF']=roots.replace('!!','')
        roots=subprocess.check_output([kpse,'-var-value=TEXMFDBS'],env=env,text=True).strip()
        env['TEXMFDBS']=roots.replace('!!','')
    fmt=subprocess.run([kpse,'pdflatex.fmt'],env=env,capture_output=True,text=True)
    if not fmt.stdout.strip():
        env['TEXFORMATS']=str(build)+os.pathsep+env.get('TEXFORMATS','')
        if not (build/'pdflatex.fmt').exists():
            run(['pdftex','-ini','-etex','-interaction=nonstopmode','-halt-on-error',
                 '-jobname=pdflatex','pdflatex.ini'],cwd=build,env=env,
                log=build/'format-build.log')
    subprocess.run([sys.executable,str(HERE/'check_math.py')],check=True,cwd=HERE)
    defs={
      'TrialBoards':boards(((data.TRIAL_JUNCTION,),)*4,.71,'junction'),
      'IntersectionBoards':boards(data.INTERSECTION_PAIRS,.82,'junction'),
      'GeneralBoards':boards(data.INVERSE_GENERAL,.83,'target'),
      'AlignedBoards':boards(data.INVERSE_ALIGNED,.62,'target',columns=3),
    }
    (build/'cases.tex').write_text('\n'.join(
        rf'\newcommand{{\{name}}}{{%'+'\n'+body+'\n}'
        for name,body in defs.items())+'\n')
    shutil.copy2(HERE/'students.tex',build/'students.tex')
    for n in (1,2):
        run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',
             'students.tex'],cwd=build,env=env,log=build/f'compile-{n}.log')
    shutil.copy2(build/'students.pdf',out/'students.pdf')
    print(out/'students.pdf')

if __name__=='__main__':
    main()
