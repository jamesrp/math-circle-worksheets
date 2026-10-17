# Week 90: Sliding number arrays / jeu de taquin

Status: detailed planning draft, unbuilt and unpiloted; manipulative masks, reset procedure and classroom launch physically untested. Week 90 is a provisional identifier checked in the root brief. No PDF production or existing packet revision is requested. The choices below support several visits and a higher-readiness route; a K–1 variant is not forced.

## Facilitator opening: mathematical destination

**The legal slide preserves increasing order and terminates.** Use an ordinary Young diagram in English orientation: left-justified rows have nonincreasing lengths from top to bottom. Remove a smaller such diagram from its upper-left corner, leaving a skew diagram. Fill the remaining cells bijectively with 1,…,n, increasing left to right and top to bottom wherever cells share a row or column. A legal inner corner is a removable southeast corner of the missing inner diagram. Place a hole there; move the smaller of the immediate right/below numbered neighbors into the hole (the sole one if only one exists). Continue until no such neighbor exists, then remove that outer cell. One inner missing cell and one outer boundary cell are removed, so the number of labels remains n. The hole moves east/south, so one slide ends in finitely many moves. The resulting skew tableau is still increasing.

**First fundamental theorem of ordinary jeu de taquin.** Repeating legal inner-corner slides until no inner diagram remains produces a straight increasing tableau independent of the sequence of legal inner corners chosen. “Independent” includes the actual final labeled array, not merely its shape or number of labels. Within a slide, the smaller-neighbor rule is deterministic because labels are distinct. The choice is between whole slides' starting inner corners. This theorem does not authorize arbitrary starting holes, arbitrary missing shapes, repeated labels, arbitrary number puzzles, shifted diagrams, or the different edge-labeled rules in the source's later sections.

**Finite explanations versus the global theorem.** Children can completely verify both legal rectification orders for a selected five-label board and all six fillings of the three-cell diagonal board. This is a proof for those finite cases. It provides evidence for the general theorem, not a proof for every skew shape. The global proof via dual equivalence is substantially harder and belongs in a gated adult continuation with an actual source proof; this plan does not promise an elementary K–5 confluence proof. Children may instead prove termination, preserved order or a complete finite classification.

**Inverse single slides.** When the original inner corner and exit cell are specified, one forward slide can be undone: insert a hole at the exit, slide the larger immediate up/left neighbor into it, and stop at the original inner corner. The decreasing path retraces the forward path. This recovers a particular slide with its boundary information; it does not say a rectified tableau uniquely identifies its original skew tableau or slide history.

What children discover: compare labels locally, watch a hole move through a mutable shape, distinguish deterministic local moves from a global choice of starts, and test whether those choices matter. Grades 2–3 can operate supplied one-hole arrays after a retained-rule check; grades 4–5 can build and sort arrays, compare legal orders and give finite proofs. K–1 participation is an optional assisted one-hole manipulation if the child already compares the number cards and retains the neighbor rule. No “easy” parallel activity has been invented to force the family into all three bands.

## Kernel-only brief for a later worksheet writer

1. A local comparison rule preserves a global row/column condition while changing the shape. Monotone hole motion guarantees termination.
2. Different legal inner-corner orders can have different intermediate states but the same ordinary rectification. A small finite catalog supports complete local verification and a conjecture about general behavior.
3. Reverse slides reconstruct a single specified history when boundary information is retained; the final tableau alone does not encode every earlier choice.

Suggested emphasis: K–1, no scheduled packet; optional retained-rule manipulation only. Grades 2–3, one-hole supplied boards and a three-hole comparison if ready. Grades 4–5, constructing preimages and pooled finite case coverage; proof of local invariants, with global confluence explicitly gated. General tableau enumeration already occurs in Week 1 extensions and is not the central novelty here.

## Materials, preparation and exact conventions

