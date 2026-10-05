"""Read the pentagon flip map drawn on guide page 6 out of the PDF and compare
it with the flip graph of the pentagon computed in tri.py.
Writes check_guide_map.out next to this script.
"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdfgeom as PG
from tri import *

OUT = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    OUT.append(s)


pg = PG.load(os.path.join(PG.WEEK, 'week-14-facilitator.pdf'))[5]
circles, lines = [], []
for p in pg['paths']:
    for pts, closed, curved in p['subpaths']:
        if curved and closed:
            xs = [q[0] for q in pts]; ys = [q[1] for q in pts]
            circles.append((((max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2), (max(xs) - min(xs)) / 2))
        elif len(pts) == 2 and not curved and p['op'] == 'S':
            lines.append(pts)
# a node label is an "F" word followed by a subscript letter, inside a circle
ws = pg['words']
labels = {}
for c, r in circles:
    inside = [w for w in ws if math.dist(((w[1] + w[3]) / 2, (w[2] + w[4]) / 2), c) < r]
    sub = [w[0] for w in inside if w[0] != 'F']
    labels[c] = 'F' + ''.join(sub)
log('nodes:', sorted(labels.values()))
edges = set()
for a, b in lines:
    # each end lies on (just outside) one circle boundary
    ea = min(circles, key=lambda cr: abs(math.dist(a, cr[0]) - cr[1]))
    eb = min(circles, key=lambda cr: abs(math.dist(b, cr[0]) - cr[1]))
    edges.add(frozenset((labels[ea[0]], labels[eb[0]])))
log('drawn joins:', sorted('-'.join(sorted(e)) for e in edges))
G5 = graph(5, by_root(5))
nm = {fan(5, v): 'F' + LET[v] for v in range(5)}
true = {frozenset((nm[t], nm[s])) for t in G5 for s in G5[t]}
log('flip graph :', sorted('-'.join(sorted(e)) for e in true))
log('drawn map matches the pentagon flip graph:', edges == true)
open(os.path.join(HERE, 'check_guide_map.out'), 'w').write('\n'.join(OUT) + '\n')
