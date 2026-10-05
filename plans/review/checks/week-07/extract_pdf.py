"""Read the delivered Week 7 student PDFs back: counters, tracks, chart.

For every page of every band it finds
  * each "Problem N:" heading,
  * every drawn counter (filled grey circle), grouped into rows and piles,
  * every number track: the numbered squares, whether consecutive numbers
    share an edge, whether a thick wall blocks a consecutive pair or leaves
    a non-consecutive edge-neighbour pair open, and the square size,
  * the 4-5 two-pile chart (grid size and labels),
  * the 1st/2nd (first/second) choice labels on each counter row.
Writes a summary to stdout (saved as extract_pdf.out) and pdf_geometry.json.
"""
import os, json, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
    d = HERE
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
        d = os.path.dirname(d)
    ROOT = d

import pymupdf

PKT = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-07')
BANDS = ['k-1', 'grades-2-3', 'grades-4-5']


def close(a, b, tol=0.6):
    return abs(a - b) <= tol


def page_data(page):
    words = page.get_text('words')
    # problem headings
    heads = []
    for i, w in enumerate(words):
        if w[4] == 'Problem' and i + 1 < len(words) and words[i + 1][4].endswith(':'):
            try:
                n = int(words[i + 1][4][:-1])
            except ValueError:
                continue
            heads.append((w[1], n))
    heads.sort()

    def problem_at(y):
        cur = None
        for hy, n in heads:
            if hy <= y + 1:
                cur = n
        return cur

    circles, squares, thick = [], [], []
    for d in page.get_drawings():
        kinds = [it[0] for it in d['items']]
        r = d['rect']
        if kinds == ['c', 'c', 'c', 'c'] and d.get('fill') is not None:
            circles.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2, r.width, r.height))
        elif d.get('fill') is None and (d.get('width') or 0) > 1.5:
            for it in d['items']:
                if it[0] == 'l':
                    thick.append((it[1].x, it[1].y, it[2].x, it[2].y))
                elif it[0] == 're':
                    rr = it[1]
                    thick += [(rr.x0, rr.y0, rr.x1, rr.y0), (rr.x1, rr.y0, rr.x1, rr.y1),
                              (rr.x1, rr.y1, rr.x0, rr.y1), (rr.x0, rr.y1, rr.x0, rr.y0)]
        elif kinds in (['l', 'l', 'l', 'l'], ['re']) and d.get('fill') is None:
            squares.append((r.x0, r.y0, r.x1, r.y1))
    return words, heads, problem_at, circles, squares, thick


def group_circles(circles, problem_at):
    rows = defaultdict(list)
    for x, y, w, h in circles:
        key = round(y, 0)
        for k in list(rows):
            if abs(k - y) < 3:
                key = k
                break
        rows[key].append((x, w, h))
    out = []
    for y in sorted(rows):
        xs = sorted(c[0] for c in rows[y])
        gaps = [b - a for a, b in zip(xs, xs[1:])]
        step = min(gaps) if gaps else 0
        piles = [1]
        for g in gaps:
            if g > 1.6 * step:
                piles.append(1)
            else:
                piles[-1] += 1
        sizes = sorted({(round(c[1], 2), round(c[2], 2)) for c in rows[y]})
        out.append({'problem': problem_at(y), 'y': round(y, 1), 'piles': piles,
                    'diameter_pt': sizes})
    return out


def number_squares(words, squares):
    """Map each square that contains exactly one integer word to that integer."""
    out = []
    for (x0, y0, x1, y1) in squares:
        inside = [w for w in words if w[0] >= x0 - 0.5 and w[2] <= x1 + 0.5 and
                  w[1] >= y0 - 0.5 and w[3] <= y1 + 0.5]
        nums = [w[4] for w in inside if w[4].isdigit()]
        if len(inside) == 1 and len(nums) == 1:
            out.append((int(nums[0]), (x0, y0, x1, y1)))
        else:
            out.append((None, (x0, y0, x1, y1)))
    return out


def shared_edge(a, b):
    """Return the shared edge segment of two axis-parallel squares, or None."""
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    if close(ax1, bx0) or close(bx1, ax0):
        x = ax1 if close(ax1, bx0) else ax0
        lo, hi = max(ay0, by0), min(ay1, by1)
        if hi - lo > 1:
            return ('v', x, lo, hi)
    if close(ay1, by0) or close(by1, ay0):
        y = ay1 if close(ay1, by0) else ay0
        lo, hi = max(ax0, bx0), min(ax1, bx1)
        if hi - lo > 1:
            return ('h', y, lo, hi)
    return None


def wall_covers(edge, thick):
    kind, c, lo, hi = edge
    mid = (lo + hi) / 2
    for (x0, y0, x1, y1) in thick:
        if kind == 'v' and close(x0, c, 1.2) and close(x1, c, 1.2):
            if min(y0, y1) - 0.5 <= mid <= max(y0, y1) + 0.5:
                return True
        if kind == 'h' and close(y0, c, 1.2) and close(y1, c, 1.2):
            if min(x0, x1) - 0.5 <= mid <= max(x0, x1) + 0.5:
                return True
    return False


