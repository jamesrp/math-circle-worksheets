#!/usr/bin/env python3
"""Build all five PDFs (three packets, the K-1 square sheet and the guide) using installed TeX packages and included fonts."""
from pathlib import Path
import os,subprocess,sys
ROOT=Path(__file__).resolve().parent
env=os.environ.copy()
# A regular TeX installation already has this standard format. Some read-only
# containers ship the sources without a usable filename database or format.
fmt=subprocess.run(['kpsewhich','pdflatex.fmt'],capture_output=True,text=True,env=env)
if not fmt.stdout.strip():
 state=ROOT/'build-state';state.mkdir(exist_ok=True)
 dist=subprocess.run(['kpsewhich','--var-value=TEXMFDIST'],capture_output=True,text=True,check=True).stdout.strip()
 if not dist or not Path(dist).is_dir():raise RuntimeError('Install a complete TeX Live distribution with pdfLaTeX and TikZ.')
 # Omit the database-only (!!) modifier, allowing normal package discovery.
 env['TEXMF']=dist
 env['TEXMFVAR']=str(state/'texmf-var');env['TEXMFCONFIG']=str(state/'texmf-config')
 env['VARTEXFONTS']=str(state/'fonts');env['TEXFORMATS']=str(state)+os.pathsep
 for k in ['TEXMFVAR','TEXMFCONFIG','VARTEXFONTS']:Path(env[k]).mkdir(parents=True,exist_ok=True)
 with (state/'format-build.log').open('w') as f:
  subprocess.run(['pdflatex','-ini','-etex','-jobname=pdflatex','-interaction=nonstopmode','-halt-on-error','pdflatex.ini'],cwd=state,env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
# The student pages are problem files; student-src/build.sh writes their LaTeX (regenerate.py) and compiles it.
subprocess.run(['bash','build.sh'],cwd=ROOT/'student-src',env=env,check=True)
# The K-1 square sheet (card fix 5, October 23, 2026): build it, then measure it against the K-1 boards.
subprocess.run([sys.executable,str(ROOT/'materials/build_materials.py')],cwd=ROOT,env=env,check=True)
subprocess.run([sys.executable,str(ROOT/'materials/verify_materials.py'),str(ROOT/'materials.pdf'),str(ROOT/'k-1.pdf')],cwd=ROOT,env=env,check=True)
subprocess.run([sys.executable,'build.py'],cwd=ROOT/'facilitator-src',env=env,check=True)

subprocess.run([sys.executable, str(ROOT/'facilitator-src/add_route_note.py')], cwd=ROOT, env=env, check=True)
