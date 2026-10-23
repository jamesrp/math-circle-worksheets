#!/usr/bin/env python3
"""Independent Week 88 mathematical checks; Python standard library only.
Run from any directory: python3 /path/to/check_math.py.
No worksheet, author data, external package or working-directory dependency.
Floating checks have >9 degree exclusion margins; proofs are in guide/facilitator.tex.
"""
import itertools
import json
import math

EPS = 1e-8
TAU = 2 * math.pi


def angle(R, r, s):
    """Minimum angle between outer centers, by the cosine rule."""
    a, b, c = R + r, R + s, r + s
    return math.acos((a*a + b*b - c*c) / (2*a*b))


def coords(R, radii):
    gaps = [angle(R, r, radii[(i+1) % len(radii)])
            for i, r in enumerate(radii)]
    slack = (TAU - sum(gaps)) / len(gaps)
    assert slack >= -EPS
    theta = 0.0
    points = []
    for r, gap in zip(radii, gaps):
        points.append(((R+r)*math.cos(theta), (R+r)*math.sin(theta), r))
        theta += gap + slack
    assert abs(theta-TAU) < EPS
    for x,y,r in points:
        assert abs(math.hypot(x,y)-(R+r)) < EPS
    for (x,y,r), (u,v,s) in itertools.combinations(points, 2):
        assert math.hypot(x-u,y-v) >= r+s-EPS
    return points


def uniform(R, r, n):
    alpha = angle(R,r,r)
    assert n*alpha <= TAU+EPS
    assert (n+1)*alpha > TAU+EPS
    # Formula independently checked with a small roundoff tolerance at integers.
    assert math.floor(math.pi/math.asin(r/(R+r))+1e-12) == n
    points = coords(R, [r]*n)
    return {'maximum':n, 'minimum_angle_degrees':math.degrees(alpha),
            'next_count_degrees':math.degrees((n+1)*alpha),
            'witness_centers_and_radii_mm':points}


def mixed(R, n):
    # Enumerate EVERY binary cyclic word with n+1 disks and both sizes.
    # Nonexistence for n+1 rules out larger rings: delete disks while keeping
    # one of each size. A valid larger ring would yield a valid forbidden ring.
    sums=[]
    words=0
    for radii in itertools.product((20,40), repeat=n+1):
        if len(set(radii)) != 2:
            continue
        words+=1
        a=sum(angle(R,r,radii[(i+1) % len(radii)])
              for i,r in enumerate(radii))
        assert a>TAU+EPS, radii
        sums.append(a)
    radii=[40]+[20]*(n-1)
    points=coords(R,radii)  # all pairs, not merely neighbors, checked
    # A centered 260 x 260 mm mat suffices, including disk edges.
    for x,y,r in points:
        assert abs(x)+r <= 130+EPS and abs(y)+r <= 130+EPS
    return {'maximum':n,'excluded_count':n+1,'words_checked':words,
            'minimum_forbidden_angle_sum_degrees':math.degrees(min(sums)),
            'witness_centers_and_radii_mm':points}


def fixed_witness(R, small_angles):
    """Reserved-plan coordinates printed in the adult guide."""
    polar = [(40, 0)] + [(20, a) for a in small_angles]
    points = [((R+r)*math.cos(math.radians(a)),
               (R+r)*math.sin(math.radians(a)), r) for r,a in polar]
    for x,y,r in points:
        assert abs(math.hypot(x,y)-(R+r)) < EPS
        assert abs(x)+r <= 130+EPS and abs(y)+r <= 130+EPS
    for (x,y,r), (u,v,s) in itertools.combinations(points,2):
        assert math.hypot(x-u,y-v) >= r+s-EPS
    return {'middle_radius_mm':R, 'outer_radius_angle_degrees':polar,
            'witness_centers_and_radii_mm':points}


def rows():
    gap=math.sqrt(40**2-20**2)
    h=40+2*gap
    points=[(x,20) for x in (20,60,100,140)]
    points += [(x,20+gap) for x in (40,80,120)]
    points += [(x,20+2*gap) for x in (20,60,100,140)]
    assert len(points)==11
    for (x,y),(u,v) in itertools.combinations(points,2):
        assert math.hypot(x-u,y-v)>=40-EPS
    for H in (112,110,h):
        for x,y in points:
            assert 20-EPS<=x<=160-20+EPS
            assert 20-EPS<=y<=H-20+EPS
    assert h>108
    # Width 160 forces a horizontal four-disk row to x=20,60,100,140.
    # Every possible middle x in [20,140] is within 20 of such a center.
    # Each interrow gap >= sqrt(40^2-20^2), yielding this lower bound.
    return {'row_constrained_minimum_height_mm':h,
            'exact_height':'40 + 40*sqrt(3) mm',
            '110_mm_spare':110-h,'108_mm_shortfall':h-108,
            'centers_mm':points,
            'unrestricted_112_mm_tray':'11 demonstrated; global optimum not asserted'}


def main():
    result={
      'equal':uniform(20,20,6),
      'large_middle_small_outer':uniform(40,20,9),
      'small_middle_large_outer':uniform(20,40,4),
      'large_middle_mixed':mixed(40,8),
      'small_middle_mixed':mixed(20,5),
      'rows':rows(),
      'fixed_large_middle_mixed':fixed_witness(40,[50,90,130,170,210,250,290]),
      'fixed_small_middle_mixed':fixed_witness(20,[80,140,200,260]),
      'worked_example':{'radii_mm':[15,25],'center_distance_mm':15+25},
    }
    # Six equal gaps sum to 360 degrees, so all attain 60 degrees.
    assert abs(6*angle(20,20,20)-TAU)<EPS
    print(json.dumps(result, indent=2))

if __name__=='__main__':
    main()
