"""Independent checks of the targeted reference examples.

Uses geometry, ranks and counts directly, without importing packet builders,
answer files or their Hamming-distance/region/matching solution machinery.
"""
from pathlib import Path
from math import hypot
import re,json
WEEK = 25
S=Path(__file__).resolve().parent

def shadows():
 picture=((1,1),(0,0))
 rows=[sum(r) for r in picture];cols=[sum(r[j] for r in picture) for j in range(2)]
 assert rows==[2,0] and cols==[1,1]
 tex=(S/'k-1.tex').read_text().split('\\newpage')[0]
 assert '\\textbf{Problem' not in tex
 assert tex.count('circle[radius=4.6mm]')==4 # same two counters on input and output
 for x,y,n in ((178,94,2),(178,116,0),(139,133,1),(161,133,1)):
  labels={(float(a),float(b),int(v)) for a,b,v in re.findall(r'at \((\d+(?:\.\d+)?),(\d+(?:\.\d+)?)\) \{(\d)\};',tex)}
  assert (x,y,n) in labels
 assert 'dashed,->' in tex and 'dotted,->' in tex
 assert '{A}' in tex and '{B}' in tex
 return 'A1,A2 occupied -> row totals 2,0 and column totals 1,1; coordinate labels remain separate.'

result=shadows()
print(f"PASS Week {WEEK}: {result}")
