#!/usr/bin/env python3
from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parent
checks=[]
for sub in ['src','facilitator-src']:
 for pattern in ['check*.py','verify*.py']:
  checks.extend(sorted((ROOT/sub).glob(pattern)))
if not checks:raise RuntimeError('No mathematical verification script found.')
for script in dict.fromkeys(checks):subprocess.run([sys.executable,str(script)],cwd=script.parent,check=True)
print('PASS: all included mathematical verification scripts completed.')
