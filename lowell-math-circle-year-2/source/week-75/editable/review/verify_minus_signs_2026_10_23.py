#!/usr/bin/env python3
"""Check the Week 75 minus-sign fix of October 23, 2026 (GGT75-S-v4, GGT75-FAC-v4).

    python3 verify_minus_signs_2026_10_23.py [students.pdf] [guide.pdf] [old-students.pdf] [old-guide.pdf]

An independent critic noticed that page 2's lift boards labelled a dot "B, copy -1" with a
hyphen while page 3's strip printed "B, copy −4" with a true minus. Version 4 prints the
true minus on page 2 as well. The defaults are ../reference-pdfs/ and, for the previous
print copies (v3), the repository's week-75/archive-before-minus-signs-2026-10-23/.
Reads the PDFs' text and pixels with PyMuPDF.

  1. Every signed number on the student pages is written with U+2212, never a hyphen.
  2. Page 2's two lift boards read B, copy −1, 0, 1, 2 and page 3's strip B, copy −4 .. 4.
  3. Every student footer reads GGT75-S-v4; every guide footer reads GGT75-FAC-v4, and the
     guide's review status names GGT75-S-v4.
  4. Against v3: pages 1, 3 and 4 differ only in the footer (text, and 100-dpi pixels below
     the footer line); page 2's text differs only in the two labels and the footer; the guide's
     text differs only in its footer and status line.
"""
import re
import sys
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent
REF = HERE.parent / 'reference-pdfs'
OLD = HERE.parents[3] / 'week-75' / 'archive-before-minus-signs-2026-10-23'
arg = lambda i, default: Path(sys.argv[i]) if len(sys.argv) > i else default
S = pymupdf.open(arg(1, REF / 'week-75-students.pdf'))
G = pymupdf.open(arg(2, REF / 'week-75-facilitator.pdf'))
OLD_S, OLD_G = arg(3, OLD / 'week-75-students.pdf'), arg(4, OLD / 'week-75-facilitator.pdf')
fails = []


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


def labels(page):
    """The 'B, copy n' labels on a page, left to right within each row of boards."""
    out = []
    for x0, y0, x1, y1, word, *_ in page.get_text('words'):
        out.append((round(y0), x0, word))
    out.sort()
    words = [w for _, _, w in out]
    return [words[i + 2] for i in range(len(words) - 2) if words[i] == 'B,' and words[i + 1] == 'copy']


def footer_rows_only(a, b):
    pa, pb = a.get_pixmap(dpi=100), b.get_pixmap(dpi=100)
    if (pa.width, pa.height) != (pb.width, pb.height):
        return False
    rows = {y for y in range(pa.height) for x in range(pa.width) if abs(pa.pixel(x, y)[0] - pb.pixel(x, y)[0]) > 32}
    return not rows or min(rows) > pa.height * (10.35 / 11)


# 1-2. signs and labels
check(len(S) == 4, f'4 student pages ({len(S)})')
hyphens = [(i + 1, m.group(0)) for i, p in enumerate(S) for m in re.finditer(r'(?<![\w)])-\s?\d', p.get_text())]
minus = sum(p.get_text().count('−') for p in S)
check(not hyphens and minus >= 13, f'no hyphen written as a minus sign ({hyphens}); {minus} true minus signs')
check(labels(S[1]) == ['−1', '0', '1', '2'] * 2, f'page 2 lift boards: B, copy {labels(S[1])}')
check(labels(S[2]) == ['−4', '−3', '−2', '−1', '0', '1', '2', '3', '4'], f'page 3 strip: B, copy {labels(S[2])}')

# 3. versions
check(all('Bellingham Math Circle / Week 75 / GGT75-S-v4' in p.get_text() for p in S), 'every student footer reads GGT75-S-v4')
check(all('GGT75-FAC-v4' in p.get_text() for p in G) and 'GGT75-FAC-v3' not in ''.join(p.get_text() for p in G),
      f'every guide footer reads GGT75-FAC-v4 ({len(G)} pages)')
check('matched to the four-page GGT75-S-v4 student pages.' in ' '.join(' '.join(p.get_text().split()) for p in G),
      'the guide names the v4 student pages')

# 4. against v3
if OLD_S.exists() and OLD_G.exists():
    old_s, old_g = pymupdf.open(OLD_S), pymupdf.open(OLD_G)
    back = lambda t: t.replace('GGT75-S-v4', 'GGT75-S-v3').replace('GGT75-FAC-v4', 'GGT75-FAC-v3')
    for i in (0, 2, 3):
        check(back(S[i].get_text()) == old_s[i].get_text() and footer_rows_only(S[i], old_s[i]),
              f'page {i + 1} matches v3 apart from the footer (text and pixels)')
    check(back(S[1].get_text()).replace('copy −1', 'copy -1') == old_s[1].get_text()
          and old_s[1].get_text().count('copy -1') == 2, 'page 2 text differs from v3 only in the two labels and the footer')
    check(len(G) == len(old_g) and all(back(a.get_text()) == b.get_text() for a, b in zip(G, old_g)),
          'guide text differs from v3 only in its footer and status line')
else:
    print(f'SKIP the v3 comparison: no previous print copies in {OLD}')

print(f'{len(fails)} failures')
sys.exit(1 if fails else 0)
