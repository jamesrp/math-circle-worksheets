# Week 57 facilitator guide source

**October 23, 2026 card fixes** (`W57-FAC-v2`, with student packet `N57-S-final-v3`): Later on October 23 the guide became W57-FAC-v3: it names the fixed tables "K–1, 2–3 and 4–5" where it printed the roster code "KK11, 3333 and 445" (K, K, 1, 1 / four third graders / 4, 4, 5); W57-FAC-v2 is in `archive-before-roster-label-fix-2026-10-23/` beside the print copy.
an adult-led K–1 route with four or five squares on p. 3 and a plain-words key; P7
does not accept "each value is the area"; the joining limits on p. 1 say a seam of
consecutive sides works; the kit pieces come from `week-57-materials.pdf`, with a
smaller untested cutting forecast; a (5, 4) triangle with base 2 and height 6 in P5's
table; process residue removed from p. 10.
Later the same day it became `W57-FAC-v4`, after an independent critic's review: the readiness map on p. 1 says the K–1 route is on guide p. 3 and uses extra copies of the student p. 4 grids, where "(p. 3)" read as student p. 3, whose 5 × 5-dot boards cannot hold a 1 × 5 strip. Only that sentence and the footer changed.

Separate guide authorship from the final ten-page student packet, version
`N57-S-final-v2`, October 4, 2026. The guide was `W57-FAC-v1`, ten US Letter
pages. It preserves the corrected general-triangle proof, full P1–10 keys,
independent area checks and actual-board witnesses. It does not revise students.
The new adaptation is **unpiloted**. Physical print/piece fit, cutting/handling,
staffing and pacing have not been rehearsed. The required checks are on guide p. 2.
That page retains the full reusable 51-student-sheet stock and offers a 25-sheet
first-visit option for Problems 1–3. The preparation forecast is explicitly
untested: 45–75 minutes (now 20–35 with the printed materials pages) for one-time cutting/bagging, 15–25 for printing/rehearsal,
then reuse the pieces with 10–15 minutes of sorting/restocking/selected printing
plus rehearsal of new procedures. These are operational estimates, not pilot data.

## Portable build and checks

Python 3 and `pdflatex` must be on PATH. Standard TeX Live/MacTeX packages:
article, geometry, fontenc, lmodern, helvet, amsmath, amssymb, array, tabularx,
booktabs, enumitem, fancyhdr, TikZ and hyperref.

```sh
python3 build.py --output-dir /absolute/path/to/build
python3 verify.py --qa-dir /absolute/path/to/qa
python3 verify.py --pdf /absolute/path/to/build/facilitator.pdf \
  --qa-dir /absolute/path/to/qa --check-rebuilds
```

Mathematical checks use only the standard library. PDF/render/rebuild checks
require PyMuPDF (`pymupdf`). The repository runtime is
`tmp/bonus-35-51-venv/bin/python`. No repository files are required by this source.
The builder accepts any output directory, fixes metadata time and removes TeX
intermediates. Logs stay outside this source. The verifier recomputes inside and
boundary dot sets, exact geometric area by horizontal-strip integration, a second
shoelace check, domain assumptions, construction-board fit, geometric certificates,
seam sets, hole subtraction and all 2,148 small-grid proof-bridge cases. Counts and
area are computed before comparison with Pick. Finite tests check implementation;
the TeX contains the general geometric argument.

With `--pdf`, the verifier checks all ten actual pages' text, header/footer, Letter
dimensions and text bounds, and renders every page to the QA directory. It also
measures the compact proof diagram's four sides, two diagonals, 49 dot centers
and equal 7 mm x/y axes (adult illustration, not a cutting template). With
`--check-rebuilds`, it copies these four source files, builds independently, ZIPs
and extracts the source, builds again, and requires identical page text, dimensions
and every 144-dpi rendered pixel. The resulting ZIP is QA evidence, not a release
or publication. Visual inspection is separate and is recorded by the guide author
outside the portable source.

## Provenance and scope

The guide credits Givental, Nemirovskaya and Zakharevich, *Math Circle by the Bay*
(AMS, 2018), printed pp. 129–134, Problems 5.30–5.34; Cambridge NRICH's *Pick's
Theorem* and *Proof of Pick's Theorem*; and Rozhkovskaya, *Math Circles for
Elementary School Students* (AMS, 2014), Lesson 3 “At the lesson” item 1 and
Lesson 8 item 2. Exact URLs, roles, source observations versus local inferences,
organizer precedents and prior-use distinctions are on guide p. 10. The overall
additivity route is credited to NRICH; the general-triangle quadrilateral bridge
is the independently repaired argument for this packet, not attributed there.

Wording, layout, figure, exact preparation arithmetic, builders and verifier are
authored here around established mathematics. Some checked coordinate data comes
from the new outline/student packet. No new-mathematics claim is made. These four
files contain no third-party excerpts, downloaded originals, workflow prompts,
borrowed exemplars or intermediate renders. `REPUBLISHING.md` was read and left
unchanged; attribution does not establish publication permission. Prior packets,
indexes and remote copies were not changed or certified by this guide stage.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
