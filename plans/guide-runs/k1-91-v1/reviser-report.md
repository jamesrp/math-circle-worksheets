# Reviser report: Week 91 K–1

Revised `final/k1-guide.pdf` is **4 US Letter pages**, footer **F91-K-FAC-v2**, serving the unchanged seven-page **F91-K-v1** student PDF. Every numbered finding was addressed: 1 must-fix, 5 should-fix and 7 minor; none declined. Original draft and critic evidence remain untouched. This is the reviser checkpoint only; packaging and insertion into the existing guide are deferred.

## Finding dispositions

| Review finding | Disposition and reason |
| --- | --- |
| Must 1: failed search and impossibility | Fixed, guide p. 1. Successful trials show possibility; exhausting both switch starts or all eight tree starts can prove impossibility. Unsuccessful coin trials are explicitly distinguished. This agrees with the finite choice spaces and the exhaustive checker. |
| Should 1: P7 first/last claim | Fixed, p. 4. Counter 5 repeats counter 1 and counter 8 repeats counter 4. The first/last condition is conditional on B being that exit. Removed the false general restriction on B; all eight starts checked. |
| Should 2: tree transition and slip recovery | Fixed, p. 3. Child demonstrates both stops and both move/flip steps before P5. Wrong flips/resets trigger clearing exits, restoring the saved start and restarting. One demonstration counter reveals no P5 answer. |
| Should 3: first route and priorities | Fixed, p. 2. P1–2 receive 20–25 minutes, P2 pictures 1/3/4 come first, setup includes the two-minute demonstration, P5 starts only if 15 minutes remain before packing. The fastest full route totals 60 minutes; longer switch work displaces P5. Timings remain estimates. |
| Should 4: recording burden | Fixed, p. 2. Quantified 40 P1 letters, 42 P3 letters, 16 predictions and 78 arrow circles. One written row per switch start suffices; repeat questions can be watched and coin piles read directly. Slanted strokes or adult drawing from a child's saved-card choice are allowed. |
| Should 5: first-use evidence | Fixed, p. 4. Record preparation time, problems reached, missed/wrong flips, saved-card accuracy, who wrote and reasons for crossing pictures out. |
| Minor 1: discoveries | Fixed, p. 1. Removed overview “programs” wording and stated extra-counter/first-arrow, predictable future, four-exit and two-card discoveries. |
| Minor 2: launch labels/size | Fixed, p. 2. Labels match student “start / move / flip”; scrap circle at least 24 mm across. |
| Minor 3: scissors/glue | Fixed, p. 1. Card-making tools separated from demonstration scrap paper. |
| Minor 4: strips | Fixed, p. 1. Optional counting aids for P4/P7, two per pair. |
| Minor 5: reviewer language/repetition | Fixed. Removed the identified reviewer-facing boilerplate, trimmed repeated saved-card/card-word definitions while retaining the launch and task-specific hazards. Extra operational guidance makes the revision approximately 2,476 extracted words versus the critic's 2,313-word draft; no hard word limit applied. Still four pages. |
| Minor 6: child explanations | Fixed, pp. 3–4. Adult asks why after children show P5, and asks the child to draw both P8 settings. |
| Minor 7: insertion overview | Fixed, p. 4. Future insertion instructions also update the existing base guide's p. 1 “not an independent packet” sentence. Existing guide itself remains untouched. |

## Student-page and materials verification

Rendered and read all seven final student pages, all six existing-guide pages and all seven materials pages. Actual student map is p. 1 P1; p. 2 P2; p. 3 P3/P4; p. 4 P5; p. 5 P6; p. 6 P7/P8; p. 7 P9. Verified the diagrams, dots, numbered exits, totals and table order against the printed key. P5 has nine trees (one spare), P7 two, P8 three (one spare), P9 four. P1 has four ten-box rows and P3 six seven-box rows.

