# Week 72 fresh revision stage

Status: independently reviewed prototype awaiting organizer review; unpiloted. Writer and independent review inputs remain unchanged. Final packet: four investigation pages plus one reusable apparatus sheet, shared Grades 4–5; footer GGT72-S-v1.

## Review decisions

- Accepted the discontinuous memory-apparatus finding. Removed both competing local number lines. Page 1 now directs partners to the same loose page 5 strip for every problem. The strip includes -10 through 10, so the two concrete target memories can be handled on one surface. It comes with two matching blank extensions and explicit one-tick overlap/continued-numbering directions; arbitrary memory is not restricted to a printed finite range.
- Added an essential apparatus page instead of shrinking task grids. Memory ticks are 7.2 mm apart; the extensions use exactly the same scale. Supply a small marker so each tick remains distinguishable.
- Made move cards real: page 5 supplies eight of each E/W/N/S card, each 1.8 cm square. The shared convention and apparatus page explicitly permit writing longer routes as ordered letters. Thus exploratory work does not silently require an unlimited card stock.
- Replaced "whole-number memory" with "integer memory (positive, zero or negative)." The unrestricted all-integer question remains intact.
- Retained all four investigations and the substantial translated negative-column/positive-column and L-loop cases. No review recommendation was rejected, and no signed-area or repeated-unit-loop recipe was added to the student pages.

## Checks

- Re-ran the EENE demonstration, six monotone routes, all 24 four-card loops, all translated rectangles, L-loop and integer-memory constructions.
- Added memory multiplicities (-1: 4 words, 0: 16, +1: 4); eight-move witnesses for memory 7 and -3 stay in the final grid and within the initial strip. Checked 101 arbitrary-memory samples using loops before arrival, and the numerical overlap convention for extending both ends of the line.
- Reviewed independent kernel/instance findings: a closed simple loop remembers signed area, translation preserves loop memory, and general self-crossing or repeated loops record algebraic area with multiplicity. The all-integer proof is by arbitrary repetition, not bounded sample enumeration.
- Built and rendered 5 final pages at 120 dpi and inspected every page individually. Clear number labels and cards, matching extension spacing, equal-scale grids, enough writing space, consistent footer IDs; no clipping, overlap or overfull/underfull box warnings.
- Copied only final/src to an isolated directory and rebuilt with --out from outside the source. Checks pass and extracted page text matches final/students.pdf. No absolute or repository dependencies are in the package; TeX environment repair was external to it.

## Handoff to the separate adult-guide author

Prepare one page 5 apparatus sheet per pair: pre-cut the memory strip, two extensions and 32 move cards. Supply tape, additional plain paper for more extensions and longer route words, a robot counter and a small separate memory marker. One adult rehearsal should use an extension on each side and a signed move on a negative column, including subtracting a negative column. The 7.2 mm tick spacing is a print specification, not a tested claim of child dexterity. Children can reuse the same memory strip alongside any task page; preserve the route and final state so a mistake can be replayed.

Page 1 remains available with only small nonnegative addition. Signed addition/subtraction is a genuine prerequisite from page 2, and the final all-integer explanation is readiness-dependent. The adult should not become the sole memory operator. The number line externalizes memory; it does not teach the signed arithmetic automatically. The page 4 board permits a general construction without leaving the mat, but discoveries remain children's choices.

In the guide preserve the integral convention z=sum(x*vertical step). An open path's z is not its signed area relative to the straight closing chord; that symmetric height is z-xy/2. The convention difference disappears for loops. For arbitrary loops distinguish algebraic area/multiplicity from the unsigned area of a drawn union. No physical apparatus rehearsal or classroom pilot has been completed.

Final mathematical recheck: ran the independent kernel and original-instance functions again, in addition to the revised source checker. Results and final source/PDF fingerprints are in final/math-recheck.json. This is a recheck, not a new independent review of the revision.
