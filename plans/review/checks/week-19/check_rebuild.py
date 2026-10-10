"""Source and PDF consistency for Week 19 (no PDF recompilation).

1. Delivered PDFs vs editable/reference-pdfs and the bonus reference-pdfs (bytes).
2. Re-run the base builder src/build_packets.py in a temporary copy and compare
   the three generated .tex files with the shipped ones (the builder is run, not
   imported; its own answer checks are ignored).
3. Compare the decks hard-coded in the builder with the decks read from the
   delivered PDFs (pdf_decks.json from extract_pdf.py).
4. Compare the editable folder with the portable source ZIP (file hashes).
"""
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

from repo import HERE, PDF, SRC, BONUS_SRC

FAILS = []


def ok(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def h(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


ref = SRC / 'reference-pdfs'
pairs = [('K-1', 'k-1.pdf'), ('2-3', 'grades-2-3.pdf'), ('4-5', 'grades-4-5.pdf'), ('guide', 'facilitator-guide.pdf')]
for band, f in pairs:
    ok(h(PDF[band]) == h(ref / f), f'{PDF[band].name} identical to editable/reference-pdfs/{f}')
for band in ('bonus', 'bonus-guide'):
    r = BONUS_SRC / 'reference-pdfs' / PDF[band].name
    ok(r.exists() and h(PDF[band]) == h(r), f'{PDF[band].name} identical to week-19-bonus/reference-pdfs copy')

with tempfile.TemporaryDirectory() as td:
    work = Path(td) / 'src'
    shutil.copytree(SRC / 'src', work)
    for f in work.glob('*.tex'):
        f.unlink()
    res = subprocess.run([sys.executable, '-I', str(work / 'build_packets.py')], capture_output=True, text=True, cwd=td)
    ok(res.returncode == 0, 'build_packets.py runs in a temporary copy')
    for t in ('k-1.tex', 'grades-2-3.tex', 'grades-4-5.tex'):
        ok((work / t).read_text() == (SRC / 'src' / t).read_text(), f'regenerated {t} equals the shipped {t}')

# builder decks vs printed decks
code = (SRC / 'src' / 'build_packets.py').read_text()
sym = 'ABCD'


def mask_name(m):
    return ''.join(sym[b] for b in range(4) if m >> b & 1)


decks = {k: [int(x) for x in re.search(k + r'=\[([\d,]+)\]', code).group(1).split(',')] for k in ('D4', 'D8', 'D16')}
pd = json.loads((HERE / 'pdf_decks.json').read_text())
printed = {}
for pg in pd['2-3']:
    for pn, gs in pg['decks'].items():
        for g in gs:
            printed.setdefault(len(g), [c['card'] for c in g])
for k, n in (('D4', 4), ('D8', 8), ('D16', 16)):
    ok([mask_name(m) for m in decks[k]] == printed[n], f'builder {k} order equals printed {n}-card deck order: {[mask_name(m) or "empty" for m in decks[k]]}')

# editable folder vs ZIP
zp = SRC.parent / 'subset-antichains-week19-editable-source.zip'
with zipfile.ZipFile(zp) as z:
    names = [n for n in z.namelist() if not n.endswith('/')]
    prefix = names[0].split('/')[0] + '/'
    zh = {n[len(prefix):]: hashlib.sha256(z.read(n)).hexdigest() for n in names}
local = {str(p.relative_to(SRC)): h(p) for p in SRC.rglob('*') if p.is_file()}
diff = sorted(k for k in set(zh) | set(local) if zh.get(k) != local.get(k))
ok(not diff, f'source ZIP ({len(zh)} files) matches editable/ ({len(local)} files); differing paths: {diff}')

print(f'{len(FAILS)} failures')
