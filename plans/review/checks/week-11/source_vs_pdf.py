"""Confirm the delivered PDFs are the source package's reference copies and carry the
problem statements and shared rules written in the editable sources.
Output: source_vs_pdf.out
"""
import hashlib
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chipfire import PKT, SRC, SRC_RV, HERE, ROOT  # noqa: E402
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problem_tex import band_parts  # noqa: E402

out = []
fails = 0


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


pairs = [('week-11-k-1.pdf', os.path.join(SRC, 'editable/reference-pdfs/k-1.pdf')),
         ('week-11-grades-2-3.pdf', os.path.join(SRC, 'editable/reference-pdfs/grades-2-3.pdf')),
         ('week-11-grades-4-5.pdf', os.path.join(SRC, 'editable/reference-pdfs/grades-4-5.pdf')),
         ('week-11-facilitator.pdf', os.path.join(SRC, 'editable/reference-pdfs/facilitator-guide.pdf')),
         ('week-11-return-visit.pdf', os.path.join(SRC_RV, 'reference-pdfs/week-11-return-visit.pdf')),
         ('week-11-return-visit-facilitator.pdf', os.path.join(SRC_RV, 'reference-pdfs/week-11-return-visit-facilitator.pdf'))]
out.append('== delivered PDF vs source reference copy (MD5)')
for a, b in pairs:
    ha, hb = md5(os.path.join(PKT, a)), md5(b)
    ok = ha == hb
    fails += not ok
    out.append(f"  [{'ok  ' if ok else 'FAIL'}] {a} {ha} == {os.path.relpath(b, ROOT)} {hb}")


def norm(t):
    t = t.replace('\u2013', '-').replace('\u2014', '-').replace('\u2019', "'").replace('\ufb01', 'fi').replace('\ufb02', 'fl')
    t = re.sub(r'-\s*\n\s*', '-', t)  # hyphenation across lines ("com-\npare")
    return re.sub(r'\s+', ' ', t).strip()


def pdftext(fn):
    return norm(subprocess.run(['pdftotext', os.path.join(PKT, fn), '-'], capture_output=True, text=True).stdout)


def tex_clean(s):
    s = s.replace('--', '-').replace("``", '"').replace("''", '"').replace('\\\\', ' ')
    s = re.sub(r'\\(?:textbf|mbox)\{([^}]*)\}', r'\1', s)
    s = s.replace("\\'", "'")
    return norm(s)


out.append('== problem statements and rules from the editable sources, found in the PDFs')
# Since October 23, 2026 the packets are built from problem files (../problem_tex.py reads them);
# the old builder build_packets.py, whose problem() calls this read, is archived.
texts = {'K-1': pdftext('week-11-k-1.pdf'), '2-3': pdftext('week-11-grades-2-3.pdf'), '4-5': pdftext('week-11-grades-4-5.pdf')}
files = {'K-1': 'k-1', '2-3': 'grades-2-3', '4-5': 'grades-4-5'}
squash = lambda s: re.sub(r'[\s-]', '', s)  # pdftotext may break "com-pare" style hyphenation
for band in texts:
    parts = band_parts('week-11', files[band])
    for n, kind, txt in parts:
        if kind != 'prompt':
            continue
        t = tex_clean(' '.join(txt.split()))
        ok = f'Problem {n}: ' in texts[band] and squash(t) in squash(texts[band])
        fails += not ok
        out.append(f"  [{'ok  ' if ok else 'FAIL'}] {band} Problem {n}: {t[:90]}")
    rules = [tex_clean(' '.join(txt.split())) for n, kind, txt in parts if kind == 'text' and n is None][0]
    ok = rules in texts[band]
    fails += not ok
    out.append(f"  [{'ok  ' if ok else 'FAIL'}] {band} shared rules")
rv = open(os.path.join(SRC_RV, 'student/return-visit.tex')).read()
rvt = pdftext('week-11-return-visit.pdf')
for n, txt in re.findall(r'\\prob\{(\d)\}\{([^}]*)\}', rv):
    t = tex_clean(txt)
    ok = t in rvt
    fails += not ok
    out.append(f"  [{'ok  ' if ok else 'FAIL'}] RV Problem {n}: {t[:90]}")
out.append(f"pdflatex available for a clean rebuild: {bool(shutil.which('pdflatex'))}")
out.append(f'{fails} FAIL lines')
open(os.path.join(HERE, 'source_vs_pdf.out'), 'w').write('\n'.join(out) + '\n')
print('\n'.join(out))
