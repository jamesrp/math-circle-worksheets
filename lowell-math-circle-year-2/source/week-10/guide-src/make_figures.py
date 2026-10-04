"""Small answer pictures of the K-1 towns and drawings, for the parent's answer key.

Every mark is computed here from the student pages (parse_pages.py + euler.py):
filled islands = islands where a walk that picks up every counter can start;
thick black bridges = bridges that work in Problem 8; dashed = one new bridge that works (Problem 6)."""

import math
import os

from parse_pages import load
from euler import start_end, has_walk, degrees
from pictures_graph import analyse

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, 'figs')
SC = 0.21           # cm on the guide per cm on the student page


def fmt(p, x0, y0, sc=SC):
    return f"({(p[0] - x0) * sc:.3f},{(p[1] - y0) * sc:.3f})"


def town_tikz(t, fill=(), bold=(), dashed=(), sc=SC):
    x0, y0, x1, y1 = t.bbox()
    out = [r"\begin{tikzpicture}"]
    for i, b in enumerate(t.br):
        pts = b['pts'] if len(b['pts']) == 2 else b['pts'][::6] + [b['pts'][-1]]
        style = 'thbold' if i in bold else 'thband'
        out.append(f"\\draw[{style}] " + " -- ".join(fmt(p, x0, y0, sc) for p in pts) + ";")
    for (u, v, h) in dashed:
        a, c = t.isl[u]['c'], t.isl[v]['c']
        if h == 0:
            out.append(f"\\draw[thnew] {fmt(a, x0, y0, sc)} -- {fmt(c, x0, y0, sc)};")
        else:
            dx, dy = c[0] - a[0], c[1] - a[1]
            L = math.hypot(dx, dy)
            nx, ny = -dy / L * h, dx / L * h
            p1 = (a[0] + dx / 3 + nx, a[1] + dy / 3 + ny)
            p2 = (a[0] + 2 * dx / 3 + nx, a[1] + 2 * dy / 3 + ny)
            out.append(f"\\draw[thnew] {fmt(a, x0, y0, sc)} .. controls {fmt(p1, x0, y0, sc)} and "
                       f"{fmt(p2, x0, y0, sc)} .. {fmt(c, x0, y0, sc)};")
    for i, d in enumerate(t.isl):
        style = 'thfill' if i in fill else 'thisland'
        out.append(f"\\draw[{style}] {fmt(d['c'], x0, y0, sc)} circle ({d['r'] * sc:.3f});")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def picture_tikz(p, crossed, dots, size=1.5):
    x0, y0, x1, y1 = p.bbox()
    sc = size / max(x1 - x0, y1 - y0)
    out = [r"\begin{tikzpicture}"]
    st = 'thstroke, draw=black!35' if crossed else 'thstroke'
    for a, b in p.segs:
        out.append(f"\\draw[{st}] {fmt(a, x0, y0, sc)} -- {fmt(b, x0, y0, sc)};")
    for c, r in p.circles:
        out.append(f"\\draw[{st}] {fmt(c, x0, y0, sc)} circle ({r * sc:.3f});")
    for q in dots:
        out.append(f"\\fill {fmt(q, x0, y0, sc)} circle (0.07);")
    if crossed:
        # a bold X beside the picture (a cross drawn over it would look like the envelope's own lines)
        w, h = (x1 - x0) * sc, (y1 - y0) * sc
        out.append(f"\\node[anchor=north west, font=\\LARGE\\bfseries, inner sep=0pt] at ({w + 0.12:.3f},{h:.3f}) {{X}};")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def cell(pic, caption, width):
    """A picture with its caption underneath, the caption wrapped to at least 2.9 cm."""
    w = max(width + 0.1, 2.9)
    return (r"\begin{tabular}[b]{@{}c@{}}" + pic + r"\\[1pt]\parbox[t]{%.2fcm}{\centering\footnotesize " % w
            + caption + r"}\end{tabular}")


def row(cells, name):
    with open(os.path.join(FIG, name), 'w') as f:
        f.write("\\par\\smallskip\\noindent\\hfill" + "\\hfill\n".join(cells) + "\\hfill\\null\\par\\smallskip\n")


