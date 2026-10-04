# Week 59 fresh adversarial critic review

Reviewed 4 October 2026. Critic stage only: no draft edits, facilitator guide, publication, or math-review substitution. Recommendation: **revise two essential convention issues, then retain the substantive route for final review**. This is a digital review of an unpiloted adaptation; it does not certify physical handling or age fit.

## Scope and evidence

I read `AGENTS.md`, `README.md`, `REPUBLISHING.md`, `plans/new-themes-52-63/STAGE-ROUTING.md`, this run's `PROMPT.md` and `CRITIC.md`, Week 59's outline/research/novelty records, and the nine files in `draft/src/`. The direct routing instruction controls the stale three-band filenames in the generated harness. I reviewed the actual combined `draft/students.pdf` (six US Letter pages) and `draft/materials.pdf` (three US Letter pages), independently rendering and looking at **every page**, including every band header and all regular-polygon/arc/cutout/template variants.

Audit inputs:

- `students.pdf` SHA-256: `351434e079d83a1beb46b0b685e390863a92ad3411931f146da7ac0ef890f232`.
- `materials.pdf` SHA-256: `4f1f572fdf9fdba649adaafe92bf0055cc54200d2e0a47f10dcf9d9c0c10454d`.
- Independent renders, extracted text, and input metadata are in `critic-evidence/`.
- A fresh copied source directory compiled successfully. `critic-evidence/clean-build-check.json` records identical page counts, page text, 612 × 792 pt dimensions, and pixels at 108 dpi for both PDFs. This review did not repeat the writer's ZIP extraction; its separate successful extraction record is in `draft/qa/rebuild-checks/rebuild-verification.json`.

I also directly reread the relevant elementary teaching precedents: Rozhkovskaya, *Math Circles for Elementary School Students*, Lesson 6 “At the lesson,” in EPUB `OEBPS/part0016.xhtml`, and Givental et al., *Math Circle by the Bay*, Preface vii–ix (PDF pp. 8–10). These inform the operational review below; neither validates this Week 59 adaptation.

## Required revisions

### R1 — High: scope the two-contact rule so the fixed-gap investigation has legal attempts

**Evidence:** Student p. 1 opens, “The two straight edges must stay parallel, enclose the whole piece and just touch it.” It presents that instruction as shared guidance. Student p. 2 / Problem 2 then sets the edges 60 mm apart and asks separately which pieces can turn inside and which can touch both edges throughout. See `draft/src/students.tex:24` and `:32`.

The mathematical distinction on p. 2 is worthwhile, but the printed legal-action rule conflicts with it. An oval at its 40 mm orientation, or a triangle at its approximately 52 mm orientation, fits between 60 mm edges while it cannot touch both. A child following the shared rule can close the rails, thereby undoing the fixed gap, or reject the legal one-contact/no-contact position. This is particularly consequential given the group's reported difficulty with rules that require repeated adult correction.

**Required change:** Scope the touching-edges rule explicitly to *measuring width*. State in Problem 2 that the 60 mm gap is kept fixed while the piece turns/slides. Preserve both classification questions and the five controls. The distinction between fixed enclosing rails and adjusted touching supports must be concrete before the child chooses a deciding position; do not resolve this only in a future adult guide.

**Why this matters:** It removes a genuine instruction conflict without prescribing the discoveries. The intended three outcome classes remain: square cannot turn fully inside; oval and straight triangle can fit through a full turn but lose simultaneous contact; disk and exact curved triangle can retain both contacts throughout.

### R2 — Medium: show the first point-to-support measurement before Problem 5

**Evidence:** Student p. 5 / Problem 5 changes the measured quantity from the two-edge gap to the perpendicular distance from O to one touching edge. The page's two miniature pieces show O (and the curved triangle's dashed construction triangle/medians), but **no touching edge or perpendicular O-to-edge segment appears anywhere on that page**. See `draft/src/students.tex:55` and `draft/src/make_assets.py`, `heightTable` through `table(..., marked=True)`. The p. 1 worked visual concerns a gap between two parallel edges, not a distance from an interior mark.

The word “perpendicular” is mathematically correct, but the change of reference point is the central new convention here. The current illustration does not distinguish measuring to a support line from measuring a slanted O-to-boundary segment or treating O as a circle center. That distinction is exactly what this task is intended to investigate. There is also no worked recording example for the changed measurement.

**Required change:** Put a small explicit non-task marked-shape → touching edge and perpendicular segment → matching recorded distance visual before first use. Use a different, preferably off-center marked example so it demonstrates the operation without displaying either target's extrema or supplying the theorem. O should be identified as a marked point, with the student retaining the choices of orientations and extrema. Keep the marked-point investigation; do not replace it with an axle/roller demonstration or disclose its answer in a procedure.

This is an essential measurement convention, not a request to append optional hints or explanatory substeps. It follows the project's first-use visual rule and its explicit concern about bridges between physical and recorded representations.

## Page-by-page coverage

