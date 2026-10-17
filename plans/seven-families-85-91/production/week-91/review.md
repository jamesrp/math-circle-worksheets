# Week 91 adversarial critic review

## Scope and verdict

Reviewed the actual production-specific outputs: `draft/students.pdf` (6 pages), `draft/return-visit.pdf` (4 pages), and `draft/materials.pdf` (7 pages). Read `PROMPT.md`, the sources and writer verification notes, freshly rendered all 17 pages, and visually inspected every page. Render evidence is in `critic-render/`; independent mathematical results are in `critic-render/math-check.txt`. I did not edit the draft. The generic three-band filenames do not apply to this brief, and no separate K–1 packet or facilitator guide is required at this stage.

This is a mathematically sound, usable draft with good concrete apparatus and a sensible separate return visit. I found no false printed example, clipping, accidental extra page, or unusable full-size board. The strongest revision is a better contrasting eight-exit target; the remaining changes are local clarifications and recording improvements. Preserve the tree theorem, the feedback investigation, and the general road/termination questions. They belong as readiness-dependent continuations, not as requirements to finish in one hour.

## Recommended revisions, in priority order

### 1. Give the eight-exit programming page an obstruction below the root

**Location:** students p. 4, Problem 4, third target `A C E G B D F H`.

The proposed order is correctly impossible, but it begins with A then C, both in the left half, so the root alone rejects it immediately. Both impossible targets on p. 3 likewise fail root alternation (`ABCD` at the first pair; `DABC` at the second and third counters). The larger apparatus therefore adds no new impossibility reasoning in its supplied target set. The two achievable eight-exit targets are the all-left and all-right starts, which are symmetric.

**Specific fix:** replace the third target with `A E B F C G D H`, or add this as another target if space is deliberately expanded. It visits each leaf once and alternates left/right at the root, but the left subtree receives A, B, C, D, which cannot alternate between its two child branches. The right subtree similarly receives E, F, G, H. Thus children must use the new level of the machine to explain failure. Independent enumeration confirms it is impossible. This changes one example without adding directions or revealing the method on the student page. Keep the original root-obstruction example on p. 3 and keep Problem 5's invention task.

### 2. Make the second experiment in Problem 2 recoverable

**Location:** students p. 2.

The main prompt explicitly asks for starting arrows and arrival order, and supplies one blank miniature and one eight-box strip. The final sentence asks for different orders with D first. There are exactly two possibilities, `DACB` and `DBCA` repeated over eight arrivals; the children have only one purpose-built record. The open space below the final prompt can take a handwritten sequence, but there is no second state diagram, despite ample whitespace above/right of the first diagram. Repeated erasing would discard the comparison the task is meant to create.

**Specific fix:** provide two compact state diagrams with associated eight-box strips, or a second clearly associated state/arrival record. Do not tell children which arrow changes. A request to find *all* such orders would make the mathematical endpoint particularly clear, but is optional. This is a small layout improvement, not a request for extra trials or tallies.

### 3. Complete the common physical convention for all boards

**Location:** students p. 1 shared rules; return-visit p. 1 shared rules; materials pp. 1–5.

The one-switch material page says the counter waits beside the card, and the first demonstration illustrates that well. The other board pages do not repeat it, and the two packets' shared rules do not state it. A child placing a counter on the arrow obscures precisely the state the partner must check; on the road, revisits make that costly.

**Specific fix:** put the short convention “Keep the counter beside the card so its arrow stays visible” in the shared rules (or establish it once in the material-kit guidance used with both packets). Keep the partner's checker role explicit on the return visit too if it will be handed out independently. Do not add step counters or simultaneous node/flip tallies. The existing one-traveling-counter and persistent-state rules should remain.

### 4. Label the state slots in the return visit's comparison record

**Location:** return-visit p. 4, Problem 4.

