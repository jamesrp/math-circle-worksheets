"""Read every diagram of the delivered Week 47 PDFs (base bands and bonus).

Writes pdf_geometry.json (the data check_base.py / check_bonus.py use) and
pdf_extract.out (the checks below plus a readable transcription).

Base bands (k-1, grades-2-3, grades-4-5), from the vector layer:
  * marker boards: grey grid columns/levels, axis labels, black clue discs
    (with the printed number inside), the star, shaded allowed-height discs;
  * box rows: rounded boxes, shaded (fixed) or white, printed values, site labels;
  * tower pictures (stacked squares) and the launch's marker strip and boxed row;
  * which "Problem N:" header each object sits under.
Bonus: squares, joining edges, letters, printed clue values, the marker board.
"""
import hashlib
import json
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, PDFS, REFS, PT_MM, Log, page_count, page_text, shapes, words)  # noqa: E402

log = Log('Week 47 PDF extraction (delivered PDFs, read with pdftocairo/pdftotext)')

GREY_LINE = (0.775, 0.775, 0.775)


def close(a, b, tol=0.6):
    return abs(a - b) <= tol


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def problem_headers(ws):
    """[(n, y)] for every 'Problem N:' on the page, top to bottom."""
    out = []
    for i, w in enumerate(ws):
        if w['s'] == 'Problem' and i + 1 < len(ws):
            m = re.match(r'(\d+):$', ws[i + 1]['s'])
            if m:
                out.append((int(m.group(1)), w['cy']))
    return out


def owner(headers, y):
    """Problem number whose header is the nearest one above y (None = before Problem 1)."""
    best = None
    for n, hy in headers:
        if hy < y:
            best = n
    return best


def word_at(ws, x, y, tol):
    c = [w for w in ws if abs(w['cx'] - x) <= tol and abs(w['cy'] - y) <= tol]
    return c


