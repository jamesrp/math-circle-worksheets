#!/usr/bin/env python3
"""Compare rebuilt band packets with the current print PDFs: text and pixels.

    python3 compare.py output/week-50 ../../lowell-math-circle-year-2/week-50 week-50
"""
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageChops

new_dir, cur_dir, prefix = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
ok = True
for name in ('k-1', 'grades-2-3', 'grades-4-5'):
    new, cur = new_dir / f'{name}.pdf', cur_dir / f'{prefix}-{name}.pdf'
    text = [subprocess.run(['pdftotext', '-layout', str(p), '-'], capture_output=True, text=True).stdout
            for p in (new, cur)]
    with tempfile.TemporaryDirectory() as tmp:
        for tag, p in (('n', new), ('c', cur)):
            subprocess.run(['pdftoppm', '-r', '100', '-png', str(p), f'{tmp}/{tag}'], check=True)
        news, curs = sorted(Path(tmp).glob('n-*.png')), sorted(Path(tmp).glob('c-*.png'))
        worst = 0
        for a, b in zip(news, curs):
            diff = ImageChops.difference(Image.open(a).convert('L'), Image.open(b).convert('L'))
            worst = max(worst, sum(diff.histogram()[33:]))
    same_pages = len(news) == len(curs)
    print(f'{name:11s} pages {len(news)}/{len(curs)}  text {"identical" if text[0] == text[1] else "DIFFERS"}  '
          f'most differing pixels on any page at 100 dpi: {worst}')
    ok &= same_pages and text[0] == text[1] and worst == 0
sys.exit(0 if ok else 1)
