# Release validation

Guidance revision prepared October 3, 2026. Draft and unpiloted.

PDF page counts: k-1: 7, grades-2-3: 6, grades-4-5: 7, facilitator-guide: 25.

Student numbered-problem counts: k-1: 7, grades-2-3: 6, grades-4-5: 7.

The source ZIP is extracted to a separate directory and rebuilt with the top-level build.sh. verify_rebuild.py checks every reference hash, page count, Letter page size, extracted text and 100-dpi grayscale rendering against that fresh rebuild. All comparisons must pass for release. PDF timestamps or object identifiers may differ without affecting displayed content.

Earlier student-review and facilitator-review files in this directory are historical records, not descriptions of the added overview and examples. The current scope is recorded in README.md.


## October 4, 2026 worked-example revision

Current reference hashes are in reference-manifest.json. All 45 pages (three student packets plus the 25-page guide) are rebuilt and compared. See [worked-example QA](worked-examples-2026-10-04.md). The original validation above is historical.
