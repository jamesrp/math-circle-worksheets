"""Rebuild the three student .tex sources from build_packets.py in a temporary
copy and compare them byte-for-byte with the shipped .tex files; also compare
the delivered PDFs with the package's reference PDFs. (No LaTeX here, so the
PDFs themselves are not recompiled; check_math.py reads data from the PDFs.)"""
import filecmp, shutil, subprocess, sys, tempfile
from pathlib import Path
from repo import SRC, WEEK

with tempfile.TemporaryDirectory() as tmp:
    dst = Path(tmp) / 'src'
    shutil.copytree(SRC / 'src', dst)
    r = subprocess.run([sys.executable, 'build_packets.py'], cwd=dst, capture_output=True, text=True)
    print('builder:', r.stdout.strip() or r.stderr.strip())
    for band in ['k-1', 'grades-2-3', 'grades-4-5']:
        same = filecmp.cmp(dst / f'{band}.tex', SRC / 'src' / f'{band}.tex', shallow=False)
        print(f'{band}.tex rebuilt identical: {same}')
for pdf, ref in [('k-1', 'k-1'), ('grades-2-3', 'grades-2-3'), ('grades-4-5', 'grades-4-5'), ('facilitator', 'facilitator-guide')]:
    same = filecmp.cmp(WEEK / f'week-18-{pdf}.pdf', SRC / 'reference-pdfs' / f'{ref}.pdf', shallow=False)
    print(f'week-18-{pdf}.pdf identical to reference-pdfs/{ref}.pdf: {same}')
