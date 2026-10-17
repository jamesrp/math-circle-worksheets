# Week 85 adversarial draft review

Reviewed 17 October 2026. Critic stage only; no draft files changed.

## Verdict

Revise before accepting the prepared printable prototype. The mathematical mechanism and task coordinates are sound, and the packet retains substantive work on copying, inverse control, an invariant, area, inverse scaling, and moving the center. Three concrete presentation/material problems need correction: the convention strokes are too small to see reliably, insert identifiers are lost when the pieces are cut, and the area grids are misregistered with their shapes. None calls for removing the deeper investigations.

This is a digital review, not a hardware rehearsal. The explicitly stated coaxial-mounting, branch-control, spacing, support and hand-clearance gates remain real. The review does not establish physical readiness or classroom piloting.

## Required revisions

### 1. Make both operation demonstrations visibly show the input stroke, intermediate stroke and output

**Locations:** shared p. 1; upper p. 3; `demo()` in `draft/src/generate.py`.

The three-panel structure and fixed O are correct, and the middle arrow points to the appropriate controlled tip. However, the raw stroke spans only 10 mm horizontally and is displayed at scale 0.245: the complete T stroke is only 2.45 mm wide. Its first segment is about 1.77 mm long, comparable to the 2.2 mm diameter endpoint ring. The stroke is 0.65 mm thick. In the actual rendered pages the small blue trace largely merges into its joint ring; the final copied mark looks like a small hook at P. The reader sees three posed mechanisms much more readily than a meaningful traced action. The same limitation affects the reversed demonstration, where seeing the small T output is especially important.

**Fix:** enlarge the non-task stroke substantially within the legal open-frame geometry, reduce the endpoint symbols/stroke thickness if needed, and place the labels clear of the traces. Make the already-traced portion visibly distinct from the current tip. Retain three real states with O fixed, and keep the scale theorem unprinted. Check both normal and reverse demonstrations at actual print size, including grayscale legibility; do not substitute extra explanatory prose for a visible stroke.

### 2. Keep A–M identifiers on the cut pieces

**Locations:** materials pp. 5–9; `input_insert()` and `output_insert()`.

Every insert letter is placed above its border. The instructions tell the adult to cut on that border, so all 13 letter labels are discarded. The student tasks then refer repeatedly to named inserts and targets, and the adult material checklist assumes an identifiable A–M set. The full-page PDF labels are legible, but the finished movable materials are not labeled.

**Fix:** place the identifier inside a clear margin of each cut rectangle, away from the tracing region and corner registration marks. Preserve the actual-size boundaries and shape coordinates. Verify all A–M pieces after a digital crop to their cut borders. The bridge can likewise carry a small identifier inside its cut border if one is useful, though it is much less ambiguous than the inserts.

### 3. Align or remove the area-insert grids

**Locations:** materials p. 7, inserts G and H; materials p. 8, insert I; `input_insert()`.

The 10 mm grids do not pass through the shape vertices or match their unit-cell boundaries. TikZ's `grid` is being drawn at page coordinates with `step=10mm`, which places grid lines at the page lattice rather than at the intended translated insert lattice. For example, G is placed at (22,32), and its square begins at (42,52); the rendered grid lines are at x=40,50,... and y=50,60,... . H is placed at x=121 and I at y=133, creating other offsets. Even a grid simply snapped to insert corners would need the correct 5 mm y-offset for these particular global input coordinates, whose horizontal boundaries use y=125,135,145,... .

The printed grid therefore gives a conflicting visual representation of the 10 mm square unit precisely where children are meant to tile and count. This is not a false area calculation, but it adds avoidable uncertainty to the concrete area investigation.

**Fix:** explicitly draw a translated 10 mm lattice aligned with the actual G/H/I vertex coordinates, or remove the decorative grid and let the supplied square/half-square pieces carry the unit. Inspect all three resulting inserts, not just G.

## Recommended small clarification

**Shared p. 4:** “the largest rectangle T can trace whose copy fills the box” mixes a traced boundary with filling an area. The intended target is the inner 40 × 30 mm box, while the diagram also contains a large dashed placement rectangle. Put F close to the inner box and use a short boundary-specific goal such as making the copy follow that box's outline. The outer dashed rectangle can remain as a placement locator. This avoids an adult having to distinguish two boxes or explain why a traced perimeter counts as filling.

**Upper p. 3:** the sentence “L is the small box on an input insert” can become part of the numbered task's essential setup or be replaced by a compact L locator. It currently reads as a separate explanatory aside, and the page otherwise has enough space for the actual box reference. This is a minor format issue, not a reason to add more procedural steps.

## Mathematical checks and solutions relevant to revision

The source implements the intended open rhombus: O–X–Q and Q–Y–P are straight 160 mm bars with 80 mm half-bars; X–T and T–Y are 80 mm. For the displayed branch, writing X−O=u and T−X=v gives Q−O=2u, Y−O=2u+v and P−O=2u+2v. Thus P=2T−O, assuming the intended simple open rhombus and exact coaxial ideal joints. Numerical sampling of the declared T zone gave equal-length squared-distance residual below 4e−12 mm². That numerical check supplements the identity; it is not a proof of physical behavior.

All A/B/C/G/H/I/M original vertices fit the declared T zone, and their copies at O=(40,140) fit the 110 × 100 mm output region. D and E are reachable by controlling T. E's inverse vertices are (120,125), (150,125), (150,145), (135,157.5), (120,145), so its roof is within the permitted zone. The supplied D dots also have preimages in the zone. Straight connections between these points remain inside the rectangular zone.

