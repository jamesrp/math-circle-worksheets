# Week 62 adversarial student-page review

Reviewed October 4, 2026. Scope: the actual **nine-page `draft/students.pdf`**, not the obsolete three-file paths in the generic CRITIC.md. Read PROMPT.md, the direct override in `plans/new-themes-52-63/STAGE-ROUTING.md`, `plans/new-themes-52-63/week-62/source-notes.md`, the source README, and relevant authored source. No draft files were changed. An independent mathematical review follows; this report concentrates on the usability and design of the student investigations.

**Verdict: preserve the packet and make four localized revisions.** It offers a legitimate Grades 2–5 entry followed by substantial Grades 4–5 continuations. There is no reason to manufacture K–1 pages, extend page count, turn the investigations into substeps, remove the arbitrary-network proof, or replace the first-fit and counting work. The main issues are a cycle-definition loophole, ambiguous repair instructions, a drawing obstruction, and an incomplete visual recording bridge.

## Revisions to make

### R1. Define a cycle so one edge traversed out and back is excluded

**Location:** PDF p. 4, shared definition before Problem 4; `draft/src/make_source.py:117`.

The definition says a cycle returns to its start “without repeating any other circle.” Read literally, W–X–W satisfies it: X is visited once and only the start is repeated. This is not a cycle in the simple undirected graphs used here. The square example demonstrates a proper cycle but does not rule out the shorter walk. A precise definition matters when Problem 5 asks for a general criterion.

**Action:** add the requirement of at least three distinct circles to the existing brief definition, with the start repeated only at the end. For example: “A cycle follows conflict lines through at least three different circles and back to its start. Only the start repeats, at the end.” Preserve the non-task square input/partway/completed visual; it already models the traversal and marking without disclosing the odd-cycle theorem. The independent math reviewer should check the final definition.

### R2. Make the objective and permission in the repair phase explicit

**Location:** PDF p. 7, shared first-fit rule and the final sentence of Problem 7; `make_source.py:155` and `:176`.

The shared rule applies to Problems 7–8 and says “Do not move a placed card.” Problem 7 then asks “Could moving placed cards improve either result?” This does not clearly release the restriction or say what improvement means. The preceding two objectives are *fewest* and *most* slots: a child could reasonably regard increasing the maximum from three to four by separating cards as an improvement, whereas the mathematical destination is repairing a valid but wasteful schedule to use fewer slots.

**Action:** explicitly put repair after completing the first-fit trials and name the objective of reducing the number of slots. One concise replacement is: “After an order is finished, you may move cards. Can you use fewer slots?” Keep the first-fit procedure mandatory only during an ordered trial. Do not provide the bad order, the optimal partition, or a repair method. The two graphs and order records are useful and should remain.

### R3. Remove collinearity that obscures legal added conflict edges

**Location:** PDF p. 6, both networks in Problem 6; `make_source.py:44` and `:46`.

A, B, C lie in one straight row, as do D, E, F. In the upper network adding AC is a valid one-edge answer, but a straight AC stroke runs through B and retraces the existing AB and BC lines. In the empty network choosing the triangle A–B–C similarly produces an ambiguous drawing. The rule that unmarked crossings add no activity does not resolve a new line passing through an already marked activity. This is an actual geometric affordance of the page, not an assumption that children cannot reason about graphs.

**Action:** slightly stagger the sites in both drawings so no three are collinear and no available straight connection runs through another site. Keep all six labels, the five original tree edges, the empty second graph, and 20 mm sites. This is preferable to introducing curved-edge rules or directing children to a particular successful triangle. Check the revised coordinates and rendered endpoints. Leave enough room for the children to add and erase their own lines.

### R4. Show the actual circle-mark record before its first use

**Location:** PDF p. 1, final panel of the shared example; repeated convention on p. 7; `make_source.py:95` and `:172`.

The graph-to-tabletop input/intermediate/output examples are present and meaningful. However, their claimed “circle marks” outputs are text lists (`X 1, Y 2, Z 1` and `X 1, Y 1, W 2`). No example actually shows a numbered mark in a circle, although the shared rule requires exactly that record. All task circles already have a centered letter, so the child still has to invent how the second label fits and distinguishes card name from slot number. This is a small remaining representation bridge, not a missing scheduling example.

**Action:** in the p. 1 final panel, show a compact copy of the X–Y / isolated-Z network with both the fixed activity labels and the chosen slot numbers visibly positioned inside the circles, matching the completed tabletop schedule. Replace the text list rather than adding another explanatory paragraph. Use the same convention in the p. 7 output, or omit that repeated record if it is already clear from p. 1. Keep the non-task examples and do not show the answers to the task graphs. The record should be visibly distinct from the letter labels and leave sufficient room for pencil marks on the full-size sites.

