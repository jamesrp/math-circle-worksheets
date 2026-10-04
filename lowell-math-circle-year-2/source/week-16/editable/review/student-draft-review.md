# Independent adversarial review: Week 16

## Verdict

**The mathematical construction is sound, and all 18 pages render cleanly. Make a few targeted wording and usability revisions before printing; a wholesale rewrite is not warranted.** The most important revision is Problem 3 in both older packets: the wording can make the intended ten-case investigation sound like a one-case task. K–1 Problem 1 also needs a very small clarification to rule out an impossible simultaneous reading.

I read the full brief, independently rendered each PDF, and visually inspected every page. I checked the source for exact dimensions and instructions. I also wrote a separate exhaustive checker, rather than relying on the author's saved results. I did not edit the draft.

## Revisions, in priority order

### 1. Clarify that repeated labels are allowed in both older packets' Problem 3

**Location:** Grades 2–3, page 3; Grades 4–5, page 3. `draft/src/generate.py`, lines 118 and 126.

The instruction begins, “Fill small triangles with R, B, and Y in every different way, counting turns and flips as the same.” Throughout the preceding problems, a triangle “with R, B, and Y” means a triangle with all three labels. A child can therefore reasonably put one of each label on every triangle and conclude that there is only one way after turns and flips are identified. That interpretation misses the repeated-label cases and destroys the local door-count investigation that the later explanation needs.

The first-page rule uses “R, B, or Y,” so the intended reading is recoverable, but the local problem should not depend on correcting its ordinary reading with a rule two pages earlier.

**Small fix:** “Put R, B, or Y on each dot. Find every different filling, counting turns and flips as the same.” Retain the existing door questions. This states the choice at each vertex without giving the cases, their number, or a method for organizing them.

The correct inventory has ten classes: three monochromatic, six using exactly two labels, and one using all three. There are seven zero-door classes, two two-door classes, and one one-door class. The twelve printed triangles leave two spare positions, which is reasonable; do not imply that all twelve must be different.

### 2. Make K–1 Problem 1 explicitly sequential

**Location:** K–1, page 1; `generate.py`, line 108.

“Move the counters to put a little triangle with R, B, and Y in each of the four places” can be heard as making all four places work in one filling. That is impossible: every one of this board's eight legal fillings has exactly one all-three cell. The intended task, moving that unique cell among the four locations over successive fillings, is good mathematics and is achievable.

**Small fix:** Add “one at a time,” or ask for “four fillings, with the R, B, and Y triangle in a different place each time.” Prefer the former for the one-hearing K–1 register. Do not state that every legal filling has exactly one; that is for the children to discover.

### 3. Enlarge the writable vertex circles on the older bands' large boards

**Location:** Grades 2–3, pages 1, 5, and 6; Grades 4–5, pages 1, 5, and 6. Shared `board()` routine, `generate.py`, line 36.

The blank circles are only **0.184 inches in diameter** (about 4.7 mm). Printed labeled circles are 0.30 inches in diameter. On the actual rendered pages, the blank circles are conspicuously small targets for handwritten capital letters, especially for the grades 2–3 group and repeated erasing. This is a usability concern rather than a clipping or mathematical defect, but it falls short of the brief's request for generous vertex dots.

**Suggested fix:** Use roughly 0.27–0.30-inch empty circles for boards on which children write. There is ample room: even the four-step board has 1.3125-inch vertex spacing. Keep the middle portions of edges clear for door marks and routes. Counter boards do not need the same enlargement because the counters cover their targets.

### 4. Consider giving the older Problem 1 tasks separate places to preserve contrasting fillings

**Location:** Grades 2–3, page 1; Grades 4–5, page 1.

Each asks for at least two distinct completed fillings, but supplies one board. The grades 4–5 task also asks for intermediate attainable counts. Children can erase and reuse the board, so this is not a blocker. However, erasing removes the first witness just when the problem invites comparison, and recreating a triangle mesh on spare blank paper is avoidable work unrelated to the question.

