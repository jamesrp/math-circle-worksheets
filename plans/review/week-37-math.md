# Week 37 math check: Mirror twins (chirality of labelled tetrahedra)

Scope:

- `lowell-math-circle-year-2/week-37/week-37-k-1.pdf` (W37-k-1-v2, 4 pp., Problems 1–5)
- `week-37-grades-2-3.pdf` (W37-grades-2-3-v2, 4 pp., Problems 1–6)
- `week-37-grades-4-5.pdf` (W37-grades-4-5-v2, 5 pp., Problems 1–6)
- `week-37-facilitator.pdf` (6 pp.)
- the bonus companion `week-37-bonus.pdf` (W37-BONUS-v1, 3 pp., Problems 1–3) and its guide `week-37-bonus-facilitator.pdf` (W37-BONUS-FAC-v1, 3 pp.)

Archive folders were ignored. Sources read: `source/week-37/editable/src/build_packets.py` and the generated `k-1.tex`, `grades-2-3.tex` and `grades-4-5.tex`, plus `source/week-37-bonus/student/build.py` and `common.py`. All six delivered PDFs are byte-identical (MD5) to the `reference-pdfs/` copies in their source folders. I did not use the packet's own `mathematical-checks.json`, `check_revised_cases.py`, `verify_math.py` or the bonus `verify.py`. Checked October 10, 2026.

Scripts (each finds the repository from its own location):

- `check_math.py` → `check_math.out`: 121 checks, 0 failures.
  - Reads all 30 tetrahedron drawings and the 3 view-from-A diagrams from the TeX. It confirms each printed letter sits at its TeX coordinate in the delivered PDF (122 letters).
  - Rebuilds each drawing as a 3D regular tetrahedron, using the dashed edges to fix which vertex is behind.
  - Decides every printed "can they match?" question from that geometry. It also recomputes the rotation group, the labelling classes, every merge, the view-from-A handedness and each guide key.
- `check_bonus.py` → `check_bonus.out`: 49 checks, 0 failures. It covers the outline congruences, all 20 three-red-edge patterns, the corner rotations, the picture geometry and the bonus guide's kit arithmetic.

Renders are in `render/` (100 dpi) and text extractions in `text/`.

**Result: every printed answer and every key answer is correct in all three bands, the bonus and both guides. All drawings match their text. I found 3 problems:**

1. One false general statement in the base guide, repeated in three places.
2. A materials list that cannot build one of the six merges.
3. A minor wording gap in Grades 4–5 Problem 6.

## What verifies

**Diagrams.**

- **Tetrahedron drawings.** Every one is an exact orthographic view of a regular tetrahedron: the orthonormality error is at most 4e-16, and TikZ x and y are both 1 cm.
  - The three dashed edges are exactly the edges to the far vertex, which projects inside the solid front face, so "Dashed edges pass behind the front face" is right.
  - Read as [apex, lower left, lower right, far], the drawings are:

    | Drawing | Labels |
    |---|---|
    | Turn demo | ABCD → ADBC |
    | P1 copies | ABCD, ABCD |
    | Mirror pair | ABCD \| ACBD |
    | D→C pair | ABCC \| ACBC |
    | A, A, B, C pair | AABC \| ABAC |
    | 4–5 P5 frame | bare |
- **Turn demo.** "After the turn" is the 120° rotation about the axis through A, as labelled "turn around A".
- **4–5 P3 view from A.** Reconstructing the model and looking from A, with A nearest the eye, gives B, C, D anticlockwise. The printed view (B lower left, C lower right, D top) has the same handedness, and the mirror twin reverses it. The view triangle has sides 4.528, 4.528 and 4.600 cm, so it is equilateral to within 1.6%, with A at its centre. Two blank view diagrams are provided.

**K–1.**

- **P1.** The two models are true copies and match.
- **P2.** The mirror pair cannot match (no).
- **P3.** ABCC | ACBC match (yes). Exactly one of the two one-third turns about A does it, as the key says.
- **P4.** All 12 A, A, B, C labellings form one rotation class, so no unmatched pair exists. The printed pair matches.
- **P5.** Both outcomes are available.

**Grades 2–3.**

- **P1–P3.** Correct as keyed.
- **P4.** All 6 merges, keeping either letter's name, let the mirror pair match (12 of 12).
- **P5.** No unmatched pair exists.
- **P6.** Both outcomes are reachable. That holds for every A, A, B, C pair a partner might build, not only the printed one. The guide's four cases are each correct:
  - top/top: no match
  - top/right: match
  - left/right: no match
  - left/top: match

**Grades 4–5.**

- **P1–P4.** Correct as keyed.
- **P5.** 12 rotations: identity 1, 120°/240° vertex-axis turns 8, half-turns about opposite-edge axes 3. The proper rotations are exactly the even vertex permutations.
- **P6.** The 24 labellings fall into 2 classes of 12, swapped by a reflection.

**Guide.** These statements are all true with the stated hypotheses:

