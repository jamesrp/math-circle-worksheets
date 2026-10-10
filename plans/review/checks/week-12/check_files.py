"""Which files were checked: page counts and MD5 of the delivered Week 12 PDFs, compared with the
reference copies kept with the editable sources.  Run: python3 check_files.py > check_files.out"""
import os
import sys
import hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfgeo as G
import pdfplumber

SRC = os.path.join(G.ROOT, 'lowell-math-circle-year-2', 'source')
pairs = [('week-12-k-1.pdf', 'week-12/editable/reference-pdfs/k-1.pdf'),
         ('week-12-grades-2-3.pdf', 'week-12/editable/reference-pdfs/grades-2-3.pdf'),
         ('week-12-grades-4-5.pdf', 'week-12/editable/reference-pdfs/grades-4-5.pdf'),
         ('week-12-facilitator.pdf', 'week-12/editable/reference-pdfs/facilitator-guide.pdf'),
         ('week-12-return-visit.pdf', 'week-12-return-visit/reference-pdfs/week-12-return-visit.pdf'),
         ('week-12-return-visit-facilitator.pdf', 'week-12-return-visit/reference-pdfs/week-12-return-visit-facilitator.pdf')]


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


bad = 0
for d, r in pairs:
    dp = G.pdf_path(d)
    rp = os.path.join(SRC, r)
    with pdfplumber.open(dp) as pdf:
        n = len(pdf.pages)
        size = (pdf.pages[0].width, pdf.pages[0].height)
    same = md5(dp) == md5(rp)
    bad += not same
    print(f'{d}: {n} pages, {size[0]:.0f}x{size[1]:.0f} pt, md5 {md5(dp)}, identical to reference: {same}')
print('FAILED:', 'none' if not bad else bad)
