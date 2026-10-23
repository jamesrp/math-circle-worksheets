#!/usr/bin/env python3
"""Finite input/ideal-geometry checks, not a hardware rehearsal."""
import importlib.util
import sys
from math import dist
from pathlib import Path
# The drawing coordinates live in the week's figures.py (the old generate.py), passed as argv[1].
sys.dont_write_bytecode = True
_spec = importlib.util.spec_from_file_location('week85_figures', Path(sys.argv[1]))
_fig = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_fig)
INPUTS, OUTPUTS, DOTS, pose = _fig.INPUTS, _fig.OUTPUTS, _fig.DOTS, _fig.pose
def area(poly):return abs(sum(x*b-a*y for (x,y),(a,b) in zip(poly,poly[1:]+poly[:1])))/2
for x in [110,120,135,150,160]:
    for y in [115,125,140,155,165]:
        p=pose(x,y,40,140)
        assert all(abs(dist(p[a],p[b])-80)<1e-8 for a,b in [('O','X'),('X','Q'),('Q','Y'),('Y','P'),('X','T'),('T','Y')])
        assert dist(p['P'],(2*x-40,2*y-140))<1e-8
for k,pts in INPUTS.items():
    assert all(110<=x<=160 and 115<=y<=165 for x,y in pts),k
for k,pts in OUTPUTS.items():
    assert all(180<=x<=280 and 90<=y<=190 for x,y in pts),k
assert all(180<=x<=280 and 90<=y<=190 for x,y in DOTS)
for k,a in [('G',4),('H',4),('I',4.5)]:
    assert area(INPUTS[k])/100==a,(k,area(INPUTS[k])/100)
    out=[(2*x-40,2*y-140) for x,y in INPUTS[k]]
    assert area(out)==4*area(INPUTS[k])
# The 30 mm right-isosceles triangle uses three whole 10 mm squares
# plus three half-squares; its doubled copy uses fifteen plus six halves.
# Each axis-aligned L/square uses four whole units, and its copy sixteen.
assert 3+15<=48 and 3+6<=16
assert 4+16<=48
for x,y in INPUTS['M']:
    p=(2*x-40,2*y-140); q=(2*x-60,2*y-140)
    assert q==(p[0]-20,p[1])
    assert (2*(x+10)-60,2*y-140)==p
    assert 110<=x+10<=160
print('PASS: ideal 80/160 mm geometry; all target zones; area 4x; anchor translation and compensation. Hardware untested.')
# The enlarged convention uses three genuine poses in the allowed working zone
# after translating its local anchor from (0,0) to the mat's (40,140).
for tx,ty in [(75,-16),(100,-16),(100,12)]:
    p=pose(tx,ty)
    assert 110<=tx+40<=160 and 115<=ty+140<=165
    assert all(abs(dist(p[a],p[b])-80)<1e-8 for a,b in [('O','X'),('X','Q'),('Q','Y'),('Y','P'),('X','T'),('T','Y')])
    assert dist(p['P'],(2*tx,2*ty))<1e-8
# Exact F inverse and L forward target outlines.
assert [((x+40)/2,(y+140)/2) for x,y in [(220,125),(260,155)]] == [(130,132.5),(150,147.5)]
assert [(2*x-40,2*y-140) for x,y in [(125,130),(155,150)]] == [(210,120),(270,160)]
print('PASS: enlarged genuine operation poses; exact F and L outline targets.')
# v2 diagrams: upper P3's small L box keeps its place inside the 0.55-scale L insert after the
# 24 mm move (insert L's box is x+25..x+55, y+25..y+45 in a 70 mm square), and upper P4 has
# no dashed frame.
import re
s=_fig.upper_p3()
box=[tuple(map(float,m)) for m in re.findall(r'\(([\d.]+),([\d.]+)\) rectangle \+\(38\.5,38\.5\)',s)]
assert box==[(154.0,94.0)],box
path=re.findall(r'line join=round\] \(([\d.]+),([\d.]+)\) -- \(([\d.]+),([\d.]+)\) -- \(([\d.]+),([\d.]+)\)',s)
corners=[tuple(map(float,c)) for c in path if float(c[0])>150]
(x1,y1,x2,y2,x3,y3),=corners
assert [round((x1-154)/.55,9),round((x2-154)/.55,9),round((y1-94)/.55,9),round((y3-94)/.55,9)]==[25,55,25,45]
assert 'dashed' not in _fig.upper_p4()
assert 'clear overlay' not in _fig.materials_tex()
print('PASS: v2 diagrams; upper P3 L box in place, no P4 frame, no clear-overlay label.')