**Suggested improvement:** Supply a second full-size copy on an additional page, or provide clearly workable duplicate recording diagrams while retaining one full-size working board. There is no need to add instructions about what the extra diagrams are for. If the packet deliberately relies on transient trials, the present board can remain, but this is the most useful additional recording support to consider.

## Mathematical audit

No false theorem, illegal printed coloring, impossible requested construction, or malformed triangulation was found.

The independent checker built regular triangular cells from geometric adjacency, checked shared-edge incidence, total area, Euler characteristic, and the absence of vertices strictly inside another edge, and enumerated the legal assignments. The fan mesh was separately formed by inserting one vertex into each cell of the two-step mesh.

### Regular and fan boards

| Board | Vertices | Small cells | Exhaustive counts of all-three cells |
|---|---:|---:|---|
| Two-step | 6 | 4 | 1 in all 8 legal fillings |
| Three-step | 10 | 9 | 1 in 108 fillings; 3 in 72; 5 in 12 |
| Four-step | 15 | 16 | 1 in 2,920; 3 in 6,192; 5 in 3,840; 7 in 848; 9 in 24 |
| Two-step with four inserted centers | 10 | 12 | 1 in 264; 3 in 288; 5 in 90; 7 in 6 |

Consequences for the actual tasks:

- K–1 Problem 1: the unique all-three cell can occupy each of the four cells, in different fillings.
- K–1 Problem 2: avoiding every all-three cell is impossible under the stated rules.
- K–1 Problem 3: the maximum is five, not nine.
- K–1 Problem 4: with the printed boundary labels fixed, the possible counts are 1, 3, 5, and 7. The maximum seven is attained by three choices of the four free labels.
- K–1 Problem 5: every one of the sixteen cell positions can be the sole all-three cell. This is a substantial task, not a request with only a few available positions.
- K–1 Problem 6: allowing Y at the noncorner bottom-side vertices gives 52 zero-cell fillings. Requesting four different examples is feasible.
- Grades 2–3 Problem 5: exactly three all-three cells is feasible on its four-step board.
- Grades 4–5 Problem 6: relaxing only the starred bottom midpoint gives 208 zero-cell fillings while retaining the other restrictions and the three fixed corner labels. The star is correctly placed under the actual midpoint vertex.

### Printed door-route cases

The printed assignments satisfy all their boundary rules.

**Grades 2–3, Problem 2:** There are three boundary doors. Two are joined by a boundary-to-boundary route through three cells. The remaining door leads through five cells to the sole all-three cell. This is a well-chosen counterexample to the false claim that every chosen entrance must find an all-three cell.

**Grades 4–5, Problem 2:** There are three boundary doors and three all-three cells. The door graph has:

- One route joining a boundary door to an all-three cell, through two cells.
- One boundary-to-boundary route, through seven cells.
- One wholly internal route joining two all-three cells, through five cells.

This internal route is an open path between two all-three cells, **not a closed loop**. The wording “including any that stay inside” is accurate. Neither the page nor a later explanation should describe this specific component as a loop. No revision is necessary if it is described correctly.

The two printed examples supply the relevant pairing phenomena. The older packet's demand for an explanation for arbitrary edge-to-edge divisions is stronger than a finite enumeration, as it should be. The draft never presents the enumerated cases as a general proof and does not smuggle in the false assertion that one arbitrarily selected entrance always succeeds.

## Physical and visual inspection

All three files are six-page, 612-by-792-point US Letter PDFs. I inspected all six pages of each newly rendered packet at 80 dpi, checked the extracted wording against the source, and checked the existing LaTeX logs for missing-character, overfull, and underfull warnings; none were found.