Per pair: one 4 × 4 grid of 30 mm cells (120 × 120 mm), numbered tiles 1–5 each 26 × 26 mm, one distinctive 26 mm open-ring hole marker, five gray removable inner-missing tiles, and eight dark outside tiles. Gray means “missing inner shape”; dark means “outside the current outer boundary.” These states must differ by both fill and pattern (gray diagonal hatch versus dark crosshatch). A hole is always the open ring, never an unmarked blank. The numbered tiles stay flat and may move only into the active hole. A partner checks the two immediately adjacent right/below neighbors; no diagonals or jumps across missing cells.

Use three board inserts per kit for outer shapes `(3,2)`, `(3,3,2)` and `(3,2,1)`, with every initially outside cell permanently printed dark, plus removable gray inner shapes `(1)` and `(2,1)`. The eight loose dark tiles cover newly removed exits and provide spares; they are not expected to fill all initial outside positions of a blank 4 × 4 grid. An initial small mask marks eligible gray cells with removable outline tabs; after a completed slide the remaining gray mask determines the new choices. Inner `(2,1)` initially has two legal corners, positions (row 1,column 2) and (row 2,column 1). Its upper-left cell (1,1) is not legal yet. The adult should show these three positions with the actual gray shape before P3, rather than asking children to infer the word “corner.”

One completed slide: remove the chosen gray tile, put the ring there, move numbers, and when the ring has no numbered right/below neighbor replace its cell with a dark outside tile. Retain all other gray tiles. Thus there is one active hole at a time; children cannot drain all gray holes together or repeatedly choose the upper-left cell. Provide a reset card for every supplied start with the original labels and both masks. The child or partner can reconstruct a state from that one card; no running move tally is required. An adult may save the final labeled board on a whiteboard.

Print Letter at 100%. Actual working grids are separate reusable materials sheets with 30 mm cells. Student task diagrams use 13–15 mm cells, uniformly scaled, and label/mask patterns exactly match the working boards. Table-size comparison uses a second grid or reset card, not simultaneous mental reconstruction. At four-child tables prepare two kits; upper three-child table one kit with rotating slider, rule checker, and recorder. Optional catalog cards are 85 × 90 mm, with a three-cell diagonal start printed at 20 mm spacing; six cards in total are sufficient for P5. No hundreds of tableaux are copied or cut.

Preparation with reusable boards: about 20–30 minutes to make masks, five tiles and reset cards per kit. Rehearse: a smaller-below choice, a smaller-right choice, a one-neighbor move, a terminal cell removal, and a full reset. Check that gray/dark/hole remain visually distinct after two slides. Children must own which legal start to try and which neighbor is smaller. If the adult repeatedly chooses every move, defer multi-hole play and retain one-hole arrays. This is a readiness gate, not a claim the family cannot work for elementary children.

## Shared launch and worked visual before first use

Let children place numbered tiles and move the ring freely for two minutes. Then make a tiny increasing board and demonstrate one full slide using a non-task instance:

```text
input                  middle                 output
gray  2                1     2                1     2
1     3                hole  3                3   outside
hole starts at         1 moved up;             3 moved left;
the gray cell          hole moved down         remove exit cell
```

The actual visual contains three consistent 2 × 2 grids, with the ring drawn in the initial gray cell after its removal, and matching labels `start`, `after one move`, `finished slide`. Numeral 1 is smaller than 2, so it slides up; then 3 is the only eligible neighbor. Keep the output's former lower-right cell visibly dark so the changed shape is explicit. This teaches the convention without demonstrating independence of different inner-corner orders.

Say: “Only the two neighbors touching the hole on the right or below can move. The smaller goes into the hole. When neither is there, this slide is finished.” Ask the partner to check one move. Page 1 states the same essential rules once. Introduce legal multi-hole starts only before P3, using its own missing-shape visual.

## Planned student pages: actual consecutive problems

Shared packet header: `Week 90 / Sliding number arrays / Grades 2–5`; footer: `Bellingham Math Circle / Week 90 / F90-S-plan`, plus page number. Use ordinary text, no Name/Date or separate page titles. Shared rules page 1: “Rows and columns increase. Put the hole in a marked missing corner. Slide in the smaller number immediately right or below; use the only one if there is just one. Keep going until neither is there, then remove the empty outside square.” Page 3 adds the newly needed legal-corner rule once, with a worked missing-mask change.

