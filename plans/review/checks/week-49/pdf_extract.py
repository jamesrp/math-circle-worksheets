"""Read every ring, mat and table of the delivered Week 49 student PDFs.

For the three base bands (TikZ) a ring is found from its arrows: each filled
arrowhead is matched to the line whose end it sits on, each end of that line
to the nearest station (a white circle or a white rounded square), and rings
are the connected groups of stations.  Printed numbers inside a station are its
height; a lone letter A-D next to a station is its label; a lone number next
to an arrow's midpoint is a printed gap.  Each ring is assigned to the last
"Problem N:" heading above it on its page ("intro" before Problem 1).

For the bonus packet (ReportLab) the cycles are white squares joined centre to
centre by plain lines; the worked-example rows are white circles in a line.

Output: pdf_geometry.json (used by check_base.py and check_bonus.py) and
pdf_extract.out (a readable listing).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, PDFS, PT_MM, Log, classify, dist, inside, npages, shapes, words)  # noqa: E402

log = Log('Week 49: geometry and printed data read from the delivered PDFs')


def headings(ws):
    hs = []
    for i, w in enumerate(ws):
        if w['t'] == 'Problem' and i + 1 < len(ws) and ws[i + 1]['t'].rstrip(':').isdigit():
            hs.append((w['y0'], int(ws[i + 1]['t'].rstrip(':'))))
    return sorted(hs)


def which_problem(hs, y):
    p = 'intro'
    for hy, n in hs:
        if hy < y:
            p = n
    return p


def find(par, i):
    while par[i] != i:
        par[i] = par[par[i]]
        i = par[i]
    return i


def base_page(pdf, page):
    shs = shapes(pdf, page)
    ws = words(pdf, page)
    stations, lines, heads = classify(shs)
    hs = headings(ws)
    # arrows
    arrows = []
    for hd in heads:
        best = None
        for ln in lines:
            for k in (0, 1):
                dd = dist(ln['pts'][k], hd['tip'])
                if dd < 3.5 and (best is None or dd < best[0]):
                    best = (dd, ln, k)
        if best is None:
            continue
        _, ln, k = best
        tip = ln['pts'][k]
        tail = ln['pts'][1 - k]
        arrows.append({'tail': tail, 'tip': tip})

    def nearest_station(p):
        best = None
        for j, st in enumerate(stations):
            half = max(st['w'], st['h']) / 2
            dd = dist(p, (st['cx'], st['cy']))
            if dd < 1.35 * half + 4 and (best is None or dd < best[0]):
                best = (dd, j)
        return None if best is None else best[1]

    edges = []
    loose = []
    for a in arrows:
        u = nearest_station(a['tail'])
        v = nearest_station(a['tip'])
        if u is None or v is None or u == v:
            loose.append(a)
            continue
        edges.append((u, v, a))
    par = list(range(len(stations)))
    for u, v, _ in edges:
        par[find(par, u)] = find(par, v)
    used = set()
    # values inside stations
    for j, st in enumerate(stations):
        inn = [w for w in ws if inside(w, st)]
        st['value'] = ' '.join(w['t'] for w in sorted(inn, key=lambda w: w['cx'])) or None
        for w in inn:
            used.add(id(w))
    # letters
    for st in stations:
        st['letter'] = None
    for w in ws:
        if id(w) in used or w['t'] not in ('A', 'B', 'C', 'D'):
            continue
        best = None
        for j, st in enumerate(stations):
            half = max(st['w'], st['h']) / 2
            dd = dist((w['cx'], w['cy']), (st['cx'], st['cy']))
            if dd < half + 6 / PT_MM and (best is None or dd < best[0]):
                best = (dd, j)
        if best:
            j = best[1]
            if stations[j]['letter'] is not None:
                raise SystemExit(f'two letters near one station on {pdf} p{page}')
            stations[j]['letter'] = w['t']
            used.add(id(w))
    # printed gaps near arrow midpoints
    gaps = []
    for w in ws:
        if id(w) in used or not w['t'].isdigit():
            continue
        best = None
        for (u, v, a) in edges:
            mid = ((a['tail'][0] + a['tip'][0]) / 2, (a['tail'][1] + a['tip'][1]) / 2)
            dd = dist(mid, (w['cx'], w['cy']))
            if dd < 26 and (best is None or dd < best[0]):
                best = (dd, u, v)
        if best:
            gaps.append({'value': int(w['t']), 'tail': best[1], 'head': best[2]})
            used.add(id(w))
    rings = {}
    for j in range(len(stations)):
        rings.setdefault(find(par, j), []).append(j)
    out = []
    for root, members in rings.items():
        if len(members) < 3:
            continue
        succ = {}
        for u, v, a in edges:
            if u in members:
                if u in succ:
                    raise SystemExit('station with two outgoing arrows')
                succ[u] = v
        ok_cycle = len(succ) == len(members)
        # order: start at A if labelled, else at the top-left station
        lab = {stations[j]['letter']: j for j in members if stations[j]['letter']}
        if 'A' in lab:
            start = lab['A']
        else:
            start = min(members, key=lambda j: (round(stations[j]['cy']), stations[j]['cx']))
        order = [start]
        while ok_cycle and succ[order[-1]] != start and len(order) <= len(members):
            order.append(succ[order[-1]])
        ok_cycle = ok_cycle and len(order) == len(members)
        top = min(stations[j]['y0'] for j in members)
        st_list = []
        for j in order:
            st = stations[j]
            st_list.append({'letter': st['letter'], 'value': st['value'], 'kind': st['kind'],
                            'cx_mm': round(st['cx'] * PT_MM, 2), 'cy_mm': round(st['cy'] * PT_MM, 2),
                            'w_mm': round(st['w'] * PT_MM, 2), 'h_mm': round(st['h'] * PT_MM, 2)})
        ring_gaps = []
        for g in gaps:
            if g['tail'] in members:
                ring_gaps.append({'tail_pos': order.index(g['tail']), 'head_pos': order.index(g['head']),
                                  'value': g['value']})
        out.append({'problem': which_problem(hs, top), 'top_mm': round(top * PT_MM, 1),
                    'arrow_cycle': ok_cycle, 'stations': st_list, 'gaps': ring_gaps})
    out.sort(key=lambda r: (r['top_mm'], r['stations'][0]['cx_mm']))
    return {'rings': out, 'loose_arrows': len(loose), 'headings': [n for _, n in hs]}


def bonus_page(pdf, page):
    shs = shapes(pdf, page)
    ws = words(pdf, page)
    stations = [s for s in shs if s['fill'] == 'rgb(100%, 100%, 100%)' and ('Z' in s['cmds'] or set(s['cmds']) <= set('MC'))
                and s['w'] > 15]
    for st in stations:
        st['kind'] = 'circle' if 'C' in st['cmds'] else 'square'
    tables = [s for s in shs if s['fill'] == 'none' and s['cmds'].startswith('MLLL') and 'Z' in s['cmds']]
    lines = [s for s in shs if s['fill'] == 'none' and s['cmds'] == 'ML']
    hs = headings(ws)
    par = list(range(len(stations)))
    for ln in lines:
        ends = []
        for p in ln['pts']:
            js = [j for j, st in enumerate(stations) if dist(p, (st['cx'], st['cy'])) < 2]
            ends.append(js[0] if js else None)
        if None not in ends:
            par[find(par, ends[0])] = find(par, ends[1])
    circles = [j for j, st in enumerate(stations) if st['kind'] == 'circle']
    for a in circles:
        for b in circles:
            if a < b and abs(stations[a]['cy'] - stations[b]['cy']) < 1 and abs(stations[a]['cx'] - stations[b]['cx']) < 60:
                par[find(par, a)] = find(par, b)
    used = set()
    for st in stations:
        inn = [w for w in ws if inside(w, st)]
        st['value'] = ' '.join(w['t'] for w in inn) or None
        used.update(id(w) for w in inn)
        st['label'] = None
    # table areas (exclude headers and row indices)
    tb = None
    if tables:
        tb = (min(t['x0'] for t in tables), min(t['y0'] for t in tables),
              max(t['x1'] for t in tables), max(t['y1'] for t in tables))
    for w in ws:
        if id(w) in used or len(w['t']) > 2:
            continue
        if tb and tb[0] - 20 <= w['cx'] <= tb[2] and tb[1] - 20 <= w['cy'] <= tb[3]:
            continue
        best = None
        for j, st in enumerate(stations):
            dd = dist((w['cx'], w['cy']), (st['cx'], st['cy']))
            if dd < max(st['w'], st['h']) / 2 + 45 and (best is None or dd < best[0]):
                best = (dd, j)
        if best:
            if stations[best[1]]['label'] is not None:
                raise SystemExit('two labels for one bonus station')
            stations[best[1]]['label'] = w['t']
            used.add(id(w))
    groups = {}
    for j in range(len(stations)):
        groups.setdefault(find(par, j), []).append(j)
    out = []
    for members in groups.values():
        edges = set()
        for ln in lines:
            ends = []
            for p in ln['pts']:
                js = [j for j in members if dist(p, (stations[j]['cx'], stations[j]['cy'])) < 2]
                ends.append(js[0] if js else None)
            if None not in ends:
                edges.add(frozenset((stations[ends[0]]['label'], stations[ends[1]]['label'])))
        top = min(stations[j]['y0'] for j in members)
        mem = sorted(members, key=lambda j: stations[j]['label'] or '')
        out.append({'problem': which_problem(hs, top), 'top_mm': round(top * PT_MM, 1),
                    'kind': stations[members[0]]['kind'],
                    'stations': [{'label': stations[j]['label'], 'value': stations[j]['value'],
                                  'cx_mm': round(stations[j]['cx'] * PT_MM, 2), 'cy_mm': round(stations[j]['cy'] * PT_MM, 2),
                                  'w_mm': round(stations[j]['w'] * PT_MM, 2), 'h_mm': round(stations[j]['h'] * PT_MM, 2)}
                                 for j in mem],
                    'edges': sorted(sorted(e) for e in edges)})
    out.sort(key=lambda r: (r['top_mm'], min(s['cx_mm'] for s in r['stations'])))
    return {'groups': out, 'table_boxes': len(tables)}


G = {}
for band in ('K-1', '2-3', '4-5'):
    G[band] = {'pages': []}
    log.p(f'\n## {band}  ({PDFS[band].split("/")[-1]}, {npages(PDFS[band])} pages)')
    for page in range(1, npages(PDFS[band]) + 1):
        res = base_page(PDFS[band], page)
        G[band]['pages'].append(res)
        log.p(f'-- page {page}: headings {res["headings"]}, loose arrows (not between stations) {res["loose_arrows"]}')
        for r in res['rings']:
            vals = [s['value'] for s in r['stations']]
            labs = ''.join(s['letter'] or '?' for s in r['stations'])
            kind = r['stations'][0]['kind']
            size = r['stations'][0]['w_mm']
            gaps = ' gaps ' + str([(g['tail_pos'], g['head_pos'], g['value']) for g in r['gaps']]) if r['gaps'] else ''
            log.p(f'   P{r["problem"]}: {len(vals)} {kind}s {size} mm, arrow order {labs}, '
                  f'arrows form one cycle: {r["arrow_cycle"]}, values {vals}{gaps}')

G['bonus'] = {'pages': []}
log.p(f'\n## bonus ({npages(PDFS["bonus"])} pages)')
for page in range(1, npages(PDFS['bonus']) + 1):
    res = bonus_page(PDFS['bonus'], page)
    G['bonus']['pages'].append(res)
    log.p(f'-- page {page}: record-table boxes {res["table_boxes"]}')
    for g in res['groups']:
        log.p(f'   P{g["problem"]}: {len(g["stations"])} {g["kind"]}s '
              f'{g["stations"][0]["w_mm"]} mm, labels/values '
              f'{[(s["label"], s["value"]) for s in g["stations"]]}, edges {g["edges"]}')

json.dump(G, open(os.path.join(HERE, 'pdf_geometry.json'), 'w'), indent=1)
log.finish()
