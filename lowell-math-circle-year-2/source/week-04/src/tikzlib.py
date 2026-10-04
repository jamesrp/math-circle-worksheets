"""Small TikZ helpers for the Week 4 packets. All lengths are in inches
(each tikzpicture uses x=1in, y=1in)."""
import math

A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def f(x):
    s = f"{x:.4f}".rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


def P(n, i, R, cx=0.0, cy=0.0, rot=90.0):
    """Point i of n evenly spaced points, clockwise from the top."""
    a = math.radians(rot - 360.0 * i / n)
    return cx + R * math.cos(a), cy + R * math.sin(a)


def pieces(n, k):
    seen, out = set(), []
    for s in range(n):
        if s in seen:
            continue
        cyc, j = [s], (s + k) % n
        seen.add(s)
        while j != s:
            cyc.append(j)
            seen.add(j)
            j = (j + k) % n
        out.append(cyc)
    return out


def pic(body, w, h, ox=None, oy=None):
    """Wrap tikz commands in a tikzpicture with a fixed bounding box
    [-w/2, w/2] x [oy, oy+h] (default centred)."""
    if ox is None:
        ox = -w / 2
    if oy is None:
        oy = -h / 2
    return ("\\begin{tikzpicture}[x=1in,y=1in]\n"
            f"\\useasboundingbox ({f(ox)},{f(oy)}) rectangle ({f(ox + w)},{f(oy + h)});\n"
            + "\n".join(body) + "\n\\end{tikzpicture}")


def cw_arrow(r, a0=150, a1=30, cx=0, cy=0, color='black!45', lw='2.2pt', tip='9pt'):
    x, y = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
    return (f"\\draw[{color}, line width={lw}, -{{Stealth[length={tip}, width={tip}]}}] "
            f"({f(x)},{f(y)}) arc[start angle={a0}, end angle={a1}, radius={f(r)}];")


def big_ring(n, R=2.05, dr=0.40, cx=0, cy=0, arrow=True):
    """K-1 hopping ring: counter-sized dots, black start dot at top."""
    s = [f"\\draw[black!35, line width=1pt] ({f(cx)},{f(cy)}) circle ({f(R)});"]
    for i in range(n):
        x, y = P(n, i, R, cx, cy)
        if i == 0:
            s.append(f"\\fill[black] ({f(x)},{f(y)}) circle ({f(dr)});")
        else:
            s.append(f"\\filldraw[fill=white, draw=black, line width=1.6pt] ({f(x)},{f(y)}) circle ({f(dr)});")
    if arrow:
        s.append(cw_arrow(R * 0.42, cx=cx, cy=cy, lw='3pt', tip='13pt'))
    return s


def small_ring(n, R, cx=0, cy=0, dr=0.075, start=True, arrow=True, guide=True):
    """Drawing ring: small open dots, start dot black, little arrow outside."""
    s = []
    if guide:
        s.append(f"\\draw[black!25, line width=0.6pt] ({f(cx)},{f(cy)}) circle ({f(R)});")
    for i in range(n):
        x, y = P(n, i, R, cx, cy)
        if i == 0 and start:
            s.append(f"\\fill[black] ({f(x)},{f(y)}) circle ({f(dr * 1.35)});")
        else:
            s.append(f"\\filldraw[fill=white, draw=black, line width=1.1pt] ({f(x)},{f(y)}) circle ({f(dr)});")
    if arrow:
        s.append(cw_arrow(R + 0.2, 70, 25, cx, cy, lw='1.4pt', tip='6pt'))
    return s


def dot_ring(n, R, cx=0, cy=0, dr=0.042, guide=True, numbers=False, numsize='\\scriptsize', numgap=0.17):
    """Ring for older children: small black dots, no start mark."""
    s = []
    if guide:
        s.append(f"\\draw[black!25, line width=0.5pt] ({f(cx)},{f(cy)}) circle ({f(R)});")
    for i in range(n):
        x, y = P(n, i, R, cx, cy)
        s.append(f"\\fill[black] ({f(x)},{f(y)}) circle ({f(dr)});")
        if numbers:
            lx, ly = P(n, i, R + numgap, cx, cy)
            s.append(f"\\node[font={numsize}] at ({f(lx)},{f(ly)}) {{{i}}};")
    return s


