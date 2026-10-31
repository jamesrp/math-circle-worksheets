# Week 63 return visit adult guide source

Writer-stage draft, not a critic or revision-stage output. Unpiloted and physically unrehearsed.

## Build

Requires Python 3, pdfLaTeX with `geometry`, `fontenc`, `lmodern`, `amsmath`, `amssymb`, `array`, `booktabs`, `fancyhdr`, and `hyperref`; and Poppler's `pdftotext`.

Place `k-1.pdf`, `grades-2-3.pdf` and `grades-4-5.pdf` beside this source directory (the same parent folder in which `facilitator.pdf` will be written). Run:

```sh
cd src
sh build.sh
```

The builder compiles twice, rejects TeX errors and overfull boxes, writes `../facilitator.pdf`, removes its temporary compilation directory, and finishes by running `check_guide.py`. It has no machine-specific TeX environment or repo import.

The checker first finds student PDFs beside the source directory; inside a checkout, it can instead locate `plans/return-visit-drafts/week-63` through ancestor directories. It pins the visually inspected student PDFs by SHA-256 and verifies their page/problem maps. Diagrams and rows were independently transcribed from those final PDFs. If any student PDF changes, re-inspect it and revise the fixture rather than simply replacing its hash.

## Verification scope

`check_guide.py` independently computes swap distances by breadth-first search on all permutations for 2--5 cards, exact-length reachability through seven moves, directed loops, every printed shortest word, fixed-point totals and exact piles, all complete catalogs, and forbidden-board counts both by full permutation filtering and nonclashing-spot inclusion-exclusion. It exhausts all 1820 four-spot boards and verifies the chain recurrence against the grid coefficients. `writer-data.json` holds the complete five-card catalogs for reproducible comparison; it is not a dependency on the student generator or its checker.

The checker does not replace visual review: diagrams, physical placement, mathematical prose and final PDF page layout need human inspection. Student hashes bind those observations to the final packet. Build and finite enumeration do not establish printing fit, preparation time or classroom readiness.
