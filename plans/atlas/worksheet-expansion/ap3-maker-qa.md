# AP3 maker QA — ready for independent PDF review

Final maker preview: `tmp/pdfs/atlas-remaining/ap3-preview-v2/`.
Renderer: `lowell-math-circle-year-2/source/atlas-remaining/ap3.py`.

- Student PDF: 25 pages including contents, 24 staged body pages, 48 tracked prompts exactly once.
- Facilitator PDF: 44 pages including contents, complete solutions and hints for all 48 prompts, all eight keyed extensions, four worked visual pages.
- Student SHA-256: `c4c5792a5b414acbf08c9cf5514ab16ba18199bfb4026cbe501d95b868d86e22`.
- Guide SHA-256: `576feae6fd8229bb3600994482f4cb05f6ab2078178d16dacaac281768cc38b2`.
- Data SHA-256: `bee5eb0290c9b99c11a25963961ebce5d102e5c086b4e9e0c5ad37ace38d5422`.
- Checker SHA-256: `0b775d7f0e9e9df468a6e7db61bc068274657d7f656b07602c1d198b3a9d6f1c`; results SHA-256: `6a32f5e674c79294b304437a8852c5c6b3b02012735fcd1e1929836d01bbc932`.
- Builder reports zero bounds, blank-page, or glyph findings; exact `ap3-checks.py` passes all eight families after the notation changes.

## Actual inspection coverage

Viewed every student page 1–25 individually at full size, with attention to diagram topology, numbers, work space, launch staging and prerequisites. Viewed all five guide contact sheets covering pages 1–44. Viewed dense or worked guide pages 4, 6, 10, 11, 14, 15, 19, 20, 25, 26, 30, 31, 35, 37, 40, 41 and 43 at full size; inspected the corrected transition figure and full extension on page 21 at full size on the fresh v2 path. This covers every custom worked figure (6, 21, 37, 43).

V2 changes were independently compared to v1 page PNGs: only student pages 2 and 19 and guide pages 21, 31 and 43 changed. Viewed all five changed pages full size on their unique v2 paths; the other 64 page images are byte-identical to the inspected v1 images. No remaining maker finding.

## Repairs made during maker QA

- Removed the first-page AP19 slowness graph because its variables were introduced only on page 2. The complete-family task now has a full open proof region; no change to the task or key.
- Removed the AP27 trial-record heading that prematurely supplied the useful difference of powers. Learners now choose their own reconstruction evidence before deriving the timing certificate.
- Moved the AP24 worked self-loop and probability label away from the introductory paragraph. The figure encodes the correct 1/4, 1/2, 1/4 transitions with both endpoints marked absorbing.
- Replaced unsupported subscript k/n and superscript k with explicit plain-text index/exponent notation. Parenthesized composite indices in AP27 (`d_(k+1)`, `x_(n+1)`) to remove ambiguity; no mathematics changed.
- Clarified the AP30 worked-figure caption so the listed I values, rather than the resistor labels, are identified as currents.
- Updated the top-level data status to reflect closed independent design review. PDF approval remains a separate review.

## Mathematical and classroom scope

Diagrams were checked against the supplied models: hidden beds and tank levels disclose no inverse-solution data; payoff entries and independent sampling are explicit; population children all copy from the old generation; reactions show availability rather than hidden atomic decomposition; supplied codes are withheld until page 2; meters form parallel branches with filled junctions and a labeled ground reference.

The strongest candidates for an early classroom trial are AP20 (counter prices and integer gap), AP25 (invented conserved labels, then a legal-path certificate), and AP28 (adversarial code design and a counting obstruction). AP22 and AP24 support concrete launches but their complete conclusions need probability reasoning. AP19, AP27 and AP30 retain honest algebra/model gates; their error and design questions are meaningful for prepared learners, but would be unsatisfying if reduced to a decorative elementary activity. None has been classroom-piloted; suggested timing and sustained engagement remain untested.
