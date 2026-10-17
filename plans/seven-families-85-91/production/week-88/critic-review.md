# Week 88 critic review

Reviewed `PROMPT.md`, current `AGENTS.md`, the embedded outline, `draft/src/students.tex`, `draft/math-checks.json`, and all eight pages of the actual `draft/students.pdf`. Independently rendered every page into `critic-render/` and inspected all eight at readable size. Shared Grades K–5 `students.pdf` is the explicit outline/user override; absence of three separate bands is not a defect. This is a critic-only review: no draft files changed.

## Judgment

The packet is coherent and substantially meets the brief. Keep its concrete first four pages, equal-circle explanation, exact row sensitivity investigation, and rich optional unequal/mixed-ring continuation. Two small clarity edits would improve independence before finalization. No mathematical error or clipping was found. Physical disk fit and classroom pacing remain untested; digital review does not certify either.

## Recommended revisions

1. **Define what the size labels measure before their first use (page 1, shared rules).** Student text repeatedly calls pieces “40 mm disks” or “80 mm disks,” but never says those numbers measure across a disk through its center. Page 5 then introduces radii. The outline knows these are diameters; a reader of the packet alone does not. One short shared convention, such as “Disk sizes measure straight across the center,” would settle this without adding a lesson or solving a problem. Adult selection of the pieces makes this a modest clarity issue, not a reason to reject the lower entry tasks. If using a diagram, a single diameter segment on the existing central disk is enough; do not add an unnecessary multi-step example of an ordinary measurement.

2. **Label the page 8 diagrams as sketches, not actual size.** Pages 3–4 explicitly establish this distinction, but page 8 uses a new reduction (80 mm disks drawn with 24 mm diameter; 40 mm with 12 mm diameter) and asks for center distances. A short figure caption or scale convention prevents treating ruler readings on these figures as millimeters of the physical disks. Preserve the compact diagrams and drawing space; no need for actual-size large rings on Letter.

Optional polish: on page 5 place the intermediate “15” and “25” directly beside their corresponding A-to-contact and contact-to-B segments, with units consistent across the figure. Currently they float well above the line. Their left-to-right correspondence is recoverable, and the diagram already passes the required full input → meaningful intermediate → output test; this is legibility refinement, not a missing-example blocker.

## Page-by-page inspection

| Page | Content | Findings |
|---|---|---|
| 1 | Rules; Problem 1 equal-disk ring | Concrete, brief, actual-size middle disk; enough space for a six-disk ring and larger legal attempts. A numeral is the only written record. Size convention recommendation above. No need to disclose six or prescribe angles here. |
| 2 | Problem 2, practical 160 × 112 mm tray | Large usable board, no encroaching boundary ink, clear maximization question. “Our best” correctly describes experimental evidence, not a proof of a global maximum. Practical tray identified; keep it distinct from the later exact comparison. |
| 3 | Problems 3–4, reversed sizes | Useful contrasting constructions. Off-page desk mat is explicit in Problem 3; reduced-size figures are identified as sketches. Two different-size cases retain mathematical choice. All text fits. |
| 4 | Problem 5, mixed sizes for both centers | “At least one outside disk of each size” removes the important ambiguity. The desk-mat instruction and non-actual-size label are present. Each center has its own record; enough space and no simultaneous tally burden. |
| 5 | Center-distance worked example; Problem 6 | Non-task radii 15 and 25 avoid giving the ring answer. Same A/B pair appears in all three stages: touching disks, centers joined with contact point splitting radii, sum 40 mm. It appears before the first explicit center-distance task. Equal-ring impossibility and equality rigidity are valuable explanation questions. Preserve them. |
| 6 | Problem 7, 160 × 110 mm, 4–3–4 rows | Exact board fits Letter and uses outward-only ink. It requests the specified row construction and center-distance justification, not unrestricted optimal packing. The small physical tolerance requires adult preparation/rehearsal, not a claim that a screen rendering proves fit. |
| 7 | Problems 8–9, 160 × 108 mm and minimum height | Correctly limits impossibility to the stated straight-horizontal-row arrangement. “Those three rows” carries the condition into the minimum-height question. Space below is sufficient for a short diagram/argument; longer working can be externalized by adults. No claim that all eleven-disk packings fail. |
| 8 | Problems 10–11, ring bounds and general size rule | Four diagrams map correctly to the four earlier cases (two congruent outer-size cases, two mixed cases). This is a substantial optional continuation, not appropriate compulsory K–1 work. Add the scale warning above. General rule should remain available for a return visit or advanced conversation. |

