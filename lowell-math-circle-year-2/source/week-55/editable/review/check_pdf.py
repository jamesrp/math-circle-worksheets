#!/usr/bin/env python3
"""Read the Week 55 PDFs and check the October 23, 2026 card fixes on the printed pages.

    python3 check_pdf.py [FOLDER]   (FOLDER holds week-55-students.pdf and week-55-facilitator.pdf;
                                     default: the repository's print folder)

With PyMuPDF it checks the student packet's headers, footers and Problems 1-10; the new
input rule on p. 1 and Problem 10's new order; that on p. 8 no grey grid segment is
painted after a dot it touches, so no line crosses a number; and the guide's new
sentences and the removal of the replaced ones.
"""
import re
import subprocess
import sys
from pathlib import Path

try:
    import pymupdf as fitz
except ImportError:
    import fitz

HERE = Path(__file__).resolve().parent


def find_repo():
    for p in HERE.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    sys.exit('repository not found; pass the folder that holds the PDFs')


WEEK = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else find_repo() / 'lowell-math-circle-year-2' / 'week-55'
FAILS = []


def check(cond, msg):
    print(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def text(page):
    return ' '.join(re.sub(r'(?<=[a-z])-\n(?=[a-z])', '', page.get_text()).split())


doc = fitz.open(WEEK / 'week-55-students.pdf')
st = [text(p) for p in doc]
nums = []
for i, t in enumerate(st):
    check(t.startswith('Week 55 / Few sums and equal spacing / Grades 3–5') and f'Bellingham Math Circle / Week 55 / W55-S-v3 {i+1}' in t,
          f'students p{i+1}: header Grades 3–5, footer W55-S-v3, page {i+1}')
    nums += [int(n) for n in re.findall(r'Problem (\d+):', t)]
check(len(doc) == 10 and nums == list(range(1, 11)), f'students: 10 pages, Problems {nums}')
check('No number repeats within an input; A and B may share numbers.' in st[0] and 'Each input has different numbers' not in st[0],
      'p1: "No number repeats within an input; A and B may share numbers." (fix 2)')
p10 = st[9]
i_suff, i_nec = p10.find('Explain why two equally spaced inputs with the same gap give exactly'), p10.find('Must both be equally spaced, with the same gap?')
check(0 < i_suff < i_nec and 'Also explain' not in p10, 'P10: the easier converse comes first (fix 6)')

page = doc[7]
draws = page.get_drawings()
grey = [(k, d['rect']) for k, d in enumerate(draws) if d.get('color') and abs(d['color'][0] - 0.775) < 0.01 and d.get('fill') is None
        and all(it[0] == 'l' for it in d['items'])]
dots = [(k, d['rect']) for k, d in enumerate(draws) if d.get('fill') and min(d['fill']) > 0.99 and abs(d['rect'].width - 9 * 72 / 25.4) < 0.5]
late = [(k, j) for k, r in grey for j, c in dots if k > j and fitz.Rect(r.x0 - .5, r.y0 - .5, r.x1 + .5, r.y1 + .5).intersects(c)]  # a segment's own rect is flat
check(len(dots) == 27 and grey and not late, f'p8: {len(dots)} dots and {len(grey)} grey segments; no segment is painted over a dot it touches ({len(late)}) (could 3)')

g = ' '.join(subprocess.run(['pdftotext', str(WEEK / 'week-55-facilitator.pdf'), '-'], capture_output=True, text=True, check=True).stdout.split())
g = re.sub(r'(?<=[a-z])- (?=[a-z])', '', g)
check(fitz.open(WEEK / 'week-55-facilitator.pdf').page_count == 9 and max(g.count('W55-F-v2'), g.count('W55-F-v3')) == 9, 'guide: 9 pages, footer W55-F-v2 (v3 after the roster-label fix)')
for s in ['An adult-led route on student pages 1–3 uses dot cards', 'K–1 route, adult-led, on student pages 1–3', '28 dot cards and 40 more counters',
          'cards 0–6 showing the numeral and that many dots', '1, 3, 5 (three places; 2 + 1 and 0 + 3 both land on 3), then 1, 3, 4, 6 (four)',
          'choose three A cards and three B cards that land on as few places as you can', 'Five is the fewest',
          'two copies of pages 4–5, one per third-grade pair', '26 landscape sheets', 'the fewest is 7, and the most, 16, needs {0, 1, 8, 9} with four cards of gap 2',
          'gives 9 totals, the most possible', 'The student page now asks first why common-gap inputs give exactly m + n − 1 totals']:
    check(s in g, f'guide has "{s[:70]}"')
for s in ['24 blue rhombi', 'one selected K–1 board per child', 'Parent uses the prior tiling guide', 'For the separate K–1 tiling route',
          'No independent sumset packet']:
    check(s not in g, f'guide no longer has "{s}"')

print('PASS: Week 55 PDFs carry the card fixes' if not FAILS else f'FAIL: {len(FAILS)} checks failed')
raise SystemExit(1 if FAILS else 0)
