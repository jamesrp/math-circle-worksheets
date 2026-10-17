# Week 90 independent mathematical review

Reviewed 2026-10-17. Scope: draft students (7 pages, Problems 1–8), materials (11 pages), all printed catalog diagrams and worked visuals, and the coordinator's read-only facilitator90.tex draft. This reviewer did not write or revise the student packet. The separate critic's pedagogical findings were read. No draft or guide file was changed.

## Verdict and located findings

The intended mathematics is correct. Independently generated exhaustive catalogs match all 5 A, 6 D and 16 B cards, including their labels. Every legal full sequence of inner-corner choices was explored recursively; neither B nor D has any additional later choice beyond its two full orders. Complete labeled results match the guide. The first, successive-corner and reverse demonstrations use unchanged inputs and legal steps.

One mathematical wording correction is required, already identified by the critic:

- **Grades 2–5, student page 5, Problem 5:** “Can two different B starts reach exactly the same target?” follows four displayed targets with only three labels. Literal reference to those targets makes the answer no solely because B has five labels, missing the intended injectivity comparison. Replace “target” with “finished five-number arrangement” (or supply five-label targets). Intended answer remains no for these 16 B starts; this is a finite fact, not universal uniqueness.

The critic's request to say “outline or any number's position” in the whole-order comparisons is mathematically useful precision: the proved equality includes labels. Restoring a constructive B target-shape task is consistent with all verified cases below; it introduces no new mathematical obstacle.

The guide's proof sketches are correct. The coordinator subsequently sharpened the reverse proof, and I reread and confirmed that revised paragraph. The forward preservation sketch would benefit from making its key corner inequality explicit. Suggested details are below. These are precision improvements, not numerical counterexamples or a demand for a general confluence proof.

## Independent executable evidence

`check_math.py` is a standalone Python-standard-library program written independently for this review. It imports neither the writer's builder nor its checks/data. Run `python3 check_math.py`; the checked full key is emitted as JSON. `math-results.json` records this run.

The checker generates all permutations on each skew shape, filters by every same-row/same-column increasing comparison, and matches the complete printed catalog. For **every recursive legal slide branch**, it checks all intermediate inequalities, label conservation, southeast hole motion, valid inner and outer partition boundaries, the exact full output, and exact reversal of that single slide including its move word. It does not simply compare two preselected deterministic runs on arbitrary shapes.

Scope: 49 full catalog rectifications (5 A, 12 D, 32 B), plus an independent regression across **317 standard skew starts and 465 complete corner sequences**, covering every outer partition of at most six cells and one to four labels, including zero-step slides. All passed. This finite regression is evidence against implementation errors, not proof of general rectification independence.

## Full answer key and coverage

In each start code, read occupied cells row by row from top to bottom and left to right. A slash separates the rows of a finished straight tableau. Thus `13/2` means top row 1,3 and bottom row 2. Distinguish these labels from the outline `(2,1)`.

### Problems 1–2, student pages 1–2: A

A has outer rows `(3,2)`, missing `(1)`, and four labels.

| Card | Start code | Finished rows | Outline |
|---|---|---|---|
| A1 | 1234 | 12/34 | (2,2) |
| A2 | 1324 | 13/24 | (2,2) |
| A3 | 1423 | 134/2 | (3,1) |
| A4 | 2314 | 123/4 | (3,1) |
| A5 | 2413 | 124/3 | (3,1) |

P1: A3 and A5 share an outline; A1 does not. A3 and A5 do not share a labeled result. P2: exactly these five starts, two with outline (2,2), three with (3,1); all five labeled outputs distinct.

Completeness: name occupied cells `a,b / c,d` in reading order. Relations are `a<b`, `a<d`, `c<d`. If a=1, there are three orders of the other labels with c<d. If c=1, then a=2 and the remaining two labels can be exchanged between b,d. Total 3+2=5. No other location can hold 1. This is an exhaustive elementary argument, not just a computer count.

### Problem 3, student page 3: D and whole-slide orders

D has outer `(3,2,1)`, inner `(2,1)`. Its occupied cells lie on the descending diagonal, so all 3!=6 assignments increase. For each card the two legal full corner orders, in one-based coordinates, are `(1,2),(2,1),(1,1)` and `(2,1),(1,2),(1,1)`. Both give the result below.