## Page-by-page coverage

Every page was newly rendered from the actual PDF with PyMuPDF at 1.6× and visually inspected. Files are in `review-working/page-01.png` through `page-09.png`; extracted text and PDF geometry are also saved there. The table reports the full-size circles in the actual rendered PDF; smaller worked-example circles are excluded.

| PDF page / problem | Band printed | Full-size sites | Design assessment |
|---|---|---:|---|
| 1 / 1 | Grades 2–5 | 10 | Good concrete entry: path versus high-degree star, with unrestricted tabletop slots. Legal placement and goal are stated. Both cases together support material handling and experimentation; do not split them into tiny questions. Repair R4. |
| 2 / 2 | Grades 2–5 | 13 | Strong contrast: diamond, complete four-vertex graph, and many-edge bipartite graph. Number of lines alone does not predict the minimum. Crossings do not silently become vertices. “Show why fewer” is the central minimum certificate, not a generic explanation appended to an easy task. |
| 3 / 3 | Grades 2–5 | 14 | The five-cycle with a leaf supplies a genuine clique-bound gap; the six-cycle with two leaves contrasts it. The every-pair condition has been concretely supported by p. 2. Keep the central comparison; branches alone are not the novelty, but its role in scheduling/minimum certificates is substantive. The clique result can be retained with the cards or discussed by pointing; no large written catalog is needed. |
| 4 / 4 | Grades 4–5 | 16 | Chorded six- and seven-cycle networks make children inspect cycles inside a network; branch and isolated activity also matter. The square convention visual has a real intermediate and output. Repair R1. The two outcomes are meaningfully different, and the marked obstruction can itself carry much of an explanation. |
| 5 / 5 | Grades 4–5 | 15 | Important general rule and arbitrary-size proof, with components and isolates explicitly present. This is appropriately harder than the preceding construction tasks. Preserve it as a readiness-dependent destination; examples are evidence for a conjecture, not the general proof. |
| 6 / 6 | Grades 4–5 | 12 | Substantial construction/minimality task: change a tree versus an edgeless graph. It deepens the rule instead of adding another ring-coloring page. Repair R3; otherwise the requested action is clear and space is ample. |
| 7 / 7 | Grades 4–5 | 8 | The repeated path now has a different mathematical purpose: first-fit depends on order and can be wasteful. A compact three-vertex non-task example models the procedure without giving the bad order. Orders plus final marks are recoverable records, with no concurrent tallies. Repair R2 and the repeated R4 convention. |
| 8 / 8 | Grades 4–5 | 8 | Worthwhile eight-vertex first-fit construction, with two versus four slots and an upper-bound explanation for five. It is not padding. The two order lines are sufficient recoverable records for trials; the adult may preserve one counter state while another is tested. Do not require enumeration of all orders or discard the degree argument. |
| 9 / 9 | Grades 4–5 | 8 | Fixed-label counts on the path and diamond are new graph families; this is not the already-used ring count. Named slots and empty slots are stated. The example fixes X and gives two completions, clearly labeled as different schedules rather than the total. Keep the complete-count argument, with readiness gating and spare paper handled by adults. |

## What passes and should be retained

- All nine pages are US Letter, 612 × 792 pt. Headers consistently give week, topic, and an honest approximate band: Grades 2–5 on pp. 1–3, Grades 4–5 on pp. 4–9. Footers consistently give Bellingham Math Circle / Week 62 / W62-S-v1 and consecutive page numbers. Problems are numbered 1–9 without restarting.
- No Name/Date boxes, extra page titles, encouragement, “go further” labels, small prescribed substeps, or facilitator hints appear. The small labels within worked visuals identify their states and outputs and are useful diagram labels. Shared rules are brief and stated at first use; the special first-fit and named-count rules have real purposes.
- No visible clipping, overlaps, distorted circles, tiny working diagrams, hidden capacity boxes, or unlabeled extra activities were found. Source and visual inspection agree on 104 full-size sites, all **20.000 mm** across in the PDF. The tightest gap between full-size site boundaries is **5.000 mm**, on pp. 3–4. At 100% print scale, the drawings meet the nominal site-size constraint for counters up to 15 mm. The vector measurements are in `review-working/diagram-measurements.json`.
- The diagrams' vertex/edge counts match the inspected task structures: p. 1 (4/3, 6/5); p. 2 (4/5, 4/6, 5/6); p. 3 (6/6, 8/8); p. 4 (8/8, 8/9); p. 5 (7/5, 8/7); p. 6 (6/5, 6/0); p. 7 (4/3 twice); p. 8 (8/7); p. 9 (4/3, 4/5). The straight-line crossings on p. 2 add no vertices. No polygon-side-count issue arises; apparent rings are graphs, with their actual vertices and edges accounted for.
- Workspaces suit the action. Children manipulate cards on a separate unlimited-capacity tabletop and can place counters or pencil marks on the large graph sites. p. 6 provides the board on which they draw. Written explanation lines are supplied where extended proof or counting may need them, and the stated materials include spare paper. Most early certificates can be shown with objects and a short oral argument.

