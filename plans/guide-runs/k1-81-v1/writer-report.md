# Week 81 K–1 guide: writer-stage report

## Delivered

- `draft/k1-guide.pdf`: **4 pages**, US Letter, pdfLaTeX, W81-K-FAC-v1.
- `draft/src/`: portable `k1-guide.tex`, generated `verified-data.tex`, independent `check_guide.py`, `build.sh`, and rebuild README.
- Writer stage only. No critic/reviser stage was run; no student or published file was edited. No commit or public write was made.

The theorem-first overview states that exactly the all-even starts favor the second player, explains the legal copying reply and the unique move to all-even from other starts, and proves capped termination and shortest/longest lengths with the weight a + 2b + 4c. It distinguishes trials, conjectures and explanations, and refers to the original overview for the older bands' uncapped destination. The route gives an anchored-adult role without adult move selection, a non-task visual launch, a sixty-minute selection rather than a seven-page completion expectation, and complete solutions/hints for all twelve final problems.

**Exact replacement:** only the paragraph beginning “K–1, adult-led, after the launch” in **Materials and common launch**, **page 2** of `lowell-math-circle-year-2/week-81/week-81-facilitator.pdf` (W81-FAC-v2), after the student pages are approved. The original general overview, shared launch and older routes stay intact.

## Evidence

- Read the final K–1 PDF and its source, outline, both prior student reviews and K–1 drafts README; consulted the original Week 81 guide, all five shared packet pages, material source, owned source notes, and the Week 98 guide/model source. No `.agents/skills` directory was present in this worktree. The original reference books named in the owned notes were absent, so no claim of newly reading those books or validating their pedagogical details is made.
- Rendered and personally inspected **all seven final student pages** at 100 dpi; all five shared student/material pages at 90 dpi; the original replacement section and the first two model pages. Directly counted PDF vector circles in every task bucket and the 21 rule-diagram buckets. The checker also verifies problem-to-page mapping, final shared-rule text, blank answer slots and the exact inspected student PDF hash.
- Wrote an independent solver, not importing the student checker or generator. Exhaustively explored all descendants for one-bucket starts 0–12, two-bucket starts 0–8 per bucket, and three-bucket starts 0–5 per bucket (**781 memoized states visited**). Checked winning/losing outcomes, unique winning moves, copy legality from every tested all-even start, all possible game lengths, Problem 5's complete reply list, all splits for totals 4/5/6, all requested board maxima, the peak constructions, and the non-task demonstration. Printed tabular answers are generated from these recomputed results; hard-coded answer claims have explicit assertions.
- Confirmed actual shared-board dimensions from PDF vector outlines: three 56 × 139 mm buckets and two 86 × 40 mm Supply/Removed boxes; 5 mm bucket gaps and 39 × 27.5 mm cards also match the owned material source. About 30 counters plus reserve remains the week's kit; all printed task plays use at most 14 counters in total. The suggested ≤20 mm counter diameter is a fit recommendation from the outline, **not a physical test**.
- Built twice with no LaTeX errors or overfull boxes. Rendered the **final four guide pages at 125 dpi and personally inspected every page**, including the demo, all answer tables, headers, footers and bottom-of-page spacing. No clipping, overlaps or missing glyphs found. Build/check evidence is in `tmp/build-check.txt` and final renders in `tmp/final-guide-*.png` (QA only, not deliverables).
- Rebuilt from a **clean copy outside the repository**, containing only `src/` and the final `k-1.pdf` beside it. The checker found that adjacent student PDF and passed there. `pdftotext -layout` output was byte-identical to the delivered guide; evidence in `tmp/clean-build-check.txt`. Local compiles used the externally supplied isolated TeX environment; `build.sh` contains no machine-specific environment or absolute paths.

Final guide SHA-256: `b02143fc6998109beb35fbf739c0b14f3b281808642542e46ef153bff7b9e517`.

Unchanged student PDF SHA-256: `a6a6e52ed4a391ccd6e10f7cd7444c779f612e73be21e58d97ac27d46d264738`.

## Final-page issues and limits

No mathematical error was found on the final student pages. The old reviews are **not** a current answer-order key: Problem 1 now orders the starts 2, 5, 3, 6, 4, 7, 11, 10; the three-bucket winning-move task is now Problem 10 on page 6; Problem 11 on page 7 has longest lengths 6, 7, 12; and Problem 12 now starts at (2,2,2), not (3,3,3). The writer guide uses these final instances and numbering.

Residual usability risks, not observed classroom findings:

- Optional refills must not become mandatory; Supply/Removed must stay distinct, and Removed must be emptied at each reset. The guide gives a two-outcome non-task demonstration and reset instructions.
- Problem 4 can monopolize one adult if every child plays every combination. The suggested route rotates selected challenges, and the adult play card gives an executable policy for every later position, not only the starts.
- Problem 6 has five slots per row but only three and four answers; the guide explicitly treats unused slots as spare recording space and accepts empty buckets and ordered splits.
- The small answer buckets and close neighboring labels (notably the three separate starts in Problem 9) need child handling/drawing checks. Use the large shared board for real counters and adult recording when requested; do not place counters on the miniature diagrams.
- Problem 12 permits a 14-move game, beyond the optional 12-move counting route; the guide asks for an ending argument, not a count to 14.

No required printable object is absent from the week files. Loose counters, pencil and scrap-paper masks are ordinary nonprinted kit items. **The guide remains unpiloted and physically unrehearsed:** exact counter fit, printing/cutting, manipulation, drawing comfort, adult workload, rule retention and timing were not verified with materials or children. Claude critique is next.
