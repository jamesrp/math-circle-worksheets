"""Text-level checks: problem numbering per packet, page counts the guide quotes,
and that the delivered PDFs are byte-identical to the source reference copies.
Writes check_text.out next to this script.
"""
import os, sys, re, subprocess, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdfgeom as PG

OUT = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    OUT.append(s)


W = PG.WEEK
SRC = os.path.join(PG.ROOT, 'lowell-math-circle-year-2', 'source')
pairs = [('week-14-k-1.pdf', 'week-14/editable/reference-pdfs/k-1.pdf'),
         ('week-14-grades-2-3.pdf', 'week-14/editable/reference-pdfs/grades-2-3.pdf'),
         ('week-14-grades-4-5.pdf', 'week-14/editable/reference-pdfs/grades-4-5.pdf'),
         ('week-14-facilitator.pdf', 'week-14/editable/reference-pdfs/facilitator-guide.pdf'),
         ('week-14-return-visit.pdf', 'week-14-return-visit/reference-pdfs/week-14-return-visit.pdf'),
         ('week-14-return-visit-facilitator.pdf', 'week-14-return-visit/reference-pdfs/week-14-return-visit-facilitator.pdf')]
for a, b in pairs:
    ha = hashlib.md5(open(os.path.join(W, a), 'rb').read()).hexdigest()
    hb = hashlib.md5(open(os.path.join(SRC, b), 'rb').read()).hexdigest()
    log(f'{a}: md5 {ha} {"== reference" if ha == hb else "DIFFERS from " + b}')

for f in ['week-14-k-1.pdf', 'week-14-grades-2-3.pdf', 'week-14-grades-4-5.pdf', 'week-14-return-visit.pdf']:
    txt = subprocess.run(['pdftotext', '-layout', os.path.join(W, f), '-'], capture_output=True, text=True).stdout
    pages = txt.split('\f')
    nums = []
    for i, pg in enumerate(pages, 1):
        for m in re.finditer(r'Problem (\d+)( \(continued\))?:', pg):
            nums.append((i, int(m.group(1)), bool(m.group(2))))
    main = [n for p, n, c in nums if not c]
    log(f'{f}: {len([p for p in pages if p.strip()])} pages; numbered problems {main}; continued {[(p, n) for p, n, c in nums if c]}')
    log('   consecutive:', main == list(range(1, len(main) + 1)))
open(os.path.join(HERE, 'check_text.out'), 'w').write('\n'.join(OUT) + '\n')
