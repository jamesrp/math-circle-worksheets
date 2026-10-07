#!/usr/bin/env python3
"""Rebuild both owned PDFs, without repository or network inputs."""
import argparse,json,shutil,subprocess,tempfile
from pathlib import Path
BASE=Path(__file__).resolve().parent

def run(command,cwd):
    result=subprocess.run(command,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if result.returncode:
        print(result.stdout)
        raise SystemExit(result.returncode)
    return result.stdout

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',default='output')
    p.add_argument('--verify-only',action='store_true')
    a=p.parse_args();out=Path(a.out).resolve()
    manifest=json.loads((BASE/'build-manifest.json').read_text())
    with tempfile.TemporaryDirectory(prefix=f"week-{manifest['week']}-source-build-") as tmp:
        work=Path(tmp)
        for name in ['student','guide','checks']:
            if (BASE/name).is_dir():shutil.copytree(BASE/name,work/name)
        for check in manifest['checks']:
            print(run(['python3',check['script'],*check.get('args',[])],work).strip())
        if a.verify_only:return
        if not shutil.which('pdflatex'):
            raise SystemExit('Install TeX Live or MacTeX with pdfLaTeX, TikZ and the listed fonts/packages.')
        out.mkdir(parents=True,exist_ok=True)
        for document in manifest['documents']:
            built=work/(document['kind']+'-output')
            print(run(['python3','build.py','--out',str(built)],work/document['source_directory']).strip())
            source=built/document['built_name']
            if not source.is_file():raise SystemExit(f'Builder did not produce {source.name}')
            shutil.copy2(source,out/document['output_file'])
    print('Portable build passed. Physical rehearsal and classroom piloting remain unperformed.')
if __name__=='__main__':main()
