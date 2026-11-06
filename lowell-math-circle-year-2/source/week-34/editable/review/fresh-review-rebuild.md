# Clean extracted-package rebuild verification

- `k-1.pdf`: unchanged current print/reference remains byte-identical; source rebuild preserves mathematical text and vector diagrams. Maximum glyph-box drift on text-identical pages is 0.02332 pt; hyphenation-only reflow pages: none.
- `grades-2-3.pdf`: unchanged current print/reference remains byte-identical; source rebuild preserves mathematical text and vector diagrams. Maximum glyph-box drift on text-identical pages is 0.01648 pt; hyphenation-only reflow pages: none.
- `grades-4-5.pdf`: unchanged current print/reference remains byte-identical; source rebuild preserves mathematical text and vector diagrams. Maximum glyph-box drift on text-identical pages is 0.01648 pt; hyphenation-only reflow pages: none.
- `facilitator-guide.pdf`: exact text, vector geometry, Letter dimensions and 100-dpi pixels on all 6 pages.

Changed packets and guides require exact reference pixels. The unchanged-font alternatives recorded in `rebuild-pixel-allowances.json` are specifically audited full-page hashes, not a general layout tolerance. `verify_revision.py` accepts the exact reference rendering or those specific unchanged alternatives. The original strict verifier remains available and deliberately rejects any pixel difference. Physical rehearsal remains unperformed.

## November 6, 2026 kid-fit revision (v4)

The references are now the v4 packets (byte-identical to the approved candidate and the print copies) and the guide that keys them. A clean build from the extracted ZIP matched the references on every page: K-1 6, Grades 2-3 5, Grades 4-5 6 and the guide 6 pages, with identical pdftotext output and exact 100-dpi pixels (pdftoppm); the guide is byte-identical and the student packets differ only in PDF metadata bytes. `verify_math.py` passed. `verify.py` and `verify_revision.py` need PyMuPDF, which was not installed in the adoption environment, so the equivalent comparison was run with Poppler and Pillow instead.
