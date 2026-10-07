# Week 74 revision record

Status: independently reviewed prototype awaiting organizer review, unpiloted. One shared Grades 4–5 student packet, four US Letter pages. This is the fresh reviser stage using the completed independent critic and mathematical reviews.

## Review decisions

- Addressed critic 1: Problem 4 explicitly asks about **seven or fewer moves**, so the lower-bound task excludes every shorter trip and not merely one exact length.
- Addressed critics 2–3 in the source README and separate-guide handoff: coordinate spacing is 0.23 inches (5.84 mm), so a pointed/very small marker or pencil tip is needed; an odd-coordinate high-level move must be rehearsed. Preserved the full integer-coordinate grid and same-x vertical alignment.
- Retained all route choices, left moves, repeated level changes, unlimited continuation beyond the printed window, budget investigations, and the final comparison among 9,15,17,23. Critic 4's later-challenge pacing concern and strict-versus-tied overshoot distinction are documented; no answer was added to the student pages.
- No review finding was rejected. Material and rule-checking concerns remain explicitly untested, and do not justify replacing the sound graph model.
- Normalized the source README status and all page footers to GGT74-S-v1. Kept the portable --out PATH builder unchanged and free of absolute dependencies.
- Strengthened the local checker to assert all printed shortest-route distances, route endpoints, every printed budget maximum with an attaining route, and the no-left 23 coin counts.

## Verification

Local exact searches give target costs 3→3, 7→6, 9→7, 15→9, 16→8, 17→9, 23→10. The corresponding no-left costs agree except 23→11. Budget maxima for 4–8 are 4,6,8,12,16. Independently reran check74() and elevator_checks(); the independent kernel search checks 4,785 states through depth 12 without coordinate clipping. The universal height-budget proof and the odd-target 23 lower bound were reviewed against the final unchanged mathematical model. Search is supporting evidence, not a replacement for the all-routes proof.

Built final/students.pdf with the repaired cloud TeX environment. Rendered and visually inspected every final page at 110 dpi: all rows retain every integer dot, vertical coordinates align, the 24 overshoot remains available, convention labels and all step sizes are correct, and the at-most wording fits. Headers, footers, tables, answer spaces and diagrams show no clipping, collision or overflow. Isolated a copy of final/src, rebuilt from an unrelated directory with --out PATH, and verified identical extracted text and all four page rasters. Logs and independent results are in final/qa.

## Required handoff to the separate adult author

- Use a marker fine enough for 5.84 mm dot spacing. Rehearse an R/L step from an odd coordinate on level 1 or 2; the partner checks the printed stride, and U/D must keep the same x. No physical marker-fit or partner-operation rehearsal has occurred.
- The graph is the stated nonnegative-height exponential-shortcut toy graph, not the full BS(1,2) Cayley graph. The drawn window is never a legal movement boundary.
- The all-routes proof spends at least 2H moves vertically, leaving at most N−2H moves of absolute horizontal size at most 2^H. This remains valid for leftward steps, intermediate-height motion and repeated excursions.
- A route via 16 then left to 15 merely ties the no-left optimum. At 23, the ten-move route via 24 truly beats the no-left optimum of eleven. Give both lower bounds in the separate guide, preserving this as a later challenge.
- Pacing and classroom suitability remain unpiloted hypotheses; retain the substantive later mathematics for readiness-dependent continuation.

No guide, publication, source ZIP or release copy was produced in this stage.