def extract_base_page(pdf, page):
    sh = shapes(pdf, page)
    ws = words(pdf, page)
    heads = problem_headers(ws)
    res = dict(page=page, problems=[n for n, _ in heads], boards=[], rows=[], hills=[], launch=None)

    # ---- marker boards: grey vertical lines grouped by vertical span
    vlines = [s for s in sh if s['kind'] == 'line' and s['stroke'] == GREY_LINE and close(s['bbox'][0], s['bbox'][2], 0.01)]
    hlines = [s for s in sh if s['kind'] == 'line' and s['stroke'] == GREY_LINE and close(s['bbox'][1], s['bbox'][3], 0.01)]
    groups = {}
    for v in vlines:
        key = (round(v['bbox'][1], 1), round(v['bbox'][3], 1))
        groups.setdefault(key, []).append(v['bbox'][0])
    for (ytop, ybot), xs in sorted(groups.items()):
        xs = sorted(xs)
        levels = sorted({round(h['bbox'][1], 3) for h in hlines
                         if ytop - 0.5 <= h['bbox'][1] <= ybot + 0.5 and h['bbox'][0] < xs[0] and h['bbox'][2] > xs[-1]},
                        reverse=True)  # bottom (level 0) first
        dx = [b - a for a, b in zip(xs, xs[1:])]
        dy = [a - b for a, b in zip(levels, levels[1:])]
        # level labels left of the board, site labels below it
        lev_labels = []
        for y in levels:
            c = [w for w in ws if w['x1'] < xs[0] and abs(w['cy'] - y) < 3 and xs[0] - w['x1'] < 40]
            lev_labels.append(c[0]['s'] if c else None)
        site_labels = []
        for x in xs:
            c = [w for w in ws if abs(w['cx'] - x) < 3 and 10 < w['cy'] - levels[0] < 40]
            site_labels.append(c[0]['s'] if c else None)
        circles = [s for s in sh if s['kind'] == 'circle' and xs[0] - 1 <= s['cx'] <= xs[-1] + 1 and levels[-1] - 1 <= s['cy'] <= levels[0] + 1]

        def site_level(s):
            i = min(range(len(xs)), key=lambda k: abs(xs[k] - s['cx']))
            j = min(range(len(levels)), key=lambda k: abs(levels[k] - s['cy']))
            return i, j, abs(xs[i] - s['cx']) + abs(levels[j] - s['cy'])

        grid_pts = set()
        clues = {}
        clue_text_ok = True
        shaded = {}
        offgrid = 0
        other_circles = []
        for s in circles:
            i, j, err = site_level(s)
            r_mm = s['w'] / 2 * PT_MM
            if err > 0.2:
                offgrid += 1
            if close(r_mm, 0.8, 0.05) and s['fill'] == (1.0, 1.0, 1.0):
                grid_pts.add((i, j))
            elif close(r_mm, 5.0, 0.1) and s['fill'] == (0.0, 0.0, 0.0):
                txt = word_at(ws, s['cx'], s['cy'], 6)
                val = txt[0]['s'] if txt else None
                if val is None or int(val) != int(lev_labels[j]):
                    clue_text_ok = False
                clues[i] = dict(level=j, printed=val)
            elif close(r_mm, 3.0, 0.1):
                shaded.setdefault(i, []).append(j)
            else:
                other_circles.append((round(r_mm, 2), s['fill']))
        star = [w for w in ws if w['s'] == '⋆' and xs[0] - 3 <= w['cx'] <= xs[-1] + 3 and w['cy'] < levels[-1]]
        star_site = None
        star_err = None
        if star:
            star_site = min(range(len(xs)), key=lambda k: abs(xs[k] - star[0]['cx']))
            star_err = abs(xs[star_site] - star[0]['cx'])
        res['boards'].append(dict(
            problem=owner(heads, levels[-1]), x_pt=[round(x, 3) for x in xs], level_y_pt=[round(y, 3) for y in levels],
            sites=len(xs), top_level=len(levels) - 1,
            dx_mm=[round(d * PT_MM, 3) for d in dx], dy_mm=[round(d * PT_MM, 3) for d in dy],
            level_labels=lev_labels, site_labels=site_labels,
            grid_points=len(grid_pts), grid_complete=len(grid_pts) == len(xs) * len(levels),
            clues={str(i): v['level'] for i, v in sorted(clues.items())},
            clue_printed={str(i): v['printed'] for i, v in sorted(clues.items())},
            clue_text_matches_level=clue_text_ok,
            shaded={str(i): sorted(v) for i, v in sorted(shaded.items())},
            star_site=star_site, star_offset_pt=None if star_err is None else round(star_err, 3),
            offgrid_circles=offgrid, other_circles=other_circles))

    # ---- box rows: rounded rectangles grouped by top y
    rr = [s for s in sh if s['kind'] == 'rrect']
    rowsets = {}
    for s in rr:
        rowsets.setdefault(round(s['bbox'][1], 1), []).append(s)
    for y, boxes in sorted(rowsets.items()):
        boxes.sort(key=lambda s: s['cx'])
        vals, locked, labels = [], [], []
        for s in boxes:
            inside = [w for w in ws if s['bbox'][0] < w['cx'] < s['bbox'][2] and s['bbox'][1] < w['cy'] < s['bbox'][3]]
            vals.append(inside[0]['s'] if inside else None)
            locked.append(s['fill'] is not None and s['fill'] != (1.0, 1.0, 1.0) and s['fill'] != 'none')
            below = [w for w in ws if abs(w['cx'] - s['cx']) < 3 and 0 < w['cy'] - s['bbox'][3] < 20]
            labels.append(below[0]['s'] if below else None)
        pitch = [b['cx'] - a['cx'] for a, b in zip(boxes, boxes[1:])]
        res['rows'].append(dict(problem=owner(heads, y), top_pt=y, values=vals, locked=locked, site_labels=labels,
                                box_w_mm=round(boxes[0]['w'] * PT_MM, 2), box_h_mm=round(boxes[0]['h'] * PT_MM, 2),
                                pitch_mm=[round(p * PT_MM, 2) for p in pitch]))

    # ---- tower pictures: small filled squares (6 mm) stacked in columns
    sq = [s for s in sh if s['kind'] == 'rect' and close(s['w'] * PT_MM, 6, 0.1) and close(s['h'] * PT_MM, 6, 0.1)]
    pics = {}
    for s in sq:
        pics.setdefault(round(s['bbox'][3], 0), []).append(s)  # not used for grouping heights
    # group by picture: squares whose x ranges are within 30 mm of each other and share a base line
    cols = {}
    for s in sq:
        cols.setdefault(round(s['cx'], 1), []).append(s)
    colinfo = []
    for x, ss in sorted(cols.items()):
        base = max(t['bbox'][3] for t in ss)
        colinfo.append((x, base, len(ss)))
    # split into pictures by gaps > 15 pt or different base
    pic = []
    for x, base, h in colinfo:
        if pic and (x - pic[-1][-1][0] < 30 and close(base, pic[-1][-1][1], 1)):
            pic[-1].append((x, base, h))
        else:
            pic.append([(x, base, h)])
    for p in pic:
        labels = []
        for x, base, h in p:
            c = [w for w in ws if abs(w['cx'] - x) < 3 and 0 < w['cy'] - base < 15]
            labels.append(c[0]['s'] if c else None)
        caption = [w['s'] for w in ws if p[0][0] - 20 < w['cx'] < p[-1][0] + 40 and 15 < w['cy'] - p[0][1] < 30]
        res['hills'].append(dict(problem=owner(heads, p[0][1]), heights=[h for _, _, h in p], labels=labels,
                                 caption=' '.join(caption)))

    # ---- launch marker strip: medium white circles r=2.1 mm with thick stroke
    mc = sorted([s for s in sh if s['kind'] == 'circle' and close(s['w'] / 2 * PT_MM, 2.1, 0.1)], key=lambda s: s['cx'])
    if mc:
        ys = sorted({round(h['bbox'][1], 2) for h in hlines if h['bbox'][1] < 250}, reverse=True)
        lev = []
        for s in mc:
            j = min(range(len(ys)), key=lambda k: abs(ys[k] - s['cy']))
            lev.append(j)
        # boxed row: one 44 x 12 mm rectangle with numbers inside
        box = [s for s in sh if s['kind'] == 'rect' and close(s['w'] * PT_MM, 44, 0.2) and close(s['h'] * PT_MM, 12, 0.2)]
        boxed = []
        if box:
            b = box[0]
            boxed = [w['s'] for w in sorted(ws, key=lambda w: w['cx']) if b['bbox'][0] < w['cx'] < b['bbox'][2] and b['bbox'][1] < w['cy'] < b['bbox'][3]]
        res['launch'] = dict(marker_levels=lev, n_levels=len(ys), boxed_row=boxed)
    return res


