# Week 53 student packet: revised review copy

One original combined student packet, nine US Letter pages. Pages 1–4 carry the approximate band Grades 2–5; pages 5–9 carry Grades 4–5. Problems are numbered 1–9 across the packet. This revision follows fresh independent critic and mathematics reviews. Facilitator-guide authoring and guide review are separate later stages. No facilitator guide is included.

## Build

From this source directory, run:

```sh
python3 build.py --output .
# Or: python3 build.py --output /absolute/path/to/output
```

The command writes `students.pdf` and puts generated TikZ, TeX logs and compiler intermediates in `output/.build/`. It uses no repository files and no network. Source files can be copied or extracted to any new folder; the output directory can be anywhere writable. Python bytecode generation is disabled in the builder so that source stays clean.

Dependencies: Python 3 standard library and `pdflatex` with the standard TeX Live packages geometry, fontenc, helvet, TikZ/PGF, fancyhdr, array, xcolor and microtype. `--pdflatex /path/to/pdflatex` selects another installed compiler. No third-party images, copied book text, prompt files or reference PDFs are needed.

## Editable files

- `students.tex`: original student wording, page order, typography and workspace.
- `networks.json`: original vertex coordinates, available edges, prices and expected finite answers. Diagonal label fractions are editable independently of link geometry.
- `diagrams.py`: original TikZ network asset builder. Prices are offset from links; circles are the only junctions. Compact diagrams retain the same labeled graph for purchase records.
- `build.py`: portable compiler wrapper.
- `verify_math.py`: original exhaustive enumeration of all connected subsets, all spanning trees, optimum counts, improving exchanges, cut/cycle evidence and all 4,096 inverse-price assignments.
- `verify_output.py`: reads actual PDF vector paths and text to reconstruct every graph, selected link, price numeral, price dot and vertex spacing; also checks headers, footers, page sizes and text bounds. It can compare rebuilds by full extracted text, dimensions and exact 144 dpi pixel arrays.
- `DESIGN-NOTES.md`, `MATH-NOTES.md`, `PROVENANCE.md`: prerequisites, physical constraints, mathematical assumptions and exact source lineage. These are source/check notes, not a facilitator guide.

## Verify

```sh
python3 verify_math.py --report /absolute/path/to/qa/math-checks.json
python3 verify_output.py /absolute/path/to/output/students.pdf --report /absolute/path/to/qa/pdf-checks.json
python3 verify_output.py /path/to/original/students.pdf --compare /path/to/rebuild/students.pdf --report /path/to/qa/rebuild-checks.json
```

`verify_output.py` requires PyMuPDF. In the current workspace it was run using `/Users/jamespfeiffer/math-circle/tmp/bonus-35-51-venv/bin/python`. Mathematical enumeration and the build itself require only the Python standard library. Render inspection remains necessary in addition to the scripted checks.

The writer checked all fixed examples and actual diagrams. Separate fresh adversarial and mathematics reviewers inspected the nine-page draft; the math reviewer independently transcribed the graphs, enumerated every connected subset and all 4,096 allowed inverse-price assignments, and reconstructed all 27 printed graph instances without importing writer code/data. This revision clarifies Problems 5, 7 and 8, corrects source spacing figures, and retains every graph. Revision QA independently reruns the reviewer audit on the final PDF, checks actual final text/geometry, visually inspects every page, and compares both a standalone-copy and an extracted-ZIP rebuild by text, page dimensions and exact 144 dpi pixels. Reports and renders live outside this source in the run's `revision-qa/` folder; `final/revision.md` records coverage and limits. These digital checks are separate from physical/classroom evidence.

Print single-sided at **100% / actual size**. This revised review copy is **unpiloted**. Exact physical handling, marker legibility, payment/refund behavior and classroom fit have not been rehearsed. No published or remote copy is claimed current.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
