# Week 53 standalone facilitator source

This separately authored eight-page guide accompanies the actual final nine-page
Week 53 student packet (Grades 2–5 on pp. 1–4; Grades 4–5 on pp. 5–9). All nine
keys, complete optimum catalogs, all specified cheaper swaps, inverse witnesses,
full inverse distribution and general proofs are included. Source contents:

- `facilitator.tex`: original prose and original TikZ launch diagram.
- `build.py`: standalone two-pass PDF build, with intermediates in a temporary directory.
- `verify_math.py`: a new union-find enumeration from manually transcribed final maps;
  it imports no student data/checker. Generates complete connected/tree catalogs,
  all improving swaps and all 4,096 inverse assignments outside this source folder.
- `verify_output.py`: text, Letter dimensions and bounds; optional exact text and
  rendered-pixel comparison with a clean rebuild.
- `SOURCE-NOTES.md`: source lineage, evidence and limits.

## Build and check

Requires Python 3 and `pdflatex` (standard TeX Live: article, geometry, T1/helvet,
microtype, TikZ, fancyhdr, array/booktabs, enumitem, amsmath and hyperref).
Verification additionally requires PyMuPDF (`pymupdf`). No repository file,
downloaded book, student PDF or generated workflow prompt is a build dependency.

```sh
python3 build.py --out /tmp/week53-guide-output
python3 verify_math.py --report /tmp/week53-guide-output/math-checks.json
python3 verify_output.py /tmp/week53-guide-output/facilitator.pdf --report /tmp/week53-guide-output/pdf-checks.json
```

For a portable-copy test, copy only this source folder elsewhere, run `build.py`,
then run `verify_output.py original/facilitator.pdf --compare copy/facilitator.pdf
--report /tmp/rebuild-check.json`. This checks extracted text, every page dimension
and every 144-dpi rendered pixel; PDF metadata can differ.

The repository's verification interpreter is `tmp/bonus-35-51-venv/bin/python`.
No physical fit, payment/refund rehearsal, timing or classroom pilot is claimed;
these are explicitly unperformed. Independent guide review is a separate release
step. No remote copy is claimed current. No borrowed exemplars, source books,
reference PDFs or generated prompts belong in this portable source bundle.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