| Actual page | Evidence and assessment |
| --- | --- |
| Students 1 / Grades 2–5 / Problem 1 | Clear non-task three-panel parallelogram visual: piece → parallel contacts → recorded gap. The perpendicular arrow/right-angle mark and matching 46 mm label distinguish width from a center chord. Five contrasting pieces and two extrema each support substantial child-chosen experimentation. Plenty of sketch space; no small directed steps. R1 concerns the scope of its shared rule, not the example's geometry. |
| Students 2 / Grades 2–5 / Problem 2 | A valuable new question, not duplicate measurement practice. Three outcome categories require distinguishing fitting from both-side contact. Sliding is explicit; there is no center pin. Table has room for one decisive drawing per piece. R1 must clarify which rule governs these fixed rails. A deciding counterexample can disprove a claim; one recorded drawing cannot establish an all-turn affirmative claim. |
| Students 3 / Grades 3–5 / Problem 3 | Input/intermediate/output compass convention is explicit and precedes use: given D,E,F → opening DE with point at D → short arc EF. It is a non-task quarter-arc instance rather than the target Reuleaux construction. Two sizes allow prediction and a scale comparison. Optional construction requires adults for compass points/cutting and is correctly treated as a continuation, not the physical entry gate. |
| Students 4 / Grades 3–5 / Problem 4 | The non-task circle → one contact → right-angle visual precedes the tangent fact's use. Three labeled, differently rotated exact curved triangles support an all-direction explanation; the task explicitly includes turns between drawings. The problem retains mathematical depth and ample work space. It is readiness dependent and requires the adult proof support described below, not merely three matching measurements. |
| Students 5 / Grades 3–5 / Problem 5 | A substantial and mathematically important distinction between total width and distance from O to one support. The marked disk and exact marked curved triangle are correctly paired. No wheel/axle claim appears. R2 is the missing essential first-use visual; preserve the question and the children's extremum choices. |
| Students 6 / Grades 4–5 / Problem 6 | Exact boundary-length comparison is clearly requested. The small disk is labeled radius 30 mm; the generating circle is radius 60 mm, with six equal sectors/dots and the matching highlighted BC arc. Those radii must remain distinct. Fractions and scaling supply a richer continuation without requiring pi notation. Good space and legibility. |
| Materials 1 | Six separate full-size pieces, thin cut boundaries, outside captions, two exact Reuleaux copies (one marked), disk, 60×40 oval, square and equilateral triangle. No caption intrudes into a piece or adjacent boundary. The 100 mm bar is separate and clear. Adult preparation instructions distinguish cutouts from compact student diagrams. |
| Materials 2 | A full 200×200 mm, 10 mm grid and separate 100 mm bar fit on Letter. Separate straight edges/right-angle guides are required; the sheet itself does not mechanically enforce rail parallelism. Physical printer margins/guide handling remain untested. |
| Materials 3 | Two 60 mm-side and two 40 mm-side equilateral A,B,C templates on the page; print three copies supplies six of each. Labeled corners and room outside each triangle permit the outward-bulging minor arcs. Correctly marked as templates rather than precut pieces. Check bar and all labels are clear. |

All student problems are numbered consecutively 1–6. Headers, footers, normal text, diagrams and recording areas follow the approved concise format. There are no Name/Date fields, encouragement, extra page titles, invented enrichment labels, or adult timing/hints on student pages. The materials sheet has preparation text appropriate to its separate role. No text or diagrams clip or overlap in the inspected renders.

## Mathematical substance and geometry assessment

This critic checked the exact source definitions against the intended geometry and read the mathematical destination/proof notes; a separate fresh math review still follows and should independently verify every task and figure.

- The geometry uses equal x/y millimeter units. The 60 mm base vertices are `(0,0)`, `(60,0)`, `(30,30 sqrt(3))`. All depicted Reuleaux figures use three radius-w minor arcs centered at the three equilateral vertices, with nominal ranges 0–60, 120–180 and 240–300 degrees (rotated/scaled when needed), not generic rounded corners. See `draft/src/geometry.py` and `Picture.shape` in `make_assets.py`. Materials templates use the same equilateral geometry at both sizes.
- The source distinguishes the comparison disk's radius 30 from each Reuleaux construction radius 60. The material marked O is the underlying equilateral centroid, not a common center for the three arcs. Dashed construction markings do not change the cut boundary.
- Source `mathematical-notes.md` retains the **whole-body support** argument, not only a radius drawn to an arc. In a direction u between AB and AC, the opposite point A+w u lies on the BC arc and the A-centered disk bounds the upper support. The B- and C-centered disk inequalities put the whole body on the correct side of the line through A. Three vertex sectors and their reversals cover every direction. These assumptions and sector coverage are essential; tangent perpendicularity by itself does not prove constant width.
- The controls are purposeful. Nominal extrema: disk and Reuleaux 60–60 mm; oval 40–60 mm; square 60–60 sqrt(2) mm; straight equilateral triangle 30 sqrt(3)–60 mm. The square broadens the fixed-gap classification and is documented as an authored addition to the four-control outline.
- Source notes correctly separate finite experiments from an all-orientation explanation. The writer's numerical arc/vector checks are error detectors, not a universal proof. Its reported greatest digital width error is approximately 0.00164 mm, a cubic-arc approximation distinction that cannot be used to certify cutting/contact tolerance.
- The marked-point witnesses are approximately 25.359 and 34.641 mm for the exact curved triangle, versus 30 mm for the disk. The target property is a change in perpendicular support distance, not an arbitrary radial-distance measurement. R2 is necessary to make that target operation visible to children.
- The perimeter comparison is the direct three-sixths-of-a-radius-60-circle calculation and comparison with its radius-30 scaled circle. It does not require a general perimeter theorem. Keep this separate from width and radial distance.
- No square-hole, fixed-center turning, smooth thin-card rolling, constant axle height, or experimentally verified platform claim appears in the student pages/materials. The source notes expressly deny those unperformed mechanical demonstrations.