“Starting arrows / After one block / After two blocks” each has four unlabeled slots, even though the child may choose the 0–4 road, which has three cards. The earlier miniatures spatially attach arrows to numbered nodes; this page silently changes to a row representation. L/R is illustrated in the first worked example, so another full worked example is unnecessary, but the row needs a small positional cue.

**Specific fix:** mark slots with positions 1, 2, 3, 4, and indicate that position 4 is used only on the 0–5 road, or provide small road diagrams in place of the generic rows. Keep the three observation times. The question may use any equal block length; do not accidentally restrict it so much that children are only reproducing an announced theorem.

The known example `LLR`, entry 1, road 0–4 yields `0,0,4,0` and changes to `RLL` after the first four launches, then stays `RLL` at later four-launch boundaries. It therefore demonstrates a failure of **immediate** full-state return, not perpetual state change at every block boundary. Any later solution/guide must preserve that distinction.

### 5. Tighten two small conventions without reducing the advanced questions

**Locations:** return-visit p. 1 worked example; p. 4 Problem 5.

- The worked example's input diagram has an entry arrow and the text “counter at 2” but no black counter dot; the intermediate and final diagrams have dots. Add the input dot beside node 2 for a fully matched input/intermediate/output visual. The trajectory and card states themselves are correct.
- In Problem 5, specify an **interior** entry `s` on the finite road `0,1,...,m` (the intended assumptions are integer `m >= 2` and `1 <= s < m`). “Always enter at the same inside circle, s” is enough student prose; formal inequalities can remain with adults. Keep the general rule and explanation task. It is a legitimate optional destination after the concrete 0–4 and 0–5 experiments.

## Mathematical audit

I independently enumerated all states of the one-, two-, and three-level trees and all states/entries for roads 0–3, 0–4, and 0–5. This was a separate implementation, not just rerunning the writer's tests.

- A one-switch run alternates. `XYXY` and `YXYX` are possible; `XXYY` and `XYYX` are not.
- Depth two has 8 initial states and 8 distinct four-arrival orders. `ACBD` and `BDAC` are achievable; `ABCD` and `DABC` are impossible. D-first orders are exactly `DACB` and `DBCA`.
- Depth three has 128 states and 128 distinct eight-arrival orders. `AECGBFDH` and `HDFBGCEA` are achievable. `ACEGBDFH` is impossible. The proposed replacement `AEBFCGDH` is also impossible for the deeper reason described above.
- All tested full tree blocks visit each leaf once and restore all arrows. The general explanation is successive splitting of an even bundle: each switch passes half to each child and flips an even number of times. This argument applies to every starting state and to any consecutive full-size block, not merely the all-left start.
- The feedback demonstration is correct: input cards at 1 and 2 are R,L; after 2→1 they are R,R; the remaining 1→2→3 ends with L,L.
- Return Problem 1 gives twelve exits `0,0,4,0,0,0,4,0,0,0,4,0`. Initial arrows LLR become RLL after four launches, and are RLL after eight and twelve.
- For every starting configuration on 0–4, eight launches from 1, 2, 3 have respectively 2, 4, 6 exits at 4. The individual orders may vary.
- For 0–5, every five-launch block from 1, 2, 4 has respectively 1, 2, 4 exits at 5. Sending all five to 5 from any of those entries is impossible.
- Across 4m launches for every state/entry of these short roads, every consecutive m-arrival window had exactly s exits at m; no simulated walk repeated a complete position-plus-card state. The longest single walks in these enumerations were 3, 6, and 10 steps for m=3,4,5, respectively. Thus the concrete experiments are manageable; this is not an argument that the general proof is elementary for every child.

The general road theorem is valid independently of the finite enumeration: with S the number of next-right arrows, every step preserves position + S. Summing over n completed launches yields `mR + S_final = ns + S_initial`. For n=m, `m(R-s) = S_initial-S_final`; the right side has magnitude at most m−1, so R=s. This forces equal counts of next-right arrows at the block boundaries, not equality of the full arrow pattern. Finite exit follows because an infinitely revisited interior vertex would send infinitely many visits to each neighbor, eventually including an absorbing endpoint. Keep proof scaffolding in the separate adult guide, as the brief requests.

