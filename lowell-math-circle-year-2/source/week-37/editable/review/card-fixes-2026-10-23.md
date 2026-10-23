# Week 37: printable kit and guide fixes from the review card, October 23, 2026

The review card is `plans/review/week-37.md` in the project, with its math check `plans/review/week-37-math.md`.

## What changed

- **Must 1 (card fix 1), guide pp. 1, 3 and 4.** The guide said a finite list of failed turns is never an impossibility proof, which rejects the natural complete argument. Page 1's overview and page 3's launch now say a failed search proves impossibility only when it covers every turn: A must go on A, and then only three turns remain. The K–1 and grades 2–3 Problem 2 keys (pp. 3 and 4) now say: "Accept a complete check: A must go on A, and all three turns about A fail." Page 1's grades 2–3 aim says the same.
- **Must 2 (card fix 2), a printable kit and guide p. 2.** New `materials.pdf` (print copy `week-37-materials.pdf`, 3 pages, US Letter at 100%, built by `materials-src/build_materials.py`): a card-stock tetrahedron net with 90 mm edges (one model per child, two for the adults: 13 sheets), letter caps A, A, B, B, C, C, D for four models per card-stock sheet (4 sheets), and a pose mat with two face-size footprints marked back, front left and front right (7 sheets of copy paper). A cap is three 26 mm equilateral triangles round one point; folded, it wraps a corner of the model and shows its letter on all three faces, held by sticky tack, so changing a letter means swapping a cap. The second B is what the B–D merge in grades 2–3 and 4–5 Problem 4 needs; the earlier spare A and C could not make it. Guide p. 2's materials section now describes this kit, says a taped card tetrahedron is the rigid "frame" the pages mention, gives counts for eleven children and about 6 minutes per model plus 30–40 minutes for the caps, and marks the kit physically unrehearsed. The pretest steps say "model" and swap caps.
- **Smaller guide items.** Launch (p. 3) stands the models on the pose mat (the guide half of should 5); the grades 2–3 Problem 4 key suggests splitting the six merges between the pairs (should 6); "frame" becomes "model" in the guide and route note; the "Status" line no longer lists problem counts (could 12).

Pages 1, 2, 3, 4 and 6 of `facilitator-guide.pdf` changed; page 5 (proofs) is pixel-identical at 100 dpi, and the three student packets rebuild with exact reference pixels.

Deferred: should 3 and 4, coulds 8–10 and "frame" to "model" on the student pages (K–1 P4, grades 2–3 P5, grades 4–5 P5–P6) change student pages and wait for a problem-file conversion; could 7 (the 0–60 minute hour) and could 11 are not done. The student-page items were made later the same day, after the conversion; see the last section.

## Verification

- `materials-src/check_materials.py` reads only the finished kit PDF: 180 checks, 0 failures. It checks headers, footers and the 100 mm scale line on every page; that the net's nine 90 mm edges bound four equilateral faces joined as a tetrahedron net, with exactly one 9 mm tab on each of the three seams; that each of the 28 caps is three 26 mm equilateral triangles round one point with the same letter in each (8 A, 8 B, 8 C, 4 D) and that neighbouring caps share straight cuts; that one model's caps build every labelling the problems ask for, including each of the six merges with one name kept; that the pose-mat footprints are 90 mm equilateral triangles with named corners; that print counts cover each table; and that guide p. 2 quotes the same sheet totals.
- `verify_math.py` runs the existing rotation-group checks and the kit checker. A clean rebuild from the extracted portable ZIP passes `verify_revision.py` and the strict `verify.py` on all five PDFs (22 pages). Every kit page and changed guide page was rendered and inspected.
- No model has been folded and no cap fitted. The adult pretest on guide p. 2 comes first. The theme remains unpiloted.

## Student-page fixes, after the problem-file conversion

The student pages became problem files first, with no wording change (`../../README.md`). Then, in the problem files, with the footer ids raised to W37-k-1-v3, W37-grades-2-3-v3 and W37-grades-4-5-v3:

- **Grades 2–3 Problem 3 (should 3):** "Keep the pair from Problem 2. Put A, B, C and D on another model in any way you like. Which of the two does it match? Can you make one that matches neither?"
- **Grades 4–5 Problem 1 (should 4):** "What has to match besides the letter at the top?" cut.
- **Grades 4–5 Problem 6 (could 8):** "Put A, B, C and D on the model. How many different models can be made if models that match by turning count as the same? Explain."
- **Grades 4–5 Problem 2 (could 9):** ends "If not, explain why no turn can."
- **Grades 2–3 Problem 4 (could 10):** ends "Which choices allow a match by turning?"
- **"Frame" to "model":** K–1 Problem 4 and grades 2–3 Problem 5 ("on each model"), grades 4–5 Problem 5 ("a bare model").

No problem was renumbered. The guide follows: the grades 2–3 Problem 3 key now says the new model matches exactly one of the pair, so none matches neither (the two four-label classes, one model of the pair in each), and how to check with the three turns about A; the grades 4–5 Problem 6 key drops "genuinely"; p. 2 says the card tetrahedron is what the pages call a model; p. 5 and every footer name the v3 packets. The problem files' keys follow the guide (`check_guide_copy.py`). The kit did not change.

Verification: `src/student_checks.py` adds a check that each of the 24 four-label models matches exactly one model of the mirror pair, and passes with the existing rotation checks; `check_revised_cases.py`, `verify_math.py` and the kit checker (180 checks) pass. The package build from the extracted ZIP and the problem-file tools give the same student pages (identical LaTeX; `compare.py` finds identical text and pixels). Every page of the three packets and guide pages 1–5 were rendered and inspected; guide page 6 and the kit are pixel-identical. The previous print PDFs are in `week-37/archive-before-student-page-fixes-2026-10-23/` beside the print copies, and the conversion's ZIP in `source/week-37/archive-before-student-page-fixes-2026-10-23/`. The pages are digitally checked only; the physical pretest remains unperformed and the theme unpiloted.