def star_lines(n, k, R, cx=0, cy=0, lw='1.4pt', color='black'):
    s = []
    for cyc in pieces(n, k):
        pts = [P(n, i, R, cx, cy) for i in cyc]
        if len(pts) == 2:
            (x0, y0), (x1, y1) = pts
            s.append(f"\\draw[{color}, line width={lw}] ({f(x0)},{f(y0)}) -- ({f(x1)},{f(y1)});")
        else:
            path = " -- ".join(f"({f(x)},{f(y)})" for x, y in pts)
            s.append(f"\\draw[{color}, line width={lw}, line join=round] {path} -- cycle;")
    return s


def box(cx, cy, w, h=None, lw='1pt'):
    h = w if h is None else h
    return f"\\draw[line width={lw}] ({f(cx - w / 2)},{f(cy - h / 2)}) rectangle ({f(cx + w / 2)},{f(cy + h / 2)});"


def hline(x0, x1, y, lw='0.6pt', color='black!60'):
    return f"\\draw[{color}, line width={lw}] ({f(x0)},{f(y)}) -- ({f(x1)},{f(y)});"


# ---------------------------------------------------------------- icons
def _poly(pts, close=True, opts='line width=1.5pt, line join=round'):
    path = " -- ".join(f"({f(x)},{f(y)})" for x, y in pts)
    return f"\\draw[{opts}] {path}" + (" -- cycle;" if close else ";")


def icon(name, cx, cy, s):
    """Icon fitting roughly in a box of side s centred at (cx, cy)."""
    u = s  # unit: icon designed in [-0.5,0.5]^2
    lw = f"{max(0.9, 1.6 * s / 0.8):.2f}pt"
    o = []
    if name == 'sun':
        o.append(f"\\draw[line width={lw}] ({f(cx)},{f(cy)}) circle ({f(0.2 * u)});")
        for j in range(8):
            a = math.radians(j * 45)
            o.append(f"\\draw[line width={lw}, line cap=round] ({f(cx + 0.28 * u * math.cos(a))},{f(cy + 0.28 * u * math.sin(a))}) -- "
                     f"({f(cx + 0.42 * u * math.cos(a))},{f(cy + 0.42 * u * math.sin(a))});")
    elif name == 'moon':
        r1, (dx, dy), r2 = 0.40, (0.20, 0.10), 0.33
        pts = []
        for j in range(181):
            a = 2 * math.pi * j / 180
            x, y = r1 * math.cos(a), r1 * math.sin(a)
            if (x - dx) ** 2 + (y - dy) ** 2 >= r2 ** 2:
                pts.append((a, x, y))
        # order the outer arc starting just after the gap
        gap = max(range(len(pts)), key=lambda i: (pts[(i + 1) % len(pts)][0] - pts[i][0]) % (2 * math.pi))
        outer = [(x, y) for _, x, y in pts[gap + 1:] + pts[:gap + 1]]
        inner = []
        for j in range(181):
            a = 2 * math.pi * j / 180
            x, y = dx + r2 * math.cos(a), dy + r2 * math.sin(a)
            if x * x + y * y <= r1 ** 2:
                inner.append((a, x, y))
        gap2 = max(range(len(inner)), key=lambda i: (inner[(i + 1) % len(inner)][0] - inner[i][0]) % (2 * math.pi))
        inner = [(x, y) for _, x, y in inner[gap2 + 1:] + inner[:gap2 + 1]]
        # outer runs counter-clockwise from one tip to the other; inner arc must run back
        e = outer[-1]
        if (inner[0][0] - e[0]) ** 2 + (inner[0][1] - e[1]) ** 2 > (inner[-1][0] - e[0]) ** 2 + (inner[-1][1] - e[1]) ** 2:
            inner = inner[::-1]
        pts = [(cx + (x - 0.04) * u, cy + y * u) for x, y in outer + inner]
        o.append(_poly(pts, opts=f'line width={lw}, line join=round'))
    elif name == 'heart':
        pts = []
        for j in range(120):
            t = 2 * math.pi * j / 120
            x = 16 * math.sin(t) ** 3
            y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
            pts.append((cx + x * 0.024 * u, cy + (y + 2.5) * 0.024 * u))
        o.append(_poly(pts, opts=f'line width={lw}, line join=round'))
    elif name == 'tree':
        o.append(_poly([(cx - 0.32 * u, cy - 0.18 * u), (cx, cy + 0.42 * u), (cx + 0.32 * u, cy - 0.18 * u)],
                       opts=f'line width={lw}, line join=round'))
        o.append(_poly([(cx - 0.07 * u, cy - 0.18 * u), (cx - 0.07 * u, cy - 0.42 * u),
                        (cx + 0.07 * u, cy - 0.42 * u), (cx + 0.07 * u, cy - 0.18 * u)], close=False,
                       opts=f'line width={lw}, line join=round'))
    elif name == 'fish':
        o.append(f"\\draw[line width={lw}] ({f(cx - 0.07 * u)},{f(cy)}) ellipse ({f(0.28 * u)} and {f(0.17 * u)});")
        o.append(_poly([(cx + 0.19 * u, cy), (cx + 0.42 * u, cy + 0.17 * u), (cx + 0.42 * u, cy - 0.17 * u)],
                       opts=f'line width={lw}, line join=round'))
        o.append(f"\\fill ({f(cx - 0.2 * u)},{f(cy + 0.04 * u)}) circle ({f(0.035 * u)});")
    elif name == 'house':
        o.append(_poly([(cx - 0.27 * u, cy + 0.06 * u), (cx - 0.27 * u, cy - 0.38 * u), (cx + 0.27 * u, cy - 0.38 * u),
                        (cx + 0.27 * u, cy + 0.06 * u)], close=False, opts=f'line width={lw}, line join=round'))
        o.append(_poly([(cx - 0.36 * u, cy + 0.04 * u), (cx, cy + 0.40 * u), (cx + 0.36 * u, cy + 0.04 * u)],
                       opts=f'line width={lw}, line join=round'))
        o.append(_poly([(cx - 0.07 * u, cy - 0.38 * u), (cx - 0.07 * u, cy - 0.12 * u), (cx + 0.07 * u, cy - 0.12 * u),
                        (cx + 0.07 * u, cy - 0.38 * u)], close=False, opts=f'line width={lw}, line join=round'))
    else:
        raise ValueError(name)
    return o


