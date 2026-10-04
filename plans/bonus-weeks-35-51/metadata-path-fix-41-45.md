# Weeks 41–45 portable metadata path correction

The released metadata had copied operative working-run paths. It now explicitly declares paths relative to the package directory containing `investigations.json`. Mathematical content, student/adult source builders, guides, worksheets and all ten released/reference PDFs are unchanged.

Current mappings: `deliverables.student` → `reference-pdfs/week-NN-bonus.pdf`; `adult_guide` → `reference-pdfs/week-NN-bonus-facilitator.pdf`; `adult_notes` → `guide.md`; `source` → `student/`; `builder` → `build.py`; `checks.enumeration` → `student/verify.py`.

Every path exists in the released folder and newly extracted ZIP. Each ZIP changes only its `investigations.json` member. All five extracted packages rebuilt both PDFs with identical page text and rendered pixels; portable mathematical verifiers pass. Released PDF bytes and their previously recorded SHA256 hashes are unchanged. Producer ZIP checksums and range inventory JSON are synchronized. The aggregate deliverable audit passes, now including operative metadata-path validation.

Working-run metadata under `tmp/worksheet-runs/` is retained as workflow provenance; the release/refresh producers normalize it into current portable paths, preventing this defect from being reintroduced. No global index or other week package was edited.

## Exact changed and added files

- `lowell-math-circle-year-2/source/week-41-bonus/investigations.json`
- `lowell-math-circle-year-2/source/week-41-bonus-source.zip`
- `plans/bonus-weeks-35-51/release-checks/week-41.json`
- `lowell-math-circle-year-2/source/week-42-bonus/investigations.json`
- `lowell-math-circle-year-2/source/week-42-bonus-source.zip`
- `plans/bonus-weeks-35-51/release-checks/week-42.json`
- `lowell-math-circle-year-2/source/week-43-bonus/investigations.json`
- `lowell-math-circle-year-2/source/week-43-bonus-source.zip`
- `plans/bonus-weeks-35-51/release-checks/week-43.json`
- `lowell-math-circle-year-2/source/week-44-bonus/investigations.json`
- `lowell-math-circle-year-2/source/week-44-bonus-source.zip`
- `plans/bonus-weeks-35-51/release-checks/week-44.json`
- `lowell-math-circle-year-2/source/week-45-bonus/investigations.json`
- `lowell-math-circle-year-2/source/week-45-bonus-source.zip`
- `plans/bonus-weeks-35-51/release-checks/week-45.json`
- `plans/bonus-weeks-35-51/inventory.json`
- `plans/bonus-weeks-35-51/check_deliverables.py`
- `tmp/bonus-weeks-35-51/release.py`
- `tmp/bonus-weeks-35-51/refresh_release.py`
- `tmp/bonus-weeks-35-51/package_metadata.py`
- `tmp/bonus-weeks-35-51/fix_metadata_41_45.py`
- `plans/bonus-weeks-35-51/metadata-path-fix-41-45.json`
- `plans/bonus-weeks-35-51/metadata-path-fix-41-45.md`

## Unchanged PDF SHA256 hashes

| Week | Student PDF | Adult PDF |
|---|---|---|
| 41 | `19c0e87682e3a6d8049f7bd6a09b4af9cc0fde214cf9c8372bbcbb2cc263d62d` | `c63934b78ae6c66ae99c55f0d9a43ae00e61feaa1d5bebf5d579aa024ea3ac76` |
| 42 | `9897c827008ba1e4e9663466dd4990fad2b47cda6b37eb5a81aaf0892cac4b6f` | `5a7f9ccaa4ec54851fc76bf55df75a5d298dec7bb431718c3f4d57e392f1e6cd` |
| 43 | `d5753561cb1eac16827b77cb530ff698a61d60f4bd6fbbe7d66b37b41b1995cf` | `923f296be34a1fa0c8e28d5e12cc9a7ec8ec1eda889d0703d5a5d0dce8a9fcbf` |
| 44 | `e10e54d25ff0430faaa4d9ed7de1ac7e924729e800a2c291efd83b053defed63` | `533803d6f67be59726eaa1e762cb4461434b03a6f5bf1af6e85f69b18eb3b04e` |
| 45 | `576749dc0f20cc4d73e989cdde5bbe2df8079de05b8140effae06da5785c0bee` | `dd4760a3232ca77068eb26775687e5456827ffb979cae07a920f207bac649271` |
