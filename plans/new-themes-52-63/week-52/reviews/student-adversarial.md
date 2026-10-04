# Week 52 adversarial student review

Reviewed October 4, 2026. Fresh critic stage only. Read `PROMPT.md`, `CRITIC.md`, the direct routing in `plans/new-themes-52-63/STAGE-ROUTING.md`, the Week 52 research notes, root README and REPUBLISHING.md, and the draft source/prerequisite notes. The routing override governs: one combined packet, honest page bands, no manufactured equal-band coverage. No draft, source, historical packet or global file was edited.

## Actual PDF inspected

Inspected **all 12 actual PDF pages**, individually at 108 dpi, after independently rendering `draft/students.pdf` with the requested Python/PyMuPDF/Pillow runtime. Also inspected three four-page contact sheets. Evidence is in `critic-assets/page-01.png` through `page-12.png`, `actual-text.txt`, and `render-checks.json`.

- PDF SHA-256: `a0a78506c7072052433879e06622805b08ce16ab55a0d0b0dab34db75f06b95a`.
- Every page is US Letter, 612 × 792 points. Problems are consecutive 1–14. Every page has a meaningful problem; page 12 is **not blank**.
- Bands: pages 1–2 K–1; 3–4 Grades 2–3; 5–9 Grades 3–5; 10–12 Grades 4–5.
- `draft/extracted.txt` is stale: it omits current rules/wording, puts Problems 13–14 together on page 11, and describes an empty page 12. Do not use that file as current review evidence. The current `draft/render/digital-checks.json` correctly records Problems 13 and 14 on separate pages.

## Judgment

This is a substantive, mostly well-designed draft. It should receive targeted revision, not a new theme or a flattening of the upper mathematics. The younger entry is appropriately shallow and genuine under the authorized routing; there is no reason to add four pages for K–1 or to repeat the same questions in three separate bands. The physical 2-by-2 and 2-by-3 investigations provide real placement choices. The later questions distinguish count, coverage, connectivity, redundancy and simultaneous removal, and can support a return visit.

No located false mathematical assertion or incorrect cell/link diagram was found in this design review. This statement is narrower than the independent mathematical audit, which follows separately. Digital inspection does not establish material fit, classroom success or physical rigidity testing; all remain unperformed.

## Revision priorities

### 1. Clarify the physical action in Problem 3 (page 2; definite wording issue)

“Remove the diagonal and make a new shape ... Which shapes can keep the diagonal?” changes from a clear action to an ambiguous one: the child has already removed the diagonal. It does not explicitly ask them to try fitting that same fixed bar into their changed frame. For children hearing this once, “keep” can mean retaining the piece nearby, keeping a bar attached while moving, or predicting a result. The mathematical investigation is worth retaining: the free four-bar shapes versus the shapes that accept the fixed square diagonal.

Use a short action such as “Remove the brace and make shapes with the four side bars. Which shapes can you fit the brace into?” Keep the opposite-corner convention in the existing definition and the fixed-length/flat rules in the shared guidance. Do not add a sequence of hints or announce the square-only conclusion. The large drawing area is useful and should remain.

### 2. Make the experimental-to-graph handoff operational before Problem 8 (page 7; material design risk, unpiloted)

The **conversion convention itself passes** the explicit-example requirement. Page 6 gives a non-task 1-by-3 frame with a single brace, the intermediate R1/C2 cell labels, and the resulting R1–C2 link while retaining isolated C1/C3. Labels match, arrows have a meaningful role, and the crossing convention is stated once. Preserve this example.

The subsequent **use of the graph as evidence about rigidity** needs a more explicit teaching route. Problem 7 supplies just one physical connected/disconnected pair on a 2-by-3 model, with the disconnected case having an isolated column. Problem 8 immediately asks children to decide about two 3-by-3 designs “using ... their link pictures.” Both designs cover every strip, so this is a genuine new obstruction, not a repeat of the isolated-column case. The supplied standard kits do not include a 3-by-3 frame. Drawing links alone does not explain why two linked groups can turn separately or why connected links stop shape change. With only the common square/triangle launch described in the outline, a child can accurately make the drawing yet have no warranted way to use it; an adult may then have to operate the entire argument.

