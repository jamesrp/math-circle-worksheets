# Week 15 return-visit draft: independent mathematics review

Reviewed the actual four-page `draft/return-visit.pdf` and its current TeX, not the harness's obsolete three-band filenames. All four rendered pages were inspected. Problems 3–4 constitute one investigation, so this packet has three distinct investigations.

## Located mathematical ambiguities

### Grades 2–3 and up / page 2 / Problem 2: square interiors lack an explicit distance convention

**Quoted rules and task:** “Travel only horizontally or vertically. One small grid edge is one step. Distance is the length of a shortest trip, in steps.” “Label grid crossings A, B, or AB for the nearer dot. Do ties fill whole small squares? Can two tied places have a midpoint that is not tied?”

**Evidence:** The rules and the worked `3 + 1 = 4 steps` example define whole-edge travel at grid crossings, but the whole-square question also concerns points between crossings. If travel is interpreted as movement along the drawn grid edges, a point inside a cell has no legal trip. If steps must be whole edges, fractional midpoints need not be legal places. The intended continuous taxi distance `|x−a|+|y−b|` instead allows horizontal/vertical travel anywhere and fractional edge lengths. Under that convention, the printed A=`(0,0)`, B=`(2,2)` configuration has a tie set consisting of the two closed quadrants `x≥2,y≤0` and `x≤0,y≥2`, together with the segment `x+y=2` inside `[0,2]²`. Sixteen unit cells in the printed frame are wholly tied. The tied endpoints `(4,0)` and `(0,4)` have midpoint B=`(2,2)`, which is not tied. The desired discoveries are therefore correct once the continuous convention is explicit.

**Smallest fix:** Keep the crossing-labeling entry, and add that travel can pass through square interiors and part of an edge counts as the corresponding fraction of a step. Extend the compact non-task worked visual before Problem 2 to demonstrate one fractional edge with a matching routed intermediate drawing and total. Preserve the whole-square and midpoint questions; do not restrict the entire investigation to crossings.

### Grades 4–5 / page 3 / shared rules for Problems 3–4: metric wording

**Quoted rules:** “For Problems 3 and 4, distances go straight across.”

**Evidence:** The intended metric is Euclidean distance in any direction. “Across” can also be heard as a horizontal trip, which would leave most point-to-site comparisons undefined. Under straight-line distance, both optimization tasks and all site diagrams are correct.

**Smallest fix:** Replace the clause with “For Problems 3 and 4, use straight-line distances.” Retain the current inside-or-on-square candidate domain. Only the candidate point is constrained: requiring a clearance circle to fit inside the square would change the mathematics and the Problem 4 answer.

## Bands that otherwise check out

- **K–1 and up / page 1 / Problem 1:** Correct throughout. A, B, C, D are the square's lower-left, lower-right, upper-right and upper-left dots; E is its center. Each corner owns the opposite closed quadrant; E never owns a place. At the origin all four corners tie, and E does not. The whole-plane domain and multiple-owner tie rule are explicit.
- **Grades 2–3 and up / page 2 / Problem 2:** All 81 crossing comparisons and the actual whole-step worked example are correct. The diagram and intended continuous results check out after the convention repair above.
- **Grades 4–5 / pages 3–4 / Problems 3–4:** Correct under the clarified straight-line metric. With the four corners of `[-2,2]²`, the center is the unique best point, at nearest distance `√8`. Adding the center gives exactly four best points, the side midpoints, at nearest distance `2`. The three-row record table does not mathematically constrain the number of answers because all four can be marked on the map. No additional mathematical defect was found.

## Independent evidence and assumptions

`math-check-independent.py` imports no author-supplied solution or checking code. Its reproducible output is `math-check-independent.json`. It checks the actual PDF vector geometry and labels, all 81 printed lattice crossings (15 A, 35 B, 31 AB), sixteen affine whole-tie cells, 1,089 rational taxi comparisons, 1,089 farthest-site comparisons, and 25,921 exact rational clearance samples. The printed convention example is three edges across and one up, total four. All four main frames have four sides and equal horizontal/vertical scaling, at approximately 4.50006 inches per side; the tiny excess is PDF coordinate rounding. Every labeled site is at its intended normalized coordinate. All four full rendered pages were visually checked.

Finite experiments do not establish continuum claims. The independent analytic checks are:

- For a test point `(x,y)`, the largest squared corner distance is `x²+y²+8+4|x|+4|y|`, strictly greater than squared distance `x²+y²` to E. The maximizing signs give the stated opposite quadrants, including boundary ties.
- Write `h(t)=|t|−|t−2|`, equal to `−2` for `t≤0`, `2t−2` for `0≤t≤2`, and `2` for `t≥2`. The taxi tie equation `h(x)+h(y)=0` gives exactly the two quadrants and central segment stated above. On each printed unit cell, the distance difference is affine, so checking its four vertices establishes whether the entire cell is tied.
- For clearance, put `u=|x|`, `v=|y|`, with `0≤u,v≤2`. The nearest corner's squared distance is `(2−u)²+(2−v)²≤8`, with equality only when `u=v=0`. After adding E, if `u+v≤2`, the center's squared distance is `u²+v²≤(u+v)²≤4`, with equality only at `(u,v)=(0,2)` or `(2,0)`. If `u+v>2`, the quadrant corner is at squared distance at most `(4−u−v)²<4`. The four corresponding side midpoints each achieve nearest distance 2, proving completeness.

These distances use the normalized coordinates, not inches. On the printed 4.5-inch square, Problems 3 and 4 attain about 3.182 inches and 2.25 inches respectively. No physical string procedure or classroom use was tested. This review creates no revised student PDF or facilitator guide.
