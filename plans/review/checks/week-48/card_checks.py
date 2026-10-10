# Card-stage spot checks for Week 48 (exact rational clipping).
from fractions import Fraction as F

def clip(poly, x0, x1, y0, y1):
    def clip_edge(pts, inside, inter):
        out = []
        n = len(pts)
        for i in range(n):
            p, q = pts[i], pts[(i+1) % n]
            ip, iq = inside(p), inside(q)
            if ip:
                out.append(p)
            if ip != iq:
                out.append(inter(p, q))
        return out
    def ix(x):
        return lambda p, q: (x, p[1] + (q[1]-p[1])*(x-p[0])/(q[0]-p[0]))
    def iy(y):
        return lambda p, q: (p[0] + (q[0]-p[0])*(y-p[1])/(q[1]-p[1]), y)
    pts = poly
    for inside, inter in [(lambda p: p[0] >= x0, ix(x0)), (lambda p: p[0] <= x1, ix(x1)),
                          (lambda p: p[1] >= y0, iy(y0)), (lambda p: p[1] <= y1, iy(y1))]:
        if not pts: return []
        pts = clip_edge(pts, inside, inter)
    return pts

def area(pts):
    if len(pts) < 3: return F(0)
    s = 0
    for i in range(len(pts)):
        (a, b), (c, d) = pts[i], pts[(i+1) % len(pts)]
        s += a*d - b*c
    return abs(F(s)) / 2

def bounds(poly, n, size=4):
    h = F(size, n)
    whole = part = 0
    for i in range(n):
        for j in range(n):
            a = area(clip(poly, i*h, (i+1)*h, j*h, (j+1)*h))
            if a == h*h: whole += 1
            elif a > 0: part += 1
    return whole, whole + part, whole*h*h, (whole+part)*h*h

trap = [(F(1,2),F(1,2)), (F(7,2),F(1,2)), (F(3),F(7,2)), (F(1),F(7,2))]
tri = [(F(0),F(4)), (F(4),F(4)), (F(4),F(0))]
dia = [(F(0),F(2)), (F(2),F(0)), (F(4),F(2)), (F(2),F(4))]
for name, p in [('triangle', tri), ('diamond', dia), ('trapezoid', trap)]:
    print(name, 'exact area', area(p))
    for n in (4, 8):
        w, c, lo, hi = bounds(p, n)
        print(f'  {n}x{n}: whole {w}, cover {c}, bounds {lo} to {hi}, gap {hi-lo}')

# A split that gains nothing can open children that do (app lookahead claim):
# a diamond of radius 3/10 centred in one unit cell.
c, r = F(1,2), F(3,10)
small = [(c-r, c), (c, c-r), (c+r, c), (c, c+r)]
for n in (1, 2, 4):
    w, cov, lo, hi = bounds(small, n, size=1)
    print(f'small diamond in one cell, {n}x{n}: whole {w}, cover {cov}, bounds {lo} to {hi}, gap {hi-lo}')