Coordinates below are writer data only: rows top to bottom, columns left to right. `g` is gray inner missing, `x` is dark outside. A dot marks the active hole only after choosing a gray corner.

| Page | Actual task wording | Exact visual data and workspace |
|---|---|---|
| 1 | **Problem 1: Finish a slide on each board. Which final arrays have the same shape?** | Worked visual above, then three outer `(3,2)` / inner `(1)` starts: A rows `[g,1,4] / [2,3,x]`; B `[g,2,3] / [1,4,x]`; C `[g,1,2] / [3,4,x]`. Each initial gray cell is marked as legal. Compact diagrams use 15 mm cells in one row; three 55 × 55 mm final diagram regions fit across a single row with 10 mm gutters. Use one actual board with supplied reset cards; adult final recording can replace the blank regions if the writer needs more room for the convention visual. No compulsory intermediate logs. |
| 2 | **Problem 2: Use 1, 2, 3 and 4 to make every increasing start on this board. Sort the starts by their final shape after one slide.** | One blank `(3,2)/(1)` board, numbers supplied as movable cards. Two empty sorting mats show straight shapes `(2,2)` and `(3,1)` at 20 mm cell scale. A 170 × 100 mm region holds discovered reset cards or adult sketches. A pair may take two or three starting fillings and pool the complete five with the table; no child is required to duplicate a full catalog. |
| 3 | **Problem 3: Start with either marked corner and finish all the slides. Then reset the board and start at the other corner. What changes, and what stays the same?** | Outer `(3,3,2)` / inner `(2,1)`, start D rows `[g,g,2] / [g,1,4] / [3,5,x]`. Before the task show a distinct three-label missing-mask bridge: **input** outer `(3,3)` / inner `(2,1)`, rows `[g,g,2]/[g,1,3]`, eligible gray (1,2),(2,1) outlined; **middle** choose (1,2), remove its gray tile and slide 1 up, leaving the hole at (2,2); **output** slide 3 left and remove exit (2,3), rows `[g,1,2]/[g,3,x]`, with only gray (2,1) eligible next. Keep (1,1) gray throughout. This shows a completed first slide before identifying the next start and does not reveal D's two-order conclusion. Essential rule: “A missing corner can be used only when no missing square is immediately right or below it. Start a new slide only after the last slide is finished.” Place the bridge in a 185 × 42 mm strip using 10 mm cells; reserve 32 mm for the rule and task text, 50 mm for D's compact 15 mm-cell start, and one row of two 80 × 90 mm final-array regions with a 15 mm gutter. These regions total 214 mm high plus up to 10 mm vertical gutters within the approximately 235 mm task area. The full 30 mm-cell board is separate; adult whiteboard recording may replace saved regions. |
| 4 | **Problem 4: Fill this board with 1, 2, 3, 4 and 5 so rows and columns increase. Make starts that finish with each of these three shapes.** | Blank outer `(3,3,2)` / inner `(2,1)` board. Three target silhouettes are `(3,2)`, `(3,1,1)`, `(2,2,1)`, with no target labels. Each silhouette 15 mm cells and a 55 mm reset-card holding zone below; large physical board remains separate. Legal choices are computed from the current gray mask. No requirement to enumerate every five-label tableau. |
| 5 | **Problem 5: Sort all six starting cards by the final labeled array. Can different starting cards finish at the same array?** | Outer `(3,2,1)` / inner `(2,1)` leaves only cells (1,3),(2,2),(3,1), a descending diagonal. Supply six cards with top-to-bottom triples `123,132,213,231,312,321`, all automatically increasing because no two labels share a row or column. Four empty sorting mats display only the possible target shapes: row `(3)`, column `(1,1,1)`, and two separate `(2,1)` mats, with empty number cells. Children fill target labels after actual slides. Six cards may be divided across the table; each group need not redo every card and order. |
| 6 | **Problem 6: What can go wrong if the larger neighbor slides into the hole? Find a start where this rule breaks increasing order.** | Two supplied `(3,2)/(1)` starts A and B from P1, plus one blank start and number cards 1–4. The rule change is explicitly task-specific. Two 85 × 80 mm drawing regions let children retain one legal start and its bad output; a full proof of the smaller rule stays in the adult guide unless children seek it. |
| 7 | **Problem 7: Undo each finished slide and recover its starting board. The marked square shows where its hole exited.** | Before task, reverse worked visual on the non-task three-label board: **input** final `[1,2]/[3,x]`, add hole at (2,2); **middle** 3 moves right, hole at (2,1); **output** 1 moves down, hole at original (1,1), restore gray missing. Shared reverse rule: “Put the hole in the marked exit square. Slide the larger number immediately above or left into it. Stop at the marked original missing corner.” Tasks have original outer `(3,2)`, inner `(1)`: outputs `[1,3,4]/[2,x,x]` with exit (2,2); `[1,2,3]/[4,x,x]` with exit (2,2); `[1,2,x]/[3,4,x]` with exit (1,3). Original missing (1,1) is marked separately on each target. One blank 3 × 2 grid per recovered start; use separate actual board. |

