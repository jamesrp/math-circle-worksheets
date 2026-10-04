# Independent review of Week 22 draft

## Verdict

**Revise a few task-design and recording details before release.** I found no incorrect geometric claim, impossible construction request, broken diagram, or page-layout failure. The packet is substantially aligned with the brief: real geometry at all three levels, ungridded full-size boards, no supplied solutions or proof-case checklist, and a genuine universal claim and sharpness question in grades 4–5. The concerns below are principally about the organizer's substantial-problem standard and whether children can retain the several answers requested on a single page.

I read `PROMPT.md`, rendered and visually inspected **every page** of the delivered PDFs (K–1: 6; grades 2–3: 6; grades 4–5: 7), inspected the LaTeX-generation source, and independently checked the finite geometric instances. The draft was not edited.

## Revisions, in priority order

### 1. K–1, page 5 / Problem 5 is too small to be a substantial standalone problem

The entire task is to test three locations for C and say which work. Two crosses lie on the line AB, one between A and B and one beyond B; the third is clearly off that line. The answers are yes, yes, no. By this point the child has already investigated three collinear triples in Problem 2 and all four successful partitions of a four-point line in Problem 3.

This is a useful change from four labels to three, but it is plausibly a one- or two-minute check for a quick child, rather than the required five minutes of experimenting without another instruction. The page does not ask for constructions, further placements, or a classification beyond the three crosses. Its large board should not be mistaken for substantial mathematical content.

**Requested revision:** Give this same three-label question more mathematical work while keeping the K–1 wording to one or two short sentences. For example, require children to find all positions for movable C that allow a meeting, beginning from the existing concrete A and B, or combine the three checks with additional purposeful configurations under the same numbered problem. Preserve the important beyond-B case; it prevents the mistaken rule that C must lie between A and B.

### 2. Several multi-answer tasks have only one usable configuration board

The most conspicuous examples are:

- **Grades 2–3, page 4 / Problem 4:** two arrangements are required, with no successful split common to them, but only one 12.6 cm square is supplied.
- **Grades 4–5, page 5 / Problem 5:** three arrangements are required, but again only one 12.6 cm square is supplied.
- **K–1, page 2 / Problem 2:** three successive positions of D, with two successful splits for each, all share one printed board.
- **The all-splits pages:** K–1 page 3, grades 2–3 page 2, and grades 4–5 pages 2 and 4 each require preserving four distinct answers on a single board. The older pages add two lines; the K–1 page has no separate picture-based record area.

These are not missing-material failures: the brief supplies tracing paper, an eraser, and blank paper, and moving markers is appropriate. However, the current pages rely on the adult to turn those materials into a record system. Drawing several colored or hatched hull pairs over one board will quickly obscure which groups belong to which answer. Erasing solves congestion but removes exactly the evidence needed for “every split” or for comparing two arrangements.

**Requested revision:** Make distinct answers retainable, prioritizing the two- and three-arrangement construction pages. Supply separate full-size work areas or continuation boards for simultaneous constructions, and small repeated recording diagrams where appropriate for enumeration. Keep a full-size manipulation board; do not shrink every configuration below the requested 12 × 12 cm. The record format should not preselect the groups, give an answer, or organize the seven cases for the child.

### 3. Grades 4–5, page 5 / Problem 5 permits a weak reading of “two different”

“Make two different four-dot arrangements with exactly one successful split” can be satisfied by copying the first arrangement a little to the left or slightly moving one point. Both arrangements can have precisely the same single successful labeled partition and the same geometric structure. The third arrangement can then simply repeat the collinear example from page 2.

That is a valid response to the actual question. The problem therefore does not reliably deepen the contrast needed before the all-arrangements explanation on page 6. This is an underconstrained task, not a mathematical error.

**Requested revision:** If the two examples are meant to have a meaningful contrast, state that contrast in the desired outcome. Requiring their unique successful splits to be different would be a modest improvement without handing out triangle/quadrilateral proof categories. Alternatively, replace the near-duplicate construction with a genuinely new restriction to investigate. Do not merely add “explain” again; the present explanation request cannot prevent the translation answer.

### 4. K–1's counting convention appears one problem late

Page 2 first asks for “every split.” Page 3 then says, “Swapping the two groups is the same split.” If colors distinguish the two groups during the demonstration, the first exhaustive search leaves room for a child to count the same partition twice, and the next page changes the apparent convention.

**Requested revision:** Put the group-swap convention at its first needed occurrence, on page 2 or in the common rules. This is a small clarity fix, not an additional hint about how to enumerate.

## Mathematical audit

