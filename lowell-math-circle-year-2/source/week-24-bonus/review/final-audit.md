# Week 24 final independent mathematical audit

**PASS: no unresolved student mathematical defect.** This audit applies to actual `final/bonus.pdf` and `final/src/bonus.tex`, not the historical draft. Current AGENTS.md was reread. All 4 actual final pages were independently rerendered; PNG hashes exactly match the inspected final page images. Every page was checked in contact sheets, and changed conventions/examples were inspected at page resolution. Actual PDF problem/page mapping was checked separately and recorded in `final-page-evidence.json`.

Final PDF SHA256: `7916b4011a795e9987d77b0121eaa91029c4715953ad7f2bc57ed0dbfccb0944`. Final source SHA256: `46eeafcfa906b2bc54c8b66de6ea293bc54b74fb3325dcf977b626878210500d`.

- Page 1/P 1: all 27 triples, no ties; champions A 10/B 10/C 7, per-card counts A 0,1,9;B 0,4,6;C 1,2,4. Every printed card value checked.
- Page 2/P 2: nine ordered draws per deck and exact sum multiplicities verified; repeated deck diagrams and recording tables checked.
- Page 3/P 3: all 81 four-card outcomes per pairing; A/B wins 37/44,ties 0;B/C 39/38,ties 4;C/A 39/38,ties 4. Point means 74/81 vs 88/81,82/81 vs 80/81,82/81 vs 80/81.
- Page 4/P 4-5: the nonempty label-bag rule resolves the edge case, permitting zero copies of an individual label. The new equally-likely-slip/card definition correctly weights repeated labels. New worked chain B -> (1,6,8) ->6 ->2 points versus A ->(2,4,9) ->4 ->0 points is legal and correct. Pure payoff rows are (1,10/9,8/9),(8/9,1,10/9),(10/9,8/9,1); each sums to 3. Equal mixing uniquely has all three means at least 1; no bag exceeds 1 against all. This is expectation, not a finite-play guarantee.

The executable standard-library `independent-check.py` has been updated to read the ACTUAL final source and PDF, assert the changed conventions, and reproduce the independent exact results in `checks.json`. It imports no writer checker or mathematical answer data. The guide is audited separately; a guide audit does not substitute for student-page coverage.

No physical-fit, folding-motion, material-fairness, procedure-rehearsal or classroom-piloting claim follows from these checks. All physical procedures remain untested/unpiloted. No student, guide, base or global authoring files were edited by this audit.
