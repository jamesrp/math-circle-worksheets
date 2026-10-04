#!/usr/bin/env python3
"""Standalone TeX build; no repository, network or absolute project paths required."""
import argparse,json,shutil,subprocess,tempfile
from pathlib import Path

BASE=Path(__file__).resolve().parent

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',default='output');a=ap.parse_args()
 dest=Path(a.out).resolve();dest.mkdir(parents=True,exist_ok=True)
 manifest=json.loads((BASE/'build-manifest.json').read_text())
 if not shutil.which('pdflatex'):raise SystemExit('Install TeX Live or MacTeX with TikZ, then rerun this command.')
 with tempfile.TemporaryDirectory(prefix='math-circle-rebuild-') as task_dir:
  for item in manifest['documents']:
   src=BASE/item['source_directory'];work=Path(task_dir)/item['kind'];shutil.copytree(src,work)
   tex=Path(item['tex_file'])
   if item.get('build_command'):
    r=subprocess.run(item['build_command'],cwd=work,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    if r.returncode:
     print(r.stdout);raise SystemExit(f'Authored build failed: {src}')
    shutil.copy2(work/item['built_pdf'],dest/item['output_file'])
    print(dest/item['output_file']);continue
   for _ in range(2):
    r=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error',str(tex)],cwd=work,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    if r.returncode:
     print(r.stdout);raise SystemExit(f'Build failed: {tex}')
   pdf=work/tex.with_suffix('.pdf');shutil.copy2(pdf,dest/item['output_file'])
   print(dest/item['output_file'])

if __name__=='__main__':main()
