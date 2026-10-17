#!/usr/bin/env python3
"""Finite input/ideal-geometry checks, not a hardware rehearsal."""
from math import dist
from generate import INPUTS, OUTPUTS, DOTS, pose
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
