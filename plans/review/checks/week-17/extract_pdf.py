"""Read every machine diagram, card row and answer slot from the delivered
Week 17 student PDFs (base bands and the return visit).

Machines are rebuilt from the drawing itself: state circles, the words inside
them, each stroked edge with the arrowhead at its end (which circle the tip
touches), and the card label nearest the middle of the edge.  Card rows are
read from coloured card shapes and the letter printed inside each.
Run: python3 extract_pdf.py  (writes out_extract_pdf.txt and pdf_data.json)
"""
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pdfgeom17 as G  # noqa: E402
import repo  # noqa: E402

OUT = []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def close(c1, c2, tol=0.03):
    return len(c1) == len(c2) and all(abs(a - b) < tol for a, b in zip(c1, c2))


RED_FILL = [(0.97961, 0.91765, 0.91765), (1.0, 0.88, 0.88)]
BLUE_FILL = [(0.91333, 0.93726, 0.96902), (0.88, 0.88, 1.0)]


def colour_of(p):
    if p['fill'] and any(close(p['fc'], c) for c in RED_FILL):
        return 'R'
    if p['fill'] and any(close(p['fc'], c) for c in BLUE_FILL):
        return 'B'
    return None


def shape_of(p):
    kinds = {s[0] for s in p['segs']}
    return 'round' if 'c' in kinds and 'l' not in kinds else ('rect' if 'c' not in kinds else 'roundrect')


def centre(b):
    return ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2)


def inside(pt, b, pad=0.0):
    return b[0] - pad <= pt[0] <= b[2] + pad and b[1] - pad <= pt[1] <= b[3] + pad


def arclen_mid(pts):
    d = [0.0]
    for a, b in zip(pts, pts[1:]):
        d.append(d[-1] + math.dist(a, b))
    half = d[-1] / 2
    for i in range(1, len(d)):
        if d[i] >= half:
            t = (half - d[i - 1]) / max(d[i] - d[i - 1], 1e-9)
            a, b = pts[i - 1], pts[i]
            return (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))
    return pts[-1]


def read_page(key, pno, content):
    ps = G.paths(content)
    ws = G.words(repo.PDF[key], pno)
    wc = [(w[0], centre(w[1:])) for w in ws]
    cards, states, edges, heads, slots, lines = [], [], [], [], [], []
    for p in ps:
        b = G.bbox(p)
        w, h = b[2] - b[0], b[3] - b[1]
        col = colour_of(p)
        if col:
            letters = [t for t, c in wc if inside(c, b) and t in ('R', 'B')]
            cards.append({'colour': col, 'shape': shape_of(p), 'bbox': b, 'size': (w, h),
                          'letter': letters[0] if len(letters) == 1 else letters})
        elif p['stroke'] and not p['fill'] and G.closed(p) and abs(w - h) < 1 and 40 < w < 52 \
                and close(p['sc'], (0.0,)):
            c = centre(b)
            label = [t for t, cc in wc if math.dist(cc, c) < w / 2]
            states.append({'c': c, 'r': w / 2, 'label': label})
        elif p['fill'] and close(p['fc'], (0.0,)) and w < 6 and h < 6:
            heads.append(G.points(p))
        elif p['stroke'] and not p['fill'] and not G.closed(p) and close(p['sc'], (0.0,)) and p['lw'] > 0.38 \
                and max(w, h) > 8:
            edges.append(G.points(p, steps=24))
        elif p['stroke'] and not p['fill'] and G.closed(p) and 28 < w < 40 and abs(w - h) < 1:
            slots.append(b)
        elif p['stroke'] and not p['fill'] and not G.closed(p) and h < 0.5 and w > 60 and not close(p['sc'], (0.0,)):
            lines.append(b)
    return ps, ws, cards, states, edges, heads, slots, lines


def build_machines(states, edges, heads, label_cards, label_words):
    """Return a list of machines read from the drawing."""
    def near_state(pt, tol):
        best = min(range(len(states)), key=lambda i: abs(math.dist(pt, states[i]['c']) - states[i]['r']))
        d = abs(math.dist(pt, states[best]['c']) - states[best]['r'])
        return (best, d) if d < tol else (None, d)

    trans, starts, notes = [], [], []
    for e in edges:
        end = e[-1]
        # the arrowhead whose nearest vertex touches the end of this edge
        h = min(heads, key=lambda hp: min(math.dist(end, q) for q in hp))
        if min(math.dist(end, q) for q in h) > 2.5:
            if min(abs(math.dist(end, s['c']) - s['r']) for s in states) < 30:
                notes.append('edge without arrowhead near a state at %s' % (end,))
            continue
        tip = max(h, key=lambda q: math.dist(end, q))
        tgt, dt = near_state(tip, 3.0)
        src, ds = near_state(e[0], 3.0)
        if tgt is None:
            notes.append('arrow tip %s touches no state (%.2f)' % (tip, dt))
            continue
        if src is None:
            starts.append(tgt)
            continue
        mid = arclen_mid(e)
        cands = sorted(((math.dist(mid, c), l) for l, c in label_cards + label_words), key=lambda t: t[0])
        lab = cands[0][1]
        margin = cands[1][0] - cands[0][0] if len(cands) > 1 else float('inf')
        trans.append((src, lab, tgt, round(cands[0][0], 1), round(margin, 1)))
    # group states into machines by connectivity
    parent = list(range(len(states)))

    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for s, _, t, _, _ in trans:
        parent[find(s)] = find(t)
    groups = {}
    for i in range(len(states)):
        groups.setdefault(find(i), []).append(i)
    machines = []
    for g in sorted(groups.values(), key=lambda g: min(states[i]['c'][0] for i in g)):
        g = sorted(g, key=lambda i: (states[i]['c'][0], -states[i]['c'][1]))
        idx = {s: k for k, s in enumerate(g)}
        lab = []
        for s in g:
            L = states[s]['label']
            if '✓' in L or 'YES' in L:
                lab.append(True)
            elif '×' in L or 'NO' in L:
                lab.append(False)
            else:
                lab.append(None)
        tr = [(idx[s], a, idx[t], d, m) for s, a, t, d, m in trans if s in idx]
        st = [idx[s] for s in starts if s in idx]
        machines.append({'states': [states[s]['label'] for s in g], 'centres': [states[s]['c'] for s in g],
                         'accept': lab, 'start': st, 'trans': tr})
    return machines, notes


