# Release validation

Guidance revision prepared October 3, 2026. Draft and unpiloted.

PDF page counts: k-1: 5, grades-2-3: 5, grades-4-5: 5, facilitator-guide: 10.

Student numbered-problem counts: k-1: 6, grades-2-3: 6, grades-4-5: 6.

The source ZIP is extracted to a separate directory and rebuilt with the top-level build.sh. verify_rebuild.py checks every reference hash, page count, Letter page size, extracted text and 100-dpi grayscale rendering against that fresh rebuild. All comparisons must pass for release. PDF timestamps or object identifiers may differ without affecting displayed content.

Earlier student-review and facilitator-review files in this directory are historical records, not descriptions of the added overview and examples. The current scope is recorded in README.md.
