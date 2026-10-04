# Clean extracted-package rebuild verification

- `k-1.pdf`: unchanged current print/reference remains byte-identical; source rebuild preserves mathematical text and vector diagrams. Maximum glyph-box drift on text-identical pages is 0.02615 pt; hyphenation-only reflow pages: none.
- `grades-2-3.pdf`: unchanged current print/reference remains byte-identical; source rebuild preserves mathematical text and vector diagrams. Maximum glyph-box drift on text-identical pages is 0.02332 pt; hyphenation-only reflow pages: none.
- `grades-4-5.pdf`: unchanged current print/reference remains byte-identical; source rebuild preserves mathematical text and vector diagrams. Maximum glyph-box drift on text-identical pages is 0.02429 pt; hyphenation-only reflow pages: none.
- `facilitator-guide.pdf`: exact text, vector geometry, Letter dimensions and 100-dpi pixels on all 11 pages.

Changed packets and guides require exact reference pixels. The unchanged-font alternatives recorded in `rebuild-pixel-allowances.json` are specifically audited full-page hashes, not a general layout tolerance. `verify_revision.py` accepts the exact reference rendering or those specific unchanged alternatives. The original strict verifier remains available and deliberately rejects any pixel difference. Physical rehearsal remains unperformed.
