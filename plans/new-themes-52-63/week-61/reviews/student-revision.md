# Week 61 fresh revision: Triangles on a ball

Completed October 4, 2026. Revision stage only, after `review.md` and `review-math.md`. The direct stage routing produces one combined [students.pdf](../../../../tmp/worksheet-runs/week-61-new-v1/final/students.pdf), seven US Letter pages, packet ID `W61-S-v2`. No facilitator guide, older material, repository index, project instruction, remote file or Git state was changed. This is ready for organizer review and remains unpiloted.

## Repairs and actual packet coverage

| Final page / actual band | Final student-page evidence | Coverage status |
| --- | --- | --- |
| 1 / Grades 2–5 | Fixed endpoints, surface contact, points → circle → shorter arc convention; close/far/opposite comparisons and records. | Already sufficient in the actual rendered page; content preserved, footer version updated. |
| 2 / Grades 2–5 | Positive surface area now explicit; distinct nonopposite corners, minor great-circle sides, smaller convex region strictly within an open hemisphere. Surface-angle convention remains before the three-right-corner construction. | Changed for scope precision; actual page inspected. |
| 3 / Grades 2–5 | Meridian explicitly defined as a great-circle semicircle. Three independently chosen pole/equator constructions and coverage comparison retained. | Changed for the mathematical condition behind the right-angle crossing; actual page inspected. |
| 4 / Grades 3–5 | Non-task 40° lune → nine equal lunes → 1/9 record; three marked meridian-gap triangle investigations. | Already sufficient in the actual rendered page; content preserved, footer version updated. |
| 5 / Grades 4–5 | First-use 80° geometry now shows input corner A with B/C labels → selected circles AB and AC → containing/opposite pair in front/back views → interior patch X with a one-pair count record of 1. The octant then has a recoverable eight-region map and blank three-pair tally. | Changed for reviews M1–M2; no target three-pair tally is printed. |
| 6 / Grades 4–5 | Genuine second covering investigation on the same 80° geometry, with unequal cells, complete front/back maps and one pair-letter/count record. It precedes generalization and applications. | Added for review M3; actual page inspected. |
| 7 / Grades 4–5 | Universal rule and explanation, including persistence of counts and antipodal equality of area, followed by the three exact numerical surface-angle applications. | Revised from draft page 6; exact records are retained as applications, not physical exact-construction tasks. |

The views on pages 5–6 look along the oriented normal of one side plane and its opposite. The positive hemisphere contains complete cells 1–4; the negative hemisphere contains complete cells 5–8. All visible cells have IDs, all limb vertices have matching labels, and hidden projected arcs are omitted. The page states that front and back show the same ball. The original Python geometry generator was extended rather than replaced; `build.py output_directory` is preserved byte for byte from the draft.

Boundary-normal views also exposed floating-point limb classification in the original clipping routine. Clipping now treats limb endpoints consistently and omits cells with no visible interior. This prevents an invisible cell's projected fill from entering the visible hemisphere. Independent final fill reconstruction confirms the repair.

## Mathematical substance and readiness

The 80° geometry is independently checked: regions 1 and 8 each occupy 1/12 of the sphere; the other six each occupy 5/36. Pair counts are 3,1,1,1,1,1,1,3. Each opposite-lune pair occupies 4/9, so total counted area is 4/3 spheres. The exact general proof, separately stated in [source notes](../../../../tmp/worksheet-runs/week-61-new-v1/final/src/source-notes.md), orients the three side-plane hemispheres, verifies all eight sign cells and pair-membership tests, and uses equal antipodal area to derive `area=R²(angle sum−π)` in radians, or whole-sphere fraction `(sum−180)/720` in degrees. This structural explanation is distinct from checking examples or sampled pictures.

The entry retains physical surface routes, actual corners, the variable-meridian family and substantial construction choices. [Source prerequisites](../../../../tmp/worksheet-runs/week-61-new-v1/final/src/README.md) distinguish concrete entry, equal-slice area work, overlapping counted area, and the exact explanation. Pages 5–7 can be a later visit; children can continue concrete covering work alongside the readiness-dependent universal explanation. Neither a supplied exact angle record nor a projected angle is treated as a calibrated physical construction or measurement.

## Verification of delivered outputs

- [Independent final reconstruction](../../../../tmp/worksheet-runs/week-61-new-v1/revision-qa/check_final_independent.py), adapted from the independent math reviewer's reconstruction and importing no builder/research geometry or verifier, checks 12 triangle instances, all area fractions and eight-cell memberships, and the final emitted figures. [Results](../../../../tmp/worksheet-runs/week-61-new-v1/revision-qa/independent-final-checks.json): 8 filled macros with 58,196 interior projection samples, 18 arc macros with 5,449 emitted arc samples, all 8 covering/example label macros, correct AB/AC selection, correct sample X signs +−− and count 1, all seven headers/bands/problems/footers and Letter dimensions.
- Finite emitted-path/fill checks have explicit limits: rounded polygonal samples, a 0.02 side-plane-dot boundary exclusion, and the outermost 1% of projected radius excluded from fill sampling. Complete four-cell hemisphere visibility and the universal multiplicity are justified structurally, rather than inferred from sampled points.
- Every latest rendered final page was inspected at 108 dpi: `revision-qa/final-page-01.png` through `final-page-07.png`. All bands, sphere/circle proportions, arc styles, antipodal labels, region IDs, sample count, blank records and writing space were checked. No overlap, clipping, unlabelled sliver or ambiguous hidden subdivision remains. TeX logs for all three builds contain no warnings or overflows. [Extracted text](../../../../tmp/worksheet-runs/week-61-new-v1/revision-qa/student-text.txt) is retained as evidence.
- [Rebuild checks](../../../../tmp/worksheet-runs/week-61-new-v1/revision-qa/rebuild-checks.json) compare `final/students.pdf` against independent clean copied-source and ZIP-extracted-source builds. Every page has exact extracted-text equality, identical Letter dimensions and identical rendered pixel bytes at 144 dpi. [Source manifest](../../../../tmp/worksheet-runs/week-61-new-v1/revision-qa/source-manifest.json) verifies the same seven source files byte for byte in both clean roots and lists the lean QA ZIP contents. No generated prompt, borrowed exemplar, third-party text, reference PDF, render cache or TeX intermediate is in `final/src` or that ZIP. The QA ZIP is a verification artifact; root handles release packaging after review.

Final PDF SHA-256: `aa7a3f3917ec83a07c877ad546029ab98e53ebf76a78e54341efd0f29efdeb96`.

Actual ball calibration, stable support, fixed-point string contact, retaining three sides, opposite-point placement, paper-corner/tangent comparison, meridian/lune handling, marking removal, physical rehearsal and classroom piloting are **unperformed**. Mathematical/digital checks establish neither physical readiness nor independent child control. These limits are preserved in the portable source notes. No remote copy is claimed current.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
