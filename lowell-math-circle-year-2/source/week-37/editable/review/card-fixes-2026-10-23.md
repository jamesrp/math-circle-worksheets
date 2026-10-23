# Week 37: printable kit and guide fixes from the review card, October 23, 2026

The review card is `plans/review/week-37.md` in the project, with its math check `plans/review/week-37-math.md`.

## What changed

- **Must 1 (card fix 1), guide pp. 1, 3 and 4.** The guide said a finite list of failed turns is never an impossibility proof, which rejects the natural complete argument. Page 1's overview and page 3's launch now say a failed search proves impossibility only when it covers every turn: A must go on A, and then only three turns remain. The K–1 and grades 2–3 Problem 2 keys (pp. 3 and 4) now say: "Accept a complete check: A must go on A, and all three turns about A fail." Page 1's grades 2–3 aim says the same.
- **Must 2 (card fix 2), a printable kit and guide p. 2.** New `materials.pdf` (print copy `week-37-materials.pdf`, 3 pages, US Letter at 100%, built by `materials-src/build_materials.py`): a card-stock tetrahedron net with 90 mm edges (one model per child, two for the adults: 13 sheets), letter caps A, A, B, B, C, C, D for four models per card-stock sheet (4 sheets), and a pose mat with two face-size footprints marked back, front left and front right (7 sheets of copy paper). A cap is three 26 mm equilateral triangles round one point; folded, it wraps a corner of the model and shows its letter on all three faces, held by sticky tack, so changing a letter means swapping a cap. The second B is what the B–D merge in grades 2–3 and 4–5 Problem 4 needs; the earlier spare A and C could not make it. Guide p. 2's materials section now describes this kit, says a taped card tetrahedron is the rigid "frame" the pages mention, gives counts for eleven children and about 6 minutes per model plus 30–40 minutes for the caps, and marks the kit physically unrehearsed. The pretest steps say "model" and swap caps.
- **Smaller guide items.** Launch (p. 3) stands the models on the pose mat (the guide half of should 5); the grades 2–3 Problem 4 key suggests splitting the six merges between the pairs (should 6); "frame" becomes "model" in the guide and route note; the "Status" line no longer lists problem counts (could 12).

Pages 1, 2, 3, 4 and 6 of `facilitator-guide.pdf` changed; page 5 (proofs) is pixel-identical at 100 dpi, and the three student packets rebuild with exact reference pixels.

Deferred: should 3 and 4, coulds 8–10 and "frame" to "model" on the student pages (K–1 P4, grades 2–3 P5, grades 4–5 P5–P6) change student pages and wait for a problem-file conversion; could 7 (the 0–60 minute hour) and could 11 are not done.

## Verification

- `materials-src/check_materials.py` reads only the finished kit PDF: 180 checks, 0 failures. It checks headers, footers and the 100 mm scale line on every page; that the net's nine 90 mm edges bound four equilateral faces joined as a tetrahedron net, with exactly one 9 mm tab on each of the three seams; that each of the 28 caps is three 26 mm equilateral triangles round one point with the same letter in each (8 A, 8 B, 8 C, 4 D) and that neighbouring caps share straight cuts; that one model's caps build every labelling the problems ask for, including each of the six merges with one name kept; that the pose-mat footprints are 90 mm equilateral triangles with named corners; that print counts cover each table; and that guide p. 2 quotes the same sheet totals.
- `verify_math.py` runs the existing rotation-group checks and the kit checker. A clean rebuild from the extracted portable ZIP passes `verify_revision.py` and the strict `verify.py` on all five PDFs (22 pages). Every kit page and changed guide page was rendered and inspected.
- No model has been folded and no cap fitted. The adult pretest on guide p. 2 comes first. The theme remains unpiloted.
