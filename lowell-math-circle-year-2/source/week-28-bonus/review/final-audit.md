# Week 28 final independent mathematical audit

**PASS: no unresolved student mathematical defect.** This audit applies to actual `final/bonus.pdf` and `final/src/bonus.tex`, not the historical draft. Current AGENTS.md was reread. All 5 actual final pages were independently rerendered; PNG hashes exactly match the inspected final page images. Every page was checked in contact sheets, and changed conventions/examples were inspected at page resolution. Actual PDF problem/page mapping was checked separately and recorded in `final-page-evidence.json`.

Final PDF SHA256: `6d9d51500247c201ea5e310c6aead5768bc5f94cf86a6aab8d262c20d3e1e046`. Final source SHA256: `a037d4223a04603877a8e6331622904538c00effbf4b08a2bc0c6ff7cc8a8bfc`.

- Page 1/P 1: tracing now preserves the exact points rather than inviting altered copying. Four cases remain yes(x=3),no(bisectors 3 vs 2.5),yes(Tonx=3),no(T(2,5)moves to(4,5)); all labels/coordinates checked. Stationary-half fixed points are distinguished from fixed points of a whole-plane reflection.
- Page 2/P 2: explicit B-original-front-up rule resolves the recorded orientation ambiguity. All six orders remain valid in the ideal model. Front/front givesACB/CAB,back/backBAC/BCA,front/backABC,back/frontCBA. Two-panelXunderY ->YX example is correct.
- Page 3/P 3: independently enumerated 16 noncrossing and 8 interleaving orders, withAB/CDsameend andBCotherend. Every valid/excluded word is in checks.json. The final page explicitly claims only static thin-paper noncrossing, supplying no real folding motion.
- Page 4 new convention visual: a 4 x 4 sheet folded atx=2 has two layers; punch offset 1.2 from the fold,y=1.1 unfolds to original local(.8,1.1),(3.2,1.1), or displayed(12.8,1.1),(15.2,1.1) aboutx=14. Both holes are off-fold/off-edge. This is an exact two-image example, not the target four/eight result.
- Page 4/P 4 and page 5/P 5: all six enlarged 4.68 cm square patterns preserve equal x/y scale and exact centers. Both task sets have possible,possible,impossible answers. Four-image punches(1.7,.9),(1.2,1.2); eight-image(1.7,.9),(1.8,.7). Four-imagepattern 3 lacks a vertical partner; eight-imagepattern 3 lacks diagonal(.8,1.7). Off-every-fold convention excludes smaller orbits.

The executable standard-library `independent-check.py` has been updated to read the ACTUAL final source and PDF, assert the changed conventions, and reproduce the independent exact results in `checks.json`. It imports no writer checker or mathematical answer data. The guide is audited separately; a guide audit does not substitute for student-page coverage.

No physical-fit, folding-motion, material-fairness, procedure-rehearsal or classroom-piloting claim follows from these checks. All physical procedures remain untested/unpiloted. No student, guide, base or global authoring files were edited by this audit.
