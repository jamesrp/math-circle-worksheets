"""Confirm the editable TeX sources say what the delivered base PDFs show.

Reads lowell-math-circle-year-2/source/week-47/editable/src/<band>.tex
(plain text parsing only; nothing is executed or imported) and compares, page
by page, with pdf_geometry.json from pdf_extract.py:
  * every problem statement;
  * every board: number of sites, top level, site/level pitch, clue discs
    (site, level, printed number), the star's site, shaded marks;
  * every box row: printed values and shaded (fixed) boxes.
Also compares the bonus builder's literal data (student/build.py) with the
bonus extraction. Writes compare_source.out.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, SRC, BONUS_SRC, Log  # noqa: E402

log = Log('Week 47: editable sources vs delivered PDFs')
G = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))
NUM = r'(-?[\d.]+)'


def tex_pages(band):
    tex = open(os.path.join(SRC, 'editable', 'src', band + '.tex')).read()
    return tex.split('\\begin{document}', 1)[1].split('\\newpage')


def strip_tex(s):
    s = s.replace('--', '–').replace('\\textbf{', '').replace('}', '').replace('{', '')
    return re.sub(r'\s+', ' ', s).strip()


def parse_page(src):
    vlines, hlines = [], []
    for m in re.finditer(r'\\draw\[gray!45\] \(' + NUM + ',' + NUM + r'\) -- \(' + NUM + ',' + NUM + r'\);', src):
        x, y, X, Y = map(float, m.groups())
        (vlines if x == X else hlines).append((x, y, X, Y))
    boards = {}
    for x, y, X, Y in vlines:
        boards.setdefault((y, Y), []).append(x)
    out_boards = []
    for (ytop, ybot), xs in sorted(boards.items()):
        xs = sorted(xs)
        levels = sorted({y for (a, y, b, Y) in hlines if ytop <= y <= ybot and a < xs[0] and b > xs[-1]}, reverse=True)
        clues = {}
        for m in re.finditer(r'\\draw\[fill=black\] \(' + NUM + ',' + NUM + r'\) circle \(5\);\s*\\node[^\n]*\{\\color\{white\}(\d+)\}', src):
            cx, cy, v = float(m.group(1)), float(m.group(2)), int(m.group(3))
            if cx in xs and cy in levels:
                clues[str(xs.index(cx))] = (levels.index(cy), v)
        shaded = {}
        for m in re.finditer(r'\\draw\[fill=gray!45\] \(' + NUM + ',' + NUM + r'\) circle \(3\);', src):
            cx, cy = float(m.group(1)), float(m.group(2))
            if cx in xs and cy in levels:
                shaded.setdefault(str(xs.index(cx)), []).append(levels.index(cy))
        star = None
        m = re.search(r'at \(' + NUM + ',' + NUM + r'\) \{\$\\star\$\}', src)
        if m and float(m.group(1)) in xs:
            star = xs.index(float(m.group(1)))
        out_boards.append(dict(sites=len(xs), top=len(levels) - 1, dx=sorted({round(b - a, 3) for a, b in zip(xs, xs[1:])}),
                               dy=sorted({round(a - b, 3) for a, b in zip(levels, levels[1:])}),
                               clues={k: v[0] for k, v in clues.items()}, clue_text_ok=all(a == b for a, b in clues.values()),
                               shaded={k: sorted(v) for k, v in shaded.items()}, star=star))
    rows = {}
    for m in re.finditer(r'\\draw\[rounded corners=1mm(,fill=gray!20)?\] \(' + NUM + ',' + NUM + r'\) rectangle \+\+\(' + NUM + r',12\);\s*\\node[^\n]*at \(' + NUM + ',' + NUM + r'\) \{([^}]*)\};', src):
        fill, x, y, w = m.group(1), float(m.group(2)), float(m.group(3)), float(m.group(4))
        rows.setdefault(y, []).append((x, m.group(7) or None, bool(fill)))
    out_rows = []
    for y, items in sorted(rows.items()):
        items.sort()
        out_rows.append(dict(values=[v for _, v, _ in items], locked=[f for _, _, f in items]))
    probs = [strip_tex(m.group(1)) for m in re.finditer(r'\\textbf\{Problem \d+:\} ([^\n]*?)\};', src)]
    nums = [int(n) for n in re.findall(r'\\textbf\{Problem (\d+):\}', src)]
    return out_boards, out_rows, list(zip(nums, probs))


for band in ('k-1', 'grades-2-3', 'grades-4-5'):
    log.section(band)
    pages = tex_pages(band)
    log.check(len(pages) == len(G[band]['pages']), '%s: %d TeX pages = %d PDF pages' % (band, len(pages), len(G[band]['pages'])))
    for src, pg, txt in zip(pages, G[band]['pages'], G[band]['text']):
        tb, tr, tp = parse_page(src)
        flat = re.sub(r'\s+', ' ', txt).replace('- ', '-')
        for n, p in tp:
            words = p.split()
            ok = all(w.replace('–', '-') in flat.replace('–', '-') or w.rstrip('.,;?') in flat for w in words)
            log.check(ok and n in pg['problems'], '%s p%d: Problem %d statement in the TeX appears in the PDF ("%s...")' % (band, pg['page'], n, p[:50]))
        pb = [b for b in pg['boards'] if b['problem'] is not None]
        tb = [b for b in tb if b['sites'] >= 5]
        log.check(len(tb) == len(pb), '%s p%d: %d task boards in TeX and PDF' % (band, pg['page'], len(pb)))
        for a, b in zip(tb, pb):
            same = (a['sites'] == b['sites'] and a['top'] == b['top_level'] and a['clues'] == b['clues'] and a['clue_text_ok']
                    and a['shaded'] == b['shaded'] and a['star'] == b['star_site']
                    and a['dx'] == sorted({round(d, 0) for d in b['dx_mm']}) and a['dy'] == sorted({round(d, 0) for d in b['dy_mm']}))
            log.check(same, '%s p%d P%s board: TeX %s == PDF' % (band, pg['page'], b['problem'], {k: a[k] for k in ('sites', 'top', 'dx', 'dy', 'clues', 'shaded', 'star')}))
        for a, b in zip(tr, pg['rows']):
            log.check(a['values'] == b['values'] and a['locked'] == b['locked'], '%s p%d P%s row: TeX %s fixed %s == PDF' % (band, pg['page'], b['problem'], a['values'], a['locked']))
        log.check(len(tr) == len(pg['rows']), '%s p%d: %d box rows in TeX and PDF' % (band, pg['page'], len(tr)))

log.section('bonus builder literals vs PDF')
b = open(os.path.join(BONUS_SRC, 'student', 'build.py')).read()
B = G['bonus']
log.check("{0:0,3:3}" in b and "{0:0,3:2}" in b and "cycle(c,167,281,5" in b and "cycle(c,446,281,5" in b,
          'build.py: row A=0,D=3; rings of 5 with clues A=0,D=3 and A=0,D=2')
log.check("[(575,'Start',[1,2,3,2,1,0,1]),(483,'Finish',[1,0,1,2,3,2,1])]" in b, 'build.py: Start 1,2,3,2,1,0,1 and Finish 1,0,1,2,3,2,1')
log.check([r['values'] for r in B[1]['start_finish']] == [list('1232101'), list('1012321')], 'PDF start/finish rows agree')
log.check("cycle(c,306,447,6,r=141,clues={0:1,3:1}" in b and "(2,5,8,10,11)" in b, 'build.py: six-ring with A=1, D=1; budgets 2,5,8,10,11')
log.dump(os.path.join(HERE, 'compare_source.out'))
