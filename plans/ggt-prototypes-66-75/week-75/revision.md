# Week 75 revision record

Status: independently reviewed prototype awaiting organizer review, unpiloted. One shared Grades 4–5 student packet, four US Letter pages. This is the fresh reviser stage using the completed independent critic and mathematical reviews.

## Review decisions

- Addressed critic 1: the shared rules explicitly require yarn to remain strictly between the rims except at the fixed endpoints A and B. This supplies the proper-arc condition without technical student jargon.
- Addressed critic 2: Problem 7 now asks whether a common twist changes the minimum and what can happen when only one route is twisted. It no longer suggests that every one-route twist must change the minimum. The equal-winding exception remains a genuine investigation.
- Addressed critics 3–4 through the source README and separate-guide handoff: the exact tape/yarn/cylinder mechanics need rehearsal, and physical overlaps represent projected surface crossings. Three-dimensional lifting cannot establish a lower crossing count for surface arcs.
- Addressed critic 5 by recording a viable first-visit stopping point after pages 1–2 and preserving later readiness-dependent work. The mathematically sound cylinder, repeated strips, twist rule and minimum-intersection tasks were not redesigned for untested pace concerns.
- Preserved child-controlled route choices, identical fixed endpoints, signed seam counting, no shared subarcs or non-crossing touches, the non-task worked visuals, and the distinction between relaying, surface slides and the whole-surface map.
- No review finding was rejected. Physical limits remain explicit rather than being presented as verified readiness.
- Normalized the source README status and all page footers to GGT75-S-v1. Kept the portable --out PATH builder unchanged and free of absolute dependencies.
- Strengthened the checker with exact assertions for every printed minimum, common-twist invariance, one-route increase/decrease/tie examples, the 20 balanced six-twist words, and shortest-word witnesses.

## Verification

Local exact checks pass: Problem 6 minima are 0,1,2,1,2,1; Problem 7 gives 4 for (2,7) and 0 for (5,5). Shared-twist invariance and the (5,5)→(6,5) zero-to-zero exception are checked. Independently reran check75() and cylinder_checks(), including 289 winding pairs, rational twist composition and endpoint-fixation checks, every printed intersection instance, and the six-twist count. Reviewed the fixed-endpoint lifted-route arguments and assumptions against the final tasks. Finite checks do not replace the universal lower-bound proof.

Built final/students.pdf with the repaired cloud TeX environment. Rendered every page at 110 dpi and visually inspected each: the added shared rule fits, the template remains 6 by 2.4 inches, A/B and quarter-height marks align, seam example entry/exit heights match, repeated-copy labels and the full-twist diagram are correct, and tables/answer areas are legible. No clipping, collision or overflow; all headers and GGT75-S-v1 footers are correct. Copied only final/src to an isolated directory, rebuilt from an unrelated current directory with --out PATH, and verified identical extracted text and all four page rasters. Logs and independent results are in final/qa.

## Required handoff to the separate adult author

- Rehearse removable tape with yarn feeding at the same geometric rim mark. Tight tape may prevent feeding; loose tape may let an endpoint slide; a 6-inch-circumference paper sleeve may buckle. Verify that a child can alter a same-winding route with both endpoints fixed and the yarn on the surface. If it fails, change the fastening detail or use a drawn route as the mathematical record. Do not allow rim rotation or endpoint motion as a shortcut.
- Explain visible yarn overlaps as projected surface intersections; this is not knot over/under data. Lifting into space is allowed to construct a new route, but it does not constitute a legal fixed-endpoint surface deformation or prove surface arcs disjoint.
- Keep relaying a strand, continuously sliding a strand, and applying the whole-surface twist distinct. The rigid cylinder does not literally perform a Dehn twist.
- The formula max(|a−b|−1,0) is a minimum for identical fixed endpoints, excluding both shared endpoints. Equal winding needs distinct nearby routes, not two overlapping copies. A common twist preserves the minimum; a one-route twist may increase, decrease or preserve it.
- Pages 1–2 may be a full substantive first visit. Keep the later mathematics available, with a mathematician supporting readiness-dependent invariance and lower-bound explanations. Physical rehearsal and classroom piloting remain outstanding.

No guide, publication, source ZIP or release copy was produced in this stage.
