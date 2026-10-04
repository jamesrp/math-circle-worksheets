# Week 15 fresh critic review

Reviewed 2026-10-04. Verdict: **revise the continuous grid-distance convention before final delivery; retain the three investigations and their depth.** No incorrect target theorem or answer was found. This is a review of the actual four-page shared `draft/return-visit.pdf`, not the harness's obsolete three-band filenames.

## Scope and evidence

Read current `AGENTS.md`, `README.md`, this run's `PROMPT.md` and `CRITIC.md`, and the draft's LaTeX, mathematical-check script, and source README. Rendered all four actual PDF pages with `tmp/example-edit-env/bin/python` and PyMuPDF at 126 dpi and inspected every full page at readable resolution. Independently checked the PDF vector geometry and taxi examples. The reviewed PDF's SHA-256 is `26b14d8eb97096a19b360d1379b1bbbd47f0dafcac2a01bd3f59abe1d070a973`.

The delivered draft has exactly three investigations and four consecutively numbered problems: farthest straight-line ownership (page 1), taxi nearest-site geometry (page 2), and one clearance investigation with a changed site set (pages 3–4). The outline explicitly overrides the generic four-pages-per-band and three-file boilerplate; its scope is satisfied. I made no source, PDF, guide, base-packet, or global edits and did not rebuild or upload the packet.

## Required convention repair

**Page 2, shared rules and Problem 2: the whole-cell question needs a continuous taxi metric, but that convention is incomplete.** The rules say “One small grid edge is one step” and the task begins by labeling grid crossings. A child can reasonably understand this as whole steps between crossings or travel along the printed grid lines. The later question “Do ties fill whole small squares?” requires distances from points inside cells, horizontal/vertical travel starting at those points, and fractional lengths in the same step unit. None of those is explicit. Labels on a square's four corners alone do not settle its interior.

Make the permitted interior points and fractional step units explicit in the shared rule, without giving the tie regions or an investigation method. The convention should say that horizontal/vertical travel can begin anywhere, including inside a square, and that part of an edge counts as that fraction of a step. Before its first use, adapt the compact non-task convention visual to include a fractional edge (for example a half-edge), with the input, routed intermediate drawing, and resulting distance consistently labeled. Preserve an accessible whole-crossing entry. Do not replace the full-square question with a lattice-only exercise: the area of the tie set is substantive mathematics in this kernel.

The current P-to-Q visual **does correctly demonstrate the whole-step metric** before Problem 2: the endpoints are three edges apart horizontally and one vertically, the intermediate route shows the horizontal and vertical lengths, and the output is `3 + 1 = 4 steps`. The arrows have a clear conversion role. It simply does not yet cover the continuous convention used by the interior question.

## Page-by-page findings

| Actual page | Findings and readiness |
|---|---|
| 1 / Problem 1 / K–1 and up | The string comparison, five named dots, and open choice of test places give a concrete entry after adult reading and a normal demonstration. The two-sentence problem retains children's choices and poses the empty-region question without printing its answer. “A tie gets all tied letters” correctly permits two corner owners on an axis and four at the center. “The map continues beyond the frame” correctly states the whole-plane domain. The full map leaves ample room to mark test places and owners. A small practical refinement would be to ask children to **mark and label** places, so a letter remains attached to a recoverable test point rather than floating ambiguously on the map. This is not a new mathematical procedure or a reason to require a second printed example. |
| 2 / Problem 2 / 2–3 and up | The large crossing grid supports immediate counting and A/B/AB labeling; all chosen records remain on the grid. Ties and the midpoint question develop the same distance investigation rather than adding a disconnected fourth investigation. The continuous-distance repair above is required. “Midpoint” and the whole-cell claim are readiness-dependent reasoning beyond the concrete counting entry; adult vocabulary help is ordinary support, and should not turn into adults choosing the child's two endpoints. The grid continues beyond its frame explicitly. |
| 3 / Problem 3 / 4–5 | A chosen point and comparisons with four fixed corner dots give a usable physical entry to the max–min objective. “Inside or on the square” defines the bounded candidate domain correctly, including edges. The nearest-tie rule produces one well-defined distance. The demand to find every best place and explain optimality is the substance of this problem; retain it. The record table and large board can preserve trials without simultaneous five-distance bookkeeping. Replace “distances go straight across” with the already established **straight-line distances** for precise consistency; the existing phrase could be heard as horizontal travel. |
| 4 / Problem 4 / 4–5 | The fifth dot is exactly centered, and the separate fresh board makes the changed reference state recoverable. New trial points are not described as additional permanent black sites. This is a natural continuation of Problem 3. There are four best places but only three table rows. The board can already hold all four, so this is not a mathematical blocker; a more flexible record area or an additional row would avoid an accidental three-place expectation while preserving child-owned recording. Keep the proof/complete-optimum demand as deeper work after concrete trials. |

