# Clean extracted-package rebuild verification

- `k-1.pdf`: exact text, vector geometry, Letter dimensions and 100-dpi pixels on all 6 pages.
- `grades-2-3.pdf`: exact text, vector geometry, Letter dimensions and 100-dpi pixels on all 6 pages.
- `grades-4-5.pdf`: exact text, vector geometry, Letter dimensions and 100-dpi pixels on all 6 pages.
- `facilitator-guide.pdf`: exact text, vector geometry, Letter dimensions and 100-dpi pixels on all 7 pages.

Changed packets and guides require exact reference pixels. The unchanged-font alternatives recorded in `rebuild-pixel-allowances.json` are specifically audited full-page hashes, not a general layout tolerance. `verify_revision.py` accepts the exact reference rendering or those specific unchanged alternatives. The original strict verifier remains available and deliberately rejects any pixel difference. Physical rehearsal remains unperformed.
