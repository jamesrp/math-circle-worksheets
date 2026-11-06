# Clean extracted-package rebuild verification

- `k-1.pdf`: unchanged current print/reference remains byte-identical; source rebuild preserves mathematical text and vector diagrams. Maximum glyph-box drift on text-identical pages is 0.01117 pt; hyphenation-only reflow pages: none.
- `grades-2-3.pdf`: unchanged current print/reference remains byte-identical; source rebuild preserves mathematical text and vector diagrams. Maximum glyph-box drift on text-identical pages is 0.01022 pt; hyphenation-only reflow pages: none.
- `grades-4-5.pdf`: unchanged current print/reference remains byte-identical; source rebuild preserves mathematical text and vector diagrams. Maximum glyph-box drift on text-identical pages is 0.01022 pt; hyphenation-only reflow pages: none.
- `facilitator-guide.pdf`: exact text, vector geometry, Letter dimensions and 100-dpi pixels on all 5 pages.

Changed packets and guides require exact reference pixels. The unchanged-font alternatives recorded in `rebuild-pixel-allowances.json` are specifically audited full-page hashes, not a general layout tolerance. `verify_revision.py` accepts the exact reference rendering or those specific unchanged alternatives. The original strict verifier remains available and deliberately rejects any pixel difference. Physical rehearsal remains unperformed.

## Kid-fit revision, November 6, 2026 (v5)

All four references were replaced by the v5 build (packets F33-K-v5, F33-23-v5, F33-45-v5; guide G33-v5) and `reference-manifest.json` updated. A clean rebuild from the extracted ZIP gave identical text and 0 differing pixels at 100 dpi on every page of all three packets (Poppler render via `problem-files/tools/compare.py`), and a byte-identical adult guide. `verify.py` and `verify_revision.py` need PyMuPDF, which the adopting environment lacked, so they were not run; the Poppler comparison stands in for them. Physical rehearsal remains unperformed.