P1 alone can be a satisfying first visit. P2 introduces organizing all possible starts, a different mathematical question from merely repeating a procedure. P3 introduces whole-slide choices only after concrete mastery. P4 designs preimages; P5 makes a finite confluence/catalog proof possible by pooled work. P6 and P7 change the rule and invert the operation, so they are encore directions rather than more starts with changed numbers.

## Solutions, finite proofs and discretionary hints

**P1.** A follows hole positions `(1,1)→(1,2)→(2,2)`, ending `[1,3,4]/[2]` of shape `(3,1)`. B follows `(1,1)→(2,1)→(2,2)`, ending `[1,2,3]/[4]`, also `(3,1)`. C follows `(1,1)→(1,2)→(1,3)`, ending `[1,2]/[3,4]`, shape `(2,2)`. Same shape does not mean same labeled array. A partner points only to the two eligible neighbors. Estimate 10–20 minutes, with reset checking included.

**P2.** Write a,b for the two top entries and c,d for bottom entries. The conditions are a<b, a<d, c<d. Five starts exhaust the possibilities:

| `(a,b,c,d)` | Final array | Shape |
|---|---|---|
| `(1,2,3,4)` | `[1,2]/[3,4]` | `(2,2)` |
| `(1,3,2,4)` | `[1,3]/[2,4]` | `(2,2)` |
| `(1,4,2,3)` | `[1,3,4]/[2]` | `(3,1)` |
| `(2,3,1,4)` | `[1,2,3]/[4]` | `(3,1)` |
| `(2,4,1,3)` | `[1,2,4]/[3]` | `(3,1)` |

Completeness: 1 must be at a or c, since b has a to its left and d has a above/c left. If a=1, then c<d gives three choices (ordered c,d from the remaining set), with b the leftover. If c=1, the three others require a<b and a<d, so a=2 and b,d can be 3,4 in either order, giving two. All five output arrays are distinct. This enumeration is new to this small skew board, while slides and changing shape are the family's core. Optional hint: where could 1 go? Estimate 15–25 minutes, readiness-dependent.

**P3.** D has two legal initial starts. Order east-first is `(1,2),(2,1),(1,1)`, with hole paths:

1. `(1,2)→(2,2)→(2,3)`;
2. `(2,1)→(3,1)→(3,2)`;
3. `(1,1)→(1,2)→(1,3)`.

South-first is `(2,1),(1,2),(1,1)`, with paths:

1. `(2,1)→(2,2)→(2,3)`;
2. `(1,2)→(1,3)`;
3. `(1,1)→(2,1)→(3,1)→(3,2)`.