- All headers, problem labels, body text, diagrams, side restrictions, footers, packet IDs, and page numbers are present and unclipped.
- There are no collisions between text and diagrams or between vertex labels and side restrictions.
- The working meshes are 5.25 inches across, within the requested 5–6 inches.
- All mesh edges are matched. The fan refinements introduce no T-junctions or gaps.
- K–1 boards have 6, 10, 10, 10, 15, and 10 vertices, respectively. All meet the fifteen-vertex limit.
- The tightest K–1 vertex spacing is 1.3125 inches, well above the 0.65-inch minimum. The roughly 0.4-inch counters have ample clearance.
- Letters distinguish all colors without relying on their pale fills. The material remains interpretable in grayscale.
- The fully printed door-route boards have enough open space within cells and across edge centers for tracing.
- The two local-classification pages have twelve legible, well-spaced triangles and room to mark doors and write counts.
- The row pages have readable endpoint labels and sufficient blank space for an explanation.
- The open lower portions of most pages provide useful space for counts, sketches, or explanations; their existence is not itself a layout defect.

### Page-by-page result

| Packet/page | Result |
|---|---|
| K–1 / 1 | Clean layout; clarify sequential readings as above. |
| K–1 / 2 | Clean; correct impossible challenge. |
| K–1 / 3 | Clean; valid maximization problem. |
| K–1 / 4 | Clean; correct fixed labels and conforming fan refinement. |
| K–1 / 5 | Clean; legal fifteen-vertex counter board; substantial search. |
| K–1 / 6 | Clean; bottom-side exception and unchanged corner labels work. |
| Grades 2–3 / 1 | Clean; valid min/max task; writable circles small; only one working copy. |
| Grades 2–3 / 2 | Clean; correct boundary-return example. |
| Grades 2–3 / 3 | Clean diagram; repeated-label wording needs clarification. |
| Grades 2–3 / 4 | Clean; all rows necessarily have an odd number of doors. |
| Grades 2–3 / 5 | Clean; exactly-three target feasible; writable circles small. |
| Grades 2–3 / 6 | Clean; correct impossibility problem on a different mesh; writable circles small. |
| Grades 4–5 / 1 | Clean; attainable counts are 1, 3, 5; writable circles small; only one working copy. |
| Grades 4–5 / 2 | Clean; the three route components have the intended contrasting endpoints. |
| Grades 4–5 / 3 | Clean diagram; repeated-label wording needs clarification. |
| Grades 4–5 / 4 | Clean; unlike endpoints force odd, like endpoints force even. |
| Grades 4–5 / 5 | Clean; valid general parity question and conforming example mesh. |
| Grades 4–5 / 6 | Clean; star is unambiguous and zero-cell fillings exist; writable circles small. |

## Fit to the organizer's standard

The draft largely follows the standard unusually closely:

- Six pages and six problems per band provide substantial material. The youngest packet is not a token shortened version: it includes impossibility, maximization, a refined mesh, relocation of a unique cell, and a changed boundary condition.
- Every numbered K–1 task has one or two sentences. Apart from the sequential ambiguity noted above, the tasks are suitable for reading aloud with the board visible.
- Only the page header and “Problem N:” labels function as headings. Side-rule annotations and vertex labels carry necessary mathematical information.
- There are no decorative activity titles, mascots, praise, exclamation marks, worked solutions, small lettered steps, or repetitive generic reflection prompts.
- The door-route rules define the object children are asked to investigate. In this context they are essential rules, not an inappropriate hint revealing the parity argument.
- Explanations are requested where they are the mathematical goal. The solution itself is not supplied.
- All tasks start from specified, drawn objects, and all color changes act on vertices rather than faces.
- The older packets build from experiments and a concrete route example to local possibilities, boundary changes, and a general explanation. The final weakened-boundary task in grades 4–5 appropriately tests the hypothesis.

The six-page count alone is not a timing guarantee, and the fully labeled route exercises may be quick for a strong child. Nevertheless, the searches, classification task, and explanation problems collectively supply plausible forty-minute depth. I do not see evidence warranting a demand for extra filler problems.

## Recommended revision scope

Make the two wording fixes, enlarge writable mesh vertices, and decide whether preserving the contrasting first-problem fillings warrants a second board. Keep the mathematical progression, the printed route assignments, the counter-board sizes, and the spare visual style. Re-render and inspect the changed pages after revision.

Independent check artifacts are in `critic-render/independent_check.py` and `critic-render/independent_check.txt`; the draft files are unchanged.
