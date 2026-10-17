# Week 86 adversarial critic review

## Decision

Revise the fold manipulation instruction and resolve roads passing through existing dots on the design boards. Preserve the packet's mathematical range, six-dot/six-road design constraint, and upper fold/two-cop investigations. This is a strong concrete draft with two localized operational defects, not a reason to replace its problems or lower its mathematical ceiling.

I read PROMPT.md, rendered the current final-path PDFs independently with PyMuPDF, and inspected every page: shared.pdf (4), upper.pdf (6), materials.pdf (3), 13 pages total. I also read build.py, verify.py and the source README. The supplied finite-game verification script passes. This review is a student-page and operational review; the separate independent mathematical review still needs to occur. No files in draft were changed. No printing, counter placement, sleeve/cover rehearsal, or classroom piloting was performed.

## Revisions needed

### 1. Upper page 4, Problem 4: the sleeve-erasing option does not work with the supplied printed boards

The instruction says, “Cover removed dots and their roads on the working copy, or erase them in a sleeve.” Materials pages 1–2 contain fully printed working graphs. Erasing dry-erase marks on a sleeve cannot remove the printed dots or roads underneath. This gives a child an impossible action at precisely the point where the current graph must be unambiguous. Merely crossing out a vertex while leaving its incident roads visually active also risks subsequent neighborhood comparisons against the wrong graph.

Make one supported procedure explicit and ensure its materials are available. The smallest revision is to retain covering and remove the sleeve-erasing option, with opaque removable pieces/strips in the material preparation. Alternatively, use a supplied blank working layout on which the relevant graph is drawn in erasable ink before folding, while the full printed original remains visible. Do not require children to transcribe a graph unless that added demand is intentional. Covering needs to remove the vertex and the visible portions of all its incident roads without obscuring surviving vertices/roads; rehearse this physically later and keep that rehearsal marked untested now.

The mathematical fold definition and the before/after demonstration are already satisfactory. Do not rewrite them into a sequence that compares neighborhoods from different graph states.

### 2. Upper page 3, Problem 3: make roads through existing dots unambiguous

D1 and D2 each use two rows of three collinear dots. A straight road from a to c passes directly through b; a straight road from f to d passes through e. “Crossings are not junctions” resolves roads crossing one another away from a dot, but it does not tell a child what to do when a proposed road runs through an existing labeled dot. Depending on interpretation, the same drawing represents an a–c shortcut or two roads through b. That changes legal moves and possibly who wins, defeating the challenge-your-partner test.

Prefer a layout with no three dots collinear, keeping the existing large working dots and ample room for roads. A regular six-dot ring would work without adding prose. Alternatively, keep the layout and add a brief essential rule that a road must miss all other dots, so such roads must bend. This is about a checkable board, not prescribing a solution. The condition “all six dots and at least six roads” should stay: for a connected simple graph it forces a cycle, so the cop-win design cannot simply be a familiar tree. Counting six dots/at least six roads is manageable here, and the condition has a substantive role.

## Smaller wording and usability considerations

- Shared page 1 and upper page 1: “quickest catch” is understandable, but “fewest C turns” would make the optimization measure explicit and independent of playing speed. Staying uses a turn. This is a small precision improvement, not a request for move logs or extra substeps.
- Upper page 4: keep the original/working-copy handling instruction with Problem 4 or the fold rules. It currently appears as a separate paragraph after the problem; this is useful essential procedure, but it need not look like a separate unnumbered task. The repeated instruction to check each fold on the remaining graph can be stated once.
- Two-cop play permits both cops on one dot. A 22 mm circle cannot contain two 18 mm counters side by side, although stacked or slightly offset counters work. Treat this as a material-rehearsal check, not a demand to enlarge every circle or restrict the game. Capture ends immediately, so cop/robber co-location is not a persistent storage issue.
- Board labels are about 9 pt and are readable in the rendered PDFs. A few labels deliberately sit in white gaps on vertical roads (for example T1 f/g, T2 c, Q6 b/f). They remain decipherable; retain this as a physical print check rather than claiming a demonstrated classroom problem.

## Page-by-page coverage

