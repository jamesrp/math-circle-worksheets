# Week 55 mathematical evidence

This is source documentation, not a facilitator guide. The student writer has not authored a session launch, teaching key, or hints. The eventual guide is a separate stage.

For finite nonempty integer sets A and B with m and n elements, count each value in A+B once. The sharp bounds are m+n−1 ≤ |A+B| ≤ mn. When m,n ≥ 2, the lower equality holds exactly when A and B are arithmetic progressions with the same positive gap. Their starting values and lengths may differ. A singleton is an essential exception: translation preserves the size of an arbitrary other nonempty set. Empty sets are excluded. Repeated input numbers are not extra elements. Ordinary integer addition is intended, with no wrapping or modular arithmetic.

The student card kit uses 0–9, and Problems 9–10 allow arbitrary whole numbers. These are special cases of the integer theorem. Negative integers need signed-addition readiness and a different labeled result strip; they are not silently required here.

Revision W55-S-v2 defines numerical equal spacing at first use: neighboring values in increasing order have equal differences. Those differences are gaps, independent of the physical positions of the printed cards. The count-conversion example before Problem 9 has A={1,4}, B={0,2,5,8}, so m=2, n=4, m+n−1=5 and mn=8. These are evaluations of count expressions, not an enumeration or assertion of the example's total count. No inverse-theorem proof procedure has been added to student pages. Each input's at-least-two-card restriction in Problem 10 excludes the singleton exception in ordinary language.

## Independent proof reconstruction

Order the inputs as a₁<⋯<aₘ and b₁<⋯<bₙ. Put aᵢ+bⱼ at grid position (i,j), with i increasing upward and j rightward. A path from (1,1) to (m,n), moving one index at a time, visits m+n−1 entries. Each entry is strictly greater than the previous one because one input increases and the other stays fixed. This proves the lower bound. There are mn input pairs, each supplying one value, which proves the upper bound.

Suppose m,n≥2 and there are exactly m+n−1 values. Every such full path is a list of all values. Fix any adjacent square. Choose a full path to its bottom-left corner and a full path from its top-right corner to the finish. Between those corners one path goes up then right, the other right then up. The paths agree everywhere except at their intermediate corner. Both are strictly increasing lists of the same complete set. Removing their common entries leaves one entry in each list, so those entries must agree:

aᵢ₊₁+bⱼ = aᵢ+bⱼ₊₁.

Thus aᵢ₊₁−aᵢ = bⱼ₊₁−bⱼ for every adjacent i and j. Because both inputs have at least two entries, fix one gap in either input; every gap in the other equals it, and then all remaining gaps in the first equal it too. Both inputs have one common positive integer gap d.

Conversely, for A={a+id:0≤i<m} and B={b+jd:0≤j<n}, every sum is a+b+kd with 0≤k≤m+n−2. Every such k occurs: take i=min(k,m−1) and j=k−i. Then j is in 0,…,n−1. There are exactly m+n−1 distinct values because d>0.

This proves the stated exact extremal theorem. It does not prove the general Freiman small-doubling theorem. Small exhaustive computer checks are evidence for the printed cases, not a replacement for this proof.

## Task evidence

The verifier separately enumerates all legal 0–9 designs for the printed sizes. Problem 3 reaches minimum 5 and maximum 9. Problem 4 reaches minima 4, 5, and 6 for sizes 2+3, 2+4, and 3+4. The complete Problem 5 catalog has B={t,t+3} for t=0,…,6, each giving {t,t+3,t+6,t+9}; all 45 two-card B choices are checked. Problem 6 counts are 4,6,4,4, distinguishing mismatched gaps, shifted starts, and another common gap. Problem 7 counts are 3,3,4 irrespective of B's spacing. All routes in all three printed grids are independently generated and tested for the stated length and strict increase. Every displayed grid entry is generated from its row and column inputs in TikZ.

The finite general check covers all 261,121 ordered pairs of nonempty subsets of {0,…,8}, including singleton exceptions and both directions of the equality characterization. The kit-specific checks cover the displayed value 9 and all design spaces.
