# Week 55 research and outline record

Prepared October 4, 2026. This is research/outline work only. The new theme is a sharp inverse sumset problem: few distinct sums force common equal spacing. [outline.md](../../../../plans/new-themes-52-63/week-55/outline.md) follows the unchanged template and leaves student problem choice to the fresh writer. No student PDF, facilitator guide, release, upload or classroom use is claimed.

## Exact theorem and proof

Let A={a1<...<am} and B={b1<...<bn} be finite nonempty sets of integers. A+B={a+b:a∈A,b∈B} counts distinct values, not pairs or probability weights. Then m+n-1≤|A+B|≤mn. The lower certificate is the strictly increasing list a1+b1,...,a1+bn,a2+bn,...,am+bn. The upper bound follows because each pair supplies at most one result.

When m,n≥2, equality in the lower bound occurs exactly when both inputs are arithmetic progressions with the same positive integer gap d. Different starts and lengths are allowed. This is the elementary exact extremal theorem, not the full Freiman small-doubling theorem.

Complete independently reconstructed inverse proof: arrange a_i+b_j in a sorted m×n array. Any path from (1,1) to (m,n) that increases one index by one at each step gives m+n-1 strictly increasing sums. In an equality case this is the entire sumset. For any adjacent square (i,j) to (i+1,j+1), choose two full paths identical except that one goes through (i+1,j), the other through (i,j+1). Both must contain exactly the same sumset. Their other entries coincide and are strictly increasing, so a(i+1)+bj=ai+b(j+1). Therefore a(i+1)-ai=b(j+1)-bj for every i,j. All gaps in both sets are one d>0. Conversely, common-gap progressions have sums a1+b1+kd for every k=0,...,m+n-2, producing exactly m+n-1 values. The proof applies to finite real sets too, but this packet keeps the integer theorem and integer-card model.

If either input is a singleton, translation gives equality for every other nonempty set, including unevenly spaced ones. Empty sets do not satisfy the stated lower formula. Inputs are sets, so repeated values are not extra elements. The ordered integer theorem is not valid with the same formula in cyclic groups (for example a whole three-residue group added to itself has only three results rather than five). Zero is an allowed input. An "inverse" conclusion gives structure, not a unique recovery of A and B.

Checked contrasting examples:

| A | B | A+B | Size / lower bound |
|---|---|---|---|
| 0,1,2 | 0,1,2 | 0,1,2,3,4 | 5 / 5 |
| 0,1,3 | 0,1,3 | 0,1,2,3,4,6 | 6 / 5 |
| 0,1,2 | 0,3,6 | 0,1,2,3,4,5,6,7,8 | 9 / 5 |
| 1,3,5 | 2,4 | 3,5,7,9 | 4 / 4 |
| 0,2,4 | 0,3 | 0,2,3,4,5,7 | 6 / 4 |
| 4 | 0,1,3 | 4,5,7 | 3 / 3, singleton exception |
| -2,0,2 | -3,-1,1 | -5,-3,-1,1,3 | 5 / 5, optional signed extension |

[checks.py](../../../../plans/new-themes-52-63/week-55/checks.py) generated [checks.json](../../../../plans/new-themes-52-63/week-55/checks.json). All 261,121 ordered pairs of the 511 nonempty subsets of {0,...,8} satisfy the bound and exact equality characterization: 1,699 nonsingleton equality pairs, and all 9,117 pairs involving a singleton. A strictly increasing lower certificate was checked for every pair. This is finite verification of examples; the path-swap argument proves the general claim. Physical readiness and classroom understanding remain untested.

## Sources actually consulted and their scope