Both end `[1,2]/[3,4]/[5]`, shape `(2,2,1)`. The intermediate states and hole paths differ. These are all orders: after either initial choice the missing inner shape has a unique removable corner, then only (1,1). Comparing both is a complete finite proof for D. It is evidence, not a proof of the general confluence theorem. Optional hint: keep the other gray tiles until their own slide begins. Estimate 15–30 minutes; repeated adult repair suggests returning to P1 rather than forcing a theorem discussion.

**P4.** Give entries in position order `(1,3),(2,2),(2,3),(3,1),(3,2)`. Checked starters:

| Target shape | Position-order entries | One final labeled array |
|---|---|---|
| `(3,2)` | `2,1,5,3,4` | `[1,2,5]/[3,4]` |
| `(3,1,1)` | `1,2,5,3,4` | `[1,4,5]/[2]/[3]` |
| `(2,2,1)` | `1,2,3,4,5` | `[1,3]/[2,5]/[4]` |

All satisfy row/column conditions. Both possible legal initial orders for each produce the listed result. A complete catalog has sixteen starts, with result shapes only the three targets; no child is asked to enumerate sixteen. The data file preserves all sixteen and their slide paths for independent verification. A proof that no other shape occurs here can be finite enumeration, but is not necessary to meet P4. Optional hint: change which small entry is accessible near a first hole. Estimate 15–30 minutes, possibly encore.

**P5.** Top-to-bottom triples yield:

| Start triple | Final array |
|---|---|
| `123` | column `[1]/[2]/[3]` |
| `132` | `[1,3]/[2]` |
| `213` | `[1,2]/[3]` |
| `231` | `[1,2]/[3]` |
| `312` | `[1,3]/[2]` |
| `321` | row `[1,2,3]` |

Thus different starts can finish at one array. The two increasing arrays of shape `(2,1)` each have two preimages, while row and column each have one. Six cards exhaust the starts because there are three unconstrained label positions: choose the top label (three choices), middle (two), bottom (one). For each card there are exactly the same two legal inner-corner orders as P3. The table may distribute the twelve runs across pairs, pool final reset cards, and compare the paired outputs. Then it has a complete finite proof of choice independence for this shape. This connects to the source's second fundamental theorem but does not prove that theorem for every target shape. Estimate 20–35 minutes; no compulsory child tally beyond sorting the six cards.

**P6.** On A, the larger rule takes 2 upward then 3 left, producing `[2,1,4]/[3]`, which violates row increase (2>1). On B it takes 2 left then 4 up, producing `[2,4,3]/[1]`, violating both the first column and top row. One counterexample suffices. Why the smaller rule works: at the first inner-corner hole, left/up positions are in the missing inner diagram, so no numbered left/up constraint is violated by an incoming label. At a subsequent hole, its former label v was moved to the preceding path position. Every untouched left/up neighbor was smaller than v; both possible incoming right/below neighbors are larger than v by the original row/column order, while the preceding moved label is v itself. Thus the incoming value exceeds all filled left/up neighbors. Choosing the smaller ensures it remains below the other filled right/below neighbor. The hole moves only east/south, so future neighbor values have not been altered. This proves preserved increasing order throughout, ignoring the active hole. The hole's row-plus-column strictly increases, so it ends; because no missing-inner cell is southeast of the starting legal corner, an end without right/below labels is an outer corner. Estimate 10–20 minutes, proof optional if children want to explain the rule.

**P7.** The reconstructed starts are A, B and C from P1. At each reverse step, the larger of up/left is the last forward label that was moved: the competing label is smaller because forward order remains increasing. This retraces the path until the known original missing corner is reached. For A the reverse labels are 3 then 1; B 4 then 1; C 2 then 1. Boundary markers are essential: the removed cell determines where to reinsert the hole, and the known original inner corner determines where to stop. Without boundary information, different starting boards or histories may share a rectification as P5 shows. Do not generalize this single-slide reconstruction to unique recovery of every skew tableau from its final straight tableau. Estimate 10–20 minutes, encore.

## First-visit and encore choices