| Card | Diagonal code | Finished rows |
|---|---|---|
| D1 | 123 | 1/2/3 |
| D2 | 132 | 13/2 |
| D3 | 213 | 12/3 |
| D4 | 231 | 12/3 |
| D5 | 312 | 13/2 |
| D6 | 321 | 123 |

The first corner choice changes neither outline nor any label position. Checking all twelve runs proves this finite collection. It does not prove the general theorem.

### Problem 4, student page 4: B; also constructive target route to be restored

B has outer `(3,3,2)`, inner `(2,1)`. The two complete corner orders are exactly the D orders. Every table entry is the common labeled result of both.

| Card | Start code | Finished rows | Outline |
|---|---|---|---|
| B1 | 12345 | 13/25/4 | (2,2,1) |
| B2 | 12435 | 14/25/3 | (2,2,1) |
| B3 | 12534 | 145/2/3 | (3,1,1) |
| B4 | 13425 | 134/2/5 | (3,1,1) |
| B5 | 13524 | 135/2/4 | (3,1,1) |
| B6 | 21345 | 12/35/4 | (2,2,1) |
| B7 | 21435 | 12/34/5 | (2,2,1) |
| B8 | 21534 | 125/34 | (3,2) |
| B9 | 23415 | 124/3/5 | (3,1,1) |
| B10 | 23514 | 125/3/4 | (3,1,1) |
| B11 | 31425 | 13/24/5 | (2,2,1) |
| B12 | 31524 | 135/24 | (3,2) |
| B13 | 32415 | 123/4/5 | (3,1,1) |
| B14 | 32514 | 123/45 | (3,2) |
| B15 | 41523 | 134/25 | (3,2) |
| B16 | 42513 | 124/35 | (3,2) |

Constructive witnesses: B8 reaches (3,2), B3 reaches (3,1,1), B1 reaches (2,2,1). Their actual placements are obtained from the supplied cards or the start codes. The full classification is:

- (3,2): B8, B12, B14, B15, B16 — 5 starts.
- (3,1,1): B3, B4, B5, B9, B10, B13 — 6 starts.
- (2,2,1): B1, B2, B6, B7, B11 — 5 starts.

These are all possible final shapes for this B input shape because the complete 16-start enumeration has been checked. Every labeled B result is different.

Completeness: label occupied cells a,b,c,d,e in reading order. Required comparisons are a<c, b<c, b<e, d<e. The smallest can occupy a,b,d only. With a=1, next b gives three completions, next d gives two; total five. With b=1, interleave two length-two chains a<c and d<e, choosing the two positions of the first chain: six. With d=1 the symmetric argument gives five. Total 5+6+5=16. The guide's counting argument is sound.

### Problem 5, student page 5: preimages

D targets: `13/2` receives D2,D5; `12/3` receives D3,D4; `1/2/3` receives D1 only; `123` receives D6 only. Thus the four output multiplicities are 2,2,1,1 in displayed target order (or 1,2,2,1 in vertical/bent/bent/horizontal order). A final array can forget its starting arrangement even when the initial skew shape is known. In contrast, all 16 B outputs are distinct labeled arrays. Do not confuse equal outline with equal labeled output.

### Problem 6, student page 6: exact recorded reversal

One-based coordinates:

| Input | S | E | Forward moved labels | Reverse moved labels |
|---|---|---|---|---|
| A2 | (1,1) | (1,3) | 1,3 | 3,1 |
| A4 | (1,1) | (2,2) | 1,4 | 4,1 |
| B4, upper corner | (1,2) | (2,3) | 1,4 | 4,1 |
| B4, lower corner | (2,1) | (3,2) | 2,5 | 5,2 |

All return exactly to the original start, including gray and outer boundaries. For B4 these are separate single-slide trials from the unchanged original, not two cumulative slides. The start and exit coordinates are required for this version of the inverse operation. The result makes no promise for arbitrary markers or an unknown full rectification history.

### Problem 7, student page 7: larger-neighbor variation

All five A cards fail increasing order under the larger-forward rule:

| Card | Finished rows | Witness failure |
|---|---|---|
| A1 | 312/4 | top row 3>1 |
| A2 | 213/4 | top row 2>1 |
| A3 | 214/3 | top row 2>1 |
| A4 | 243/1 | first column 2>1 |
| A5 | 24/13 | first column 2>1 |

