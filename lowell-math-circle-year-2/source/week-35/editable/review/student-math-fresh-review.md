# Week 35 independent mathematics review

Reviewed October 4, 2026. No located mathematical defects. K–1, grades 2–3 and grades 4–5 all check out completely for the stated ideal infinite borders, with only footprint positions and orientations counted.

## Independent method

The reviewer built an independent exact periodic decorated-point model: a footprint is identified by its position modulo a period and its signed orientation. Candidate isometries must match both position and orientation. The supplied notched motif was independently checked by fitting every cyclic permutation and every reversed cyclic permutation of its twelve polygon vertices; among all 24 candidates, only the identity is a plane isometry. Thus orientation distinctions are real, not assumed from an ordinary symmetric footprint.

Independent witnesses and assertions are saved in `critic-render/math-checks.json`. Preservation evidence, including actual-PDF strip dimensions, is in `critic-render/preservation-checks.json`. The author's checkers were read after the independent computation but were not run or imported.

For the constructions below, I is the original motif, H its horizontal mirror, V its vertical mirror and R its half-turn. Coordinates are motif placement origins in centimetres, with repetition in x. Place motifs on loose material; printed guide lines are not pattern data.

| Witness | Period and one repeated part | Verified motions |
|---|---|---|
| Single slide border | P=3: I at (0,0) | Slides 3 and 6 match; slide 1.5 fails. A larger P=6 one-motif border supplies a different shortest slide. |
| Glide without bare reflection | P=6: I at (0,1.5), H at (3,-1.5) | Flip over y=0 then slide 3 matches; flip alone and slide 3 alone fail. Shortest slide is 6; shortest glide is 3. |
| A different glide border | P=12: I at (0,1.5), H at (6,-1.5) | Flip plus slide 6 matches while flip alone fails. |
| Horizontal reflection without half-turn | P=6: I at (0,1.5), H at (0,-1.5) | Horizontal reflection matches. Any half-turn would require R/V orientations, which are absent, so no half-turn about any point matches. Moving the lower H to a different x-position in every repeat breaks the reflection while preserving repetition. |
| Half-turn without either reflection | P=6: I at (0,1.5), R at (3,-1.5) | Half-turn about (1.5,0) matches. Horizontal and every vertical reflection fail because either requires H/V orientations, which are absent. |
| Both perpendicular reflections | P=6: I at (1,1.5), H at (1,-1.5), V at (5,1.5), R at (5,-1.5) | Reflection in y=0 and reflection in x=0 match; their composition, the half-turn about (0,0), also matches. |
| Larger repeat edit | P=6: I at (0,0), I at (4,0) | Replacing the regular 3 cm placement by this repeating arrangement breaks the old 3 cm slide, retains a 6 cm slide, and implements a moved-footprint edit. |

## K–1 verification coverage

| Problem / page | Asked outcome and verification |
|---|---|
| 1 / 1 | Make one repeating border and find matching/failing slides. The single-slide witness does so; the stated nonzero-slide rule excludes the identity. |
| 2 / 2 | Make two borders with different shortest matching slides. Single identically oriented motifs every 3 cm and every 6 cm give respective primitive periods 3 and 6. |
| 3 / 3 | Make a flip-plus-slide match and attempt failure of the flip alone. The glide-only witness satisfies both. The worked visual precedes the task and correctly reflects the same footprint before sliding it. |
| 4 / 3 | Make a different border with the same match type. The P=12 witness provides a different glide-only border. |
| 5 / 4 | Make a horizontal-reflection border and change it to break that reflection. The paired I/H witness and a repeated offset of the lower motif supply both arrangements. |
| 6 / 5 | Make one half-turn border and one with no half-turn about any point. The I/R and I/H witnesses supply the two outcomes; missing required orientations prove universal failure for the latter. |
| 7 / 5 | Trade and find matching motions. This is an investigation of the constructed object; checks must cover the generating rule of the endless repetition, not only its finite scrap. No claimed fixed answer is printed. |

All six original K–1 problems are retained as 2–7; only Problem 1 is added. The shared rules are unchanged. The moved glide visual has unchanged geometry and labels.

## Grades 2–3 verification coverage

| Problem / page | Asked outcome and verification |
|---|---|
| 1 / 1 | Build two different shortest slides and mark one on each copy. Primitive periods 3 and 6 supply a witness. |
| 2 / 2 | Build a glide match with failed bare reflection. The P=6 I/H staggered witness succeeds. |
| 3 / 2 | Compare the shortest glide and slide on that border. Because reflection alone fails, the shortest glide is half the primitive translation period; the witness gives 3 versus 6 cm. |
| 4 / 3 | Build horizontal reflection while avoiding every half-turn. The aligned I/H witness works; orientation incompatibility excludes all centres. |
| 5 / 4 | Build a half-turn with failed horizontal reflection. The staggered I/R witness works. |
| 6 / 4 | Move footprints to destroy an old match but retain repetition, allowing a larger repeated part. The period-edit witness destroys a 3 cm slide and retains a 6 cm slide. |

## Grades 4–5 verification coverage

| Problem / page | Asked outcome and verification |
|---|---|
| 1 / 1 | Build and justify different primitive slides. A single asymmetric motif every P cm matches translations exactly at integral multiples of P, so periods 3 and 6 give complete proofs. |
| 2 / 2 | Build glide without bare reflection and find shortest distances. The staggered I/H witness has translations 6k and glides 3+6k, with no bare horizontal reflection; shortest positive lengths are 6 and 3 cm. |
| 3 / 2 | Decide which slides are forced by a flip plus 3 cm slide. Its square is a 6 cm slide, so 6 is forced. A 3 cm slide is not forced, as the glide-only witness proves. |
| 4 / 3 | Build matches across both drawn crossing lines and infer forced moves. The diagram's lines are perpendicular. Their composition is a half-turn about their crossing; periodic copies of this motion and reflection axes are also obtained with translations. The four-orientation witness realizes the condition. |
| 5 / 4 | Build half-turn, fail horizontal reflection, and attempt failure of every perpendicular reflection. The I/R witness meets all requirements. |
| 6 / 4 | Describe every matching motion of one construction and justify it for the infinite pattern. For example, the glide-only witness has translations 6k, horizontal glides 3+6k, and no vertical reflection or half-turn because the needed V/R orientations are absent. Other rotations cannot preserve a discrete strip with a primitive horizontal translation. This supplies a complete description rather than a few successful experiments. |

## Theorems and limits checked

For G_a(x,y)=(x+a,-y), direct composition gives G_a²(x,y)=(x+2a,y). The horizontal reflection and along-axis translation commute. If the primitive translation is P and the bare reflection fails, every glide displacement lies in the half-period coset P/2+Pℤ; if the bare reflection matches instead, the glide displacements lie in Pℤ. The older packet's shortest-distance question refers to the former construction. The drawings and wording do not assume that every arbitrary successful glide is shortest.

The two printed reflection axes are perpendicular, so their composition is a half-turn. That conclusion would not hold for arbitrary crossing lines, but no such lines are printed. Finite matching attempts supply experiments; a generating-rule or orientation argument establishes the endless pattern's symmetry. All bands retain this limit in the shared rules.

Every delivered page was rendered and inspected. The nine K–1 working rectangles measure 17.65 by 6 cm from actual PDF paths, preserving original scale. Older-band source and PDFs are byte-identical. Physical tracing/cutout fit and classroom piloting remain untested.