- the overview's facts
- the pretest steps (including step 4's turn about A)
- the K–1, 2–3 and 4–5 keys
- the page-5 proofs: the cyclic-order certificate, the determinant sign, the reflection S that swaps a vertex pair and fixes the plane through the other two vertices and the pair's midpoint, the parity argument for A, A, B, C, and 4 × 3 = 1 + 8 + 3 = 12
- the status line, which matches the printed problem counts 5 / 6 / 6

**Bonus.**

- **P1.**
  - The F-like outline has no reflection symmetry. Face up, its mirror does not match; turned over, it does.
  - The L has equal 65-unit arms, and a face-up quarter turn carries it onto its mirror.
  - The T is symmetric about x = 9.
  - So the answers are no, yes, yes, and all three match once turning over is allowed. The face dots lie inside each tile.
- **P2.**
  - Of the 20 three-red patterns, 12 are paths (chiral), 4 are stars and 4 are triangles (both achiral). The printed path, star and triangle give no, yes, yes.
  - The guide's three one-sleeve edits each change the answer. Other changing moves exist too: 4 of 9 for the path, 6 of 9 for the star and the triangle.
- **P3.**
  - R/B/G is chiral; R/R/G and R/R/R are not. One colour with lengths 30/60/90 is chiral; 60/60/90 is not.
  - The guide's certificate holds: with G toward the viewer and R to the right, B points up in the model and down in its mirror.
  - The corner pictures are exact views along the cube diagonal, and the cube-corner sketch is an exact orthographic projection.
- **Kit arithmetic.** The guide's figures are consistent: 36/12/36/12, 36 R/12 B/12 G and 12 for the full kits; 36/4/12/8, 24 R/8 B/8 G and 4 for the practical minimum.

**Not problems:**

- The bonus p. 2 tetrahedra are schematic, not exact projections: D sits 13 pt from its exact place on a 130-pt edge. The far vertex is still inside the front face, so the drawings read correctly.
- A three-arm picture cannot show whether its arms point toward or away from the eye. No bonus answer depends on reading a picture's handedness, because children build each corner and its mirror.

## Problems found

### 1. Guide pp. 1, 3 and 4: "a finite list of unsuccessful turns" is said never to prove impossibility, but an exhaustive one does

**Quoted text.**

- Guide p. 1, Orientation obstruction: "A finite list of unsuccessful turns alone is not an impossibility proof."
- Guide p. 3, Flexible hour: "A failed search is not proof of impossibility."
- Guide p. 4, 2–3 Problem 2: "'No turn has worked yet' does not by itself establish 'no turn can work.'" This key offers only the cyclic-order certificate as a reason.

**Evidence.** The rotation group is finite, so a list of failed turns that covers every case is a complete proof.

- Any matching motion must carry A to A. With both models posed alike and A at the same corner, only 3 rotations remain: leaving it still and the two one-third turns about A.
- On the mirror pair, all 3 fail. The check is in `check_math.out`, section "Exhaustive testing as a proof".
- Several prompts invite exactly this argument:
  - 4–5 P2: "Seek a reason that settles this even if no more turns are tried."
  - 2–3 P2: "If no turn has worked, does that mean no turn can work?"
  - 4–5 P5, where children count the 12 rotations themselves.
- A child might say: "A has to sit on A. Then there are only three ways to turn it, and we tried all three." That is a complete proof, and arguably the most accessible one. As printed, the guide tells the adult it is not.

The intended point is right for an unorganised handful of failures, but the hypothesis "unless the list covers every possible turn" is missing.

**Smallest fix.** On p. 1, replace the sentence with: "Failed turns prove impossibility only when they cover every case. Once A is aligned on both models, only three turns about A remain, so failing all three is a complete proof. A handful of unorganised failures is not."

On p. 3, change the sentence to "A failed search proves impossibility only if it provably covers every turn."

On p. 4, add to the 2–3 P2 key: "Accept a complete check: A must go on A, and all three turns about A fail."

### 2. Guide p. 2, materials: the B–D merge cannot be built with "duplicate As and Cs"

**Quoted text.** "…category markers A, B, C, D with duplicate As and Cs."

The merges this list has to support:

- 2–3 P4: "Try other choices of two letters to make equal".
- 4–5 P4: "Choose two letters in the mirror pair and make them equal on both models … Explain why your conclusion covers every choice".
- The guide's 2–3 P4 key, which lists "AB, AC, AD, BC, BD and CD" and adds "Which name is retained for the merged pair does not change the result."

**Evidence.** To make two letters X and Y equal on a model, you need a spare X or a spare Y.

- With spares of only A and C:
  - AB, AC and AD can keep A.
  - BC and CD can keep C.
  - BD needs a spare B or D, so it cannot be made.
- The table is in `check_math.out`, section "Markers needed for the merges". So 4–5 children cannot test one of the six choices their conclusion must cover, and an adult following the list cannot set it up.
- Removing both markers would work, since two blank corners count as equal, but nothing on the page or in the guide says so.

**Smallest fix.** Change the list to "with duplicate As, Bs and Cs". Alternatively, add: "For the B–D merge, take both markers off; two blank corners count as equal."

### 3. Grades 4–5, p. 5, Problem 6: the answer 2 assumes the letters are A, B, C, D

**Quoted text.** "Put four different letters on the frame. How many genuinely different models can be made if models that match by turning count as the same?"

**Evidence.** The answer 2 holds only for one fixed set of four letters.

- If a child takes "four different letters" to mean any letters, the count is 2 × C(n, 4): 10 from 5 letters, 29,900 from the alphabet. The figures are in `check_math.out`.
- The kit has only A–D, and the guide's key ("All 24 distinct assignments split into two classes of size 12") silently assumes A–D.
- So most children will read it as intended. A child who answers "it depends which letters" is not wrong, though, and the key does not cover that answer.

**Smallest fix.** Change the first sentence to "Put A, B, C and D on the frame, one at each corner."