The guide correctly limits this exhaustive claim to A. Larger is not always harmful: a single row with one missing initial square has only one eligible neighbor at every step, so larger and smaller give the same increasing output. At a two-neighbor choice, choosing larger causes an immediate inversion with the unchosen smaller neighbor. The finite A check is what additionally establishes failure of every final A output.

### Problem 8, student page 7: local invariants and termination

All three proposed failures are impossible under the stated ordinary skew-tableau assumptions and the smaller rule. Each swap preserves the multiset of labels; exit deletion removes an empty cell. The hole increases row+column by one at every move in a finite bounded outer diagram. Whole slides reduce the number of missing inner cells by one, so full rectification also ends. Order preservation has the local proof below. None of these elementary facts alone proves independence of different whole-slide orders.

## Guide precision: explicit proofs of the two local rules

**Forward order preservation.** Maintain strict order among occupied cells in each row and column, even when a hole separates them. If a tile x moves left into the hole, its new left neighbors were already smaller than x in the same row. A new above neighbor u is smaller than the tile v immediately to its right, and v is smaller than x in the original column of x. The skew partition boundaries ensure v exists when u does. Thus u<v<x. The choice of the smaller candidate makes x less than the unchosen candidate when both exist; the remaining rightward labels were already larger than x. The case of a tile moving up is the row/column transpose. Unchanged comparisons and comparisons across the newly vacated cell follow from the previous increasing order. This supplies the induction behind the guide's “pre-existing increasing rows/columns, together with the previous path move.” One can point to this three-cell corner in an adult diagram; no student notation is needed.

**Reverse larger choice.** Consider the last forward swap currently being undone. If x moved left, the reverse candidates are x immediately left of the new hole and possibly a label y immediately above it. Before that forward swap, y and x occupied the same column, with y above x, so y<x. Therefore reverse must choose x, the larger candidate. If x moved up, the other reverse candidate lies left of x's original position, hence is again smaller by the original row inequality. Undoing the last swap restores precisely the previous state; induction reverses the whole path. Stop at saved S, and restore its gray piece. This justifies rather than merely asserts the guide's “the most recently moved label is the larger available up/left one.” It assumes the endpoints and final state came from an actual legal forward slide.

The theorem attribution was independently reopened: Robichaux–Yadav–Yong, arXiv:1908.11224v1 §3, Theorem 3.1 explicitly states independence of successive inner-corner sequence for ordinary tableaux; Theorem 3.3 discusses preimage counts. The guide's strict distinct-label ordinary setting is appropriate. The source does not need to be bundled. Source: https://arxiv.org/html/1908.11224v1 . A broad proof-method label such as “via dual equivalence” is unnecessary unless that continuation is actually provided; “its general proof is substantially deeper” suffices here.

## Diagram and material review

Opened all seven student rendered pages and all eleven material rendered pages. Checked the actual TeX positions and PDF-extracted labels against the independent catalog, rather than assuming source comments were correct. Gray inner masks, dark outer masks and open-ring hole states match all three families. A/B/D board inserts have outer rows (3,2)/(3,3,2)/(3,2,1); the demonstration insert is (2,2). Catalogs have precisely five A, six D and sixteen B cards in the checked reading order. Tiles 1–5, three gray pieces, eight dark pieces, one ring and S/E markers are present; board cells are 30 mm and pieces 26 mm in source coordinates. The 3×3 blank grouping-card grids can contain every possible supplied output. No mathematical diagram correction was found.

Forward visual: missing top-left, top-right 2, bottom-left 1, bottom-right 3 → 1 moves up → 3 moves left, bottom-right covered. Reverse visual reopens exactly that bottom-right and restores the same original input. Multi-hole visual uses outer (3,2), inner (2,1), labels 1 at top-right and 2 at lower-middle; opening lower-left moves 2 left, covers its exit, preserves both upper gray squares, then opens the upper-middle legal corner. It deliberately demonstrates only one completed slide before selecting the next corner, as its rule requires.

This is mathematical and digital review of draft outputs, not physical handling, classroom piloting, a final-guide visual inspection, or a ZIP reconstruction. The constructive task and wording revisions need ordinary final-page review after revision.

Final guide reread: the updated “Why larger?” paragraph explicitly uses the off-path upper/left candidate and then inducts on restored states; this is correct. The three-gray-piece preparation now matches the actual materials. No guide source was edited by this reviewer.
