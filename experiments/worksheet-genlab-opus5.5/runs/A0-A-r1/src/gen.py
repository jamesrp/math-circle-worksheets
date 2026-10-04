"""Generate TikZ figure files (src/fig/*.tex) for the three worksheets.

All pictures use x=1in, y=1in, so a scale factor s=1 means ACTUAL SIZE:
the small triangle's edge is exactly 1 inch.
"""
import os
from geom import *

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, 'fig')
os.makedirs(FIG, exist_ok=True)

TYPE_FILL = {'L': 'tyL', 'R': 'tyR', 'S': 'tyS'}


def env(body, opts=''):
    o = 'x=1in,y=1in,line cap=round,line join=round,sharp corners'
    if opts:
        o += ',' + opts
    return '\\begin{tikzpicture}[' + o + ']\n' + body + '\\end{tikzpicture}%\n'


def write(name, body, opts=''):
    with open(os.path.join(FIG, name + '.tex'), 'w') as f:
        f.write(env(body, opts))


def shift_of(reg, s):
    """Offset so that the region's bounding box starts at (0,0)."""
    x0, y0, _, _ = bbox(reg)
    return (-x0 * s, -y0 * s)


def board(reg, s=1.0, fill='white', grid='gridline', outline='boardline', holes=(), off=None,
          dots_up=False):
    """TikZ commands for a board: fill, interior grid lines, black holes, thick outline."""
    if off is None:
        off = shift_of(set(reg) | set(holes), s)
    cmds = []
    full = set(reg) | set(holes)
    # fill each triangle (robust for any shape)
    if fill:
        for t in sorted(full):
            cmds.append(f"\\fill[{fill}] {poly_path(tri_verts(t), s, off)};")
    for t in sorted(holes):
        cmds.append(f"\\fill[holefill] {poly_path(tri_verts(t), s, off)};")
    if grid:
        inner, _ = edge_census(full)
        for p, q in sorted(inner):
            cmds.append(f"\\draw[{grid}] {P(p, s, off)} -- {P(q, s, off)};")
    if dots_up:
        for t in sorted(reg):
            if t[0] == 'U':
                cx, cy = centroid(t)
                cmds.append(f"\\fill[black!55] ({fmt(cx * s + off[0])},{fmt(cy * s + off[1])}) circle (0.05);")
    if outline:
        for loop in boundary_loops(full):
            cmds.append(f"\\draw[{outline}] {poly_path(simplify_loop(loop), s, off)};")
        for t in sorted(holes):
            cmds.append(f"\\draw[{outline}] {poly_path(tri_verts(t), s, off)};")
    return '\n'.join(cmds) + '\n'


def tiling_cmds(reg, tiling, s=1.0, off=None, fills=None, edge='tileedge', highlight=None,
                hl_style='hlfill', outline='tileoutline', extra_fill=None):
    """Draw a rhombus tiling. fills: dict type->color or None.  highlight: set of (u,d) pairs."""
    if off is None:
        off = shift_of(reg, s)
    cmds = []
    for u, d in sorted(tiling):
        typ = rhombus_type(u, d)
        pts = rhombus_pts(u, d)
        f = None
        if extra_fill and (u, d) in extra_fill:
            f = extra_fill[(u, d)]
        elif highlight and (u, d) in highlight:
            f = hl_style
        elif fills:
            f = fills.get(typ)
        if f:
            cmds.append(f"\\fill[{f}] {poly_path(pts, s, off)};")
    for u, d in sorted(tiling):
        cmds.append(f"\\draw[{edge}] {poly_path(rhombus_pts(u, d), s, off)};")
    if outline:
        for loop in boundary_loops(reg):
            cmds.append(f"\\draw[{outline}] {poly_path(simplify_loop(loop), s, off)};")
    return '\n'.join(cmds) + '\n'


def piece_cmds(tris, color, s, off, inner=False, lw='piece'):
    reg = set(tris)
    cmds = []
    for loop in boundary_loops(reg):
        cmds.append(f"\\filldraw[{lw}, fill={color}, draw={color}!60!black] {poly_path(simplify_loop(loop), s, off)};")
    if inner:
        ie, _ = edge_census(reg)
        for p, q in ie:
            cmds.append(f"\\draw[{color}!60!black, densely dotted, line width=0.6pt] {P(p, s, off)} -- {P(q, s, off)};")
    return '\n'.join(cmds) + '\n'


