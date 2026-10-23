# Week 88 verification and limits

Prepared October 17, 2026. One shared Grades K–5 student packet (8 pages, 11 problems) and one separate adult guide (6 pages). Every final page was rendered and visually inspected. All material is **unpiloted; physical rehearsal is untested**.

## Review chain

Kernel-only outline generated the unchanged workflow stage set. Distinct fresh agents performed writer, adversarial critic, independent mathematics and reviser stages, followed by an independent student–guide review. The coordinator separately authored the theorem-first guide; this guide-authoring workflow is untested. The writer selected the tasks from mathematical kernels rather than copying the reserved problem list. Shared-packet output is the explicitly authorized alternative to mechanically producing three bands.

The critic requested a diameter convention and a scale label on late sketches; the reviser made both and brought radius labels closer to their segments. Independent mathematics found no required correction. Final pair review checks the current source/PDF pair and complete solutions. Repository records are in `plans/seven-families-85-91/production/week-88/`.

## Mathematical and digital checks

`python3 check_math.py` recomputes ring bounds 6/9/4, checks all pair distances of witnesses, excludes all 510 mixed nine-disk cyclic orders about the large center and all 62 mixed six-disk orders about the small center, and verifies both fixed mixed witnesses printed in the guide. It checks all 55 pairs of tray centers, boundaries and the exact row-constrained height. Numerical evidence supplements the written angle and row proofs, rather than claiming a global packing optimum.

The final eight student pages are pixel-identical to the revised student stage at 1.35×; only PDF metadata settings were added for deterministic publication. Actual tray interiors measure 160×112, 160×110 and 160×108 mm to within 0.002 mm of their nominal vector dimensions. Circles use equal x/y scaling. The six final guide pages were separately rendered and inspected, including both mathematical diagrams. No clipped text, collisions, accidental blank pages, missing glyphs or overfull TeX boxes remain.

The portable source ZIP was extracted into a fresh directory and rebuilt using only its contents and documented dependencies. Both rebuilt PDFs match the delivered PDFs byte-for-byte; packaged reference PDFs match too. `release-check.json` in the repository production record gives exact output hashes, archive membership and reconstruction results.

## Per-page visual coverage

| PDF/pages | Actual final inspection |
|---|---|
| Student 1–4 | Rules and diameter convention; actual-size center and practical tray; both reversed-size diagrams and mixed-size tasks; complete footers and available work areas. |
| Student 5 | Same tangent pair through input, split radii and output; close matching labels; proof/rigidity question and full-size center. |
| Student 6–7 | Both exact tray interiors and outside-only border ink; horizontal row restrictions and minimum-height continuation. |
| Student 8 | All four ring references, separately centered labels, sketch-scale caption and generalization. Enlarged page inspection independently confirms separated labels. |
| Guide 1–2 | Theorem-first assumptions, limits and band map; material counts, first route, launch and untested preparation gates. |
| Guide 3–4 | Complete construction keys; exact coordinate table; equilateral least-gap triangle and rigid-equality proof. |
| Guide 5–6 | Eleven-disk diagram, row-height argument, size formula and both mixed-ring bounds; sources, recordkeeping and limits. |

Actual printing, disk roundness, narrow physical fit, material handling, timings and children’s comprehension have not been tested. No school session or Drive upload is implied.

## Card fixes, October 23, 2026

Changed from the review card: student pages 2, 3, 5–8 (Problems 7, 10 and 11 reworded, Problem 11's 120 mm ring, Problem 4's caption, Problem 6's clearance, tray captions cut), all six guide pages, and a new 3-page materials PDF of disk sheets. Each changed page and every materials page was rendered at 80 dpi and inspected; student pages 1 and 4 are pixel-identical to the previous build. `review/check_pdf.py` measures every materials disk (40.000, 80.000 and 120.000 mm, round, centre dot, at least 3 mm apart, 15 mm inside the paper), the 100 mm bars, the unchanged tray interiors and Problem 6's 72 mm clearance, and reads the wording; `review/check_card_fixes_2026_10_23.py` checks the guide's tolerance figures (rings unchanged for disks 0–0.5 mm under size; trays need 39.63–40.00 mm), the 18.5° and 21° comparison, the 120 mm ring, the circumference estimate and the sliding chains. Cutting accuracy, disk fit and handling remain physically unrehearsed.
