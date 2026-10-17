# Week 91 independent mathematical review

Reviewed the **actual** `draft/students.pdf` (6 pages), `draft/return-visit.pdf` (4 pages), and `draft/materials.pdf` (7 pages), all corresponding TeX and the builder. Freshly rendered and visually inspected all 17 pages. The generic three-band placeholder names do not apply. No draft was edited.

**Verdict:** no false printed calculation, target classification, worked example, tree theorem, or road theorem was found. Grades 2–3 student tasks, Grades 4–5 tree continuations, and the shared coin task check out completely mathematically. The road tasks also check out under their intended assumptions, with the small located convention issues below. The proposed target replacement `AEBFCGDH` is independently verified impossible and suitable.

## Located issues and smallest fixes

1. **Grades 4–5, return-visit p4, Problem 4: the four slots in each row labeled “Starting arrows”, “After one block”, “After two blocks” lack node labels.** The prompt permits either supplied road. The 0–4 road has only three cards; the 0–5 road has four. The first representation therefore has an unexplained extra slot, and the page does not define the mapping of row slots to numbered vertices. **Smallest fix:** label slots 1,2,3,4 and mark slot 4 as only for the 0–5 road, or supply numbered miniature roads. This is a recording ambiguity, not a false theorem.

2. **Grades 4–5, return-visit p4, Problem 5: “Always enter at the same place s.”** The intended theorem requires a fixed integer interior vertex on a finite path, with the endpoints absorbing. Shared rules imply a road vertex but do not explicitly restrict s to the interior. Endpoint sources give trivial immediate absorption; nonvertex sources are not defined. **Smallest fix:** “Always enter at the same inside circle, s.” Preserve m≥2 and 1≤s<m in later adult mathematical notes. The existing numerical conclusion is not wrong if endpoint sources are deliberately admitted; this clarification makes the intended assumptions explicit.

3. **Grades 4–5, return-visit p4, Problem 4: “Can the exit counts repeat in equal blocks while the complete arrow positions change?”** A valid example is m=4, s=1, initial LLR, block size 4: each block has exits 0,0,4,0, but states at boundaries are **LLR → RLL → RLL**. This establishes transient full states, not a different pattern after every block forever. The printed existential question is valid, but that stronger reading would be a different task. **Smallest fix in solutions:** explicitly distinguish the initial state change from later state return; do not claim perpetual change or infer an infinite rule from two blocks. No student rewrite is mathematically necessary.

## Requested replacement check

**Students p4, Problem 4:** replace `A C E G B D F H` with `A E B F C G D H` if adopting the critic's recommendation. The original is correctly impossible at the root. The replacement alternates at the root, but its left subtree receives A,B,C,D and its right subtree E,F,G,H, each violating alternation one level lower. Exhaustive enumeration of all 128 starting patterns independently rejects it. The other supplied eight-exit targets remain achievable from all-L and all-R respectively. This is a safe mathematical strengthening, not a repair of a wrong answer.

## Evidence and limits

- [Complete task-by-task solutions and general proofs](math-evidence/solutions.md) independently resolve every printed task and both procedure examples.
- [Standalone standard-library checker](math-evidence/independent_check.py), run with `python3 math-evidence/independent_check.py` from this run folder; no imports from the writer or earlier critic checker.
- [Computed results](math-evidence/check-results.txt): all tree states at depths 1–4; every road state/interior entry for m=2..10; 227,329 walks, 3,598,327 checked single-step invariants, and every sliding m-launch block in each 3m-launch run. Every assertion passed.
- [Actual PDF measurements](math-evidence/pdf-measurements.txt) confirm all specified board centers/diameters within 0.02mm, page sizes and the 50mm scale line. Fresh render PNGs and extracted page text are in `math-evidence/`.

The general proofs explicitly use follow-then-flip, a finite absorbing path 0..m, persistent cards, a fixed interior source s, and one counter at a time. They establish **every consecutive m launches has exactly s right exits from arbitrary initial arrows**, with no burn-in. Equal next-right-card counts at block boundaries do not imply equality of the entire pattern.

All material geometry and labels match the supplied specification. Tree-card corners extend 2.213mm outside centered 24mm junction circles; 20mm road-card corners extend 0.142mm outside 28mm circles. These are harmless placement-outline overhangs at the drawn separations, not evidence of fully contained cards. Physical cutting, folding, flipping, printing calibration, and handling with counters remain untested; this stage makes no classroom-piloting claim. No mathematical blocker remains.
