# Week 77 final student/adult pair review

Date: 2026-10-07 UTC. Stage: fresh independent, review only. Reviewer read the final five-page student PDF and four-page guide, then checked the portable sources. No earlier review supplied an answer. No student/guide sources or PDFs were edited; no later stage, commit, push, or publication was performed.

## Verdict

**PASS for mathematical, digital, and portable-source review. No actionable or blocking issues found.** No revision is required by this review. This verdict applies only to the exact PDFs below. It does not establish material fit, classroom usability, observed learning, or readiness without the stated physical rehearsal. Those remain untested.

- `final/students.pdf`: SHA-256 `e27735de07fee5b65d5f8ea1be06e260f4724a12ca039e10bd8b8d704a4d4787`; 5 US Letter pages; 60,534 bytes.
- `final/facilitator.pdf`: SHA-256 `86d65e917d1b11f04e107921a26189a68cc777a03b53f65c9d9d1021fd6775fc`; 4 US Letter pages; 120,076 bytes.

## Located review of the mathematical answers

A new checker in `pair-review/independent_math.py` transcribes the printed boards and uses exhaustive edge/face subsets. It does not import the student checker, guide checker, previous reviews, or persistence libraries. The guide checker was inspected and run separately, after the reviewer's computation had been written and run. Results and full case data are in `pair-review/independent-math-results.json`.

### Student page 1; guide page 2: launch and Problem 1

- The non-loop demonstration is correct: XY + YZ plus the boundary XY + YZ + XZ leaves XZ. Its input, intermediate duplicate cancellation, and output are visible before first use.
- Exactly three nonempty edge loops occur in the divided square: P = {AB, BC, AC}, Q = {AC, CD, DA}, and R = {AB, BC, CD, DA}.
- P dies when ABC is filled; Q dies when ACD is filled. R survives either single filling and dies after both. The cancellation identities R + P = Q and R + Q = P are correct.
- The guide correctly tells the adult to add AC before filling either half, even when AC is not part of the saved outer rim. Saved edges and test tokens are distinguished.

### Student page 2; guide page 3: Problem 2

Starting with AB, BC, CD at stage 0, the exhaustive schedules are:

| Stage 2 | Stage 4 | Stage 5 | Stage 8 | Saved loop | Death | Meets target |
|---|---|---|---|---|---:|---|
| DA | AC | ABC | ACD | R | 8 | yes |
| DA | AC | ACD | ABC | R | 8 | yes |
| AC | DA | ABC | ACD | P | 5 | no |
| AC | DA | ACD | ABC | P | 8 | yes |

Thus all three successful schedules and the single unsuccessful alternative are correctly given. Two edge orders times two face orders is a complete argument; the guide does not substitute case testing for that argument. All four have counts 0, 1, 2, 1, 0.

### Student page 3; guide page 3: Problem 3

The four solid edges are AC, BC, CD, CE, with a genuine shared vertex at C. Starting from that tree:

| Stage 2 | Stage 4 | Stage 5 | Stage 8 | First loop dies |
|---|---|---|---|---:|
| AB | DE | ABC | CDE | 5 |
| AB | DE | CDE | ABC | 8 |
| DE | AB | ABC | CDE | 8 |
| DE | AB | CDE | ABC | 5 |

These exactly match the guide. Each saved triangular rim requires its own tile; another chamber cannot cancel it. Counts are identical in all four cases and do not determine first-loop death. The two witness schedules requested by students are supplied without falsely assigning identity to a visible cavity.

### Student page 4; guide page 3: Problems 4 and 5

- The unchanged simultaneous-stage schedule has hole counts 0, 1, 1, 0 at 0, 2, 4, 8 and no finished stage with two holes. The guide honors the complete-batch convention.
- Of the four one-item modifications, AC to 3 and ABC to 5 are the only legal ones, and both create a two-hole finished stage. AC to 5 and ABC to 3 violate face-before-boundary legality. The saved outer rim still dies at 8 in both legal modifications.
- The no-resurrection proof is valid for every growing board: a particular triangle selection witnessing zero remains available forever, so the exact same saved edge list still cancels. This argument does not need planarity. Resetting is explicitly distinguished from continuing a build.

### Student page 5; guide page 4: Problem 6, including the fresh-board order question

The fan has eight edges meeting at the explicitly marked center O; no crossing is silently treated as a vertex. Among all 15 nonempty even edge subsets, exactly these four meet the first condition:

| Label | Saved edges | Unique required tiles |
|---|---|---|
| L0 | AO, CO, CD, DA | CDO, DAO |
| L1 | AB, BO, CO, CD, DA | ABO, CDO, DAO |
| L2 | AO, BO, BC, CD, DA | BCO, CDO, DAO |
| L3 | AB, BC, CD, DA | ABO, BCO, CDO, DAO |

All four are legal connected loops. Their pairwise differences are boundaries of the initially filled ABO and BCO, so they represent the same nonzero class at that stage. Each needs both remaining triangles, hence survives either possible next filling and dies at the last.

All six unordered pairs were checked in all 24 filling orders. Only L1/L2 permits both strict orders. The guide's two explicit orders produce deaths (3,4) and (4,3), respectively. As an additional check, that pair ties in 12 orders, puts L1 first in 6, and L2 first in 6; the guide correctly promises existence of both orders, not strictness in every order.

The completeness/impossibility proof is sound: each fan triangle owns one outside edge, making the required face set unique. All candidate sets contain CDO and DAO. Five pairs are nested, so their completion order cannot reverse. Only the L1/L2 sets are incomparable. No visual or arbitrary barcode matching is used.

## General mathematical claims and scope

Located at guide pages 1 and 4:

- The guide starts with actual facts, assumptions, and limits before timing or individual solutions. It states finite planar triangulation, nonoverlapping triangle interiors, common-face intersections, increasing pieces, legal face boundaries, whole tied batches, and mod-2 cancellation.
- Injectivity of the planar triangle-boundary map is justified: a nonempty finite selected union has an exposed outside edge. Therefore two different fillings cannot have the same boundary.
- The graph cycle-space formula E - V + C follows from a spanning forest; the independent triangle boundaries subtract F. The resulting E - V + C - F counts independent holes, not all drawn cycles.
- The square formula [b,max(u,v)) and [s,min(u,v)) is correct under b < s <= min(u,v), using the first-filled triangular rim with the old outer rim as the basis. Zero-length intervals are omitted, and death-stage disappearance is explicit. The direct-sum calculation and inclusion-map interpretation supply the proof; finite computations are supplemental.
- Independently computed inclusion-map ranks reproduce all printed square/joined/tied-stage barcodes and the formula on 296 legal finite schedules, including equality cases. A supplemental check covers all 555 legal subcomplexes of the three printed boards and verifies the count formula and boundary monotonicity.
- The guide expressly warns that an arbitrary saved loop's first appearance and eventual disappearance do not by themselves define an interval generator. It does not claim a general stability theorem, identify long life with signal, or call finite tests an infinite proof.

## Teaching route, preparation, and fit

Located at guide pages 1–2 and each problem's hints:

- The single Grades 4–5 prototype is explicitly prerequisite-led. The three-child target group has an organizer, two active builders/testers, and a rotating referee. Short-label reading, unchanged records, and pair cancellation are listed. No algebra or multiplication is required for the first concrete route, and formal homology remains adult content.
- The other eight children and two adults are acknowledged; the guide requires separately prepared activities rather than pretending this packet serves their tables.
- A specific 3-minute launch names the adult actions, child's legal tile check, and cancellation action. Handling time precedes the main problems. Problems 1–3 form the first route; 4 or 5 is optional; 6 has a separate 15–25-minute return visit. The fallback stays with a single square and rotating roles. These are sensible proposed timings, not observed evidence.
- Hints begin with an object action or question, progress in order, and leave constructions and claims distinguishable from completeness proofs. Problem 6 explicitly allows a checked construction to remain such until the adult-supported necessity argument is understood.
- Preparation arithmetic is internally correct: 16 student sheets, four guide sheets, 17 tiles including eight spares and the launch triangle, 44 edge-token cards including launch tokens and blanks, seven active edge strips plus two spare lengths, and six numbered plus two blank stage cards.
- Three copies of every edge token suffice even when a saved-loop token and both incident face-boundary tokens are out simultaneously. All required labels are included; reverse labels denote the same edge. Board-specific tile envelopes avoid confusing the differently sized ABC pieces.
- Final-PDF vector measurements confirm square sides of about 6.2001 cm on pages 1, 2, and 4 and diagonals 8.7682 cm; the guide's 6.2 cm and approximately 8.8 cm instructions match. The page-3 missing edges are 5.8001 cm, and the fan is 8.0001 cm square. Matching-copy cutting at 100% is coherent. These are digital dimensions, not a physical fit test.
- The initially unshaded fan is handled correctly: the guide explicitly instructs the adult to place ABO and BCO before starting. It requests fit, label-visibility, cancellation, and reset rehearsals and candidly says they have not been performed.