Materials F91-M-v1: p. 1 one switch (32 mm circles); p. 2 landscape four-exit board (24 mm switches, 30 mm exits); p. 6 seven tree-card pairs and four road-card pairs, with folded tree cards 18 × 22 mm; p. 7 four strips of twelve 15 mm squares, three entry markers and a 50 mm scale bar. Roads and eight-exit board are excluded from the K–1 table. Two added K–1 kits need 14 tree cards, 32 supplied counters no wider than 12 mm, two coins, two copies of pp. 1/2/6 and optionally one p. 7 (four strips). Each kit uses three working cards, three saved cards and one spare. The approximately 30 minutes of extra preparation is untimed. No printed or student files changed.

## Mathematical verification

The portable `final/src/check_guide.py` independently implements follow-arrow-then-flip as a graph, binds the student PDF by SHA-256, verifies problem/page mapping and checks answers against the compiled guide text. It passes for both switch starts, all eight tree starts, all seven-toss coin words, all 256 eight-toss prediction words and 488 four-counter windows. The preserved independent critic checker also passes; its draft-guide checks concern the original evidence, while the final checker verifies the revised PDF.

- P1 alternates ten arrivals, five at each exit.
- P2 starts in picture order: X; either; Y; impossible; X; impossible.
- P3 has 42 of 128 orders producing 5/2 in either direction; missing this across six independent trials has probability 9.198794%.
- P4 counters 5/8/7/4 are same/other/same/other relative to counter 1.
- P5 all eight starts give one arrival at each exit and restore all three cards after four counters. Printed first-four key verified in full.
- P6 successful-start sets in printed order: all eight; LLL/RLL; none; all eight; LRR/RRR; none.
- P7 B first at counter 5: LRL/LRR; B last at counter 8: RLL/RLR. Every start's second-arrival times are 5,6,7,8; counter 5 repeats 1 and counter 8 repeats 4.
- P8 RLL/RRL only. P9 AD: LLR; DC: impossible; CB: RRL; BA: impossible.

## Student-page issues and guide workarounds

No student mathematical error was found. Student pictures are small recording diagrams, so use the full-size material boards. The pages do not separately draw the lower-card stop; the added tree demonstration supplies it. Preserve starts off-board: odd switch runs reverse the working arrow and six tree counters reverse each lower arrow. P4's printed 5/8/7/4 ordering is handled by guessing first and recording arrivals chronologically in one run. Full written completion is optional; P5/P8 spare frames need no invented answers. A coin missing a target is not evidence of impossibility. These are guide workarounds; student pages remain unchanged.

## Build and visual QA

`bash final/src/build.sh` compiled twice with real pdfLaTeX 2026, with no errors, missing glyphs or overfull boxes, then passed the checker. Rendered and inspected every final page with Poppler `pdftoppm` as the authoritative rasterizer; checked all headers, footers, tables, arrows, spacing and page breaks. Page 2 and 3 text stays clear of the footer. Rendered/read every served student page with Poppler as well. The alternative fitz renderer's display clipping was not used as evidence of a PDF defect.

A clean directory outside the repository contained only copied final source plus the unchanged sibling `k-1.pdf`. Its two-pass build and full checker passed. Extracted layout text was identical, and the rebuilt PDF was byte-identical to the final PDF. Source contains no machine-specific paths or generated prompt dependencies. Build leaves no LaTeX intermediate files in the source tree.

Final PDF SHA-256: `4319fed89664d3c1d14f426f9fe2c7085e9058eb6b52ecdf6e89b709e93cbd1f`.
Student PDF SHA-256: `bbf6588bb112f7eadc9f4c480e50315baa44615ad0b3da7c228d04e8082c68c8`.

## Limits and remaining dependency

Untested with children and physically unrehearsed: no actual cutting/folding/gluing, flip handling, counter fit/piles, card-copy accuracy, staffing or timing trials. Mathematical and PDF checks establish the stated content/layout only. The later packaging stage must wait for catalog integration, replace the indicated base-guide section, update its p. 1 overview and retain the shared launch/older-band solutions. No integration or git operations were performed by this reviser.
