# Week 27 final independent mathematical audit

**PASS: no unresolved student mathematical defect.** This audit applies to actual `final/bonus.pdf` and `final/src/bonus.tex`, not the historical draft. Current AGENTS.md was reread. All 4 actual final pages were independently rerendered; PNG hashes exactly match the inspected final page images. Every page was checked in contact sheets, and changed conventions/examples were inspected at page resolution. Actual PDF problem/page mapping was checked separately and recorded in `final-page-evidence.json`.

Final PDF SHA256: `178b0b9c083e49054f27fe38fa7a1697a673dbb720def7f925dc725cf548030d`. Final source SHA256: `66f9088b3462bd938fdcd5b8d9c5b50a057cd532fcd202c2879155d5aaa624bf`.

- Page 1 worked visual: currentUP/VQ, actual input strips V:P,Q and P:V,U with boxed currentQ/U. Both strict comparisons hold against that SAME matching; VP is unpaired and blocks. The revised input ->two checks ->output bridge is correct.
- Page 1/P 1: all six perfect pairings have scores 15,13,11,10,11,12. Unique minimumAY/BZ/CX at 10 is blocked byBX; unique stableAY/BX/CZ has 11. All preference labels/ranks checked.
- Page 2/P 2: allowed partial matchings exhaustively enumerated. First profile uniquelyAX, unmatchedB/Y; second exactlyAX/BY andAY/BX, unmatchedC/Z. Omissions/mutual acceptance/unpaired conventions match the diagrams.
- Page 3/P 3: all three perfect roommate pairings checked for both profiles. Left no stable pairing, blockersBC/AB/AC respectively; right uniquelyAB/CD stable. Same-typeA-D diagrams impose one group correctly.
- Page 4/P 4: strict two-sided acceptable-partner-above-unpaired matched-set invariant holds by alternating-path argument;625 strict incomplete 2 x 2 and 2,0483 x 3 edge/rank supporting profiles checked. Counterexample requested is impossible under the final rules, as the task openly permits explaining.

The executable standard-library `independent-check.py` has been updated to read the ACTUAL final source and PDF, assert the changed conventions, and reproduce the independent exact results in `checks.json`. It imports no writer checker or mathematical answer data. The guide is audited separately; a guide audit does not substitute for student-page coverage.

No physical-fit, folding-motion, material-fairness, procedure-rehearsal or classroom-piloting claim follows from these checks. All physical procedures remain untested/unpiloted. No student, guide, base or global authoring files were edited by this audit.
