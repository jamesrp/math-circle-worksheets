# Portable release validation

2026-10-03. This revision adds a three-page mathematical overview to the adult guide, which now has 12 pages. Its detailed solutions are retained. All three student PDFs and all student source files remain byte-identical to the preceding release.

The source ZIP was extracted into a directory whose path contains spaces. Its portable build completed using ordinary pdflatex and the documented Python dependencies. All four rebuilt PDFs matched the current reference files in page count, US Letter media size, extracted text, and every page's 100-dpi grayscale pixels. The supplied guide PDF is identical to its reference copy.

PASS facilitator-guide.pdf: 12 Letter pages; identical extracted text and 100-dpi grayscale pixels.
PASS grades-2-3.pdf: 6 Letter pages; identical extracted text and 100-dpi grayscale pixels.
PASS grades-4-5.pdf: 6 Letter pages; identical extracted text and 100-dpi grayscale pixels.
PASS k-1.pdf: 6 Letter pages; identical extracted text and 100-dpi grayscale pixels.
PASS: all 30 pages match. Binary differences caused by PDF timestamps or document IDs are not displayed content.

The revised adult guide has passed an independent mathematical and every-page visual review. These checks do not constitute classroom piloting. Earlier facilitator review records describe the previous nine-page guide.

Validation used TeX Live 2025 and its installed package tree. The test container required temporary TeX search settings and a fresh format outside the source bundle because its home configuration is read-only. No original cached format was reused, and no test-environment settings or binaries are shipped. A normal working TeX Live or MacTeX installation supplies these distribution-level settings.

Third-party fonts, downloads, caches, logs, render images and TeX format files are excluded. The bundle contains portable source, reproducible checks, supplied reference PDFs and release documentation.