I independently enumerated unordered nonempty partitions using exact rational coordinates and direct point-in-triangle / segment-intersection tests, rather than relying on the author's checker. The independent results agree with the draft's checks.

The target counts below follow the order of crosses in `build_packets.py`; the crosses are not numbered on the student pages.

- **K–1 P1:** one successful split at each of the three positions. The central target is genuinely inside ABC, and the two outside targets produce different diagonal pairings.
- **K–1 P2:** exactly two successful splits at each of the three positions. All intended boundary incidences are exact, including the sloping AC-side target.
- **K–1 P3:** four successful splits for the order A, D, C, B: AB|CD, AC|BD, ABC|D, ABD|C.
- **K–1 P5:** the middle target works with AB|C, the rightmost target works with AC|B, and the upper target does not work.
- **Grades 2–3 P1:** successful-split counts 1, 1, 2, 1. The third target is exactly on AB; the fourth is below it, not an accidental boundary contact.
- **Grades 2–3 P2:** four successful splits for the order A, D, B, C: AB|CD, AC|BD, ABC|D, ACD|B.
- **Grades 2–3 P3:** sharing a positive-length segment is possible. Sharing a nondegenerate filled triangle is impossible because a partition of four labels has a group of size at most two, whose hull cannot contain such a triangle. This is a sound and useful problem.
- **Grades 2–3 P4:** the requested pair exists. An arrangement with D strictly inside ABC has only ABC|D; a convex quadrilateral has only its diagonal pairing, so there need be no successful split common to the two arrangements.
- **Grades 2–3 P5:** the printed triangle has no successful split. For the moving-C question, the answer is the entire line through A and B clipped to the box, including extensions beyond both fixed points and coincident positions. It is not only segment AB. The stated question correctly allows this full answer.
- **Grades 4–5 P1:** successful-split counts 1, 1, 2, 1; all locations are valid.
- **Grades 4–5 P2:** the diagonal line really is collinear, in the order A, C, B, D. Its four successful splits are AB|CD, AD|BC, ABD|C, ACD|B.
- **Grades 4–5 P4:** the single mark labeled “A, D” represents the intended exact coincidence without hiding a label. The four successful splits are A|BCD, AB|CD, AC|BD, ABC|D. Separating the coincident labels guarantees an intersection in the general follow-up too.
- **Grades 4–5 P5:** the requested counts are attainable, subject to the task-design weakness noted above.
- **Grades 4–5 P6–7:** the universal four-point claim and sharp threshold are correct. The earlier pages supply contact, collinearity, and coincidence experiences before the universal explanation. The printed three-point instance is noncollinear and impossible. Two distinct points also fail, and one point cannot form two nonempty groups, so the requested minimum is four.
- The open placement games in **K–1 P4/P6, grades 2–3 P6, and grades 4–5 P3** are well-defined under the common rules. Their questions do not falsely promise a counterexample.

## Visual and editorial inspection

All 19 inspected pages pass the basic production checks:

- US Letter pages; boards are 12.6 × 12.6 cm in the source, meeting the working-size requirement at 100% printing.
- Clear point centers, distinguishable target crosses, legible labels, and no grid or precolored grouping.
- No overlapping labels, clipped text, accidental page breaks, or header/footer collisions. No overfull-box warnings were found in the three packet logs.
- Correct week, level, packet ID, and page numbering throughout.
- Only the permitted header and “Problem N:” headings; no decorative framing, encouragement, exclamation marks, or labeled substeps.
- Every K–1 problem stays within two sentences. Its common rules are relatively dense, but the planned oral demonstration makes that acceptable; the rules explicitly admit points and segments and say that one shared point counts.
- The shading instruction correctly requests the filled region rather than an outline alone. The center-of-marks instruction addresses the risk of thick strokes manufacturing contact.
- The older explanation requests are generally purposeful: completeness, impossibility, or a guarantee. They are not indiscriminately appended to every task.

The packet has enough page count and substantial open-ended work overall, especially in the older bands. I would not claim a demonstrated forty-minute timing failure from an unpiloted draft. The concrete short-task concern is K–1 P5, while K–1 P4 and P6 also deserve attention in a pilot because their game instructions are similar, despite the meaningful change from one movable dot to four.

## What to preserve

Keep the neutral voice, large ungridded configurations, mixed label orders on the straight-line examples, actual boundary-contact cases, and the distinct coincidence problem. Keep the child responsible for finding and organizing the argument. The needed revisions do not justify adding coordinates, a seven-case worksheet scaffold, the proof's case headings, worked partitions, or a separate facilitator guide.
