# Week 26 final independent mathematical audit

**PASS: no unresolved student mathematical defect.** This audit applies to actual `final/bonus.pdf` and `final/src/bonus.tex`, not the historical draft. Current AGENTS.md was reread. All 4 actual final pages were independently rerendered; PNG hashes exactly match the inspected final page images. Every page was checked in contact sheets, and changed conventions/examples were inspected at page resolution. Actual PDF problem/page mapping was checked separately and recorded in `final-page-evidence.json`.

Final PDF SHA256: `c562a4ddcc83a67ea357abae34e748ed7171b0eff97dc22eccc0fac3071f9020`. Final source SHA256: `f76bef35828d19b60da691444644556244c2d1cc7e9566578c9726ed7ff5dcb5`.

- Page 1/P 1-2: all 12,870 balanced colorings and all 65,536 divisions checked. Minimum interface 4, exactly four labeled straight-middle optima; room perimeters 12/12. IdentityP_R+P_B=16+2 L holds beyond balance/connectivity.
- Page 2/P 3: the revised shared rule now expressly forbids a LOCAL two-diagonal occupancy even when tiles connect elsewhere; this resolves any global-connectivity reading. Actual shapes have(C,R,H)=(4,0,0),(5,1,0),(4,4,1),(4,8,2), all nonpinched and side-connected. C-R=4(1-H) follows from loop turning. The one-/three-occupied-square corner visuals match their labels.
- Page 3/P 4-5: the new shared cube rule explicitly counts bottoms before all cube tasks, replacing duplicate task instructions without changing scope. Worked 2 square x 2 layer diagram has 4 cubes. Printed 8 cube buildings have 34,28,24 faces. Equal positive-height surfaceS=2 m+kP includes all hole boundaries;1,533 independent footprint/height voxel tests agree.
- Page 4/P 6: all 24 arrangements of heights 1,2,3,4 checked;16 give 34 faces,8 give 36. Extrema and the 6 recording 2 x 2 boards are correct; shared bottom rule applies here.

The executable standard-library `independent-check.py` has been updated to read the ACTUAL final source and PDF, assert the changed conventions, and reproduce the independent exact results in `checks.json`. It imports no writer checker or mathematical answer data. The guide is audited separately; a guide audit does not substitute for student-page coverage.

No physical-fit, folding-motion, material-fairness, procedure-rehearsal or classroom-piloting claim follows from these checks. All physical procedures remain untested/unpiloted. No student, guide, base or global authoring files were edited by this audit.