def tw(t):
    x0, y0, x1, y1 = t.bbox()
    return (x1 - x0) * SC


def pick(t, where):
    """Index of the island at a corner of the town: where in {'bl','br','tl','tr','b','t'}."""
    xs = [d['c'][0] for d in t.isl]
    ys = [d['c'][1] for d in t.isl]
    def score(i):
        x, y = t.isl[i]['c']
        sx = {'l': -x, 'r': x}.get(where[1:] or 'c', -abs(x - (min(xs) + max(xs)) / 2))
        sy = {'b': -y, 't': y}[where[0]]
        return sy * 10 + sx
    return max(range(t.n), key=score)


def main():
    os.makedirs(FIG, exist_ok=True)
    K = {pr['num']: pr for pr in load('k-1')}

    def starts(t):
        return set(start_end(t.n, t.edges()))

    def closed(t):
        return any(s in e for s, e in start_end(t.n, t.edges()).items())

    # P1, P2: filled = possible starts
    caps = ['start anywhere', 'start anywhere', 'start on a filled island', 'start on a filled island']
    row([cell(town_tikz(t, starts(t)), c, tw(t)) for t, c in zip(K[1]['towns'], caps)], 'k1-p1.tex')
    caps = ['only the 2 filled islands', 'every island']
    row([cell(town_tikz(t, starts(t)), c, tw(t)) for t, c in zip(K[2]['towns'], caps)], 'k1-p2.tex')
    # P3: check or X
    cells = []
    for t in K[3]['towns']:
        s = starts(t)
        cells.append(cell(town_tikz(t, s), (r'\checkmark\ start on a filled island' if s else r'\textbf{X}')
                          if len(s) < t.n else r'\checkmark\ any island', tw(t)))
    row(cells, 'k1-p3.tex')
    # P4: closed walk
    cells = []
    for t in K[4]['towns']:
        s = starts(t)
        cells.append(cell(town_tikz(t, s), r'\checkmark' if closed(t) else r'\textbf{X} (ends elsewhere)', tw(t)))
    row(cells, 'k1-p4.tex')
    # P5: pictures, one of each pair
    cells = []
    for p in K[5]['pictures'][::2]:
        a = analyse(p)
        crossed = a['strokes'] > 1
        dots = a['odd_pts'] if a['odd'] == 2 else []
        cap = r'\textbf{cross out}' if crossed else ('start at a dot' if dots else 'start anywhere')
        cells.append(cell(picture_tikz(p, crossed, dots, size=1.7), cap, 1.7))
    row(cells, 'k1-p5.tex')
    # P6: filled = odd islands; dashed = one new bridge that works (checked)
    t1, t2, t3 = K[6]['towns']
    examples = [(t1, (pick(t1, 'bl'), pick(t1, 'br'), 0)),
                (t2, (pick(t2, 'tl'), pick(t2, 'tr'), 2.2)),
                (t3, (pick(t3, 'tl'), pick(t3, 'tr'), 0))]
    cells = []
    for t, (u, v, h) in examples:
        d = degrees(t.n, t.edges())
        odd = {i for i in range(t.n) if d[i] % 2}
        assert u in odd and v in odd and has_walk(t.n, t.edges() + [(u, v)]), 'P6 example must work'
        cells.append(cell(town_tikz(t, odd, dashed=[(u, v, h)]), r'join two filled islands', tw(t)))
    row(cells, 'k1-p6.tex')
    # P8: bold = bridges that work when doubled
    cells = []
    for t in K[8]['towns']:
        E = t.edges()
        good = {i for i in range(len(E)) if has_walk(t.n, E + [E[i]])}
        cap = 'all 6 bridges' if len(good) == len(E) else f'only the {len(good)} thick bridges'
        cells.append(cell(town_tikz(t, bold=good), cap, tw(t)))
    row(cells, 'k1-p8.tex')
    print('figures written to', FIG)


if __name__ == '__main__':
    main()