def base():
    data = {}
    for band in ('k-1', 'grades-2-3', 'grades-4-5'):
        pdf = PDFS[band]
        n = page_count(pdf)
        data[band] = dict(pages=[extract_base_page(pdf, p) for p in range(1, n + 1)])
        data[band]['text'] = [page_text(pdf, p) for p in range(1, n + 1)]
    return data


# ---------------------------------------------------------------- bonus

def extract_bonus():
    pdf = PDFS['bonus']
    out = []
    for p in range(1, page_count(pdf) + 1):
        sh = shapes(pdf, p)
        ws = words(pdf, p)
        heads = problem_headers(ws)
        squares = [s for s in sh if s['kind'] == 'rect' and close(s['w'], s['h'], 0.01) and s['w'] > 40
                   and s['stroke'] == (0.133, 0.169, 0.2)]
        edges_raw = [s for s in sh if s['kind'] == 'line' and s['stroke'] == (0.133, 0.169, 0.2)
                     and s['bbox'][1] > 60 and not close(s['bbox'][1], 49, 1)]
        letters = [w for w in ws if re.fullmatch(r'[A-G]', w['s'])]
        graph_nodes = []
        for s in squares:
            vals = [w['s'] for w in ws if s['bbox'][0] < w['cx'] < s['bbox'][2] and s['bbox'][1] < w['cy'] < s['bbox'][3]]
            graph_nodes.append(dict(cx=s['cx'], cy=s['cy'], side_mm=round(s['w'] * PT_MM, 2),
                                    clue=(s['fill'] != (1.0, 1.0, 1.0)), value=vals[0] if vals else None))
        # nearest letter to each node
        for nd in graph_nodes:
            best = min(letters, key=lambda w: math.hypot(w['cx'] - nd['cx'], w['cy'] - nd['cy']))
            dists = sorted(math.hypot(w['cx'] - nd['cx'], w['cy'] - nd['cy']) for w in letters)
            nd['letter'] = best['s']
            nd['letter_dist_pt'] = round(dists[0], 1)
            nd['runner_up_pt'] = round(dists[1], 1) if len(dists) > 1 else None
        # edges: a line whose two endpoints each lie at a node centre
        edge_list = []
        for e in edges_raw:
            (x0, y0), (x1, y1) = e['pts'][0], e['pts'][1]
            a = [k for k, nd in enumerate(graph_nodes) if math.hypot(nd['cx'] - x0, nd['cy'] - y0) < 1]
            b = [k for k, nd in enumerate(graph_nodes) if math.hypot(nd['cx'] - x1, nd['cy'] - y1) < 1]
            if a and b:
                edge_list.append((a[0], b[0]))
        # marker board (page 2): light grey grid lines
        light = (0.835, 0.855, 0.867)
        gv = sorted({round(s['bbox'][0], 2) for s in sh if s['kind'] == 'line' and s['stroke'] == light and close(s['bbox'][0], s['bbox'][2], 0.01)})
        gh = sorted({round(s['bbox'][1], 2) for s in sh if s['kind'] == 'line' and s['stroke'] == light and close(s['bbox'][1], s['bbox'][3], 0.01)
                     and s['w'] < 500}, reverse=True)
        board = None
        if len(gv) >= 3 and len(gh) >= 3:
            dots = [s for s in sh if s['kind'] == 'circle' and s['fill'] == (0.133, 0.169, 0.2)]
            dot_pos = []
            for d in dots:
                i = min(range(len(gv)), key=lambda k: abs(gv[k] - d['cx']))
                j = min(range(len(gh)), key=lambda k: abs(gh[k] - d['cy']))
                dot_pos.append((i, j, round(abs(gv[i] - d['cx']) + abs(gh[j] - d['cy']), 3)))
            col_labels = [min((w for w in ws if abs(w['cx'] - x) < 3 and w['cy'] > gh[0]), key=lambda w: w['cy'])['s'] for x in gv]
            board = dict(columns=len(gv), levels=len(gh), col_labels=col_labels,
                         dx_mm=sorted({round((b - a) * PT_MM, 2) for a, b in zip(gv, gv[1:])}),
                         dy_mm=sorted({round((a - b) * PT_MM, 2) for a, b in zip(gh, gh[1:])}),
                         dots=dot_pos)
        # start/finish boxes on page 2 (squares 48 x 46 pt; not equal sides)
        sf = [s for s in sh if s['kind'] == 'rect' and close(s['w'], 48, 0.1) and close(s['h'], 46, 0.1)]
        sfrows = {}
        for s in sf:
            vals = [w['s'] for w in ws if s['bbox'][0] < w['cx'] < s['bbox'][2] and s['bbox'][1] < w['cy'] < s['bbox'][3]]
            sfrows.setdefault(round(s['cy'], 0), []).append((s['cx'], vals[0] if vals else None, s['fill'] != (1.0, 1.0, 1.0)))
        rows = []
        for y, items in sorted(sfrows.items()):
            items.sort()
            title = [w['s'] for w in ws if w['x1'] < items[0][0] - 20 and abs(w['cy'] - y) < 15]
            rows.append(dict(title=' '.join(title), values=[v for _, v, _ in items], fixed=[f for _, _, f in items]))
        # budget slots (page 3)
        budget = [w['s'] for w in sorted(ws, key=lambda w: w['cx']) if re.fullmatch(r'\d+', w['s']) and any(v['s'] == 'Budget' and abs(v['cy'] - w['cy']) < 4 for v in ws)]
        slots = [s for s in sh if s['kind'] == 'rect' and close(s['w'], 58, 0.1) and close(s['h'], 53, 0.1)]
        out.append(dict(page=p, problems=[n for n, _ in heads], nodes=graph_nodes, edges=edge_list,
                        board=board, start_finish=rows, budgets=budget, budget_slots=len(slots),
                        header=[w['s'] for w in ws if w['cy'] < 45],
                        text=page_text(pdf, p)))
    return out