The coin comparison makes the right distinction between possible strings and guaranteed balance. It does not incorrectly equate rotor routing with independent randomness. An ordinary coin is added in the source README; ensure that requirement survives later preparation notes.

## Page-by-page visual and action audit

| PDF / pages | Inspected outcome |
|---|---|
| students 1 | Clear move-then-flip demonstration with matching X/Y exits; two legible 12-box strips; substantial comparison included. No collision. |
| students 2 | Task and four-exit state miniature are clear; second-trial record is the local weakness described above. |
| students 3 | Four distinct target records, correct leaf labels and geometry; ample margins. All invalid examples currently test the same root-level restriction. |
| students 4 | Three eight-exit miniatures have distinct readable leaf labels. State circles are small but adequate for a single drawn arrow; full handling happens on the separate large board. Third target should test a deeper restriction. |
| students 5 | Invented-order and full-block questions preserve mathematical depth. Both tree miniatures are correct. Oral or separate-paper explanations fit the classroom setup; no need to replace them with worksheets of intermediate steps. |
| students 6 | Coin and switch records are clear and large. This page is accessible again to Grades 2–3 despite its placement after upper continuations; the source README identifies the route. |
| return-visit 1 | Complete correct revisiting example, distinct from the target road. Add the missing input dot for visual consistency. Twelve record slots match eight observed plus four predicted arrivals. |
| return-visit 2 | All three entry arrows match the stated 0–4 road. Eight-box records and blank node states are legible. |
| return-visit 3 | Entry markers correctly indicate 1, 2, 4 on 0–5. Five-box records match block length. The impossibility question and ratio search remain concrete. |
| return-visit 4 | Generalization and termination are preserved as advanced tasks. No overflow. Label the row-to-node mapping in Problem 4 and make the interior-entry assumption explicit in Problem 5. |
| materials 1 | One-switch board correct: junction at (108,95) mm, exits at (55,175) and (161,175); counter-beside-card note present. |
| materials 2–3 | Correct landscape US Letter tree boards, exact specified node centers, 24 mm junctions, four 30 mm exits / eight 22 mm exits. No line or label collisions. |
| materials 4–5 | Correct landscape roads and endpoint/vertex labels; specified 30/28 mm interior circles and 36/32 mm endpoint bins; ample space for the movable entry marker. |
| materials 6 | Seven paired 18×22 mm tree cards and four paired 20×20 mm road cards. Opposing arrow faces, common upright NEXT labels, clear dotted folds; no duplex-registration dependency. |
| materials 7 | Four 12-box strips, each box 15 mm; three entry markers; 50 mm scale check; no footer collision. |

All pages have consistent headers/footers and consecutive problem numbers within their task packet. Apparatus labels are appropriate on the materials pages. There are no Name/Date fields or unnecessary activity titles on student sheets.

## Age fit and limits

The first tree problems let third graders choose settings, operate a concrete machine and judge orders with a checker. The upper tasks retain those choices while asking for explanations. The separate feedback packet uses a worked revisit before asking children to operate roads themselves. This directly addresses the supplied classroom evidence about invisible rules, although paper cards still need a partner to enforce each flip.

The optional K–1 one-switch station is consistent with the special brief. Do not force a new packet merely to satisfy the generic harness. Return-visit Problems 5–6 require general reasoning and adult discussion; treat this as an expected readiness difference, not evidence that the concrete packet is unusable. There is enough work for multiple visits.

The apparatus dimensions and rendering are digitally checked. Cards have not been cut, folded, glued or handled with counters; a 100% print rehearsal and classroom piloting remain untested. This review does not claim physical readiness. A clean extracted-source rebuild, final revised-PDF inspection, source ZIP/version synchronization, and facilitator-guide verification remain later workflow responsibilities. They are not draft changes performed in this critic stage.