# ---------- standard pieces as triangle sets ----------
GREEN = {('U', 0, 0)}
BLUE = {('U', 0, 0), ('D', 0, 0)}
RED = {('U', 0, 0), ('D', 0, 0), ('U', 1, 0)}
YELLOW = region([hexagon(1, 1, 1)])
# purple chevron: two blues meeting at a 240-degree corner ("<" zig-zag)
PURPLE = {('U', 0, 1), ('D', 0, 1), ('U', 1, 0), ('D', 0, 0)}
PIECES = {'green': (GREEN, 'pbgreen'), 'blue': (BLUE, 'pbblue'), 'red': (RED, 'pbred'),
          'yellow': (YELLOW, 'pbyellow'), 'purple': (PURPLE, 'pbpurple')}


def icon(name, s=0.2):
    tris, col = PIECES[name]
    off = shift_of(tris, s)
    return piece_cmds(tris, col, s, off, lw='iconline')


def outline_shape(tris, col, s=1.0, tint=True):
    off = shift_of(tris, s)
    cmds = []
    for loop in boundary_loops(set(tris)):
        path = poly_path(simplify_loop(loop), s, off)
        if tint:
            cmds.append(f"\\fill[{col}!14] {path};")
        cmds.append(f"\\draw[{col}!75!black, line width=2.2pt] {path};")
    return '\n'.join(cmds) + '\n'


def ribbon_arrows(w, rh, i0, j0, s, off, labels=True, letters=True, size='\\small', color='ribbontext'):
    """Arrows from the midpoint of each horizontal edge down the ribbon, with L/R letters."""
    i, j = i0, j0
    pts = []
    for k in range(len(w)):
        x0, y0 = xy((i, j))
        pts.append((x0 + 0.5, y0))
        u, d = rh[k]
        i = u[1]
        j -= 1
    x0, y0 = xy((i, j))
    pts.append((x0 + 0.5, y0))
    c = ''
    for k in range(len(w)):
        (xa, ya), (xb, yb) = pts[k], pts[k + 1]
        c += (f"\\draw[ribbon arrow, draw={color}] ({fmt(xa * s + off[0])},{fmt(ya * s + off[1])}) -- "
              f"({fmt(xb * s + off[0])},{fmt(yb * s + off[1])});\n")
        if letters:
            lx = (xa + xb) / 2 * s + off[0]
            ly = (ya + yb) / 2 * s + off[1]
            dx = (-0.17 if w[k] == 'L' else 0.17) * (s / 0.8) ** 0.5
            c += f"\\node[font=\\bfseries{size}, text={color}] at ({fmt(lx + dx)},{fmt(ly)}) {{{w[k]}}};\n"
    for (xa, ya) in pts:
        c += f"\\fill[{color}] ({fmt(xa * s + off[0])},{fmt(ya * s + off[1])}) circle (0.035);\n"
    if labels:
        xt, yt = pts[0]
        c += f"\\node[font=\\scriptsize, above=1pt] at ({fmt(xt * s + off[0])},{fmt(yt * s + off[1])}) {{start}};\n"
        xb, yb = pts[-1]
        c += f"\\node[font=\\scriptsize, below=1pt] at ({fmt(xb * s + off[0])},{fmt(yb * s + off[1])}) {{end}};\n"
    return c


