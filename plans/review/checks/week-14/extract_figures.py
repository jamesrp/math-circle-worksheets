"""Read every polygon drawing out of the delivered Week 14 PDFs.

For each page: closed stroked polylines are polygon outlines; open stroked
two-point segments whose ends sit on two corners of one outline are diagonals;
single-character words placed just outside a corner (along the outward ray from
the polygon's centre) are corner labels.  Reports, for every polygon, its corner
count, label order, regularity (side lengths, circumradii, angular spacing),
size, and diagonal set, and compares each page with my own transcription
(expected.py), typed from the rendered page images.

Writes extract_figures.out and extracted_figures.json next to this script.
"""
import os, sys, json, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdfgeom as G
from expected import EXPECTED

OUT = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    OUT.append(s)


FILES = ['week-14-k-1.pdf', 'week-14-grades-2-3.pdf', 'week-14-grades-4-5.pdf',
         'week-14-return-visit.pdf', 'week-14-facilitator.pdf']


def dedup_closed(pts):
    pts = list(pts)
    if len(pts) > 1 and math.dist(pts[0], pts[-1]) < 0.05:
        pts = pts[:-1]
    return pts


def analyse_page(page):
    polys = []
    segs = []
    dots = []
    rings = []
    for p in page['paths']:
        sps = [sp for sp in p['subpaths'] if len(sp[0]) > 1]
        if p['op'] == 'S':
            for pts, closed, curved in sps:
                if curved:
                    continue
                if closed and len(dedup_closed(pts)) >= 3:
                    polys.append({'pts': dedup_closed(pts), 'lw': p['lw']})
                elif len(pts) == 2:
                    segs.append({'a': pts[0], 'b': pts[1], 'lw': p['lw'], 'rgb': p['srgb'], 'dash': p['dash']})
                elif not closed and len(pts) > 2:
                    for a, b in zip(pts, pts[1:]):
                        segs.append({'a': a, 'b': b, 'lw': p['lw'], 'rgb': p['srgb'], 'dash': p['dash'], 'chain': True})
        for sp in p['subpaths']:
            if sp[2]:
                xs = [q[0] for q in sp[0]]; ys = [q[1] for q in sp[0]]
                w = max(xs) - min(xs); h = max(ys) - min(ys)
                c = ((max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2)
                if w < 6 and h < 6 and p['op'] in ('f', 'B'):
                    dots.append(c)
                elif 6 <= w < 30 and abs(w - h) < 0.5 and p['op'] in ('S', 'B'):
                    rings.append((c, w / 2))
    # A closed polyline whose corners are all corners of a larger outline is a
    # set of diagonals drawn in one stroke (e.g. the central triangle ACE).
    keep = []
    for P in polys:
        host = [Q for Q in polys if Q is not P and len(Q['pts']) > len(P['pts']) and
                all(any(math.dist(q, h) < 0.6 for h in Q['pts']) for q in P['pts'])]
        if host:
            pts = P['pts']
            for a, b in zip(pts, pts[1:] + pts[:1]):
                segs.append({'a': a, 'b': b, 'lw': P['lw'], 'rgb': (0, 0, 0), 'dash': False, 'chain': True})
        else:
            keep.append(P)
    polys = keep
    words = [w for w in page['words'] if len(w[0]) == 1 and w[0].isalnum()]
    res = []
    for P in polys:
        pts = P['pts']
        n = len(pts)
        cx = sum(x for x, y in pts) / n; cy = sum(y for x, y in pts) / n
        radii = [math.dist(q, (cx, cy)) for q in pts]
        sides = [math.dist(pts[i], pts[(i + 1) % n]) for i in range(n)]
        angs = [math.degrees(math.atan2(y - cy, x - cx)) for x, y in pts]
        steps = [((angs[i] - angs[(i + 1) % n]) % 360) for i in range(n)]  # clockwise positive
        # labels
        labels = []
        for q in pts:
            ux, uy = (q[0] - cx), (q[1] - cy)
            L = math.hypot(ux, uy); ux /= L; uy /= L
            best = None
            for w in words:
                wc = ((w[1] + w[3]) / 2, (w[2] + w[4]) / 2)
                dx, dy = wc[0] - q[0], wc[1] - q[1]
                along = dx * ux + dy * uy
                perp = abs(-dx * uy + dy * ux)
                if -2 < along < 24 and perp < 7:
                    if best is None or along < best[0]:
                        best = (along, w[0])
            labels.append(best[1] if best else '?')
        on_dots = sum(any(math.dist(q, d) < 0.6 for d in dots) for q in pts)
        on_rings = sum(any(math.dist(q, r[0]) < 0.6 for r in rings) for q in pts)
        diags = []
        for s in segs:
            ia = [i for i, q in enumerate(pts) if math.dist(q, s['a']) < 0.6]
            ib = [i for i, q in enumerate(pts) if math.dist(q, s['b']) < 0.6]
            if ia and ib:
                i, j = ia[0], ib[0]
                if (j - i) % n in (1, n - 1):
                    kind = 'side-overdraw'
                else:
                    kind = 'diag'
                diags.append((kind, ''.join(sorted([labels[i], labels[j]])), s['lw'], s['rgb'], s['dash']))
        top = max(range(n), key=lambda i: pts[i][1])
        res.append({
            'n': n, 'labels': labels, 'center': (cx, cy),
            'circumradius_in': sum(radii) / n / 72,
            'radius_spread': (max(radii) - min(radii)) / (sum(radii) / n),
            'side_spread': (max(sides) - min(sides)) / (sum(sides) / n),
            'angle_steps': [round(s, 3) for s in steps],
            'clockwise': all(0 < s < 180 for s in steps),
            'top_vertex_label': labels[top],
            'top_is_unique': sorted(q[1] for q in pts)[-1] - sorted(q[1] for q in pts)[-2] > 0.5,
            'dots_on_corners': on_dots, 'rings_on_corners': on_rings,
            'diagonals': sorted(d[1] for d in diags if d[0] == 'diag'),
            'diag_detail': diags,
            'width_in': (max(q[0] for q in pts) - min(q[0] for q in pts)) / 72,
            'height_in': (max(q[1] for q in pts) - min(q[1] for q in pts)) / 72,
        })
    # segments not attached to any polygon corner pair but touching a polygon
    loose = []
    for s in segs:
        attached = False
        for P in polys:
            if any(math.dist(q, s['a']) < 0.6 for q in P['pts']) and any(math.dist(q, s['b']) < 0.6 for q in P['pts']):
                attached = True
        if not attached:
            loose.append(s)
    return res, loose, dots, rings


def main():
    allres = {}
    problems = 0
    for f in FILES:
        pages = G.load(os.path.join(G.WEEK, f))
        log('=' * 78)
        log(f, len(pages), 'pages')
        for pi, page in enumerate(pages, 1):
            res, loose, dots, rings = analyse_page(page)
            if not res:
                continue
            log(f'-- page {pi}: {len(res)} polygons')
            for r in res:
                reg = 'regular' if r['radius_spread'] < 1e-3 and r['side_spread'] < 1e-3 else 'NOT regular'
                lab = ''.join(r['labels'])
                expect_lab = ''.join(r['labels'])
                log(f"   n={r['n']} labels={lab} cw={r['clockwise']} top={r['top_vertex_label']} {reg}"
                    f" (r-spread {r['radius_spread']:.1e}, side-spread {r['side_spread']:.1e}) "
                    f"size {r['width_in']:.2f}x{r['height_in']:.2f}in  dots={r['dots_on_corners']} rings={r['rings_on_corners']}"
                    f"  diagonals={' '.join(r['diagonals']) or '-'}")
                odd = [d for d in r['diag_detail'] if d[0] != 'diag']
                if odd:
                    log('     side overdraws:', odd)
                styled = [d for d in r['diag_detail'] if d[0] == 'diag' and (d[3] != (0, 0, 0) or d[4])]
                if styled:
                    log('     coloured/dashed diagonals:', [(d[1], d[3], d[4]) for d in styled])
            if loose:
                short = [s for s in loose if math.dist(s['a'], s['b']) > 3]
                log(f'   {len(short)} other stroked segments (arrows, rules, marks)')
            allres[f'{f}#{pi}'] = res
            exp = EXPECTED.get((f, pi))
            got = sorted((r['n'], ' '.join(r['diagonals'])) for r in res)
            if exp is None:
                log('   (no transcription for this page)')
            else:
                want = sorted((n, ' '.join(sorted(d.split()))) for n, d in exp)
                if want == got:
                    log('   transcription matches PDF')
                else:
                    problems += 1
                    log('   MISMATCH with transcription')
                    log('     expected', want)
                    log('     got     ', got)
    log('=' * 78)
    log('pages whose PDF drawings differ from my transcription:', problems)
    json.dump(allres, open(os.path.join(HERE, 'extracted_figures.json'), 'w'), indent=1, default=str)
    open(os.path.join(HERE, 'extract_figures.out'), 'w').write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