def tracks(words, squares, thick, problem_at):
    numbered = [(n, r) for n, r in number_squares(words, squares) if n is not None]
    # connected components by shared edges
    idx = list(range(len(numbered)))
    parent = idx[:]

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for i in idx:
        for j in idx:
            if i < j and shared_edge(numbered[i][1], numbered[j][1]):
                parent[find(i)] = find(j)
    comps = defaultdict(list)
    for i in idx:
        comps[find(i)].append(i)
    out = []
    for comp in comps.values():
        sq = {numbered[i][0]: numbered[i][1] for i in comp}
        nums = sorted(sq)
        top = min(r[1] for r in sq.values())
        rec = {'problem': problem_at(top), 'y': round(top, 1), 'numbers': f'{nums[0]}..{nums[-1]}',
               'complete': nums == list(range(nums[0], nums[-1] + 1)) and len(nums) == len(comp)}
        sides = sorted({(round(r[2] - r[0], 2), round(r[3] - r[1], 2)) for r in sq.values()})
        rec['square_pt'] = sides
        rec['square_in'] = sorted({round((r[2] - r[0]) / 72, 3) for r in sq.values()})
        bad_consecutive, open_nonconsecutive, walled_pairs = [], [], 0
        for a in nums:
            for b in nums:
                if a < b:
                    e = shared_edge(sq[a], sq[b])
                    if e is None:
                        if b == a + 1:
                            bad_consecutive.append((a, b, 'not adjacent'))
                        continue
                    walled = wall_covers(e, thick)
                    if b == a + 1 and walled:
                        bad_consecutive.append((a, b, 'thick wall between'))
                    if b != a + 1 and not walled:
                        open_nonconsecutive.append((a, b))
                    if b != a + 1 and walled:
                        walled_pairs += 1
        rec['consecutive_problems'] = bad_consecutive
        rec['open_nonconsecutive_neighbours'] = open_nonconsecutive
        rec['walled_nonconsecutive_pairs'] = walled_pairs
        out.append(rec)
    out.sort(key=lambda r: r['y'])
    return out


def choice_labels(page, problem_at):
    # Only the large-type labels printed beside piles and tracks, not body text.
    out = defaultdict(list)
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for sp in l['spans']:
                t = sp['text'].strip()
                if t in ('1st', '2nd', 'first', 'second') and sp['size'] > 15:
                    y = sp['bbox'][1]
                    key = next((k for k in out if abs(k - y) < 6), round(y))
                    out[key].append(t)
    rows = []
    for y in sorted(out):
        rows.append({'problem': problem_at(y), 'y': y, 'labels': out[y]})
    return rows


def chart(words, squares):
    small = [r for r in squares if 20 < r[2] - r[0] < 35]
    if not small:
        return None
    xs = sorted({round(r[0], 1) for r in small})
    ys = sorted({round(r[1], 1) for r in small})
    side = sorted({(round(r[2] - r[0], 2), round(r[3] - r[1], 2)) for r in small})
    x0, x1 = min(r[0] for r in small), max(r[2] for r in small)
    y0, y1 = min(r[1] for r in small), max(r[3] for r in small)
    col_labels = sorted([(w[0], w[4]) for w in words if w[4].isdigit() and w[3] <= y0 + 0.5 and w[1] > y0 - 30
                         and x0 - 1 <= w[0] <= x1])
    row_labels = sorted([(w[1], w[4]) for w in words if w[4].isdigit() and w[2] <= x0 + 0.5 and w[0] > x0 - 30
                         and y0 - 1 <= w[1] <= y1])
    return {'cells': len(small), 'columns': len(xs), 'rows': len(ys), 'cell_pt': side,
            'column_labels': [l for _, l in col_labels], 'row_labels': [l for _, l in row_labels]}


def main():
    result = {}
    for band in BANDS:
        path = os.path.join(PKT, f'week-07-{band}.pdf')
        doc = pymupdf.open(path)
        print(f'== {band}: {os.path.relpath(path, ROOT)} ({doc.page_count} pages)')
        bandres = []
        for pno in range(doc.page_count):
            page = doc[pno]
            words, heads, problem_at, circles, squares, thick = page_data(page)
            pd = {'page': pno + 1, 'problems': [n for _, n in heads]}
            pd['counter_rows'] = group_circles(circles, problem_at)
            pd['choice_rows'] = choice_labels(page, problem_at)
            pd['tracks'] = tracks(words, squares, thick, problem_at)
            c = chart(words, squares)
            if c:
                pd['chart'] = c
            # header and footer lines
            lines = page.get_text('text').strip().splitlines()
            pd['header'] = lines[0] if lines else ''
            pd['footer'] = ' '.join(lines[-2:]) if len(lines) >= 2 else ''
            bandres.append(pd)
            print(f'-- page {pno + 1}: problems {pd["problems"]}')
            print(f'   header: {pd["header"]!r}; footer: {pd["footer"]!r}')
            for r in pd['counter_rows']:
                print(f'   P{r["problem"]} counter row y={r["y"]}: piles {r["piles"]} (diameter {r["diameter_pt"]})')
            for r in pd['choice_rows']:
                print(f'   P{r["problem"]} choice labels y={r["y"]}: {r["labels"]}')
            for t in pd['tracks']:
                print(f'   P{t["problem"]} track {t["numbers"]} complete={t["complete"]} square={t["square_in"]} in '
                      f'{t["square_pt"]} pt; consecutive problems={t["consecutive_problems"]}; '
                      f'open non-consecutive neighbours={t["open_nonconsecutive_neighbours"]}; '
                      f'walled non-consecutive pairs={t["walled_nonconsecutive_pairs"]}')
            if 'chart' in pd:
                print(f'   chart: {pd["chart"]}')
        result[band] = bandres
    with open(os.path.join(HERE, 'pdf_geometry.json'), 'w') as f:
        json.dump(result, f, indent=1)


if __name__ == '__main__':
    main()