The upper-band record tables do not prescribe a distance unit. That is acceptable for this scale-invariant comparison: children can use one consistent ruler unit or compare marked string lengths. There is no need to add coordinates, square roots, or a numerical target to student pages. Exact symmetry arguments and geometric bounds remain distinct from approximate measurements.

## Independent mathematical checks

The actual PDF has US Letter pages. Each main frame is exactly 324 by 324 PDF points, or **4.5 by 4.5 inches**, with equal horizontal and vertical scaling. Extracted site centers agree with the intended coordinates on every page: page 1 has the four `(±2,±2)` corners plus `(0,0)` inside a frame `[-3,3]²`; page 2 has A=`(0,0)`, B=`(2,2)` on `[-2,6]²`; pages 3 and 4 use the bounded square `[-2,2]²`, with the center added only on page 4. Square side counts, corner locations, and all grade-band variants in this shared draft were inspected.

- **Farthest:** Each corner owns its opposite closed quadrant, with ties on its boundaries. E has no farthest point anywhere in the plane. For any `(x,y)`, the average squared distance to the four corners is `x²+y²+8`, strictly greater than the squared distance to E. Thus at least one corner is farther than E. Measurements suggest this; the inequality establishes it globally.
- **Taxi:** For continuous taxi distance, the complete tie set is the two closed quadrants `x≥2,y≤0` and `x≤0,y≥2`, together with the segment `x+y=2` inside `[0,2]²`. This follows from the three pieces of `|t|−|t−2|`: `−2`, `2t−2`, and `2`. Fractional rational checks agreed with that set. Tied places `(4,0)` and `(0,4)` both have distance 4 to A and B; their midpoint `(2,2)` is B, so its two distances are 4 and 0. All three points are available on the printed board. No need to print this witness for children.
- **Clearance with corners:** Write `u=|x|`, `v=|y|`, with `0≤u,v≤2`. The nearest corner's squared distance is `(2−u)²+(2−v)²≤8`, with equality only at the center. This proves the unique optimum and separates proof from a numerical search.
- **Clearance with center:** If `u+v≤2`, distance squared to E is `u²+v²≤(u+v)²≤4`. If `u+v>2`, squared distance to the quadrant corner is at most `(4−u−v)²<4`. Equality at 4 occurs precisely at the four edge midpoints, and direct comparison shows each has nearest distance 2. These are all best places.

**There is no circle-fitting assumption in the student draft.** Only the new point must remain in the square. A clearance circle need not lie inside it; imposing that additional condition would change Problem 4 and invalidate its intended edge-midpoint answer. Preserve the current point-only domain.

## Layout and classroom limits

All four rendered pages have legible headers, footers, problem numbers, site letters, diagrams, and record areas. I found no clipping, overlaps, broken symbols, or unequal scaling. There are no Name/Date fields, extra page titles, generic encouragement, or printed solutions. The shared rules appear once per investigation; page 4 correctly inherits page 3's rules. The worked metric visual is a needed convention example, not a spoiler.

Operational prerequisites are appropriate as entry guides: page 1 needs spoken instructions, identifying letters with adult help, and length comparison; page 2 adds small-integer counting/addition and the repaired fractional-length convention, with midpoint/continuous-region reasoning later; pages 3–4 add the ability to compare several lengths, retain the nearest one, and reason about all candidate places. Adults can read or record while children choose and check points. A parent measuring every point and choosing every comparison would be a different, less independent activity, but the draft does not require that.

String handling, holding the comparison origin fixed, marking dot centers precisely, and pacing the abstract questions remain **unpiloted concerns and rehearsal questions**, not observed classroom failures or automatic grounds for redesign. Twelve-inch string readily spans the printed 4.5-inch frames, but finite measurements do not prove the whole-plane claim. Exact ties should ultimately be settled by symmetry or an explanation, not measurement tolerance. This review does not establish physical readiness or that a single investigation will occupy every child for the whole session. Retain the depth and flexible pacing; do not inflate this explicitly scoped return visit with routine tasks or force every child through the global arguments.

## Revision priorities

1. Repair page 2's continuous/fractional taxi convention and demonstrate it visually before the whole-cell question.
2. Use “straight-line distances” for Problems 3–4 to match the stated metric exactly.
3. Consider the small recoverability refinements on pages 1 and 4; retain the mathematical questions, open choice of trials, and exactly three investigations.

Only the critic stage is complete. Final revised PDFs, rebuild verification, facilitator-guide integration, and classroom rehearsal remain outside this review stage.
