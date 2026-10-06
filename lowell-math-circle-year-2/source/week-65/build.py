#!/usr/bin/env python3
"""Rebuild the Week65 release in isolation using only this extracted package."""
import argparse,json,shutil,subprocess,tempfile
from pathlib import Path
BASE=Path(__file__).resolve().parent

def run(cmd,cwd):
 result=subprocess.run(cmd,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 if result.returncode:
  print(result.stdout);raise SystemExit(result.returncode)
 return result.stdout

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',default='output');ap.add_argument('--verify-only',action='store_true');a=ap.parse_args()
 dest=Path(a.out).resolve()
 if not a.verify_only and not shutil.which('pdflatex'):raise SystemExit('Install TeX Live or MacTeX with pdfLaTeX, TikZ, amssymb, geometry, enumitem, fancyhdr, hyperref and Helvetica, then rerun.')
 manifest=json.loads((BASE/'build-manifest.json').read_text())
 with tempfile.TemporaryDirectory(prefix='week65-release-') as temp:
  work=Path(temp)
  for directory in ['student','guide']:shutil.copytree(BASE/directory,work/directory)
  for script in ['verify_geometry.py','verify_routes.py']:
   print(run(['python3',script],work/'guide'))
  if a.verify_only:
   print(run(['python3','build.py','--verify-only'],work/'student'));print(run(['python3','independent_check.py'],work/'student'));return
  dest.mkdir(parents=True,exist_ok=True)
  for document in manifest['documents']:
   out=dest/document['output_file']
   print(run(['python3','build.py','--output',str(out)],work/document['source_directory']).strip())
   if document['kind']=='student':print(run(['python3','independent_check.py'],work/'student'))
 print('Both PDFs rebuilt from the portable source package. Physical rehearsal and classroom piloting remain unperformed.')
if __name__=='__main__':main()
