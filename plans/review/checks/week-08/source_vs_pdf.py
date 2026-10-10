"""Confirm that the delivered student PDFs carry the text of the sources I read.

For each band it pulls the opening rules and every "Problem N:" statement out of
source/week-08/src/<band>.tex, strips the LaTeX, and looks for it in the
pdftotext output of the delivered PDF.  It also confirms that the .tex files in
src/ are what src/build.py generates now (so the sources are current), and that
the return-visit statements in its .tex are in its PDF.  Output saved as
source_vs_pdf.out.
"""
import importlib.util
import os
import re
import subprocess
import sys
sys.dont_write_bytecode = True  # never leave __pycache__ beside the packet sources
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import repo  # noqa: E402


def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in (('\u2019', "'"), ('\u201c', '"'), ('\u201d', '"'), ('\u2013', '-'), ('\u2212', '-')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip()


def detex(s):
    s = s.replace('--', '-').replace("\\'", "'").replace('``', '"').replace("''", '"')
    s = re.sub(r'\\prob\{(\d+)\}', r'Problem \1:', s)
    s = re.sub(r'\\textbf\{([^}]*)\}', r'\1', s)
    s = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})?', ' ', s)
    s = s.replace('{', '').replace('}', '').replace('~', ' ')
    return norm(s)


ok = bad = 0
for band, pdf in repo.STUDENT.items():
    tex = open(os.path.join(repo.SRC, 'src', band + '.tex')).read()
    body = tex.split('\\begin{document}', 1)[1]
    txt = norm(subprocess.run(['pdftotext', pdf, '-'], capture_output=True, text=True).stdout)
    pieces = []
    for m in re.finditer(r'\\prob\{\d+\}.*?(?=\n\n|\\vspace|\\end\{minipage\}|\\newpage|\n\\end\{document\})', body, re.S):
        pieces.append(m.group(0))
    rules = re.search(r'\\raggedright\n(?:\\noindent\\begin\{minipage\}\[c\]\{[\d.]+in\}\\raggedright\n)(.*?)\\end\{minipage\}', body, re.S)
    if rules:
        pieces.insert(0, rules.group(1))
    for p in pieces:
        for para in [q for q in re.split(r'\\vspace\{[^}]*\}', p) if detex(q)]:
            d = detex(para)
            if d in txt:
                ok += 1
                print('OK        %-10s %s' % (band, d[:110] + ('...' if len(d) > 110 else '')))
            else:
                bad += 1
                print('MISMATCH  %-10s not in PDF: %s' % (band, d))

# are the .tex files what build.py makes now?
spec = importlib.util.spec_from_file_location('w08build', os.path.join(repo.SRC, 'src', 'build.py'))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
for band, fn in (('k-1', mod.k1), ('grades-2-3', mod.g23), ('grades-4-5', mod.g45)):
    same = fn() == open(os.path.join(repo.SRC, 'src', band + '.tex')).read()
    if same:
        ok += 1
    else:
        bad += 1
    print('%s  src/%s.tex equals build.py output' % ('OK       ' if same else 'MISMATCH ', band))

# return visit
tex = open(os.path.join(repo.RV_SRC, 'student', 'return-visit.tex')).read()
txt = norm(subprocess.run(['pdftotext', repo.RV_STUDENT, '-'], capture_output=True, text=True).stdout)
for m in re.finditer(r'\\txt\{[^}]*\}\{[^}]*\}\{[^}]*\}\{(.*?)\}\n', tex):
    d = detex(m.group(1))
    if d in txt:
        ok += 1
        print('OK        return    %s' % (d[:110] + ('...' if len(d) > 110 else '')))
    else:
        bad += 1
        print('MISMATCH  return    not in PDF: %s' % d)
print('Summary: %d OK, %d MISMATCH' % (ok, bad))
