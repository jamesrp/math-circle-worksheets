# Week 16 independent mathematics review

Reviewed the actual four-page `draft/return-visit.pdf`, its diagram coordinates, and the writer brief. I rendered and inspected all four actual PDF pages at 1.6×. I did not read or run the writer's mathematical checking scripts or use their results as evidence. No mathematical correction is required in the reviewed draft.

All represented bands check out: Grades K–1 and up (page 1), Grades 2–3 and up (pages 2–3), and Grades 4–5 (page 4).

## Verification record

The independent checker and full results are saved in `math-review/check_independent.py` and `math-review/independent-results.json`. The checker reconstructs the three-step triangular lattice independently, enumerates its legal fillings, compares that lattice with the printed source coordinates, and measures vectors from the actual PDF. Its assertions all passed.

| Band / page / problem | Question and independently verified outcome |
|---|---|
| K–1 and up / 1 / 1 | “Which middle letters leave no small triangle with R, B and Y? Find every choice.” Of the four permitted middle labels, **G is the only answer**. R, B and Y each leave exactly one RBY cell. G leaves zero RBY cells but three cells with three different letters. The picture has three cells, with the fixed corners R, B, Y and one interior blank. |
| 2–3 and up / 2 / 2 | “Fill the blank dots so no small triangle has R, B and Y. Among those fillings, how few small triangles can have three different letters?” The printed mesh has 10 vertices, 9 cells, 6 free binary boundary labels and one interior four-way label, hence **256 legal fillings**. Exactly **27** have zero RBY cells. Among those, **18 have three any-three cells and 9 have five**; the requested minimum is **3**. Every zero-RBY filling has G at the interior vertex. The shared rules on page 1 permit G only inside; page 2's three boundary restrictions agree with those rules. |
| 2–3 and up / 3 / 3 | “Can switching the diagonal change the number of rainbow triangles? Can it change whether that number is even or odd? Find a rule from the outside letters.” Switching can change the count by two; it **cannot change parity**. Around the square, the parity equals the number of outside R–B edges modulo two. All **81** R/B/Y corner assignments were checked on both diagonals. Count pairs are (0,0):45, (0,2):6, (1,1):24 and (2,0):6. |
| 4–5 / 4 / 4 | “What can change between fillings, and what stays the same about the two totals?” For all **192** legal three-label fillings of this printed mesh, **plus total minus minus total equals 1**. The attainable (plus,minus) pairs are (1,0):108, (2,1):72 and (3,2):12. Both totals, and their sum, can change. The plus/minus examples and all six arrow directions agree with the counterclockwise instruction. |

The square enumeration indexes corners counterclockwise from bottom left. For example, R,B,R,Y gives zero rainbows on the bottom-left–top-right diagonal and two on the other; its two R–B boundary edges have even parity. R,B,Y,Y has one rainbow on either diagonal and one R–B boundary edge. Repeated letters, no rainbow cells, and both diagonals are included in the exhaustive checks. There is no hidden assumption of distinct outside labels on page 3; its local rule explicitly permits arbitrary R/B/Y choices.

## Explanations independent of finite enumeration

**Boundary parity.** Count incidences between cells and R–B edges. A three-label RBY cell contributes one, an R/B two-label cell contributes either zero or two, and every other cell contributes zero. Interior edges occur twice; boundary edges occur once. Thus the rainbow count and the number of boundary R–B edges have the same parity. This proves the square rule and, with the usual three triangular side restrictions, ordinary Sperner existence. The assumption is an edge-to-edge triangulated disk; the displayed meshes satisfy it.

**Four-label minimum.** Start with any legal filling having no RBY cell. Save that original filling. Replace every G by R: ordinary Sperner existence produces an RBY cell that was GBY in the original. Restore the original and replace every G by B: a resulting RBY cell was RGY. Restore again and replace every G by Y: it was RBG. These are three distinct original cell types, proving a lower bound of three any-three cells. Equivalently, parity applied to each pair of boundary colors shows that the number of each of RBG, RYG and BYG cells is odd when no RBY cell is present.

The bound is attained on the actual mesh by the independently checked bottom-to-top rows `RRBB / RGB / YY / Y`: one cell each of RBG, RYG and BYG, three two-label cells, and three monochromatic cells; no RBY cell. This is review evidence, not a suggested student-page answer.

**Signed count.** Orient every cell counterclockwise. Give an edge contribution +1 for R→B, −1 for B→R, and zero otherwise. A positive rainbow's contributions sum to +1, a negative rainbow's to −1, and a non-rainbow's to zero. Every interior edge cancels with its reverse from its neighbor. On the outside, the permitted R/B side is directed from R to B, so its contributions telescope to +1; the other two sides contribute zero. Therefore plus total minus minus total is exactly 1, with the printed outer corners ordered R,B,Y counterclockwise. Reversing the outer order would reverse the sign; that alternative is not the printed diagram.

## Printed geometry and conventions

Actual PDF vector measurements confirm:

- Page 1: an equilateral outer triangle with side approximately **4.05008 inches**, one interior vertex and three triangular cells. Its smaller star cells are intentionally not equilateral.
- Page 2: **nine** equilateral mesh cells, side approximately **1.50002 inches**, and a **4.5-inch** outer side. Each cell's greatest side-length difference is below **0.00025 point**. All boundary and interior vertices match the independently constructed lattice.
- Page 3: **four true squares**, each side approximately **2.50003 inches**, paired with opposite diagonals. Corresponding corner positions match across each row; no boundary label is preassigned.
- Page 4: **nine** equilateral mesh cells, side approximately **1.40001 inches**, and a **4.2-inch** outer side. The two 1.25-inch convention triangles are also equilateral. Their arrows travel counterclockwise: bottom left→bottom right→top→bottom left. The first reads R→B→Y and is positive; the second reads R→Y→B and is negative. Both have the required input labels, traversal, and output sign before first use.

There are no holes, T-junctions, overlapping cells or missing mesh cells. Letters and arrows agree with the mathematics in every inspected page. G is confined to the first investigation, with explicit three-label resets on pages 3 and 4. Page 2 relies on the packet-wide rules on page 1, as the student-page specification permits; it should be offered with those rules available.

These are mathematical and digital checks. Physical use and classroom piloting were not tested.
