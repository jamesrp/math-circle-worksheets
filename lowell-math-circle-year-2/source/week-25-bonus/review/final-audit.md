# Week 25 final independent mathematical audit

**PASS: no unresolved student mathematical defect.** This audit applies to actual `final/bonus.pdf` and `final/src/bonus.tex`, not the historical draft. Current AGENTS.md was reread. All 4 actual final pages were independently rerendered; PNG hashes exactly match the inspected final page images. Every page was checked in contact sheets, and changed conventions/examples were inspected at page resolution. Actual PDF problem/page mapping was checked separately and recorded in `final-page-evidence.json`.

Final PDF SHA256: `516009fdd420d0c9d957e392b998be131d7de71e8e916fc954a277e6a666b0b5`. Final source SHA256: `3e320d7757bff29fba67c0818b84f4fabdef9ec5c2fa09d33d835cdd3abb8f37`.

- Page 1/P 1: the new d 1-d 5 guides on both actual 22 mm working grids have exactly the intended complete NW-SE memberships. The unchanged non-task picture A 1,A 2,B 3,C 1 gives 1,0,1,2,0. Among six legal permutation pictures, precisely 100/001/010 and 010/100/001 share 0,1,1,1,0.
- Page 2/P 2: moved free-naming/paid-cell convention preserves the exact adaptive optimum 3. All six pictured candidates checked; the two-question information lower bound is 4 histories<6, and a 3-query decision tree exists.
- Page 3/P 3: fixed-query optimum 4, with A 1,A 2,B 1,B 2 a separating set; every 0-,1-,2-,3-cell query set was checked and fails.
- Page 4/P 4: all 512 binary boards checked. In printed order, realization counts 0,3,1,0; legal local counts/equal totals alone are insufficient. Possible examples 111/110/001 and 110/110/110 meet their margins; both impossible boards violate two-row capacity.

The executable standard-library `independent-check.py` has been updated to read the ACTUAL final source and PDF, assert the changed conventions, and reproduce the independent exact results in `checks.json`. It imports no writer checker or mathematical answer data. The guide is audited separately; a guide audit does not substitute for student-page coverage.

No physical-fit, folding-motion, material-fairness, procedure-rehearsal or classroom-piloting claim follows from these checks. All physical procedures remain untested/unpiloted. No student, guide, base or global authoring files were edited by this audit.