| PDF/page | Content inspected | Assessment |
|---|---|---|
| shared 1 | Rules; three-panel T example; P5/P7 | Correct concrete launch: C moves w to x, R stays at y; turn indicators change C/R/C. The original graph, labels and robber location stay consistent. P5/P7 offer an accessible optimization investigation. Working boards fit the prescribed sizes. |
| shared 2 | T1/T2 | Both are connected trees with different branching. Large labeled dots and complete roads support actual play. The universal cop-plan question is substantial and permits children to choose moves. |
| shared 3 | R3/R4 | Triangle/square contrast is visually clear, regular, and mathematically purposeful. The prompt asks for a plan against every reply, not just a winning sample game. |
| shared 4 | R5/R6 | Both regular rings are large enough for play. Odd/even examples extend rather than merely duplicate the square. The distinction between a long test and endless escape is explicit. |
| upper 1 | Rules; T example; P5/P7 | Same complete, valid entry procedure as shared 1. Duplication permits this packet to stand alone; no need to remove it solely because shared also contains it. |
| upper 2 | E4/E5 road editing | Full working boards, clear objective, open method. Minimum added roads requires a reason for failure as well as a successful example. Crossing rule is present. Preserve this task's depth. |
| upper 3 | D1/D2 construction | Substantial synthesis, correct six-dot/six-road purpose. Fix collinear-dot road ambiguity described above. Otherwise ample working area and readable labels. |
| upper 4 | Fold definition/example and Problem 4 | Stay/self included explicitly. Both accessible sets are compared on the same unchanged four-vertex path; highlighted sets match the printed descriptions. Deletion then produces exactly x–y–z, with original retained. F1/F2 references match supplied material boards. Fix the unsupported sleeve erasure. |
| upper 5 | Two-cop rules; Q6 | Both cops placed before R; each gets one move/stay per cop turn; R gets one turn; immediate capture and shared cop dots are explicit. Large six-ring board. Concrete first two-cop investigation, without giving the stationary-blocker method away. |
| upper 6 | Q8 and all-rings question | Eight distinct vertices and eight cycle edges, regular geometry, generous explanation space. Good continuation from concrete Q6 to general reasoning. Preserve the all-rings explanation. |
| materials 1 | F1 original/working pair | Two identical full-size triangle-with-branches graphs, same labels, visible together. No missing roads or intersections. |
| materials 2 | F2 original/working pair | Two identical pentagons with chord a–c. Labels and topology match. This is a useful triangle-containing map with an evasive square after the appropriate fold. |
| materials 3 | Turn tiles and counters | Two explicit front/back pairs; one-cop and both-cops versions; four distinct labeled counters. Preparation text is appropriate to a separate material sheet. Printed size is correct digitally. |

## Size, layout, and mathematical observations

The actual PDFs are US Letter (612 × 792 pt). I measured vector circle bounds from the delivered PDF drawings: playable dots are 22 mm on every relevant page except P7's allowed 20 mm circles; reference examples use 8 mm circles; cut-out counters are 18 mm. P7 has 28 mm center spacing; the other working layouts meet or exceed 32 mm nearest-center spacing. Thus an individual centered 18 mm counter has 2 mm radial room in ordinary dots and 1 mm in P7 dots, with readable labels outside the counter footprint. This is digital geometry evidence, not a physical-fit test. The regular polygons use equal x/y scaling and the triangle, square, pentagon, hexagon and octagon have the intended vertex counts. No clipped text, footer overlap, or unintended printed edge crossing was found.

The game conventions support the intended distinctions. P5/P7 have center starts with worst-case capture in two/three cop turns respectively. T1/T2 are trees. R3 is cop-win; R4/R5/R6 admit perpetual evasion. E4 needs one added diagonal; a single added chord does not suffice on E5, while a two-chord fan does. F1 can fold to a point; F2 folds away b onto a or c and leaves a four-cycle. Two cops suffice for Q6/Q8 and for longer rings. The printed questions do not prematurely reveal these conclusions. The verifier checks these finite win/loss examples and supplied fold sequences; it does not itself establish the entire general theorem, optimal path capture times, or physical procedures.

## Substance, independence, and readiness

The shared packet gives enough independent play, contrasting boards, and strategy questions for the working time; no artificial problem splitting is needed. Upper page 3 is a real construction task, upper page 4 introduces a new representation with its own paired boards, and upper pages 5–6 preserve a separate two-cop direction. Treat the later upper pages as continuations/return visits rather than expecting every child to finish six pages in one meeting. Do not simplify them merely to enforce one-hour completion.

The one-cop rules and miniature sequence support an adult's brief whole-group demonstration. Children still choose the actual starting positions and moves. Routine adult reading may be needed; graph strategy, universal claims, and repeated neighborhood comparison are the cognitive prerequisites. The fold work is a readiness-dependent extension, not evidence that all upper-band children can run it independently without a launch. The no-K–1 decision follows the outline's explicit override.

This stage contains student pages only. It would be inappropriate to demand a theorem-first facilitator guide as a condition of this draft, or to author one during the critic stage. Any later guide must preserve the distinction between experiments, conjectures, and explanations, and identify the material rehearsal and classroom use as untested until actually performed.