## Adult-guide and operational handoff, not additional student instructions

The source README already distinguishes matching A–H labels / counting through eight on pp. 1–3, path and component reasoning / ordered trials on pp. 4–8, and systematic counting with multiplication on p. 9. These prerequisites are meaningful. The following are **unpiloted operational hypotheses and required guide planning**, not claims that the children will fail or reasons to remove the mathematics:

1. **Make partner checking enforce the conflict rule.** A tabletop placement does not physically stop two conflicting cards from sharing a slot. After the brief whole-group demonstration and material handling, the checker should match endpoints on the fixed graph and accept or reject a candidate. The scheduler should retain the choices. This is especially important with two pairs at the third-grade table and one anchored adult. No second tally or copied edge table is needed. The source-notes proposal is appropriate, but it has not been rehearsed.
2. **Test the actual kit before calling it ready.** The draft has lettered networks, not printable activity cards or slot headers. Adults must prepare the specified A–H picture/letter cards and numbered slot headers or the eventual bundle must supply them. Rehearse one p. 2 network and a p. 7 first-fit trial with the real kit. Check that 15 mm counters do not obscure the activity labels or needed edge endpoints: the digital size check does not establish that fact. Cards belong under headers on the table, not on the 20 mm graph sites. Physical handling remains untested.
3. **Offer concrete tasks alongside the general proof.** p. 5's converse for arbitrary networks is substantially harder than alternating colors around one visible ring. The adult overview must distinguish experiments, an odd-cycle conjecture, the obstruction direction, and a general sufficiency explanation component by component. A matching lower bound certifies a minimum; unsuccessful attempts do not. Preserve the proof, and let children continue concrete work or return to it later if they are not yet ready to explain the converse.
4. **Gate p. 9 by counting readiness.** The path has 24 and 108 named assignments for three and four available slots; the diamond has 6 and 48. The goal is a complete organized argument, not mandatory transcription of all 186 assignments. Children who are not yet ready for products can explore smaller cases with cards; systematic branches, product reasoning, and optional later chromatic-polynomial context belong with the adult. Do not add the formula or a directed counting recipe to the student page.
5. **Keep the theorem-first facilitator overview and flexible route.** The future guide should open with the precise scheduling assumptions, clique lower bound and its limits, bipartite iff no odd cycle (including components and isolates), and first-fit validity / degree bound versus optimality. A first visit can spend its time on pp. 1–3 plus chosen concrete upper tasks; pp. 5, 8, and 9 can support deeper work or another visit. A nine-page packet is not a requirement to finish nine pages in forty minutes.

The local teaching evidence supports this caution without proving our adaptation: Rozhkovskaya, *Math Circles for Elementary School Students*, Lesson 7, “At the lesson,” item 1 reports game outcomes probably caused by missed legal moves; Lesson 8, item 2 reports slow and uneven copying/coloring. *Math Circle by the Bay*, Preface printed pp. viii–x, supports deep themes, manipulatives, and varied pace. Relevant locally extracted passages were consulted. Partner checking, durable marks, and the proposed readiness routes are our inferences, not classroom results from those books.

## Novelty and limits of verification

The inspected draft passes the source-notes novelty test as a whole. Week 33/35 ring alternation is background; Week 36 triple constraints are different. This packet's distinct work is pairwise simultaneous scheduling with minimum certificates; the clique bound's failure; internal cycles in chorded, branched, disconnected networks; and order-dependent first-fit on paths and a larger tree. Path/diamond named counts are a further new direction. Preserve those investigations and do not add ring-only exercises merely to increase coverage.

This critic personally rendered and inspected every actual draft page and measured the PDF's sites. The writer's existing `draft/clean-rebuild-checks.json` reports equal text, dimensions and pixels for every page of its clean rebuild; that claim was read, not independently rerun here, because this is a read-only critic stage. No extracted-release ZIP exists to test at this stage. The independent mathematics reviewer and later final-release inspection remain necessary. No physical rehearsal, classroom piloting, remote upload, publication, or claim about the rest of the worksheet collection is established by this review.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