def main():
    log.section('Delivered PDFs match the reference copies in the source folders')
    for k in PDFS:
        log.check(md5(PDFS[k]) == md5(REFS[k]), '%s: delivered MD5 == reference MD5 (%s)' % (k, md5(PDFS[k])))

    data = base()
    data['bonus'] = extract_bonus()
    with open(os.path.join(HERE, 'pdf_geometry.json'), 'w') as f:
        json.dump(data, f, indent=1)

    log.section('Base bands: transcription and structural checks')
    for band in ('k-1', 'grades-2-3', 'grades-4-5'):
        pages = data[band]['pages']
        probs = [n for p in pages for n in p['problems']]
        log.check(probs == list(range(1, len(probs) + 1)), '%s: problems numbered consecutively %s' % (band, probs))
        for p in pages:
            for b in p['boards']:
                if b['problem'] is None:
                    log.note('%s p%d launch board: %d sites x levels 0..%d, pitch %s / %s mm (checked as the launch strip below)' % (band, p['page'], b['sites'], b['top_level'], sorted(set(b['dx_mm'])), sorted(set(b['dy_mm']))))
                    continue
                log.note('%s p%d P%s board: %d sites x levels 0..%d, site pitch %s mm, level pitch %s mm, clues %s, star %s, shaded %s' % (
                    band, p['page'], b['problem'], b['sites'], b['top_level'], sorted(set(b['dx_mm'])), sorted(set(b['dy_mm'])),
                    b['clues'], b['star_site'], b['shaded']))
                log.check(b['grid_complete'], '%s p%d P%s: a grid point at every site and level (%d)' % (band, p['page'], b['problem'], b['grid_points']))
                log.check(b['level_labels'] == [str(j) for j in range(b['top_level'] + 1)], '%s p%d P%s: level labels 0..%d in order' % (band, p['page'], b['problem'], b['top_level']))
                log.check(b['site_labels'] == [str(i) for i in range(b['sites'])], '%s p%d P%s: site labels 0..%d in order' % (band, p['page'], b['problem'], b['sites'] - 1))
                log.check(b['clue_text_matches_level'], '%s p%d P%s: every clue disc prints the level it sits on %s' % (band, p['page'], b['problem'], b['clue_printed']))
                log.check(b['offgrid_circles'] == 0 and not b['other_circles'], '%s p%d P%s: every disc sits exactly on a grid point' % (band, p['page'], b['problem']))
                log.check(len(set(round(d, 1) for d in b['dx_mm'])) == 1 and len(set(round(d, 1) for d in b['dy_mm'])) == 1,
                          '%s p%d P%s: uniform spacing' % (band, p['page'], b['problem']))
                if b['star_site'] is not None:
                    log.check(b['star_offset_pt'] < 0.5, '%s p%d P%s: star centred over site %d (offset %.2f pt)' % (band, p['page'], b['problem'], b['star_site'], b['star_offset_pt']))
            for r in p['rows']:
                log.note('%s p%d P%s row: values %s fixed %s labels %s box %sx%s mm pitch %s' % (
                    band, p['page'], r['problem'], r['values'], r['locked'], r['site_labels'], r['box_w_mm'], r['box_h_mm'], sorted(set(r['pitch_mm']))))
                log.check(r['site_labels'] == [str(i) for i in range(len(r['values']))], '%s p%d P%s: row site labels 0..%d' % (band, p['page'], r['problem'], len(r['values']) - 1))
                log.check(all((v is not None) == l for v, l in zip(r['values'], r['locked'])) or band != 'k-1' or r['problem'] == 6,
                          '%s p%d P%s: printed values exactly in shaded boxes (P6 K-1 prints whole landscapes)' % (band, p['page'], r['problem']))
            for h in p['hills']:
                log.note('%s p%d P%s towers %s labels %s caption "%s"' % (band, p['page'], h['problem'], h['heights'], h['labels'], h['caption']))
                log.check(h['labels'] == [str(x) for x in h['heights']], '%s p%d: tower labels match stacked squares %s' % (band, p['page'], h['heights']))
            if p['launch']:
                L = p['launch']
                log.note('%s launch strip: marker levels %s on %d levels; boxed row %s' % (band, L['marker_levels'], L['n_levels'], L['boxed_row']))
                towers = [h for h in p['hills'] if h['problem'] is None]
                log.check(towers and towers[0]['heights'] == L['marker_levels'] == [int(v) for v in L['boxed_row']],
                          '%s launch: towers %s -> markers %s -> boxed row %s agree' % (band, towers[0]['heights'] if towers else None, L['marker_levels'], L['boxed_row']))
                log.check(all(abs(a - b) <= 1 for a, b in zip(L['marker_levels'], L['marker_levels'][1:])), '%s launch: the "allowed" example is legal' % band)
                bad = [h for h in p['hills'] if h['problem'] == 1]
                log.check(bad and any(abs(a - b) > 1 for a, b in zip(bad[0]['heights'], bad[0]['heights'][1:])), '%s launch: the "jump too big" example %s really has a jump > 1' % (band, bad[0]['heights'] if bad else None))

    log.section('Bonus: transcription')
    for p in data['bonus']:
        log.note('bonus p%d header %s problems %s' % (p['page'], ' '.join(p['header']), p['problems']))
        for nd in p['nodes']:
            log.note('  node %s clue=%s value=%s side %.2f mm at (%.1f, %.1f); letter %.1f pt away, next letter %.1f pt' % (
                nd['letter'], nd['clue'], nd['value'], nd['side_mm'], nd['cx'], nd['cy'], nd['letter_dist_pt'], nd['runner_up_pt'] or -1))
        if p['edges']:
            log.note('  edges %s' % ['%s%s' % (p['nodes'][a]['letter'], p['nodes'][b]['letter']) for a, b in p['edges']])
        if p['board']:
            log.note('  marker board %s' % p['board'])
        for r in p['start_finish']:
            log.note('  row %s' % r)
        if p['budgets']:
            log.note('  budgets %s, %d answer slots' % (p['budgets'], p['budget_slots']))
    probs = [n for p in data['bonus'] for n in p['problems']]
    log.check(probs == [1, 2, 3], 'bonus: problems numbered 1, 2, 3')
    log.dump(os.path.join(HERE, 'pdf_extract.out'))


if __name__ == '__main__':
    main()
