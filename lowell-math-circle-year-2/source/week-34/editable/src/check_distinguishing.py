"""Finite checks of the distinguishing numbers of rings with 3 to 10 spots, carried over
unchanged from the old builder (build_packets.py), which ran them after writing the LaTeX.
Writes mathematical-checks.json beside this file."""
from pathlib import Path
import itertools,json
SRC=Path(__file__).resolve().parent
def surviving(w):
 n=len(w);return [('turn',k) for k in range(1,n) if all(w[i]==w[(i+k)%n] for i in range(n))]+[('flip',k) for k in range(n) if all(w[i]==w[(k-i)%n] for i in range(n))]
checks={}
for n in range(3,11):
 c=next(q for q in [1,2,3] if any(not surviving(w) for w in itertools.product(range(q),repeat=n)))
 witness=[int(i in [0,1,3]) for i in range(n)]
 checks[n]={'minimum_kinds':c,'013_binary_asymmetric':not surviving(witness)}
assert [checks[n]['minimum_kinds'] for n in range(3,11)]==[3,3,3,2,2,2,2,2]
(SRC/'mathematical-checks.json').write_text(json.dumps(checks,indent=2))
