# Week 54 facilitator guide

Original adult guide for the final combined student packet W54-S-v1 (9 pages): Grades 2–5 on student pp. 1–5, Grades 4–5 on pp. 6–9. The guide is W54-FAC-v1, 8 US Letter pages. It is an unpiloted adaptation; all physical pretests are unperformed. K–1 uses accepted prior Week 1 material, not a new Week 54 student packet.

Build from any location:

```sh
sh build.sh /absolute/output/directory
python3 check_answers.py /absolute/output/directory/answer-checks.json
```

`build.sh` writes `facilitator.pdf`, compiles twice in a temporary directory, and removes the intermediates. Requires pdfLaTeX/TeX Live with standard packages: geometry, fontenc, lmodern, helvet, amsmath, amssymb, array, tabularx, booktabs, enumitem, fancyhdr, tikz/arrows.meta, hyperref. The checker uses Python 3 standard library only, reads no other repository files, and transcribes final student inputs independently of student verifiers and source comments. `answer-checks.json` records the complete printed catalogs, constructions, all-route endpoint and finite checks. General proofs are in the guide; finite checks supplement them.

Mathematical and pedagogical provenance is stated on guide p. 8, with precise book titles/pages and plain repository reference paths. The verified research record is `plans/new-themes-52-63/week-54/research.md`. Wording, answer tables, route examples and guide source are newly authored. No borrowed exemplar text, workflow prompts, books or reference PDFs are bundled here. Root `REPUBLISHING.md` was read and left unchanged.

QA renders, extracted text and isolated rebuilds are outside this portable source folder in `../guide-qa/`. Every final guide page was rendered with PyMuPDF and visually inspected; a clean isolated source copy was built and compared for text, dimensions and rendered pixels. This is digital verification, not physical rehearsal or classroom piloting. The parent stage handles the subsequent independent guide review and release packaging.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
