# Independent coordinator review: accepted F52-FAC-v2

Reviewed all solutions and the mathematical overview against current F52-S-v2,
then rendered and visually inspected every page of the ten-page final guide.
Current guide render: `tmp/new-themes-52-63/final-inspection/week-52-guide-v2/`.
No clipping, crowded labels, distorted grid cells or inaccessible print was found.

The review found and required a substantive correction to Problem 3: the unchanged
student task allows overlapping bars/coincident corners after a collapse. A fixed
square-length diagonal can refit a square or a doubled right-isosceles triangle.
The corrected guide credits this exception and limits square-only reasoning to
the ordinary simple nondegenerate rhombus branch. It distinguishes continuous
local rigidity at the initial square placement from disconnected distant refits.
No new restriction was inserted into the child's open investigation.

`guide-review-independent.py` uses union-find, independently of authored checks,
to enumerate all brace subsets through 4-by-4, verify minimum counts, all twelve
2-by-3 minimum sets, all successful/failing paired removals, one-addition repairs,
all 78 covered six-brace 3-by-3 sets and the sharp disconnected capacity of ten
for a covered 4-by-4 grid. It also derives the four labelled P3 refits directly
from circle equations and verifies both branches of a continuous unbraced path
through a collinear collapse. The independent record is in
`guide-review-assets/independent-guide-checks.json`.

The overview states complete planar square-grid assumptions, the infinitesimal
theorem, the separate finite-motion construction, invariants and their limits,
and actual destinations by readiness. Row/column links have a concrete physical
handoff before general paper proofs. Solutions, optional hints, return routes,
full kit counts and hole-center dimensions agree with the student tasks.
Source descriptions accurately distinguish the Bolker–Crapo abstract from the
full paper that was not obtained; local adaptation and timing estimates are
identified as untested. Physical fabrication, fit, staffing rehearsal and
classroom piloting remain unperformed and are explicit pretests.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
