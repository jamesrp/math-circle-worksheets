"""Reconstruct every printed network in the delivered Week 53 student PDF and
compare it with a hand transcription made from the rendered pages.

Checks: places, links, bought (thick) links, price numerals and dot counts,
which link each price label is nearest to (and how close the runner-up is),
labels whose white background box cuts across a different link or is cut by a
place circle, nearest-place spacing, and equal scaling of the square maps.
Run: python3 check_diagrams.py  (writes out_check_diagrams.txt beside itself)
"""
import itertools
import math
import os as _os
import sys

HERE = _os.path.dirname(_os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdfgeom  # noqa: E402

PT_MM = 25.4 / 72

# Hand transcription from the 80/300 dpi renders (page -> list of diagrams,
# left-to-right, top-to-bottom). Prices None = blank to fill in; 'rec' = no prices.
# Each diagram: (name, {edge: price}, bought set)
T = {
    1: [('convention available', {'XY': 2, 'YZ': 4, 'XZ': 3}, set()),
        ('convention paid', {'XY': 2, 'YZ': 4, 'XZ': 3}, {'XY', 'YZ'}),
        ('convention record', {'XY': 'rec', 'YZ': 'rec', 'XZ': 'rec'}, {'XY', 'YZ'}),
        ('P1 left', {'AB': 1, 'BC': 2, 'AC': 3}, set()),
        ('P1 right', {'AB': 1, 'BC': 2, 'AC': 2}, set())],
    2: [('P2', {'AB': 1, 'AC': 1, 'BC': 1, 'CD': 2, 'AD': 3}, set())] +
       [('P2 record %d' % k, {e: 'rec' for e in ('AB', 'AC', 'BC', 'CD', 'AD')}, set()) for k in (1, 2, 3)],
    3: [('P3', {'AB': 1, 'BC': 2, 'AC': 3, 'CD': 4, 'AD': 5}, set())] +
       [('P3 record %d' % k, {e: 'rec' for e in ('AB', 'AC', 'BC', 'CD', 'AD')}, set()) for k in (1, 2)],
    4: [('P4', {'AB': 1, 'AC': 1, 'BC': 1, 'AD': 5, 'CD': 2, 'DE': 2, 'CE': 3, 'BE': 6}, set())] +
       [('P4 record %d' % k, {e: 'rec' for e in ('AB', 'AC', 'BC', 'AD', 'CD', 'DE', 'CE', 'BE')}, set())
        for k in (1, 2, 3)],
    5: [('P5 demo before', {'UV': 2, 'VW': 4, 'UW': 3}, {'UV', 'VW'}),
        ('P5 demo buy', {'UV': 2, 'VW': 4, 'UW': 3}, {'UV', 'VW', 'UW'}),
        ('P5 demo return', {'UV': 2, 'VW': 4, 'UW': 3}, {'UV', 'UW'}),
        ('P5 left', {'AB': 1, 'BC': 2, 'CD': 3, 'AD': 4, 'AC': 5}, {'AB', 'AD', 'AC'}),
        ('P5 right', {'AB': 1, 'BC': 2, 'CD': 3, 'AD': 4, 'AC': 5}, {'AB', 'BC', 'CD'})],
    6: [('P6', {'AB': 1, 'AC': 3, 'BC': 2, 'CD': 2, 'BD': 5, 'CE': 6, 'DE': 1, 'EF': 2, 'DF': 4}, set())],
    7: [('P7 left', {e: None for e in ('AB', 'AC', 'AD', 'BC', 'BD', 'CD')}, set()),
        ('P7 right', {e: None for e in ('AB', 'AC', 'AD', 'BC', 'BD', 'CD')}, set())],
    8: [('P8 top', {'AB': 1, 'AC': 3, 'BC': 2, 'CD': 2, 'BD': 5, 'CE': 6, 'DE': 1, 'EF': 2, 'DF': 4},
         {'AB', 'BC', 'CD', 'DE', 'EF'}),
        ('P8 bottom', {'AB': 1, 'AC': 3, 'BC': 2, 'CD': 2, 'BD': 5, 'CE': 6, 'DE': 1, 'EF': 2, 'DF': 4},
         {'AB', 'AC', 'BD', 'DE', 'DF'})],
    9: [('P9', {'AB': 1, 'BC': 2, 'CD': 3, 'AD': 4, 'AC': 5, 'BD': 6}, set())],
}


def key(a, b):
    return ''.join(sorted((a, b)))


def seg_dist(px, py, ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    qx, qy = ax + t * dx, ay + t * dy
    return math.hypot(px - qx, py - qy)


def seg_hits_rect(ax, ay, bx, by, r, pad=0.0):
    """Does segment AB pass through rectangle r (expanded by pad)? Liang-Barsky."""
    x0, y0, x1, y1 = r['x0'] - pad, r['y0'] - pad, r['x1'] + pad, r['y1'] + pad
    dx, dy = bx - ax, by - ay
    t0, t1 = 0.0, 1.0
    for p, q in ((-dx, ax - x0), (dx, x1 - ax), (-dy, ay - y0), (dy, y1 - ay)):
        if abs(p) < 1e-12:
            if q < 0:
                return False
            continue
        t = q / p
        if p < 0:
            t0 = max(t0, t)
        else:
            t1 = min(t1, t)
    return t0 <= t1


def circle_rect_overlap(cx, cy, rad, r):
    nx = min(max(cx, r['x0']), r['x1']); ny = min(max(cy, r['y0']), r['y1'])
    return math.hypot(cx - nx, cy - ny) < rad


def analyse(pageno, page, out):
    verts = [c for c in page['curves'] if c['op'] == 'B' and c['rx'] > 5]
    dots = [c for c in page['curves'] if c['op'] in ('f', 'F') and c['rx'] < 3]
    letters = [t for t in page['texts'] if len(t['s']) == 1 and t['s'].isupper()]
    vname = {}
    for i, c in enumerate(verts):
        inside = [t for t in letters if math.hypot(t['x'] + 0.33 * t['size'] - c['cx'],
                                                  t['y'] + 0.36 * t['size'] - c['cy']) < c['rx']]
        assert len(inside) == 1, (pageno, c, inside)
        vname[i] = inside[0]['s']
    # Union-find of vertices via line endpoints
    parent = list(range(len(verts)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x

    def vat(p):
        for i, c in enumerate(verts):
            if math.hypot(p[0] - c['cx'], p[1] - c['cy']) < 0.6:
                return i
        return None

    segs = []
    for ln in page['lines']:
        i, j = vat(ln['p']), vat(ln['q'])
        if i is None or j is None:
            continue
        parent[find(i)] = find(j)
        segs.append((i, j, ln))
    comps = {}
    for i in range(len(verts)):
        comps.setdefault(find(i), []).append(i)
    # order diagrams: top-to-bottom bands then left-to-right
    diag = sorted(comps.values(), key=lambda vs: (-round(max(verts[v]['cy'] for v in vs) / 60),
                                                  min(verts[v]['cx'] for v in vs)))
    digit_texts = [t for t in page['texts'] if len(t['s']) == 1 and t['s'].isdigit()]
    white = [r for r in page['rects'] if r['fill'] == 1.0]
    # answer blanks: short thin horizontal strokes (\rule drawn as a stroke) not touching places
    blanks = []
    for ln in page['lines']:
        (ax, ay), (bx, by) = ln['p'], ln['q']
        if ln['width'] < 0.5 and abs(ay - by) < 0.01 and 5 < abs(bx - ax) < 20:
            blanks.append({'x0': min(ax, bx), 'x1': max(ax, bx), 'y0': ay, 'y1': ay})
    expected = T[pageno]
    problems = []
    if len(diag) != len(expected):
        problems.append('diagram count %d != transcription %d' % (len(diag), len(expected)))
    for (name, eprices, ebought), vs in zip(expected, diag):
        vset = set(vs)
        edges = {}
        for i, j, ln in segs:
            if i in vset:
                k = key(vname[i], vname[j])
                e = edges.setdefault(k, {'i': i, 'j': j, 'thick': False, 'thin': False})
                if ln['width'] > 2:
                    e['thick'] = True
                else:
                    e['thin'] = True
        names = sorted(vname[v] for v in vs)
        rad = verts[vs[0]]['rx']
        # spacing
        mind = min(math.hypot(verts[a]['cx'] - verts[b]['cx'], verts[a]['cy'] - verts[b]['cy'])
                   for a, b in itertools.combinations(vs, 2))
        line = '%s: places %s, circle diameter %.1f mm, nearest centres %.1f mm' % (
            name, ''.join(names), 2 * rad * PT_MM, mind * PT_MM)
        out.append(line)
        if set(edges) != set(eprices):
            problems.append('%s: links %s != transcription %s' % (name, sorted(edges), sorted(eprices)))
        bought = {k for k, e in edges.items() if e['thick']}
        if bought != ebought:
            problems.append('%s: bought %s != transcription %s' % (name, sorted(bought), sorted(ebought)))
        # bbox of this diagram for label association
        xs = [verts[v]['cx'] for v in vs]; ys = [verts[v]['cy'] for v in vs]
        bb = (min(xs) - 40, min(ys) - 40, max(xs) + 40, max(ys) + 40)
        labs = []
        for r in white:
            cx, cy = (r['x0'] + r['x1']) / 2, (r['y0'] + r['y1']) / 2
            if not (bb[0] <= cx <= bb[2] and bb[1] <= cy <= bb[3]):
                continue
            if any(abs(cx - verts[v]['cx']) < 1 and abs(cy - verts[v]['cy']) < 1 for v in range(len(verts))):
                continue
            ts = [t for t in digit_texts if r['x0'] - 0.5 <= t['x'] <= r['x1'] and r['y0'] - 0.5 <= t['y'] <= r['y1']]
            nd = sum(1 for d in dots if r['x0'] <= d['cx'] <= r['x1'] and r['y0'] <= d['cy'] <= r['y1'])
            bl = [b for b in blanks if r['x0'] - 0.5 <= b['x0'] and b['x1'] <= r['x1'] + 0.5
                  and r['y0'] - 0.5 <= b['y0'] <= r['y1']]
            if not ts and not bl:
                continue
            val = int(ts[0]['s']) if ts else None
            labs.append((r, val, nd, ts[0] if ts else None))
        claimed = {}
        for r, val, nd, t in labs:
            if t is not None:
                # glyph centre from Helvetica metrics (digit advance 0.556 em, height ~0.7 em)
                gx, gy = t['x'] + 0.278 * t['size'], t['y'] + 0.35 * t['size']
                # dots extend the white box to the right; use the numeral for distance
            else:
                gx, gy = (r['x0'] + r['x1']) / 2, (r['y0'] + r['y1']) / 2
            ds = []
            for k, e in edges.items():
                a, b = verts[e['i']], verts[e['j']]
                ds.append((seg_dist(gx, gy, a['cx'], a['cy'], b['cx'], b['cy']), k))
            ds.sort()
            nearest = ds[0][1]
            # intended owner: nearest link whose transcribed price matches this label
            cand = [(d, k) for d, k in ds if eprices.get(k) == val]
            owner = cand[0][1] if cand else nearest
            d_own = [d for d, k in ds if k == owner][0]
            others = [(d, k) for d, k in ds if k != owner]
            ratio = others[0][0] / d_own if d_own > 0 else float('inf')
            crossed = []
            for k, e in edges.items():
                if k == owner:
                    continue
                a, b = verts[e['i']], verts[e['j']]
                if seg_hits_rect(a['cx'], a['cy'], b['cx'], b['cy'], r):
                    crossed.append(k)
            circ = [vname[v] for v in vs if circle_rect_overlap(verts[v]['cx'], verts[v]['cy'], verts[v]['rx'], r)]
            claimed.setdefault(nearest, []).append(val)
            msg = '  label %s -> intended %s at %.1f mm; nearest other link %s at %.1f mm (ratio %.2f)' % (
                val if val is not None else 'blank', owner, d_own * PT_MM, others[0][1], others[0][0] * PT_MM, ratio)
            if nearest != owner:
                msg += '; NEARER TO %s THAN TO ITS OWN LINK' % nearest
                problems.append('%s: label %s for %s is nearer to link %s (%.1f mm vs %.1f mm)' % (
                    name, val, owner, nearest, others[0][0] * PT_MM, d_own * PT_MM))
            if t is not None and eprices.get(owner) not in (None, 'rec'):
                if nd and nd != val:
                    problems.append('%s: label %s has %d dots' % (name, val, nd))
                if nd:
                    msg += ', %d dots' % nd
            if crossed:
                msg += '; WHITE LABEL BOX CUTS ACROSS LINK %s' % ','.join(crossed)
                problems.append('%s: label %s (for %s) is painted over link %s' % (name, val, owner, ','.join(crossed)))
            if circ:
                depth = 0.0
                if t is not None:
                    # Helvetica digit glyph box (AFM, approx): x 0.03-0.52 em, y -0.02-0.70 em
                    s_ = t['size']
                    gx0, gx1 = t['x'] + 0.03 * s_, t['x'] + 0.52 * s_
                    gy0, gy1 = t['y'] - 0.02 * s_, t['y'] + 0.70 * s_
                    for v in vs:
                        if vname[v] not in circ:
                            continue
                        c = verts[v]
                        for k in range(201):
                            x = gx0 + (gx1 - gx0) * k / 200
                            dx = x - c['cx']
                            if abs(dx) < c['rx']:
                                h = math.sqrt(c['rx'] ** 2 - dx * dx)
                                lo, hi = c['cy'] - h, c['cy'] + h
                                depth = max(depth, min(gy1, hi) - max(gy0, lo))
                msg += '; label box overlaps circle %s (numeral hidden up to %.2f mm of %.2f mm)' % (
                    ','.join(circ), max(depth, 0) * PT_MM, (gy1 - gy0) * PT_MM if t is not None else 0)
                problems.append('%s: label %s (for %s) is partly covered by place circle %s (%.2f mm of the numeral hidden)' % (
                    name, val, owner, ','.join(circ), max(depth, 0) * PT_MM))
            if 1 <= ratio < 1.5:
                msg += '; AMBIGUOUS (other link within 1.5x)'
                problems.append('%s: label %s for %s has link %s within %.2fx of its distance' % (
                    name, val, owner, others[0][1], ratio))
            out.append(msg)
        got = {k: (v[0] if len(v) == 1 else v) for k, v in claimed.items()}
        exp = {k: v for k, v in eprices.items() if v not in ('rec', None)}
        nblank = sum(1 for r, val, nd, t in labs if t is None)
        if any(v is None for v in eprices.values()):
            out.append('  %d blank price slots for %d links' % (nblank, len(eprices)))
            if nblank != len(eprices):
                problems.append('%s: %d blank slots for %d links' % (name, nblank, len(eprices)))
        elif got != exp:
            problems.append('%s: assigning each numeral to its nearest link gives %s (transcription %s)' % (name, got, exp))
        # equal scaling check for square maps
        if name in ('P5 left', 'P5 right', 'P9'):
            P = {vname[v]: (verts[v]['cx'], verts[v]['cy']) for v in vs}
            sides = [math.dist(P[a], P[b]) for a, b in ('AB', 'BC', 'CD', 'DA')]
            diags = [math.dist(P['A'], P['C']), math.dist(P['B'], P['D'])]
            out.append('  square sides (mm) %s, diagonals %s' % (
                ['%.2f' % (s * PT_MM) for s in sides], ['%.2f' % (d * PT_MM) for d in diags]))
            if max(sides) - min(sides) > 0.05 or abs(diags[0] - diags[1]) > 0.05:
                problems.append('%s: not a square' % name)
    return problems


def main():
    pages = pdfgeom.read(pdfgeom.STUDENT_PDF)
    out = ['Delivered PDF: %s (%d pages)' % (_os.path.relpath(pdfgeom.STUDENT_PDF, pdfgeom.ROOT), len(pages))]
    allp = []
    for n, page in enumerate(pages, 1):
        out.append('--- page %d ---' % n)
        hdr = [t['s'] for t in page['texts'] if t['y'] > 740]
        ftr = [t['s'] for t in page['texts'] if t['y'] < 40]
        out.append('header %s | footer %s' % (hdr, ftr))
        p = analyse(n, page, out)
        allp += ['page %d: %s' % (n, x) for x in p]
    # Source data consistency: networks.json (writer's editable source) vs. this transcription
    import json
    src = json.load(open(_os.path.join(pdfgeom.ROOT, 'lowell-math-circle-year-2', 'source', 'week-53',
                                       'student', 'networks.json')))
    pairs = {'convention': 'convention available', 'triangle_one': 'P1 left', 'triangle_two': 'P1 right',
             'four_ties': 'P2', 'four_trap': 'P3', 'five_ties': 'P4', 'swap_demo': 'P5 demo before',
             'swaps': 'P5 left', 'six_cert': 'P6', 'price_design': 'P7 left', 'distinct': 'P9'}
    alld = {nm: pr for diags in T.values() for nm, pr, b in diags}
    for sk, nm in pairs.items():
        sp = {key(a, b): w for a, b, w in src[sk]['edges']}
        if sp != alld[nm]:
            allp.append('networks.json %s differs from printed %s: %s vs %s' % (sk, nm, sp, alld[nm]))
    out.append('networks.json checked against the printed maps for %d graphs' % len(pairs))
    out.append('=== findings (%d) ===' % len(allp))
    out += allp
    txt = '\n'.join(out)
    print(txt)
    open(_os.path.join(HERE, 'out_check_diagrams.txt'), 'w').write(txt + '\n')


if __name__ == '__main__':
    main()
