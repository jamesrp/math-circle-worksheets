# Week 59 independent mathematical review

Reviewed 4 October 2026. **Revise the two located convention issues below; the six intended task outcomes and nominal geometry are mathematically correct.** This is the fresh math-review stage only. No draft, guide, global file, or release was edited.

I read the project instructions, README, REPUBLISHING.md, direct stage routing, PROMPT.md, CRITIC-MATH.md, outline/research, adversarial review and all nine source files. The direct routing supersedes the stale three-band filenames: the actual audit inputs are `draft/students.pdf` (6 pages) and `draft/materials.pdf` (3 pages). I independently rendered and inspected all nine pages, including every approximate band header and every regular polygon, rotated arc figure, cutout and template size.

Input SHA-256:

- Students: `351434e079d83a1beb46b0b685e390863a92ad3411931f146da7ac0ef890f232`.
- Materials: `4f1f572fdf9fdba649adaafe92bf0055cc54200d2e0a47f10dcf9d9c0c10454d`.

## M1 / required — shared two-contact rule conflicts with the fixed gap

**Band/page/problem:** Grades 2–5, student p. 1 shared rule and p. 2 Problem 2.

**Exact text:** “The two straight edges must stay parallel, enclose the whole piece and just touch it.” Problem 2 then says, “Set the edges 60 mm apart. Which pieces can turn all the way around inside them? Which can keep touching both edges throughout the turn? Sliding is allowed.”

**Independent evidence:** At the oval's short-axis position, its support width is 40 mm. It fits between 60 mm rails, but no translation can make both rails touch: the two support lines are only 40 mm apart. The straight equilateral triangle gives the same contradiction at width `30√3 = 51.961524…` mm. Enforcing the shared two-contact rule would close the rails and destroy the fixed-gap condition, or wrongly reject these fitting positions. Both properties cannot be imposed at those orientations.

The intended fixed-gap outcomes, with free translation, are:

| Piece | Turns fully inside 60 mm rails | Touches both throughout |
| --- | --- | --- |
| Disk | yes | yes |
| Oval | yes | no |
| Square | no | no |
| Straight equilateral triangle | yes | no |
| Exact curved triangle | yes | yes |

**Smallest fix:** Scope the shared two-contact instruction explicitly to measuring width. In Problem 2 explicitly keep the 60 mm gap fixed while the piece turns/slides. Preserve both questions and all five controls. This correction must be on the student page, before the child's fixed-gap attempts; adult-only notes cannot remove the printed conflict.

This independently confirms adversarial-review R1. The contact requirement for measuring width, and the fixed enclosing rails for Problem 2, are individually valid.

## M2 / required — the new point-to-support measurement has no first-use visual

**Band/page/problem:** Grades 3–5, student p. 5 Problem 5 and its marked-piece diagrams.

**Exact text:** “Use the marked disk and curved triangle. Find the smallest and largest perpendicular distances from O to one touching edge. Can a piece have constant width while those distances change?” The page depicts O on each piece, with dashed construction lines/medians on the curved triangle, but no touching straight edge, O-to-edge perpendicular, right-angle marker or matching measured record.

**Independent evidence:** The correct measurements are `h_O(u)`, the perpendicular distance to a supporting line enclosing the whole piece. They are not the total two-edge gap, or a slanted O-to-boundary segment. For the exact curved triangle a support whose outward normal is 30° gives `60 − 60/√3 = 25.358984…` mm; the reverse support gives `60/√3 = 34.641016…` mm. A child who continues measuring the shared two-edge gap records 60 mm at every turn and misses the task's distinction. Arbitrary oblique segments measure yet another quantity. The p. 1 width example does not demonstrate the changed operation.

**Smallest fix:** Before first use, show a small non-task marked shape → enclosing touching line plus perpendicular O-to-line segment/right-angle mark → matching distance record. Identify O as a marked point. A separate off-center marked rectangle is sufficient and avoids displaying either target's extrema. Keep the choices of orientation and extrema with the children. Preserve the task and use a support enclosing the whole body; an intersecting line is not a legal substitute.

This independently confirms adversarial-review R2. The question and the marked locations themselves are correct.

## Checked scope and evidence handoff

Grades 2–5: Problem 1 and all five control extrema check out; Problem 2 checks out after M1. Grades 3–5: Problems 3–4, exact construction constraints and the all-direction support argument check out; Problem 5 checks out after M2. Grades 4–5: Problem 6 and its direct three-arc perimeter argument check out completely. All three materials pages check out digitally. No K–1 packet is required by the direct routing.

The independently authored [derivation and coverage record](../../../../tmp/worksheet-runs/week-59-new-v1/math-evidence/derivation.md) gives all task answers, angle/contact cases, whole-body support proof, marked-point bounds, source distinctions and digital limits. [Independent code](../../../../tmp/worksheet-runs/week-59-new-v1/math-evidence/independent_audit.py) imports no author geometry or verifier. [Machine-readable results](../../../../tmp/worksheet-runs/week-59-new-v1/math-evidence/independent-math-checks.json) record 7,200 analytic disk-intersection directions, 9 actual Reuleaux paths, 10 regular polygons, all 30 nominal arcs, markers, worked examples, 6 equally spaced boundary dots, all 100 mm bars and the 200 mm grid. Every clean ZIP-extracted rebuild page matches the input in text, dimensions and pixels at 108 dpi. The evidence ZIP is a scratch rebuild test, not a release source package.

Actual PDF curves are cubic approximations. The largest Reuleaux width error observed in 3,600 directions is 0.001631 mm. The full-size comparison disk's sampled widths are 60.000456–60.016920 mm; testing only its coordinate axes would miss that deviation. These figures are digital measurements, not certified physical error bounds or universal numerical proofs. Nominal geometry has the exact properties proved in the derivation.

Actual printer scale, stiff-card cutting/contact, rail clearance and parallelism, 60 mm fixed-gap handling, point-to-line measurement, compass stability, timing and classroom piloting remain **unperformed**. No physical tolerance, smooth rolling, platform, axle or square-hole test has been established. ThinkMaths's KS3/4/5 labels and the HMC construction/theorem are mathematical/activity precedents, not validation of elementary handling or this adaptation. The reviser should fix M1–M2 and recheck its actual final PDFs; this review applies only to the hashed draft.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
