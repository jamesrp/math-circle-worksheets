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
    s = re.sub(r'\\textbf\{([^}]*)\}', r'\1', s)
    s = s.replace("\\'", "'")
    return norm(s)


out.append('== problem statements and rules from the editable sources, found in the PDFs')
builder = open(os.path.join(SRC, 'editable/src/build_packets.py')).read()
texts = {'K-1': pdftext('week-11-k-1.pdf'), '2-3': pdftext('week-11-grades-2-3.pdf'), '4-5': pdftext('week-11-grades-4-5.pdf')}
probs = re.findall(r"problem\((\d),'([^']*)'", builder)
bands = ['K-1'] * 6 + ['2-3'] * 6 + ['4-5'] * 6
for (n, txt), band in zip(probs, bands):
    t = tex_clean(txt)
    # pdftotext may break "com-pare" style hyphenation; compare without hyphens and spaces
    squash = lambda s: re.sub(r'[\s-]', '', s)
    ok = f'Problem {n}: ' in texts[band] and squash(t) in squash(texts[band])
    fails += not ok
    out.append(f"  [{'ok  ' if ok else 'FAIL'}] {band} Problem {n}: {t[:90]}")
rules = tex_clean(re.search(r"txt=\('(.*?)'\)", builder, re.S).group(1).replace("'\n         '", ''))
for band in texts:
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
