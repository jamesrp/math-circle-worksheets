#!/usr/bin/env python3
"""Guide digital checks, renders and clean copy/ZIP source round trips.

Requires PyMuPDF and Pillow. QA artifacts stay outside delivered source.
Visual inspection of every rendered page is still a separate human/model step.
"""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import zipfile
import pymupdf
from PIL import Image, ImageDraw

SOURCE_FILES = ['facilitator.tex', 'build.py', 'check_answers.py', 'check_pdf.py',
                'README.md', 'provenance.md']


def digest(b):
    return hashlib.sha256(b).hexdigest()


def signature(pdf):
    doc = pymupdf.open(pdf)
    return [(p.get_text(), tuple(p.rect), digest(p.get_pixmap(matrix=pymupdf.Matrix(1.7, 1.7)).samples))
            for p in doc]


def main():
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python check_pdf.py /path/to/facilitator.pdf')
    pdf = Path(sys.argv[1]).resolve()
    src = Path(__file__).resolve().parent
    qa = pdf.parent / 'guide-qa'
    if qa == src or src in qa.parents:
        raise SystemExit('QA must be outside source')
    qa.mkdir(parents=True, exist_ok=True)
    render = qa / 'render'
    render.mkdir(exist_ok=True)
    doc = pymupdf.open(pdf)
    assert len(doc) == 8, len(doc)
    pages = []
    crops = []
    all_text = ''
    for i, p in enumerate(doc):
        assert tuple(p.rect) == (0.0, 0.0, 612.0, 792.0)
        txt = p.get_text()
        all_text += txt
        assert 'Week 60 / Take it or pass / Adult guide' in txt
        assert 'Bellingham Math Circle / Week 60 / W60-FAC-v1' in txt
        assert txt.strip().endswith(str(i + 1))
        # Bounds for all real text including headers and footers.
        bounds = []
        for block in p.get_text('dict')['blocks']:
            for line in block.get('lines', []):
                for span in line['spans']:
                    r = pymupdf.Rect(span['bbox'])
                    assert 27 < r.x0 <= r.x1 < 590, (i + 1, span)
                    assert 25 < r.y0 <= r.y1 < 780, (i + 1, span)
                    bounds.append(tuple(r))
        pix = p.get_pixmap(matrix=pymupdf.Matrix(1.7, 1.7))
        dest = render / f'page-{i + 1:02d}.png'
        pix.save(dest)
        im = Image.open(dest).convert('RGB')
        crops.append((i + 1, im.crop((0, 0, im.width, 140)),
                      im.crop((0, im.height - 110, im.width, im.height))))
        pages.append({'page': i + 1, 'dimensions': list(p.rect),
                      'render_sha256': digest(pix.samples), 'text_spans_checked': len(bounds)})
    # Prevent an orphan continuation page or process-pending release prose.
    assert all(len(p.get_text().split()) > 250 for p in doc)
    for forbidden in ['review pending', 'awaiting review', 'TODO', 'TBD']:
        assert forbidden not in all_text
    for problem in range(1, 10):
        assert f'Problem {problem} /' in all_text
    assert all_text.index('Finite-horizon stopping theorem') < all_text.index('Problem 1 /')
    montage = Image.new('RGB', (1041, len(crops) * 280), 'white')
    draw = ImageDraw.Draw(montage)
    for j, (n, top, bottom) in enumerate(crops):
        y = j * 280
        draw.text((8, y), f'Guide page {n}', fill='black')
        montage.paste(top, (0, y + 20))
        montage.paste(bottom, (0, y + 163))
    montage.save(qa / 'headers-footers.png')

    baseline = signature(pdf)
    copied = qa / 'copied-source'
    if copied.exists():
        shutil.rmtree(copied)
    copied.mkdir()
    for filename in SOURCE_FILES:
        shutil.copyfile(src / filename, copied / filename)
    copy_out = qa / 'copy-build'
    subprocess.run([sys.executable, str(copied / 'build.py'), str(copy_out)], check=True)
    assert signature(copy_out / 'facilitator.pdf') == baseline
    zpath = qa / 'guide-source-roundtrip.zip'
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for filename in SOURCE_FILES:
            z.write(src / filename, 'week-60-guide-source/' + filename)
    extracted = qa / 'zip-extracted'
    if extracted.exists():
        shutil.rmtree(extracted)
    with zipfile.ZipFile(zpath) as z:
        assert sorted(z.namelist()) == sorted('week-60-guide-source/' + f for f in SOURCE_FILES)
        z.extractall(extracted)
    zip_src = extracted / 'week-60-guide-source'
    zip_out = qa / 'zip-build'
    subprocess.run([sys.executable, str(zip_src / 'build.py'), str(zip_out)], check=True)
    assert signature(zip_out / 'facilitator.pdf') == baseline
    subprocess.run([sys.executable, str(zip_src / 'check_answers.py')], check=True)
    evidence = {'pages': pages, 'copied_source_rebuild': 'identical text, dimensions, rendered pixels',
                'zip_extracted_source_rebuild': 'identical text, dimensions, rendered pixels',
                'source_files': SOURCE_FILES, 'zip': str(zpath),
                'visual_inspection_is_separate': True,
                'physical_rehearsal_and_classroom_pilot': 'unperformed'}
    (qa / 'verification.json').write_text(json.dumps(evidence, indent=2) + '\n')
    print('PASS: 8 pages; clean copied and ZIP-extracted rebuilds match text, dimensions, pixels')


if __name__ == '__main__':
    main()
