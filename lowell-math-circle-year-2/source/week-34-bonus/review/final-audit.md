# Week 34 final independent mathematical audit

**Pass.** Audited actual `final/bonus.pdf` (four pages), every rendered page, and actual `final/src/bonus.tex`. All six tasks, both occurrences of the starting pattern, motion cards, and ordered-layer example remain mathematically valid. No correction remains.

The final shared rules simplify identity wording to “Do not count a whole turn.” The adult rotation-count theorem still includes identity explicitly. The layer rules now state that only each spot's mark counts and a square's orientation is ignored; this correctly excludes icon-direction data from the ordered-pair model. The P5 large working ring and three recording rings are repositioned, without changing scale or spot geometry. P6 now supplies three additional regular six-spot record rings. Each new small ring has six equally spaced spots and no overlap; large spots remain 28 mm.

Fresh independent calculations give the same verified facts: six-ring reflection counts 0,1,2,3,6; half-turn repair minimum 2 with four best patterns; selected vertical-flip minimum 3 with eight, one-spot turn minimum 4 with two, two-spot turn minimum 4 with four; all 4,096 ordered six-layer pairs obey the intersection rule. Unique marks at adjacent vertices satisfy P5, and all pairs of half-turn-symmetric layers retain the half-turn in P6.

`independent-check.py` now uses only final source/PDF paths, recomputes motion/repair/layer enumerations and all final ring sizes, checks actual PDF task numbers and mark-only convention, and binds the inspected source by hash. No draft is required. Final source SHA-256: `0dff27ad474e9d3f47d33468f247a378f2b8155482d21f5cb3889c0dbff3b3dc`. Final PDF SHA-256: `92929372ee875bdea99e4fd6e1e9aa3752e4deb2f61e2ba2b4bb3d413e292c25`.

Actual tracing-sheet readability, overlay alignment, counter fit and classroom rehearsal remain untested. This is mathematical verification, not physical-readiness or pilot evidence.