def rows_of(cards):
    """Group row cards into rows: same baseline, gaps under 15 pt."""
    cs = sorted(cards, key=lambda c: (-round(centre(c['bbox'])[1]), centre(c['bbox'])[0]))
    lines = []
    for c in cs:
        y = centre(c['bbox'])[1]
        if lines and abs(lines[-1][0] - y) < 3:
            lines[-1][1].append(c)
        else:
            lines.append([y, [c]])
    rows = []
    for y, cl in lines:
        cl.sort(key=lambda c: c['bbox'][0])
        cur = [cl[0]]
        for a, b in zip(cl, cl[1:]):
            if b['bbox'][0] - a['bbox'][2] > 15:
                rows.append((y, cur[0]['bbox'][0], ''.join(c['letter'] for c in cur)))
                cur = [b]
            else:
                cur.append(b)
        rows.append((y, cur[0]['bbox'][0], ''.join(c['letter'] for c in cur)))
    return rows


def main(quiet=False):
    data = {}
    OUT.clear()
    for key in ('K1', 'G23', 'G45', 'RV'):
        pcs = G.page_contents(repo.PDF[key])
        say('=' * 70)
        say(key, repo.PDF[key].name, 'pages:', len(pcs))
        data[key] = []
        for pno, content in enumerate(pcs, 1):
            ps, ws, cards, states, edges, heads, slots, lines = read_page(key, pno, content)
            bad = [c for c in cards if c['letter'] not in ('R', 'B') or c['letter'] != c['colour']]
            # card shape convention
            shapes = {(c['colour'], c['shape']) for c in cards}
            # label cards: cards lying on an edge label (small, in diagrams)
            lab_cards, row_cards = [], []
            for c in cards:
                cc = centre(c['bbox'])
                if states and min(math.dist(cc, s['c']) for s in states) < 260 and c['size'][0] < 18.5 \
                        and key != 'RV':
                    lab_cards.append((c['letter'], cc))
                else:
                    row_cards.append(c)
            lab_words = []
            if key == 'RV' and states:
                # return-visit labels are plain letters near the diagram
                for t, x0, y0, x1, y1 in ws:
                    cc = ((x0 + x1) / 2, (y0 + y1) / 2)
                    if t in ('R', 'B') and not any(inside(cc, c['bbox']) for c in cards) \
                            and min(math.dist(cc, s['c']) for s in states) < 80:
                        lab_words.append((t, cc))
            machines, notes = build_machines(states, edges, heads, lab_cards, lab_words) if states else ([], [])
            rows = rows_of(row_cards) if row_cards else []
            say('-- page', pno, '| card shapes', sorted(shapes), '| letter/colour mismatches:', len(bad))
            say('   states', len(states), 'edges', len(edges), 'arrowheads', len(heads),
                'answer boxes', len(slots), 'grey answer lines', len(lines))
            for n in notes:
                say('   NOTE', n)
            for i, m in enumerate(machines):
                say('   machine', i, 'labels', m['states'], 'accept', m['accept'], 'start', m['start'])
                for t in sorted(m['trans'], key=lambda t: (t[0], t[1])):
                    say('     %d --%s--> %d   (label %.1f pt from edge middle; next label %.1f pt farther)' % t)
            for y, x, r in rows:
                say('   row y=%.0f x=%.0f  %s' % (y, x, r))
            # answer-box rows (K-1)
            if slots:
                ys = {}
                for b in slots:
                    ys.setdefault(round(b[1]), []).append(b)
                say('   answer-box rows:', len(ys), 'boxes per row:', sorted({len(v) for v in ys.values()}))
            data[key].append({'page': pno, 'machines': machines, 'rows': rows,
                              'slots': len(slots), 'lines': len(lines),
                              'heads': len(heads), 'edges': len(edges), 'states': len(states)})
    (HERE / 'pdf_data.json').write_text(json.dumps(data, indent=1))
    (HERE / 'out_extract_pdf.txt').write_text('\n'.join(OUT) + '\n')
    if not quiet:
        print('\n'.join(OUT))
    return data


if __name__ == '__main__':
    main()