def main():
    # ---- icons ----
    for n in PIECES:
        write('icon_' + n, icon(n, 0.11 if n in ('yellow', 'purple') else 0.2))
        write('iconbig_' + n, icon(n, 0.36))
    # up / down small triangle icons
    write('icon_up', board({('U', 0, 0)}, 0.2, fill='upfill', grid=None, outline='iconline'))
    write('icon_dn', board({('D', 0, 0)}, 0.2, fill='white', grid=None, outline='iconline'))

    # ============ K-1 ============
    for n in ['blue', 'red', 'yellow', 'purple']:
        tris, col = PIECES[n]
        write('k1_outline_' + n, outline_shape(tris, col, 1.0))
    hx = region([hexagon(1, 1, 1)])
    write('k1_hex', board(hx, 1.0, fill='pbyellow!10', grid='dotgrid', outline='boardline'))
    star = region([big_up(3), big_down(3, (-1, -1))])
    write('k1_star', board(star, 1.0, fill='white', grid='dotgrid', outline='boardline'))
    write('k1_star_blue', board(star, 1.0, fill='pbblue!8', grid='dotgrid', outline='boardline'))
    for n in (2, 3, 4):
        write(f'k1_tri{n}', board(region([big_up(n)]), 1.0, fill='pbgreen!8', grid='dotgrid', outline='boardline'))
        write(f'k1_tri{n}_b', board(region([big_up(n)]), 1.0, fill='pbblue!8', grid='dotgrid', outline='boardline'))
    # example: hexagon filled with two reds (small)
    t1 = {('U', 0, 0), ('D', -1, 0), ('D', 0, 0)}
    ex = piece_cmds(t1, 'pbred', 0.45, shift_of(hx, 0.45))
    ex += piece_cmds(hx - t1, 'pbred', 0.45, shift_of(hx, 0.45))
    write('k1_hex_example', ex)

    # ============ Grades 2-3 ============
    para = region([[(0, 0), (4, 0), (4, 3), (0, 3)]])
    write('g23_para', board(para, 1.0, fill='white', grid='gridline', outline='boardline'))
    boards = {
        'A': region([big_up(2)]),
        'B': region([hexagon(2, 1, 1)]),
        'C': region([[(0, 0), (1, 0), (1, 2), (-2, 2)]]),
        'D': star,
    }
    for k, r in boards.items():
        write('g23_board' + k, board(r, 1.0, fill='white', grid='gridline', outline='boardline'))
        print('board', k, counts(r), 'tilings', len(all_tilings(r)))
    hx2 = region([hexagon(2, 2, 2)])
    holesA = [('U', -2, 3), ('U', 1, 0)]
    holesB = [('U', -2, 3), ('D', 1, 0)]
    for nm, hl in (('X', holesA), ('Y', holesB)):
        r = hx2 - set(hl)
        print('broken', nm, counts(r), 'tilings', len(all_tilings(r)))
        write('g23_broken' + nm, board(r, 1.0, fill='white', grid='gridline', outline='boardline', holes=hl))
    for n in (3, 4, 5):
        write(f'g23_tri{n}', board(region([big_up(n)]), 1.0, fill='white', grid='gridline', outline='boardline'))
    # ============ Grades 4-5 ============
    # three positions of a blue
    s = 0.42
    c = ''
    x = 0
    for tris in ({('U', 0, 0), ('D', 0, 0)}, {('U', 1, 0), ('D', 0, 0)}, {('U', 0, 1), ('D', 0, 0)}):
        off0 = shift_of(tris, s)
        c += piece_cmds(tris, 'pbblue', s, (off0[0] + x, off0[1]))
        x += 1.05
    write('g45_dirs', c)
    write('g45_hex1', board(hx, 1.0, fill='white', grid='gridline', outline='boardline'))
    # the two tilings of the small hexagon, with flip arrow
    ts = all_tilings(hx)
    s = 0.55
    off = shift_of(hx, s)
    c = tiling_cmds(hx, ts[0], s, off, fills={'L': 'pbblue!35', 'R': 'pbblue!35', 'S': 'pbblue!35'})
    off2 = (off[0] + 2 * s + 1.1, off[1])
    c += tiling_cmds(hx, ts[1], s, off2, fills={'L': 'pbblue!35', 'R': 'pbblue!35', 'S': 'pbblue!35'})
    ym = H * s
    c += f"\\draw[flip arrow] ({fmt(2 * s + 0.15)},{fmt(ym)}) -- ({fmt(2 * s + 0.95)},{fmt(ym)}) node[midway, above=1pt, font=\\small\\bfseries] {{flip}};\n"
    write('g45_hex1_flip', c)
    # cube shading of the small hexagon
    c = tiling_cmds(hx, ts[0], s, off, fills={'L': 'cubeL', 'R': 'cubeR', 'S': 'cubeS'})
    c += tiling_cmds(hx, ts[1], s, off2, fills={'L': 'cubeL', 'R': 'cubeR', 'S': 'cubeS'})
    c += f"\\draw[flip arrow] ({fmt(2 * s + 0.15)},{fmt(ym)}) -- ({fmt(2 * s + 0.95)},{fmt(ym)});\n"
    write('g45_hex1_cubes', c)
    # record grids for the small hexagon
    write('g45_hex1_rec', board(hx, 0.55, fill='white', grid='recgrid', outline='recline'))

    # tall hexagon (1,2,2)
    tall = region([hexagon(1, 2, 2)])
    write('g45_tall', board(tall, 1.0, fill='white', grid='gridline', outline='boardline'))
    write('g45_tall_rec', board(tall, 0.4, fill='white', grid='recgrid', outline='recline'))
    tts = all_tilings(tall)
    words = {}
    for t in tts:
        w, rh = ribbons_from_top(t, 4, [-2])[0]
        words[w] = (t, rh)
    print('tall words', sorted(words))
    blues = {'L': 'pbblue!30', 'R': 'pbblue!30', 'S': 'pbblue!30'}
    s = 0.5
    for w in ('LLRR', 'RRLL'):
        write('g45_tall_' + w, tiling_cmds(tall, words[w][0], s, fills=blues))
    # flip example: LRLR -> LRRL  (find the 3 rhombi that change)
    a, b = words['LRLR'][0], words['LRRL'][0]
    ch_a = set(a) - set(b)
    ch_b = set(b) - set(a)
    assert len(ch_a) == 3 and len(ch_b) == 3
    s = 0.5
    offa = shift_of(tall, s)
    c = tiling_cmds(tall, a, s, offa, fills=blues, highlight=ch_a, hl_style='hlfill')
    offb = (offa[0] + 3 * s + 1.0, offa[1])
    c += tiling_cmds(tall, b, s, offb, fills=blues, highlight=ch_b, hl_style='hlfill')
    ym = 2 * H * s
    c += f"\\draw[flip arrow] ({fmt(3 * s + 0.15)},{fmt(ym)}) -- ({fmt(3 * s + 0.85)},{fmt(ym)}) node[midway, above=1pt, font=\\small\\bfseries] {{flip}};\n"
    write('g45_flip_example', c)

    # ribbon example: word LRRL
    w = 'LRRL'
    t, rh = words[w]
    s = 0.8
    off = shift_of(tall, s)
    c = tiling_cmds(tall, t, s, off, fills={'L': 'white', 'R': 'white', 'S': 'white'}, highlight=set(rh),
                    hl_style='ribbonfill')
    c += ribbon_arrows(w, rh, -2, 4, s, off, labels=True)
    write('g45_ribbon_example', c)

    # big hexagon (2,2,2)
    big = region([hexagon(2, 2, 2)])
    write('g45_big', board(big, 1.0, fill='white', grid='gridline', outline='boardline'))
    write('g45_big_rec', board(big, 0.36, fill='white', grid='recgrid', outline='recline'))
    bts = all_tilings(big)
    bw = {}
    for t in bts:
        rr = ribbons_from_top(t, 4, [-2, -1])
        bw[(rr[0][0], rr[1][0])] = (t, rr)
    # two-ribbon example
    t, rr = bw[('LRLR', 'RLRL')]
    s = 0.68
    off = shift_of(big, s)
    ef = {}
    for p in rr[0][1]:
        ef[p] = 'ribbonfill'
    for p in rr[1][1]:
        ef[p] = 'ribbonfillB'
    c = tiling_cmds(big, t, s, off, fills={'L': 'white', 'R': 'white', 'S': 'white'}, extra_fill=ef)
    c += ribbon_arrows(rr[0][0], rr[0][1], -2, 4, s, off, labels=False, letters=True, size='\\scriptsize')
    c += ribbon_arrows(rr[1][0], rr[1][1], -1, 4, s, off, labels=False, letters=True, size='\\scriptsize', color='ribbontextB')
    write('g45_big_ribbons', c)
    # cube picture
    t, rr = bw[('LLRR', 'LRLR')]
    c = tiling_cmds(big, t, 0.55, None, fills={'L': 'cubeL', 'R': 'cubeR', 'S': 'cubeS'})
    write('g45_big_cubes', c)
    print('big pairs', len(bw))


if __name__ == '__main__':
    main()