## Page-by-page visual inspection

All nine final pages were rendered at 110 dpi and opened individually under the PDF skill. Renders are retained in `pair-review/render/`.

- Student 1: both rule paragraphs, input/intermediate/output cancellation visual, square labels/dashes, Problem 1 and two record areas are clean.
- Student 2: stage list agrees with the three solid/two dashed square edges; ample schedule space; header/footer intact.
- Student 3: four solid arms and two dashed closing edges, marked central vertex, schedule records, and final comparison question are legible and separated.
- Student 4: tied-stage wording and diagram match; Problems 4/5 and their answer areas fit without collision.
- Student 5: all eight fan edges, corner and center labels, two saved-edge records, and both fresh-board outcome records are intact.
- Guide 1: theorem-first opening, prerequisite/staffing scope, and print/strip preparation fit cleanly.
- Guide 2: continued preparation, launch, hour, fallback, Problem 1 solution/hints, and Problem 2 introduction are complete.
- Guide 3: both full schedule tables, four timing changes, no-resurrection proof, and hints are readable and unclipped.
- Guide 4: four fan edge/face rows, reversible-pair witnesses, necessity proof, adult proofs, source URL, and observation prompts all fit.

No missing labels, incorrect polygon proportions, overlap, clipping, missing glyphs, inconsistent IDs, or damaged footers were found. Programmatic text bounds also lie within all nine pages. All fonts are embedded.

## Portable build and provenance

Only `facilitator.tex`, `build.py`, `check_math.py`, and `README.md` were copied into `pair-review/isolated/source/`. From that isolated directory, `env -u TEXMF -u TEXFORMATS python3 build.py --out ../output` passed. The builder initializes a temporary format from the installed TeX distribution; no run-local format, sibling student source, research file, or unbundled custom asset was required.

The rebuilt PDF has identical extracted layout text, identical decoded content streams on every page, and byte-identical 110-dpi PNGs on all four pages. Its PDF hash differs because PDF build metadata/IDs differ; content/raster equality, rather than byte-identical whole PDFs, was the requirement. The minimal TeX installation emits a missing default `pdftex.map` warning; the source loads installed Computer Modern maps explicitly. All fonts are embedded and the rendering matches, so this is not a deliverable defect. No overfull or underfull boxes or missing-character warnings were found.

The portable guide folder has exactly those four owned files and no symlinks. There are no papers/books, borrowed figures, workflow examples/prompts, fonts, raw reports, or format dumps inside it. Standard TeX Live/MacTeX is the documented prerequisite. The student source folder likewise contains only its four owned source/build/check/readme files.

The primary [paper linked by the guide](https://pub.ista.ac.at/~edels/Papers/2002-J-04-TopologicalPersistence.pdf) was opened directly. Its mod-2 boundary and age-filter material appears on PDF pages 2–3; Section 3 starts on page 4 and treats persistent classes, pairing, and time-based persistence. The [author's publication list](https://pub.ista.ac.at/~edels/Papers/) and [institutional record](https://research-explorer.ista.ac.at/record/3996) confirm the named authors, 2002 publication, and title. Attribution is substantive and accurately bounded. The elementary square, joined-board, and fan tasks are identified as independently devised, not as copied source exercises.

## Untested limits and retained evidence

Unrun: actual printing/scaling on the intended printer; physical cutting and fitting; handling and token/label visibility with children; launch visibility for the whole group; a real cancellation/reset rehearsal; adult preparation time; one-hour pacing; and classroom learning/piloting. No digital result establishes these. No revised PDF or public publication was created by this review.

Evidence:

- `pair-verification.json`: checks, exact PDF hashes, inspected page counts, and limits.
- `pair-review/independent_math.py`, `independent-math-results.json`, `independent-math.log`: fresh mathematical computation.
- `pair-review/check_pdf_output.py`, `pdf-output-results.json`, `pdf-output-check.log`: dimensions, text bounds, content and raster comparison.
- `pair-review/render/`: all nine inspected page images.
- `pair-review/isolated/`: portable-source copy, rebuild output/logs, rebuilt text and four rasters.
- `pair-review/source-sha256.txt`, `students-fonts.txt`, `facilitator-fonts.txt`: source manifest and font inspection.
