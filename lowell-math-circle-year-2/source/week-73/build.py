#!/usr/bin/env python3
"""Build both PDFs from this portable authored-source package."""
import argparse,json,shutil,subprocess,tempfile
from pathlib import Path
BASE=Path(__file__).resolve().parent

def run(args,cwd):
    p=subprocess.run(args,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if p.returncode:
        print(p.stdout)
        raise SystemExit(p.returncode)
    return p.stdout

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',default='output')
    parser.add_argument('--verify-only',action='store_true')
    a=parser.parse_args()
    out=Path(a.out).resolve()
    data=json.loads((BASE/'build-manifest.json').read_text())
    with tempfile.TemporaryDirectory(prefix=f"week{data['week']}-build-") as temporary:
        work=Path(temporary)
        for directory in ['student','guide','checks']:
            if (BASE/directory).exists(): shutil.copytree(BASE/directory,work/directory)
        for check in data.get('checks',[]):
            script=work/check
            print(run(['python3',script.name],script.parent).strip())
        if a.verify_only: return
        if not shutil.which('pdflatex'): raise SystemExit('Install TeX Live or MacTeX with pdfLaTeX and TikZ.')
        out.mkdir(parents=True,exist_ok=True)
        for document in data['documents']:
            source=work/document['source_directory']
            build_out=work/(document['kind']+'-output')
            print(run(['python3','build.py','--out',str(build_out)],source).strip())
            built=build_out/document['built_name']
            if not built.is_file(): raise SystemExit(f'Builder did not produce {built}')
            shutil.copy2(built,out/document['output_file'])
    print('Portable build complete. Physical rehearsal and classroom piloting are unperformed.')
if __name__=='__main__': main()
