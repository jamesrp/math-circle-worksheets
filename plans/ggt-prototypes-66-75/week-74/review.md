# Adversarial review: Week 74, Doubling elevators

## Verdict

**Pass with one recommended wording clarification and a material-size check.** This is a coherent four-page Grades 4–5 investigation. The graph model is stated honestly, vertical moves retain the same horizontal coordinate, left moves are permitted, the printed window is explicitly not a boundary, and the best-route questions progress to a genuine all-routes argument. No mathematical or rendering error was found. Retain the packet rather than redesigning it.

Read `AGENTS.md`, the full run prompt and scope addendum, the exact source and README, and the independent kernel review. Rendered the delivered PDF afresh and visually inspected **all four pages**. Ran the supplied exact route checker successfully and independently checked the upper-bound argument below. No source or student PDF was edited.

Reviewed PDF SHA-256: `e580529742cb928476c26ac35efd63a960e0d13b803f39650ff429bef642b0e2`.
Reviewed LaTeX SHA-256: `a4bcdadb599dfd12fc7e3d3c17056f256274651d359ec3b0786bf1f078558c16`.

## Findings in priority order

1. **Page 3, Problem 4: say “seven or fewer moves.”** The intended lower bound excludes every trip of length at most seven. “In seven moves” is conversationally understandable but can also mean exactly seven; excluding one exact length is not by itself a shortest-path proof. Problem 3 already uses an at-most budget, so “Can any trip reach 16 and return to level 0 in seven or fewer moves?” is a small, scope-preserving precision improvement. Keep the requirement to include left moves and repeated level changes.

2. **Board usability needs a small marker, not an unspecified broad pawn.** Adjacent coordinate dots are 0.23 inches, about **5.84 mm**, apart. Many ordinary board-game pawns cover two or three dots. High rows must retain every integer coordinate because U/D are legal at odd coordinates as well; deleting intermediate dots would be mathematically wrong. Before classroom use, choose a pointed/very small marker or a pencil tip and rehearse a trip through an odd coordinate at a high level. This is a material specification/physical-rehearsal issue, not a finding that the board is unusable. A later adult guide can specify the marker without adding student clutter.

3. **Rule checking is a real partner job.** The continuous row lines and evenly spaced dots do not mechanically prevent a child taking a one-dot horizontal step at level 3. The printed step labels plus the checking partner make the intended rule external and recoverable, a marked improvement over a memory-only puzzle. Rehearse an R from an odd coordinate at level 1 or 2 during the launch, so the checker uses the stride rather than hunting for specially numbered high-level stops. Do not replace the board with sparse high-level coordinates or let U change x. This is a launch note, not an additional worksheet sub-step.

4. **Keep the final left-move comparison as a later challenge.** The contrast is purposeful: left moves tie the best non-left solution at 15, while 23 genuinely needs fewer moves when left is allowed. A child who finds an attractive overshoot route to 15 has not yet answered the existential question. The printed choice among four destinations is good; preserve it. The eventual adult guide needs the exact comparison and should not label every overshoot as an improvement. No student hint identifying 23 is needed.

## Mathematical audit

The model has states (x,h), with x any integer and h a nonnegative integer. R/L change x by ±2^h, U/D change h by one, and every move costs one. The drawn dots correctly include every integer x at every drawn level. The source README properly calls this an exponential-shortcut toy graph, not the full Cayley graph of BS(1,2).

- **Problem 1:** 3 needs 3 moves (`RRR`); 7 needs 6 (`URRRDR`). The non-task convention example starts at coordinate 1 and reaches coordinate 3 with `URD`; its coordinate/level labels are correct and do not claim to be a route from the usual start 0.
- **Problem 2:** both `UURRRRDD` and `UUURRDDD` reach (16,0) in 8 moves. They are genuinely different maximum-height choices, not merely relabelings. The task asks for best candidates before demanding a universal explanation.
- **Problem 3:** for budgets 4, 5, 6, 7, 8 the largest attainable rightward coordinates are respectively **4, 6, 8, 12, 16**. Each is attained by going up to a suitable level, taking all available horizontal moves to the right there, then returning to ground.
- **Problem 4:** a route of at most N moves reaching maximum height H spends at least 2H moves vertically. At most N−2H horizontal moves remain; each has size at most 2^H. Consequently its net rightward displacement is at most (N−2H)2^H, even with left moves, intermediate-height moves, or extra excursions. For N=7 and H=0,1,2,3 the bounds are **7, 10, 12, 8**, all below 16. The proof is for the infinite stated graph, not merely this board.
- **Problem 5:** optimal lengths to 9, 15, 17, 23 are **7, 9, 9, 10**. Without left moves they are **7, 9, 9, 11**. Witnesses with left allowed are `UURRDDR`, `UUURRDDDL`, `UUURRDDDR`, and `UUURRRDDDL` respectively. The last trip overshoots to 24, which is included in the printed window.

For the 23 comparison, nine total moves permit displacement at least 23 only at maximum height 3. That allows at most three horizontal moves, but an odd endpoint requires at least one ground-level horizontal move. Thus the maximum possible displacement is at most 8+8+1=17, contradiction. Ten is attained. With no left moves, at maximum height H the minimum horizontal count is floor(23/2^H) plus the number of 1s in the binary remainder; adding 2H gives 23,14,11,11,12 for H=0 through 4. Heights above 4 cannot help a no-left route to 23. This confirms a strict 10-versus-11 distinction.

The supplied BFS limits move depth, not horizontal coordinates, and its return-to-ground pruning is legitimate. The universal lower bounds above are still necessary for the explanatory claims; finite search alone is not the printed proof.

## Page-by-page visual review

- **Page 1:** shared rules precede use and cover costs, starts, negative-level prohibition, horizontal stride, continuation off the page, and partner recording. The U/R/D example has input, intermediate states, output, and matching labels. All row levels and even coordinate labels are legible. The level-0 origin ring is clear. No overflow, overlap, or incorrect vertical alignment.
- **Page 2:** a full board remains available for the principal 16 investigation. The three generous record rows and “shortest trip so far” wording correctly support evolving conjectures. There is room to record a whole word and count afterward; no simultaneous redundant tally is demanded.
- **Page 3:** the five budget rows offer substantial work without prescribing a method. The proof question follows the experiment and has adequate writing space. Reuse of the previous loose board is reasonable for a single-sided packet; a second board need not be squeezed onto this page.
- **Page 4:** the full board accommodates all target coordinates and the useful overshoot to 24. Each destination has a separate route line, with additional space for the comparison. The amount of work supports flexible continuation rather than a forced one-hour completion target.

All four pages use the required header/footer and consecutively numbered problems. There are no Name/Date fields, decorative headings, answer leaks, or automatic explanation requests after every small action. The reading and arithmetic prerequisites are operationally plausible for the stated table: letter recording, signed horizontal position, doubling, and simple move budgets; the exhaustive upper bound is a readiness-dependent late step.

## Revision acceptance checks

Re-render and inspect all final pages after the wording change. Preserve a shared coordinate scale, all integer high-level positions, no implicit finite boundary, and explicit permission for left/repeated vertical moves. Verify the marker fits the coordinate spacing in a physical rehearsal. The prototype remains unpiloted and physical pawn/board operation remains untested until that happens.