## Preserve depth, with honest operational gates

The current bands are honest approximations under the direct authorization: Grades 2–5 for support-gap comparison; ready Grades 3–5 for compass construction, all-turn argument and marked-point support distance; ready Grades 4–5 for arc fractions/scaling. There is no forced K–1 packet. Casual adult-led handling alone is not evidence that younger children understand the investigation.

Source README specifies practical prerequisites: choose/retain orientations, compare whole-mm readings up to about 85, maintain/understand parallel supports and perpendicular gaps, read or hear the short prompts, use a fixed compass radius, and later reason across continuously many orientations or use sixths and scaling. Adult reading/recording and alignment assistance can be compatible with child ownership: children still choose orientations, search for extrema, decide the categories and check observations. If an adult selects every turn, adjusts every state and dictates the comparison, the core is not functioning as a child investigation. This is a pretest criterion, not an observed failure or a reason to remove the accepted upper mathematics.

Problem 4 is genuinely substantial. Keep it. The adult route must be ready to help children connect a contacting vertex to its opposite arc and to account for the transition between vertices/orientations. It must not accept “the radius is always 60” without explaining why both parallel lines enclose the whole shape, or accept equal gaps in three printed turns as proof. The independently authored notes already contain the destination; a future separately authored guide should make its concrete use feasible. The absence of that guide in this writer-only stage is correct and is not a writer-stage defect.

The first two pages can sustain a concrete first visit. Construction, universal explanation, marked-point comparison and boundary length can support later visits; they do not need to be compressed into the available 35–40 working minutes. Construction itself is procedural, but choosing/testing predictions at two sizes and connecting the constructed object to a later invariant is a meaningful continuation. Preserve that connection.

## Preparation, physical limits and evidence discipline

The notes properly call all physical pretests and piloting **unperformed**. A digital render/clean build cannot turn this into a physically ready packet. Before describing it as classroom ready, the eventual adult preparation/rehearsal must resolve:

- Five kits require **30 accurately cut stiff-card pieces**, ten long straight rails, five measuring rulers, ten movable right-angle guides, and five full grid mats. Optional construction offers twelve templates across two sizes and six adjustable compasses, with additional adult cutting if all are used. This is a real preparation load; no preparation time has been measured.
- Two pairs at the third-grade table share one adult. Rails/guides must let pairs keep the supports parallel, enclosing and lightly contacting while the children choose positions, rather than needing an adult to operate each measurement. The marked-point perpendicular measurement also needs a workable physical method.
- A 60 mm fixed gap against a nominal 60 mm piece is especially sensitive to print scale, cut smoothness, rail movement and contact. Test the actual printer, measured bar and models; do not silently widen the gap and then claim both-side contact. The proposed ±1–2 mm trial tolerance is explicitly unestablished, not a guaranteed error interval.
- The grid is 200 mm wide, while the described rails are 300 mm long; bench space and rail clearance must be tested on the actual tables. Use of right-angle guides is mentioned, but a printed ideal parallel-line diagram does not establish successful hand control.
- Compass radius stability, cuts, contact clarity, the child's retention of the changed rule in R1, the changed measured quantity in R2, timing and realistic staffing remain physical tests. No actual observations from this Week 59 group are reported.

Pedagogical source discipline is sound in the research/source notes and must remain so. ThinkMaths is labeled KS3–5; its parallel-edge investigation and construction establish a mathematical/activity precedent for older learners, not validated elementary feasibility. The HMC source supports the established construction/result, not elementary piloting or this exact all-direction proof. Rozhkovskaya actually reports low child enthusiasm for her angle-cutting experiments and offers insufficient experience as an explanation; that explanation is a hypothesis, not a rule banning geometry. *Math Circle by the Bay* supports deep themes, unambiguous understandable tasks, manipulatives and adult help with explanation. My inference is that the contrasting physical controls and visible legal supports are promising, while actual retention and independence still require rehearsal.

## Handoff

Reviser: fix R1 and R2 in the student pages, retaining all six substantial tasks and the exact geometry/upper depth; update source notes/verification coverage as needed and inspect every new render. Independent math reviewer: audit the actual task answers and every arc/template/cutout, including the support-sector proof's whole-body and coverage steps. Future guide author/reviewer: use the final student version, begin with a theorem-first overview, retain readiness gates and realistic material counts, and continue to mark rehearsal/piloting unperformed unless actual evidence is recorded. Do not publish or move this critic-stage draft into the current library.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