This is a **hypothesis about the transition**, not evidence that Grades 3–5 cannot use this mathematics. Keep Problems 8 and 11–14. Before treating the paper-only designs as decidable, ensure the later adult guide/source route does one of the following:

- uses an actual rehearsed 3-by-3 comparison; or
- revisits a recoverable physical contrast already available, especially the two opposite braces in the 2-by-2 frame from Problem 4B, converts its brace record, and lets children see/check the two linked groups' separate turns before generalizing; or
- explicitly introduces the geometric reason that a brace couples a row-strip direction and a column-strip direction, then lets children use that reason independently.

The important bridge is fixed bar directions and separate group turns, not merely renaming cells. A brief adult demonstration/support can supply it without printing the full connectivity conclusion or a solution method on the student page. If the bridge is deferred to a return visit, identify Problems 8 onward as that readiness-dependent route in the notes. The source README currently says “diagram reasoning with adult support”; make the support and physical-kit alternative concrete enough for a facilitator to reproduce. A student wording adjustment that distinguishes a conjecture from an established explanation would also help if the theorem has not yet been justified.

### 3. Remove unnecessary technical reading from the K–1 opening (page 1; minor)

The flat, fixed-length, turning-joint rules are essential and correctly distinguish shape change from moving the whole object. “The kit's side bars measure 60 mm between pins” is fabrication information, gives the youngest readers nothing to choose, and interrupts the launch. Keep that dimension in the source/material notes. The statement that drawings are small recording maps has a legitimate scale-convention purpose, but can be shorter; do not replace it with an implied full-size promise.

### 4. Give the graph and response area a little more separation (pages 7 and 9; minor layout)

The first writing line is very close below the R3/C3 graph row. At full resolution it **does not intersect** the dots or labels, so this is not a clipping defect. A modest additional vertical gap would make child-drawn links and the writing area easier to distinguish. Plenty of unused lower-page room is available. Do not shrink the graph to solve this.

### 5. Refresh stale evidence at the revision stage (digital consistency)

Regenerate extracted text and render/check evidence from the final PDF. The stale `draft/extracted.txt` illustrates why file names alone do not establish version consistency. The current actual PDF agrees with `students.tex`, the current rendering report and the reported 12-page clean-rebuild checks. No old or global materials should be changed to resolve this draft-local issue.

## Page-by-page findings