- Shared P1: corresponding lengths double; angles, straightness, shape and orientation are preserved. A is a 35 by 20 mm elbow; B is an asymmetric triangle; C is a stepped path. These make useful contrasting experiments.
- Shared P2: D's five preimages are (115,125), (130,160), (155,150), (150,120), (125,140). E produces the half-size house above. The child's control choice is clear and substantial.
- Shared P3: no intended ideal pose breaks O–T–P collinearity; OP=2OT and OT=TP. Trying positions is evidence for a conjecture; the upper frame argument supplies a universal explanation.
- Shared P4: F's inner box occupies output x=220..260, y=125..155. Its tracer rectangle is x=130..150, y=132.5..147.5, of size 20 × 15 mm. It is reachable.
- Upper P1: the six equal-length marks and two straight midpoint bars support the factor-two explanation on the stated simple open frame. Do not infer universality across collapsed or crossed states.
- Upper P2: **actual generated** areas are G=4, H=4, I=4.5 square units, with copies 16, 16, 18. These differ from some illustrative values in the earlier plan. G and H intentionally can serve as equal-area, different-shape comparisons. The 48 squares and 16 half-squares suffice for each original/copy pair at a time. For I, the original can use three squares and three halves, and the copy fifteen squares and six halves: 18 squares and nine halves total.
- Upper P3: J shrinks to a 30 × 20 mm rectangle, and K to a 40 × 20 mm arrow. L is x=125..155, y=130..150; the required P rectangle is x=210..270, y=120..160, of size 60 × 40 mm. All fit.
- Upper P4: O′=(60,140), a 20 mm rightward anchor shift. With M unchanged, the copy shifts 20 mm left. Shifting M 10 mm right makes the O′ copy coincide with the original O copy. The shifted M vertices stay in the T zone, including the x=160 boundary. The movable insert's paper border will shift beyond its original registration box, which is consistent with the deliberate final task; the traced shape remains within the allowed zone.

## Print and materials checks

All 18 actual PDFs pages are US Letter, 612 × 792 PDF points. The source uses equal millimeter scaling on both axes. The templates have 182 × 18 mm long strips, 102 × 18 mm short strips, and 80 mm adjacent hole-center spacing. The unit page contains 48 squares and eight diagonal-split squares yielding 16 half-square triangles. Input pieces are 70 × 70 mm; output pieces are 110 × 100 mm.

The two-sheet mat uses x=215.9 mm as its join. Its intentional printer-margin gap spans x=207.9..223.9 mm. The 44 mm bridge covers x=194..238 mm and y=70..215 mm; its four registration centers correspond to x=204/228 and y=80/205. The bridge restores the output rectangle across the gap. Its isolated text fragments on p. 5, and truncated text on p. 3, are intentional pieces of joined labels rather than ordinary PDF overflow. The drawing coordinates and registration scheme are digitally consistent. No printed-paper assembly or calibration measurement was performed.

The materials explicitly require rigid strips, freely rotating spacers, a coaxial T hinge/tracer and centered P tip; they do not pretend that a line drawing is a manufactured sleeve or proven stack. This is appropriate prototype honesty. Retain the fabrication gate in the eventual guide and release notes. The warning alone does not make classroom use ready.

## Complete rendered-page coverage

Every page was individually opened as a 1.1× raster render after reading the brief and generator. Images are in `critic-renders/` for audit; no draft was rebuilt or changed.

| PDF/page | Inspected content | Result |
|---|---|---|
| shared 1 | Rules, normal operation example, A/B/C, response space | Required demonstration fix; otherwise clear, substantial entry |
| shared 2 | D dots, E house, inverse-control task | Clear; no clipping or wrong target |
| shared 3 | Invariant task and labeled mechanism | Correct diagram, ample response area |
| shared 4 | F target and constraint task | Boundary/inner-box wording clarification recommended |
| upper 1 | Equal-length frame and explanation task | Correct six marks and labels; suitable gated continuation |
| upper 2 | Half-square join visual, G/H/I area task | Meaningful visible convention; correct contrasting shapes |
| upper 3 | Reverse example, J/K and L task | Required demonstration fix; minor L setup clarification |
| upper 4 | Fixed-input anchor change and M compensation | Clear successive tasks, no theorem leaked |
| materials 1 | Four actual-size drilling strips | Labels, margins and spacings clear |
| materials 2 | Assembly topology, board, joining, rehearsal gate | Honest and readable prototype instructions |
| materials 3 | Left mat, O/O′, input region, calibration | Matches intended coordinates and bridge scheme |
| materials 4 | Right mat and registration | Correct continuation and join marks |
| materials 5 | Bridge, A/B | Join geometry consistent; cut-piece letters lost |
| materials 6 | D/E | Actual-size shapes fit; cut-piece letters lost |
| materials 7 | F/G/H | Cut-piece letters lost; G/H grid alignment wrong |
| materials 8 | I/L/M/C | Cut-piece letters lost; I grid alignment wrong |
| materials 9 | J/K | Actual-size targets fit; cut-piece letters lost |
| materials 10 | Squares, halves, supplies and per-pair checklist | Correct counts and dimensions; practical cutting remains adult prep |

The deliberate shared Grades 2–5 packet and upper Grades 4–5 continuation comply with the outline override. There is no missing mandatory K–1 packet. Headers, footers and consecutive numbering are consistent; no Name/Date fields, decorative titles, or generic encouragement were found. Most tasks leave genuine choices with children once the machine and insert placement have been demonstrated. The area, inverse and anchor work can support return visits rather than an expectation to finish all eight problems in one sitting.

After revision, rerender both student demonstrations and all affected material pages, recheck labels after crop and grids against dimensions, and retain the full final-page/source-package checks required by the repository. This critic review has not performed an extracted-source clean rebuild, physical rehearsal, classroom trial or remote upload check.
