"""Do the delivered student PDFs carry the text and boards of the sources I read?

1. Every problem statement and the opening rules in src/k-1.tex, grades-2-3.tex and
   grades-4-5.tex (the generated LaTeX) appear, after normalising, in the PDF text.
2. Every table size drawn by the generated TikZ (the thick wall rectangles and the
   sheet outlines) matches the board sizes read out of the PDFs (pdf_geometry.json).
pdfLaTeX is not installed here, so this stands in for a clean rebuild.
"""
import json
import re
import subprocess
from pathlib import Path

from pdfgeom import PDF, SRC

HERE = Path(__file__).resolve().parent
bad = 0


def norm(s):
    s = s.replace('\u201c', '"').replace('\u201d', '"').replace('\u2019', "'").replace('\u2013', '-')
    return re.sub(r'\s+', ' ', s).strip()


def detex(s):
    s = s.replace('--', '-').replace('\\\\', ' ')
    s = re.sub(r'\\textbf\{([^}]*)\}', r'\1', s)
    s = re.sub(r'\\prob\{(\d+)\}', r'Problem \1:', s)
    s = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?', ' ', s)
    s = s.replace('{', ' ').replace('}', ' ')
    return norm(s)


if not (HERE / 'pdf_geometry.json').exists():
    subprocess.run(['python3', str(HERE / 'extract.py')], check=True, stdout=subprocess.DEVNULL)
geo = json.loads((HERE / 'pdf_geometry.json').read_text())

for band, name in (('K-1', 'k-1'), ('2-3', 'grades-2-3'), ('4-5', 'grades-4-5')):
    tex = (SRC / 'src' / f'{name}.tex').read_text()
    pdf = norm(subprocess.run(['pdftotext', str(PDF[band]), '-'], capture_output=True, text=True).stdout).replace('\u2013', '-')
    pdf = re.sub(r'Week 9 / Bouncing paths / \S+ ', ' ', pdf)
    pdf = re.sub(r'Bellingham Math Circle / Week 9 / F09-\S+ \d+', ' ', pdf)
    pdf = norm(pdf)
    stmts = re.findall(r'\\prob\{\d+\}.*?(?=\n\\begin|\n\\vspace|\n\\newpage|\n\\par|\\begin\{itemize|\n\\end\{document\})', tex, re.S)
    rules = re.findall(r'\\begin\{minipage\}\[c\]\{0\.5\d\\textwidth\}\\setlength\{\\parskip\}\{5pt\}\n(.*?)\n\\end\{minipage\}', tex, re.S)
    for s in stmts + rules:
        t = detex(s)
        ok = norm(t) in pdf
        print(f"  {'ok      ' if ok else 'MISMATCH'} {band}: {t[:80]}")
        bad += not ok
    # table sizes in the generated TikZ: thick (2.2pt) rectangles
    rects = re.findall(r'\\draw\[line width=2\.2pt\] \(([\d.]+),([\d.-]+)\) rectangle \(([\d.]+),([\d.-]+)\);', tex)
    src_sizes = []
    for x0, y0, x1, y1 in rects:
        wid, hei = float(x1) - float(x0), float(y1) - float(y0)
        u = 0.75 if band == 'K-1' else 0.5
        # the rules picture uses smaller squares
        cands = [u, 0.5, 0.4]
        for c in cands:
            if abs(wid / c - round(wid / c)) < 1e-3 and abs(hei / c - round(hei / c)) < 1e-3:
                src_sizes.append((round(wid / c), round(hei / c)))
                break
    pdf_sizes = [(g['w'], g['h']) for pg in geo[band].values() for g in pg['grids'] if g['walls']]
    ok = sorted(src_sizes) == sorted(pdf_sizes)
    print(f"  {'ok      ' if ok else 'MISMATCH'} {band}: walled boards in the source = walled boards in the PDF "
          f"({len(src_sizes)} / {len(pdf_sizes)})")
    bad += not ok
print(f'{bad} mismatches')
