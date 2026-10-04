# Week 8 return-visit revision stage

Revision candidate: `final/return-visit.pdf`, **five landscape US Letter
pages**, packet id `F08-RV-v1`. One shared companion has three numbered
investigations and page-level entry bands. There are no separate variants.
Editable, portable sources are in `final/src/`.

## Changes and review resolution

- Problem 1 now requests a rule for all two-pile starts **with at least one
  counter**, excluding the undefined empty start from the game that ends
  when the last counter is taken.
- Start 7 now shows `(2,0)` instead of `(3,4)`, providing a purposeful
  contrast with `(1,0)`. Start 7 remains a first-player win: remove one
  counter and leave the last counter for the opponent.
- A rule-record line sits below the three unchanged 2.9-by-1.4-inch pile
  mats. The task text wraps to two clear lines; neither the cards nor the
  mats were reduced.
- The footer identifies the revised candidate rather than the writer
  draft. The source checker now checks the replacement, parses every
  printed start and worked example from the actual source, verifies both
  worked moves, and checks the full actual four-by-four rook domain.
- The adversarial critic's five-by-five board request was superseded by
  the coordinator and parent agent's confirmed four-by-four adaptation,
  also recognized by the independent math review. All selected distances
  are 0 through 3 and moves only decrease them. The four-by-four boards
  support the full cancellation/invention entry, including 18 unordered
  pairs of distinct individually winning components that cancel. No
  board was enlarged or shrunk; active cells remain 0.85 inches.

## Final student-page coverage

| Page | Entry band | Status and actual-page evidence |
|---|---|---|
| 1 | Grades 2-5 | Changed: nonempty-domain wording, Start 7's two dots and empty second pile, and Rule line. All 12 starts inspected; all 50 pile dots match the checked states. Three pile mats preserved. |
| 2 | Grades K-3 | Already sufficient: six two-coin starts, before/slide/after worked visual, and a 12-cell active strip. All 18 coin marks and all number labels checked. |
| 3 | Grades 2-5 | Already sufficient: eight three-coin starts, rule space, and the same active strip. All 24 coin marks and all number labels checked. |
| 4 | Grades 4-5 | Already sufficient under the confirmed board adaptation: legal two-turn worked visual and two active 4-by-4 boards. All six worked tokens and all eight grids checked. |
| 5 | Grades 4-5 | Already sufficient: six purposeful pairs and an invented-pair record. All 12 catalog tokens and all 14 grids checked. |

All five final pages were rendered at 108 dpi and individually inspected:
no clipping, overlap, or incorrect diagrams were seen. Headers, footer id,
page numbers, stars, labels, clear tasks, and recording spaces are legible.
Every active coin and rook cell is 0.85 by 0.85 inches. Coin strips are
10.2 by 0.85 inches; active rook boards are 3.4 by 3.4 inches. All **22**
rook grids have exactly four squares per side with matching orientation.
No final PDF text span extends beyond its page.

## Reproducible checks

- `final/src/build.sh` performs the mathematics checker followed by two
  pdfLaTeX passes for remembered page anchors. The second-pass log has no
  overfull or underfull boxes. It builds from any working directory and
  has no external diagram files or repository dependencies.
- `final/build/math-check.json`: all 168 nonempty ordered two-pile and
  2,196 nonempty ordered three-pile states with entries 0-12; all 66
  two-coin, 220 three-coin, and 495 four-coin starts on squares 1-12;
  all 256 positions on two four-by-four rook boards. Actual legal-move
  recurrences agree with the formulas and the expected outcomes of every
  one of the 32 catalog starts. Worked sequences are legal; the new
  cancellation invention is feasible.
- `final/src/check_pdf.py` optionally uses PyMuPDF to check every actual
  PDF token center, all coin-row boundaries and number-label centers,
  every rook grid, active dimensions, page sizes, and text bounds. It
  also renders every page. Results: `final/build/layout-check.json`;
  inspected images: `final/render/page-01.png` through `page-05.png`.
- Clean extracted-source test: the five source files were zipped,
  extracted in `final/build/rebuild-test/extracted/`, then rebuilt from
  `/tmp` with two pdfLaTeX passes. All five pages have identical text,
  vector drawings, and rendered pixels to the candidate. Evidence:
  `final/build/rebuild-check.json` and the rebuild log.

Prepared and unpiloted. Physical printer scale/counter-fit rehearsal and
classroom use remain untested. This stage created no facilitator guide,
edited no base packet or global index, and uploaded nothing. Release
packaging, adult guide, approval, and installation remain with the parent
workflow.