| Route | Prerequisites and mathematical choices | Adult role |
|---|---|---|
| Optional child at K–1 readiness | Compare 1–4, locate adjacent right/below after the launch, retain one hole. P1 supplied starts only. | Read once, partner or adult checks a move. If the adult makes each comparison, use a different family; do not create a nominal K–1 worksheet. |
| 2–3 concrete route | P1, then optionally P3; reading unnecessary with adult launch, number ordering to five, one persistent hole and a reset card. | Adult removes completed outer cell if dexterity requires it; child chooses the smaller neighbor and later which eligible start to try. |
| 4–5 classification route | P1–2 or P3–5; distinguish shape from labels, retain a changing mask, sort supplied cards. | Adult saves final arrays and coordinates pooled case coverage; no simultaneous move tally. |
| Encore: why this rule? | P6 after play; seek a counterexample and prove order/termination with drawings. | Keep global confluence proof gated. Local invariants are real proof opportunities. |
| Encore: undoing history | P7; understand exit/original-hole markers and compare up/left. | New operation and information-loss question; reuse physical boards. |

First hour may be five-minute movement, five-minute handling/launch, 25–35 minutes P1 plus freely chosen starts, and a sharing of changed shapes. A later visit adds the gray-mask demonstration and P3. “All slides” means one hole to completion before a new inner-corner choice. Finishing seven pages is not the goal. Record board IDs, whether legal starts were child-chosen, and actual investigations used; these plans have not been piloted.

## Adjacent corpus, primary source and verification limits

Actually inspected `plans/week-01-extensions.md` and `source/week-01/week-01-extensions-facilitator.tex`, X3 printed guide section “Forty-two shortest routes,” including its adult continuation. X3 labels successively added squares 1–9 and counts 42 standard tableaux of a 3 × 3 square via predecessor recurrence; it also counts 14 for a 4 × 2 shape. Week 90 does not repeat those tableau counts or the hook-length question. It begins with increasing skew arrays and studies changing shape by legal slides, order choice, finite classification and undoing. Returning children can reuse increasing-row/column familiarity but need the new hole convention explicitly demonstrated.

Primary source checked 2026-10-11: Colleen Robichaux, Harshit Yadav and Alexander Yong, [*Equivariant cohomology, Schubert calculus, and Edge labeled tableaux*](https://arxiv.org/html/1908.11224v1), §3, slide rules J1/J2 and rectification definition; Theorem 3.1 (first fundamental theorem), Example 3.2 (different orders); Theorem 3.3 and Example 3.4 (preimage counts). The supplied UCLA `edgeTab.pdf` lead failed in browsing; the author-linked arXiv version was inspected instead. §3 recommends Haiman's dual-equivalence argument for the general theorem. Later edge-labeled and shifted rules are excluded here. The source gives adult mathematical context; our small boards, masks, prompts and finite checks are independently designed, not claims of a classroom-ready lesson copied from the chapter.

Digital evidence: `python3 plans/seven-families-85-91/growth-math-check.py` checks all five increasing four-label starts, sixteen five-label starts, and six diagonal three-label starts, enumerating every successive legal inner-corner choice, verifying increase and legal exit, and comparing the full final arrays. `growth-math-data.json` contains initial arrays, all start sequences, hole paths, outputs and multiplicities. Those finite computations do not prove the global theorem or establish physical/classroom readiness. Independent mathematical and operational reviews are recorded in [REVIEW-RESOLUTION.md](REVIEW-RESOLUTION.md); the independent enumeration also covers 2,706 standard tableaux on 449 small skew shapes.

Remaining risks: multiple kinds of missing cells; a child opening all holes at once; retaining old outer-boundary cells; using the smaller of all visible numbers instead of immediate neighbors; mixing deterministic neighbor selection with choice of whole slides. The three-state masks, single ring, explicit terminal removal and delayed legal-corner bridge address these risks. They are unpiloted design hypotheses and should be checked in rehearsal, not treated as bans. Global confluence remains honestly attributed and gated; small finite proof opportunities remain on the table.