PICS = ['sun', 'moon', 'heart', 'tree', 'fish', 'house']  # clockwise from the top


def picture_ring(R=1.55, pr=0.42, cx=0, cy=0, arrow=True):
    s = [f"\\draw[black!35, line width=1pt] ({f(cx)},{f(cy)}) circle ({f(R)});"]
    for i, name in enumerate(PICS):
        x, y = P(6, i, R, cx, cy)
        s.append(f"\\filldraw[fill=white, draw=black, line width=1.4pt] ({f(x)},{f(y)}) circle ({f(pr)});")
        s += icon(name, x, y, pr * 1.45)
    if arrow:
        s.append(cw_arrow(R * 0.45, cx=cx, cy=cy, lw='3pt', tip='13pt'))
    return s


# ---------------------------------------------------------------- wheel template
def wheel(R, r_letters, tick_in, cx, cy, font, center_r=0.05):
    s = [f"\\draw[line width=1.4pt] ({f(cx)},{f(cy)}) circle ({f(R)});"]
    for i in range(26):
        a = 90 - 360 * i / 26
        x, y = cx + r_letters * math.cos(math.radians(a)), cy + r_letters * math.sin(math.radians(a))
        # underline every letter so that M and W (or P and d) cannot be read upside down
        s.append(f"\\node[font={font}, rotate={f(a - 90)}] at ({f(x)},{f(y)}) {{\\underline{{{A[i]}}}}};")
        b = math.radians(a - 180 / 26)
        s.append(f"\\draw[line width=0.6pt] ({f(cx + tick_in * math.cos(b))},{f(cy + tick_in * math.sin(b))}) -- "
                 f"({f(cx + R * math.cos(b))},{f(cy + R * math.sin(b))});")
    s.append(f"\\fill ({f(cx)},{f(cy)}) circle ({f(center_r)});")
    s.append(f"\\draw[line width=0.6pt] ({f(cx - 0.18)},{f(cy)}) -- ({f(cx + 0.18)},{f(cy)}) "
             f"({f(cx)},{f(cy - 0.18)}) -- ({f(cx)},{f(cy + 0.18)});")
    return s


def wheel_page(which, textwidth=7.3, height=8.9):
    """One cut-out wheel centred on its own page: 'outer' (5.5 in) or 'inner' (4 in)."""
    if which == 'outer':
        body = wheel(2.75, 2.43, 2.08, textwidth / 2, height / 2, '\\bfseries\\LARGE')
    else:
        body = wheel(2.0, 1.70, 1.42, textwidth / 2, height / 2, '\\bfseries\\Large')
    return pic(body, textwidth, height, ox=0, oy=0)