## Mathematical audit

- Equal disks: consecutive outside centers lie at distance 2r from the middle center. Nonoverlap forces each cyclic separation to be at least 60 degrees. Thus at most six fit, six exist, and six forces every separation to be 60 degrees, so every neighboring outside pair touches. Problem 6 asks the correct rigid-equality question.
- Congruent outside disks: the minimum pair angle is `2 asin(r/(R+r))`; summing cyclic angles gives `floor(pi/asin(r/(R+r)))`. Independent numerical evaluation gives 6 for diameter 40 around 40, 9 for diameter 40 around 80, and 4 for diameter 80 around 40. The packet does not print an unsupported answer.
- Mixed cases in the writer's check file are 8 about diameter 80 and 5 about diameter 40, with witnesses using one large outside disk and the remaining small ones. The student pages correctly require both sizes but do not equate a physical best attempt with a proof. A full upper-bound derivation belongs in the separate mathematical review/guide; the saved JSON alone is not a reproducible proof or exhaustive verification script.
- For each four-disk row in a 160 mm width, centers are forced to horizontal coordinates 20, 60, 100, 140 mm. A middle-row center is at horizontal distance at most 20 mm from a center in each neighboring four-disk row. Each row gap is consequently at least `sqrt(40^2-20^2)=20 sqrt(3)` mm. Aligned three-disk midpoints attain this. Minimum total height is `40+40 sqrt(3)=109.2820323...` mm. Hence the specified arrangement fits 110 mm and 112 mm but not 108 mm; unrestricted arrangements are outside this argument.
- PDF vector geometry and source agree on the three interiors. The tray consists of four filled strips outside the interior, rather than a centered line consuming some of it. The slight PDF coordinate rounding is far below a millimeter. Physical print scaling, disk tolerances, and actual placement remain to be rehearsed.

## Operational age fit and limits

These are unpiloted hypotheses, not classroom observations or reasons to remove the advanced material:

- Problems 1–5 offer a viable shared concrete route with adult reading and physical pieces. The lower table can work on these without understanding radii, angles, or exact arithmetic. The practical packing and reversed/mixed size cases provide distinct work rather than a short token kindergarten entry.
- Page 5 changes the prerequisite level. The adult can support tracing centers and distances, but equal-ring impossibility needs a route to the 60-degree bound. Exact height needs right-triangle reasoning; the complete general ring formula uses inverse trigonometry. Problems 6–11 should therefore be selected by readiness and available adult support, with returning visits encouraged. The shared K–5 header does not imply every child completes them.
- The 110 mm tray has only about 0.718 mm geometric slack. A ruler, printer, cutting tolerances, and imperfect rigid disks may overwhelm it. Keep the practical 112 mm board as the main physical construction and present 110/108 as exact models supported by geometry. The writer has not claimed physical rehearsal passed.
- A future facilitator guide must supply the brief whole-group legal-placement launch, prerequisites, stopping points, materials quantities and 260 × 260 mm desk mat, and theorem-first explanations. Their absence from this student-only workflow stage is not a defect. No extra launch script or adult commentary should be added to the student pages.

## Verification scope

All eight draft pages visually checked. Source and PDF inspected for scale conventions and tray geometry. Writer log has no reported overfull/underfull warnings. Reviewer computed the congruent-ring ratios and row-height value independently. No source ZIP reconstruction, physical fit test, or classroom pilot performed in this critic stage. No final revised outputs reviewed yet.
