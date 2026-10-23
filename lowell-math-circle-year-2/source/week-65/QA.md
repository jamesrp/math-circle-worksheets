# Week 65 verification

Prepared 2026-10-05. Current IDs: W65-S-v4 and W65-FAC-v4 (October 23, 2026 critic follow-up after the card fixes). Seven student pages, seven adult-guide pages. Prepared for review; physical rehearsal and classroom piloting remain unperformed.

**October 23, 2026, critic follow-up (v4).** Problem 6's octagon map, the guide's "encloses only those n rooms" and its other three notes are checked by `student/build.py` (the map's 17 rooms, each neighbour's 1 + 2 + 5 doors, 40 distinct off-map rooms) and by `plans/review/checks/week-65/check_critic_fixes.py` in the repository (an independent tiling: 48 rooms, the turning rule on 1, 2 and 3 rooms and 72 for the ring of 16 around Home, page 7's 112 walls, unchanged pages 1–6 apart from footers, the guide's wording). Every page of both PDFs was rendered and inspected; both keep seven pages, and a clean rebuild from the extracted ZIP matches every page's text and 100-dpi pixels.

**October 23, 2026.** The v3 changes are checked by `review/verify_card_fixes_2026_10_23.py` (turning rule 4 + 4n on every simple cluster of up to four rooms, shortest full return 8 with no odd return, Problem 6 counts 48 and 8, R label distances, wording and footers) and recorded in `review/card-fixes-2026-10-23.md`. All seven pages of each PDF were rendered and inspected; page 1 of the packet differs from v2 only in its footer, and a clean rebuild from the extracted ZIP matches every page's text and 100-dpi pixels. The notes below describe the v2 release of October 5–6.

## Checked mathematics

- Genuine {8,4} circle-arc geometry: eight equal hyperbolic sides, eight right angles, and four rooms at a junction. An independent Lorentzian reconstruction corroborates the reflection builder across all 57 radius-two tiles.
- One-room repeated local left/right turns: after four moves the robot is at E; its first full-state return is eight moves.
- Two-room outside boundary: fourteen edge moves, twelve left quarter-turns, two straight junctions. Two ordinary squares: six edge moves, four quarter-turns, two straight junctions. The shared wall midpoint has no movement dot.
- The two selected complete streets through P are disjoint from the entire supporting circle of R. The guide includes a whole-line separation proof, not a finite-picture inference.
- Four-room routes: exactly two two-door routes and eight four-door routes. The guide supplies the complete list and a completeness argument. Optional whole-tiling layers are 1,8,48; no unproved general growth formula is asserted.
- Diameter geodesics are handled separately from finite orthogonal circles, in both code and the corrected adult explanation.

## Final document checks

Every final student page was rendered and inspected at 130 dpi; every adult page at 110 dpi. Later changes were rerendered and inspected, with unchanged page rasters verified. No clipping, overlap, missing glyphs or unusable diagram labels was found. All 13 pages are US Letter, have consistent headers/footers, and contain text within the page bounds. Fonts are embedded.

The student pages include explicit move/arrival/turn visuals before curved-road use, a counter-sized two-room board, whole-line scope, and a separate record sheet that can remain beside the coin board. Independent inspection checked side counts, local turn directions, full-road endpoints, absence of a false midpoint junction, and the four-room adjacency.

The two-room board has equal x/y scale of 3.6 inches per disk unit, a 6.26990 by 3.51844-inch room footprint, and minimum distinct junction separation 17.85020 mm. For two 10 mm counter footprints this leaves 7.85020 mm. Central-octagon label centers are 11.61639 mm from their dots; the nearest glyph clearance is 8.83603 mm. These are digital spacing checks; print and try the actual slim 10 mm arrow before the session.

## Portable reconstruction

The actual source ZIP was extracted into a fresh directory, and its root build.py rebuilt both PDFs using only packaged authored inputs, standard Python and TeX dependencies. Text, dimensions and rendered pixels match all 13 delivered pages exactly in the production environment. PDF metadata timestamps need not match; different TeX/font versions may change rendering.

The ZIP contains current editable builders and TeX, original vector geometry, independent verification code/data, source notes and this QA record. It excludes workflow prompts, copied style exemplars, third-party books/artwork, old versions, build logs and image caches. Reference websites are cited but are not build inputs.

The repository's plans/week-65 directory preserves the draft reviews, checked construction notes and machine-readable final checks. Review findings were addressed before this release; those draft reports do not describe unresolved final defects.