- Tao and Vu, *Additive Combinatorics*, author-hosted sample DVI: Prologue Definition 0.1, sample pp.6–7; chapter 2 opening pp.67–69; §2.1 pp.70–71, Lemma 2.1. [Primary sample](https://www.math.ucla.edu/~tao/preprints/additive_sample.dvi), linked from the [author's book page](https://teorth.github.io/tao-web/additive-combinatorics.html). [Downloaded original](../../../../external-resources/new-themes-52-63/week54-55/tao-additive-sample.dvi); converted reading PDF and extracted text are in tmp/new-themes-54-55-research/. It supplies finite nonempty additive-set definitions, cardinality estimates, progression examples and the inverse problem context. The contents mention §5.1, but the sample omits that chapter body, so no exact equality theorem number from it is claimed. The proof above is ours, rather than falsely attributed to an uninspected chapter.
- Tao, [*Sumset and inverse sumset theorems for Shannon entropy*, June 25, 2009](https://terrytao.wordpress.com/2009/06/25/sumset-and-inverse-sumset-theorems-for-shannon-entropy/): opening discussion and final combinatorial comparison state standard sumset context and |A+A|≥2|A|-1. [Local HTML](../../../../external-resources/new-themes-52-63/week54-55/tao-sumset-entropy-2009.html). It does not prove our two-set equality theorem, and entropy material is not adapted into the child activity.
- Givental, Nemirovskaya and Zakharevich, *Math Circle by the Bay*, Preface printed pp.viii–ix (PDF pp.9–10), "How we select our topics" and "How we teach", [local book](<../../../../external-resources/msri-math-circle-books/Math Circle by the Bay.pdf>): deep thematic development, independent work/dialogue, clear statements and manipulatives. Our inference is a visible set/result-strip entry before introducing an addition-array proof; the source does not prescribe our cards or age gate.
- Stankova and Rike, eds., *A Decade of the Berkeley Math Circle*, chapter 6 §3.6 "The burden of proof", printed pp.113–114 (PDF pp.133–134), [local book](<../../../../external-resources/msri-math-circle-books/A decade of the Berkeley Math Circle.pdf>): distinguishes empirical case evidence from a proof. Our adaptation distinguishes tested small sets, a common-spacing conjecture, and the complete array argument.
- Organizer's year-1 [*Handouts 1*](<../../../../lowell-math-circle-year-1/lowell-math-circle/Math Circle Fall 2025/Handouts 1.docx>), unnumbered figurate-number and sum/difference pictures, was read through DOCX XML. It gives local precedent for making addition visible with objects. It contains no sumset cardinality or inverse theorem; the result-strip procedure is a new design inference informed by the current context's recorded lamp-rule failure.

No borrowed prose, figures or tables are placed on student pages. Source HTML and original reference files remain under external-resources; temporary reading/render products remain under tmp/.

## Overlap audit and novelty

Both WEEKS-11-51.md and BONUS-AND-RETURN-VISITS.md were read. Closest actual current PDFs were inspected:

| Existing material | Page evidence | Distinction |
|---|---|---|
| Week 24 bonus | pp.2–3: ordered two-draw sums from a fixed deck, followed by average points over four draws | Those tasks keep pair multiplicities and compare distributions. Week 55 counts each result once, designs the input sets, and proves the exact common-gap structure at minimum cardinality. |
| Week 29 upper base and bonus | Base pp.1–5: repeated fixed rod lengths and unreachable targets; bonus pp.1–4: ordered words, finite complement, redundant generators | These are unrestricted repeated sums or finite kit selections. Week 55 takes exactly one member from each of two fixed sets and studies the whole result set. |
| Week 30 upper base and bonus | Base pp.1–5: signed assignments of kit weights; bonus pp.1–4: loss tolerance, comparisons and equal teams | Additive representations appear, but neither this sharp two-set bound nor its inverse equality condition is a weight-kit problem. |
| Week 50 upper base and bonus | Base pp.1–6: Euclidean/staircase lengths; bonus pp.1–3: priced moves, obstacle route counts and arbitrarily long strip paths | Right/up routes are a proof device in the addition array. Week 55 does not ask for geometric route length or number of grid routes. |

The central novelty is additive structure determined from a minimum count of distinct results. Ordinary addition, counters and an eventual grid proof are familiar representations, not the criterion for theme identity. This audit covers indexed themes and the closest printed neighbors, not a fresh review of every atlas page.

## Operational recommendation

Recommend a combined packet chiefly for Grades 3–5. A ready third grader can add small whole numbers, retain fixed inputs, merge repeated results and choose new sets; adult reading or an occasional supplied addition fact can support this without operating the whole investigation. A second grader with these prerequisites can enter. The inverse proof requires coordinating two ordered inputs and a result count, so no independent K–1 packet is recommended. Small visible sets, a single result strip and partner checking keep bookkeeping light. Use a short non-task placement demonstration; the grid/array becomes relevant only after concrete collisions and minimum-count attempts. The 0–18 strip at 12 mm cells needs landscape orientation or a separate table strip. An eventual adult guide must open with the exact bound, equality assumptions, singleton exception and proof map. That is a separate stage.

The current context matches the October 3 fixed KK11 / 3333 / 445 tables and three anchored adults; omitted young bands do not constitute a meeting plan for the K–1 table. The root supplies combined-file routing; no tested workflow prompts or global files are edited here.
