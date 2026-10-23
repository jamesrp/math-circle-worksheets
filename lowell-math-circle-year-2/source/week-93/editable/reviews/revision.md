# Week 93 revision record

Deliverable: `final/students.pdf`, five US Letter pages, packet W93-S-v2. All seven substantial problems are preserved. This is the consolidated packet authorized by the stage override, with Grades 3–5 on pages 1–4 and Grades 4–5, ready for general reasoning on page 5. No separate K–1 packet was created. No facilitator guide or shared workflow template was edited.

## Changes

- Page 3 now gives the exact quotient `20 / 6 = 10/3` before Problem 3, instructs children to retain fraction labels, and distinguishes calculator placement estimates from exact bounds. Proposed decimal bounds require exact square checks. This supports the first repeating quotient without teaching an invalid rounded-endpoint convention.
- Problem 3 explicitly chooses its tightest bracket from the four old/new side lengths, removing the unintended unrestricted optimization question.
- Problem 4 explicitly calls for cutting its four cards from a spare copy of page 4. The shuffled order, exact values, enclosure explanation, and writing space are retained.
- Page 5's header makes readiness for general reasoning explicit. Problems 6–7 retain the general area identity, narrowing-bound investigation, and finite-termination question.
- The non-task reshaping visual on page 3 was retained and verified: input sides 1 and 3; joined 1+3 and the half-sum 2 as intermediate; output sides 2 and `3 / 2 = 3/2`, area 3. Both output side lengths are present.

## Exact print and material preparation

Per working pair, print one full five-page packet single-sided on US Letter at 100% actual size, plus one extra copy of page 2 and one extra copy of page 4. Retain the full packet intact for mats, reference, drawing and explanations. On the spare page 2, cut out the two rectangles A and B; use the corresponding squares on the intact page as targets. On the spare page 4, cut around all four card boxes; supply those four loose cards for Problem 4, leaving the main page's explanation area and Problem 5 intact. The student prompt also explicitly identifies the spare copy. Provide scissors and 24 equal square tiles for the first investigation, plus pencil and optional calculator. The drawings on page 1 are a recording grid, not a physical tile-fit mat.

The page 2 scale is 1.5 cm per mathematical unit in both axes: rectangle A is 9 by 3 cm, its square is 6 by 6 cm; rectangle B is 6 by 3 cm, its square is 4.5 by 4.5 cm. Problem 4 cards are 7 by 2 cm. Do not cut the only student working copy or print with fit-to-page scaling.

## Verification

- Rebuilt `final/students.pdf` from `final/src/build.py` using pdfLaTeX; five pages; no overfull, underfull or warning entries in the compilation log.
- Rendered and visually inspected every final page in `final/render/page-01.png` through `page-05.png`. Headers, footers, all seven problem labels, cards, fraction labels, number lines and answer space are readable with no overlaps or clipping. Page 1's 24-by-20 grid, page 2's four equally scaled cutting shapes, page 3's complete worked visual and all three task rows, page 4's movable-card cut boundaries, and page 5's schematic diagrams were checked.
- Re-ran the independent review's exact arithmetic checker against the final PDF. All seven problems and 9,150 rational cases passed; printed cutting-shape geometry remains correct. Results are in `final/verification.txt`. General conclusions rely on the algebraic and geometric arguments recorded there, not finite sampling alone.
- Packed only `build.py` and `students.tex` into `final/source.zip`, extracted into `final/clean-rebuild/`, and built again. The extracted-source PDF is byte-identical to the final PDF, SHA-256 `9478fffa7d62bd3f8b0c1a36ddb4b2f815b644d678fe80a0164dab67a8dc6158`.

## Remaining limits

Physical print/cut/fit rehearsal and classroom piloting remain untested. The review's concerns about introducing guaranteed bounds alongside reshaping, and about fraction arithmetic or universal reasoning requiring adult support, remain readiness hypotheses to test. The exact quotient support removes an unannounced arithmetic prerequisite; it does not establish independent classroom use. Adults may assist with reading or arithmetic while children retain the mathematical choices. Page 5 is a readiness-dependent continuation, not a completion expectation for every fourth or fifth grader. No remote upload or integration is claimed.
