# Adversarial review: Week 66, Lamplighter streets

## Verdict

**Pass for revision-stage handoff, with small clarity refinements; no mathematical or rendering blocker found.** The single shared Grades 3–5 packet matches the authorized outline/addendum. Do not create missing K–1 or separate Grades 2–3 packets. Preserve the concrete partner rule and the final distance-from-the-original-start question.

## Scope and evidence

Read the actual repository `AGENTS.md`, `README.md`, this run's complete `PROMPT.md` and `CRITIC.md`, and the draft's LaTeX, README, and mathematical checker. Rendered `draft/students.pdf` at 120 dpi into `critic-render/page-1.png` through `page-4.png` and visually inspected **all four pages**. Checked extracted text against diagrams. PDF is four US Letter pages; SHA-256: `10800936604ae4ce9cfbe5d26b06b2958504a05c4dfc427aa8971ae2c8a70fe0`.

The writer's checker passes all 4,608 finite-street states. Independently checked the target distances by required flips plus a shortest walk visiting both extreme required positions and finishing at the pictured walker. The separate kernel audit agrees and uses an unbounded-state check; the later exact-instance audit also agrees and its recorded PDF/source fingerprints match this draft. No student source or PDF was edited. Physical counter/pawn rehearsal and classroom piloting were not performed.

## Mathematical and task audit

- **Page 1, Problem 1:** Targets are A: lamp 1 on, walker 1; B: lamps −1 and 1 on, walker 1; C: lamps 0 and 2 on, walker 0. Correct optima are **2, 5, 6**. They contrast reaching one lamp, visiting both sides, and returning to the start. The example accurately shows the non-task sequence R then F from −2 to −1; it preserves both lamp and walker state and does not reveal the main result.
- **Page 2, Problem 2:** All three targets have lamps −2, 0, 2 on, with final positions −2, 0, 2. Correct optima are **9, 11, 9**. This is a purposeful comparison, not three arbitrary copies: final walker position changes distance even when the lit set is unchanged.
- **Page 3, Problem 3:** The pictured target is exactly lamps −1, 0, 1 on, walker 0. At least three flips and four walking steps are needed; seven is achievable. Asking for a convincing lower bound is substantial and belongs here after concrete trials.
- **Page 4, Problem 4:** L and R keep the same lit set and change the final walker; F turns off lamp 0 and keeps the walker at 0. The three distances from all-off at 0 are **6, 6, 6**. The emphasized original starting state prevents the dangerous confusion between distance from the origin and distance to the previous target. Treat the three moves as independent moves from Problem 3, not a running L/R/F sequence.
- **Page 4, Problem 5:** The correct answer is no, using the seven-move state whose every neighbor has distance six. This is an actual counterexample to a universal claim and does not ask children to infer a universal theorem from a few measurements.
- The finite printed street does not invalidate any optimum: leaving the interval containing the start, required lamps, and final walker only adds unnecessary walking. An adult mathematical account may identify the unlimited street, but no additional abstract group language belongs on these pages.

## Clarity and format refinements

1. **Minor, page 3:** The second large street is plainly usable as the working mat, but it is unlabeled immediately after a fully drawn target. A small “Workspace” label would follow the repository's specific request to identify additional blank boards. This is a clarity refinement, not a new numbered problem or an instruction sequence.
2. **Minor, page 4:** “Make one move from the target in Problem 3” is mathematically adequate. A compact explicit “Reset to that target for L, R, and F” would reduce the risk of a child changing the three states sequentially. Keep the already explicit original all-off starting state for each distance calculation.
3. **Do not overcorrect the shared rules.** One recoverable move word plus a final count is appropriate. Do not add simultaneous flip/walk tallies or a mandatory checklist of intermediate observations.

## Visual, operational, and age-fit review

- All four pages have consistent week/topic/level headers, packet/footer identification, and consecutive Problem 1–5 labels. No names/dates, decorative sections, clipped text, overlapping labels, missing glyphs, or stray blank pages were found.
- Large street lamp circles are about 13 mm in diameter, with roughly 19 mm center spacing; they comfortably accommodate typical small two-sided counters. Small target streets are reference diagrams, not working mats. The walker sits separately above the line, which makes lamp and walker state distinguishable.
- Page 1 is the densest page, but all three move-word spaces and target labels remain usable. Pages 2–4 leave substantial writing space; page 3's lower half has room for the minimum-move argument.
- The designated Grades 3–5 gate is honest: children must order signed positions, keep one pawn plus lamp states, record short words, and compare move counts. They need no formal group notation. Page 3's lower-bound proof and page 4's counterexample are appropriately later.
- Partner roles materially enforce the unfamiliar flip restriction: one handles the walker while the other verifies the current position before flipping. This is a genuine response to the prior paper-lamp failure, though rehearsal is still needed to see whether a pawn and counter can coexist comfortably at a station.
- The ten target-distance investigations plus explanation/counterexample work are a plausible 35–40-minute route with adult discussion. This is an unpiloted timing judgment, not a claim that every group will take the full period. A quick group that sees the distance rule early may finish faster; an adult can later offer target invention without expanding this prototype mechanically.

## Revision priority

Keep the mathematics, examples, partner enforcement, and four-page structure. Apply the two small clarity refinements if useful, then re-render every page. No student redesign or extra age-band version is justified by this review.
