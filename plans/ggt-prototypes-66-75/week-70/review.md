# Week 70 adversarial student-packet review

## Verdict

**Revise two concrete-use details, then retain the investigation.** The mathematics is sound, the four-page progression reaches a substantial finite-blocking theorem, and the diagrams are clean. The important weaknesses are the unstated replication of shield points on the unfolded map and a first map task that permits avoiding its intended new experience. These are narrow revisions, not a reason to simplify the mathematical destination or add younger packets.

Reviewed the authorized shared Grades 4–5 `draft/students.pdf`, all four pages. I read `PROMPT.md`, its scope addendum, `CRITIC.md`, the repository `AGENTS.md` and `README.md`, and the student source and checker. I freshly rendered all pages at 105 dpi and inspected each image in `critic-render/`. The draft SHA-256 is `5f80820aed0514c746af5c5c47226b3b8a3c4a0a11e3886d411dea5ce003eda5`. The draft and its source were not changed.

## Important revisions

### 1. Page 3: make a shield's repeated locations operational

The child places four points in the small room but the partner checks shots on a sixteen-room map. No instruction or worked visual explicitly shows that **each shield occurs at the same relative location in every copied room**. Page 2 explains that every T is the same target, but never extends that correspondence to an arbitrary marked point. A child may reasonably draw four shields only in the bold square, then regard a line that misses that square's four points as an escape. This is especially consequential because the shots are continuous and the printed grid is only a coordinate aid.

Add one short shared statement and a small non-solution visual showing one arbitrary point in two adjacent copies and its single-room location. The existing seam-crossing example could incorporate this without adding a new page. Do not print the four midpoint shields or direct children to use midpoints. Require the revision to be checked by tracing a non-diagonal line that meets a copy of a shield outside the bold room. This is an unfamiliar representation convention, not optional proof scaffolding.

### 2. Page 2: ensure its selected examples actually exercise portals

“Choose four different copies of T” permits choosing the four nearest targets, whose first-hit paths merely reproduce Problem 1's four short diagonals after identifying the corners. It also permits several collinear farther targets that all stop at the same earlier target. Therefore completing the task need not supply concrete practice in an interior seam crossing or folding back a genuinely wrapped shot before the difficult shielding investigation.

Give a small purposeful set of target copies, or a comparably concise constraint that guarantees contrasting crossings. For example, the displayed targets `(2,6)`, `(6,2)`, `(6,6)` and `(10,6)` supply horizontal/vertical wrapping, an earlier target hit, and a longer non-diagonal trajectory. They are all already in the printed window. This chooses examples, not the solving method. The partner should still determine which target is hit first and choose a shot to transfer to the single-room board.

## Page-by-page review

- **Page 1 / Problem 1:** The point-shield rule, first-target stopping rule, equal seam position and unchanged direction are present. The two seam pictures supply a useful non-task input/output bridge. All four S labels correctly denote one location. The four short diagonal interiors are disjoint, so the minimum is four, with many choices of positions. The four separate boards make the launch approachable, although some pairs may finish it quickly; it is an entry task, not a full-page duration guarantee. Keep the partner check and avoid appending a proof routine here.
- **Page 2 / Problem 2:** The unfolded window has accurate 4-by-4 room boundaries, a distinguished original room, sixteen target copies and a visible origin. There is ample straightedge space. The finite map includes earlier-hit examples. The weakness is selection of examples, described above. “Each square” could be changed to “Each large square” because the picture also has unit-grid squares. The final sentence about the bold square is a low-priority caption rather than substantive mathematical content.
- **Page 3 / Problem 3:** Testing proposed blockers against a partner's chosen ray is a good concrete investigation. The finite test is appropriately followed by a separate universal problem. The missing shield-copy convention must be repaired. The small room is roughly 4.2 cm across with about 1 cm unit spacing; counter centers can mark points, but physical accuracy has not been rehearsed.
- **Page 4 / Problem 4:** The task clearly distinguishes a finite map from all possible straight shots and asks for both sufficiency and minimality. The large room and writing space are adequate. The midpoint/parity explanation is genuinely late and readiness-dependent; keep hints in the later adult guide. Do not mistake successful tests on Page 3 for the universal explanation requested here.

## Mathematical checks

The supplied rational checker passes its 10,201 target lifts, first-hit normalization and midpoint tests. I also checked the argument in the independent kernel report: a lift ends at `(2+4m,2+4n)`; the midpoint of the segment to the **first** target folds to one of `(1,1)`, `(1,3)`, `(3,1)`, `(3,3)`. Thus the four point shields intercept before the target. The four signed shortest diagonal paths have pairwise disjoint open interiors, giving the matching lower bound. Neither endpoint can be used as a shield, and duplicate seam labels do not create extra physical shield locations. The student wording respects these assumptions.

No claim depends on treating a shield as a positive-radius disc, restricting shots to grid edges, or treating a segment beyond its first target hit as a valid unblocked journey. The independent kernel report supports the theorem; the code's finite sample alone is not its proof.

## Visual, scope and readiness checks

All four pages have the correct consistent header, footer, page number and consecutive numbered problem. No clipping, overlapping text, missing glyphs, distorted squares or insufficient answer area was found. The four-page shared packet is the authorized scope; absent K–1/Grades 2–3 PDFs and the absent adult guide are not defects at this stage. Sources are editable and contain no bundled borrowed reference text.

The source README honestly gates matching repeated locations and continuous straightedge tracing, and identifies the final proof as readiness-dependent. Before classroom use, the separate adult guide should show one legal line transfer and one repeated-shield check, provide spare erasable copies, and rehearse actual counter-center precision. This review is digital and unpiloted, not evidence that children can independently manage the representations.

## Independent exact-instance cross-check

Before closing this review I read the completed independent `draft-instance-review.md`. Its Week 70 result is PASS for all four problems. I verified that its PDF and student-source SHA-256 fingerprints match this reviewed draft. Its findings agree with this review; the proposed revisions above concern task selection, conventions or physical usability rather than a failed mathematical instance.