| Actual page | Problems | Design and rendered evidence |
|---|---:|---|
| 1 | 1 | Concrete triangle-versus-square action after the live launch. Three and four sides/joints are shown correctly; equilateral triangle and square use equal x/y scaling. Separate drawing areas are generous. Remove the irrelevant 60 mm reading burden. No fabricated extra younger task is needed. |
| 2 | 2–3 | Two square maps accommodate either diagonal; definition of a brace is present before its later grid use. The common launch already shows attaching a diagonal, so Problem 2 may be quick, but Problem 3 can deepen the entry by testing changed shapes. Clarify the refitting action. No pin-by-pin fabrication is demanded. |
| 3 | 4 | Four purposeful 2-by-2 contrasts: one brace; opposite braces; three braces; all four braces. This gives time with the first obstruction and tests count versus placement. Flexible designs have usable drawing areas. C/D spaces need not be filled: the task requests changed drawings only for frames that change. |
| 4 | 5 | Minimum bracing plus several placements supports sustained exploration rather than merely repeating the successful design on page 3. Four blank maps can hold the four three-brace cell sets; drawing opposite diagonal orientations need not generate additional required cases. Maps are sufficient for recording, not promised as physical mats. |
| 5 | 6 | The 2-by-3 enlargement has materially more choices; four maps are adequate for “several,” and exhaustive enumeration is not required. Children choose both count and placement on a preassembled model. Preserve this concrete page before the graph. |
| 6 | 7 | Explicit input/intermediate/output visual is correct and compact. A/B each have four braces, yet one leaves C3 unlinked. Five graph dots are correctly retained under each frame. Strong physical comparison and graph-conversion work; it establishes an observation, not by itself the general rigidity theorem. |
| 7 | 8 | Five-brace 3-by-3 A/B contrast correctly defeats strip coverage alone. A has an upper-left 2-by-2 block plus the bottom-right brace; B joins all row/column dots. Six blank graph dots per case, enough space for links. Important mathematical question; operational bridge/optional kit needed as above. |
| 8 | 9–10 | Problem 9 explicitly restores each brace before another single-deletion test, maintaining one reference design. Frame and link drawings agree: R1 connects to all columns; R2 to C1/C2. Problem 10 deliberately starts from all six braces, distinguishes simultaneous pairs, and gives four independent records. It asks for working and failing pairs, not a compulsory 15-pair transcription. These are different worthwhile tasks. |
| 9 | 11 | A needs more than one added brace, while B can be joined by a single bridge; “every place” is a substantive finite search. Six graph dots per case and clear empty cells. Paper-only 3-by-3 reasoning needs the same earlier bridge. Writing line is close but below the graph. |
| 10 | 12 | Clear minimum-design-and-lower-bound question on a complete 4-by-5 grid, 20 square cells, labeled rows/columns and ample drawing/explanation room. This is readiness-dependent proof work, not a realistic physical model promised in the supplied kit. Keep it as a continuation/return visit. |
| 11 | 13 | Two 3-by-3 maps provide room for attempts at a counterexample or a packing argument. Six braces plus complete row/column coverage forces connectivity here; the contrast with page 7 is mathematically substantive. Two ruled lines are supplemented by a large blank lower page; no content is clipped. Preserve the universal question. |
| 12 | 14 | Complete 4-by-4 grid, 16 square cells, legible row/column labels and explanation space. Nine braces with coverage can still split into separate groups. This changes the answer to the preceding universal question and adds extremal reasoning, rather than just changing a number. No empty final page or footer problem exists in the current PDF. |

## Independence, staffing and scope

- Children retain meaningful choices of shape, brace placement, designs, deletions and additions. Existing pin/bar geometry is intended to enforce legal actions. Adult assistance with attaching/removing pins is compatible with children choosing locations. Whether one anchored adult can service two pairs without excessive waiting must be rehearsed; it is not established by this review.
- No simultaneous tallying is required. One marked brace map remains the main recoverable record, with link pictures added only after physical work. Problem 9's restore-before-next wording is especially good. Problem 10's separate maps help keep simultaneous deletions distinct.
- Whole-group handling and a legal gentle flat push are described in the outline/source notes. That physical launch is essential for the younger action, and should remain brief. The facilitator's later graph handoff has a different purpose and should not be compressed into the initial launch.
- The finite-rigidity question is appropriate for the physical core. Pin friction, bar bending, slop, lifting or mismatched diagonal length could falsify an apparent hand-test conclusion. These are physical rehearsal requirements for the later adult guide, not new child-facing warning text. Preserve the research notes' distinction between experiment, conjecture and mathematical explanation.
- The all-sides-present complete-grid assumptions are satisfied by every diagram. There are no holes, cross-grid braces, new joints at link crossings or promised full-size frames. All grid cells have equal axis scale, corner pins are visible, and braces terminate at real opposite corners. Text, headers and footers are legible with no overflow or clipped content found.
- Directions are generally concise, numbered tasks ordinary, and shared conventions stated once. No Name/Date boxes, decorative headings, generic encouragement or mandatory explanation after every small action appears. The worked convention example's labels are functional, not a second activity title.
- Returning-child novelty is real: this investigates length constraints and geometric flex, rather than reusing a fixed polygon triangulation or a rooted-tree code task. The existing research notes appropriately limit the novelty claim to this activity design around established mathematics; this review does not extend the collection-wide source audit.

## Completion condition for the reviser

Clarify Problem 3, trim the K–1 technical line, provide a concrete experimental-to-graph route without prescribing every child choice, and refresh draft-local evidence. Preserve the explicit conversion example, the contrasting physical designs, the reset convention and the upper universal/minimum questions. Render every final page again and complete the separate independent mathematical review and later theorem-first facilitator-guide review. Mark physical rehearsal and classroom piloting unperformed until they actually occur.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
