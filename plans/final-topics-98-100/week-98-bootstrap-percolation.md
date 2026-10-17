# Week 98 Growing from a few seeds

Planning proposal, October 17, 2026. Bootstrap percolation supplies the new investigation: design a sparse start that eventually fills a square, then separate efficient starts from starts with no removable seed. This is a finite deterministic model related to statistical physics; randomness is optional and comes later.

## Mathematical destination before solutions

Use an n-by-n square grid, n at least 1. Only side-neighbors count. Initially chosen cells are seeds. Any empty cell with at least two filled neighbors may fill; filled cells never empty. There are no cells outside the board and no wrapping. Continue until no legal addition remains.

**The finish is well defined.** Each addition increases the filled set, so the process stops. Every completed legal order reaches the smallest set containing the seeds and closed under the two-neighbor rule. To prove this, each legal addition must belong to every such closed superset. Thus all terminal runs equal that least closed set. This does not make the number of parallel rounds independent of the timing convention.

**Exactly n seeds suffice and are necessary to fill an n-by-n board.** Count all exposed unit sides, including board edges and hole boundaries. Adding a cell with k filled neighbors changes this perimeter by 4−2k, which is nonpositive for k≥2. A start with s seeds has perimeter at most 4s; the full board has perimeter 4n. Therefore s≥n. The n main-diagonal cells fill the board: cells one diagonal away fill, then those two away, and so on. An n-by-n filled picture alone is evidence; the perimeter argument plus the construction proves optimality for every n. Do not replace the open square boundary by a torus or silently change the neighbor rule.

**Indispensable does not mean smallest.** A seed set is inclusion-minimal when removing any one seed prevents filling; it is minimum when no start with fewer seeds fills. A checked 3-by-3 set has four indispensable seeds, although the diagonal uses three. The children can encounter this distinction before adults supply either term.

Grades 2–3 can choose, run and compare seed patterns. Ready grades 3–5 can mark exposed edges and argue why fewer seeds are impossible; the indispensability investigation offers a second mathematical direction. Experiments establish individual finishes, conjectures predict wider patterns, and the two arguments above establish universal facts. The random critical probability and its asymptotic behavior are research context, not results children establish here.

## Materials and a complete opening

Per pair: one reusable 4-by-4 grid with 30 mm cells, a removable 3-by-3 mask, 16 counters or square tiles, and a second color or small seed dots to distinguish the original seeds. Keep the reset picture beside the board. A partner points to two filled side-neighbors before a new tile is placed. Growth is sequential; do not require simultaneous-round bookkeeping. The upper trio rotates grower, checker and seed designer. Prepare three older-table kits and a demonstration kit from existing pieces; allow roughly 15–20 minutes for drawing grids and reset cards, subject to rehearsal. A 120 mm square fits a Letter page. No millimeter-perfect tile fit is mathematically necessary, but pieces must not hide neighboring cells.

After two minutes handling tiles, demonstrate on a separate 2-by-3 board. Shared rule: “Fill an empty square when at least two squares sharing its sides are filled. Filled squares stay filled. Keep going until no more can fill.”

```text
Input               Legal middle           Finish
S . .               S + .                  S + .
S S .               S S .                  S S .
                    top middle touches     Neither right-hand cell
                    two filled sides       has two filled neighbors
```

Here S marks a seed and + a later addition. Point to the lower-left and lower-middle seeds and show that a diagonal touch is insufficient; then fill the top middle using its left and lower neighbors. This teaches one full run including stopping, without displaying an optimal start for a target square. Children then choose their own starts.

## Five substantial investigations

1. **Make two three-seed starts on a 3-by-3 board: one that fills every square and one that gets stuck.** Let children seek very different finishes rather than merely repeat the demonstrated L. A diagonal fills; a full top row cannot grow. Optional adult question: what can move next in the unsuccessful start? Save just the seeds and final picture.
2. **What is the fewest seeds that can fill a 4-by-4 board? Find different starts that reach your best number.** Children should own the construction and search. Four diagonal seeds work; the antidiagonal also works. Adjacent seeds can waste initial perimeter, suggesting a useful later obstruction. Do not print the answer or prescribe a diagonal search.
3. **Choose a seed start. Can two different legal orders finish with different filled squares?** Partners replay the same reset picture, choosing different available additions, then invent starts that might defeat their prediction. For a concrete contrast, the three main-diagonal seeds on 3-by-3 immediately allow four choices. Every completed run has the same finish by the least-closed-set argument. Different temporary pictures do not refute that claim. An adult may ask why any cell one run adds must eventually appear in the other.
4. **Can three seeds fill a 4-by-4 board? What about four seeds on a 5-by-5 board? Find a reason that settles every possible start.** After substantial attempts, an adult may introduce short sticks on exposed edges. Compare adding a tile against two, three and four already filled sides; the perimeter changes by 0, −2 and −4. At most 12 initial sides cannot end as 16; at most 16 cannot end as 20. This is a new use of the familiar perimeter, not an extra table to fill in. General n is an optional spoken continuation.
5. **This start fills a 3-by-3 board. Does it still fill if you remove any one seed? If every seed is needed, must four be the smallest possible number?** Supply the four-seed pattern below; let pairs share the four removal trials, preserving each reset picture. Then invite them to invent another indispensable start. This is a later investigation, not a trick replacing the earlier optimum task.

```text
S S .
. . S
. . S
```

For P5, parallel layers are (1,3),(2,2), then (2,1),(3,2), then (3,1); coordinates are row,column from the upper left, starting at 1. These layers are an adult verification device, not a required student record. Removing seeds at (1,1),(1,2),(2,3),(3,3) leaves final filled counts 6,3,3,6 respectively. Thus all four seeds are indispensable, while the three-seed diagonal disproves minimum size. The complete 3-by-3 check finds 14 minimum sets of size 3 and 9 additional inclusion-minimal sets of size 4, counting rotations/reflections as different placements. Children need not reproduce that enumeration.

## Plausible sequence and limits

First visit: five-minute movement opening; five-minute material exploration and shared example; 20–25 minutes on P1–2; 10–15 minutes choosing P3 or beginning the perimeter discussion; brief sharing. P4’s general explanation and P5 are substantial continuations for another visit. Introduce boundary sticks only when a lower bound would answer a question children have encountered. The newer mathematical idea is not “fill rows faster”; it is the gap between local indispensability and global economy.

A later random-start experiment may compare seed densities, using one random decision independently at each site. Do not infer an infinite-grid threshold from a handful of 4-by-4 trials or confuse uniformly choosing exactly k seeds with independent occupancy. That experiment is deliberately outside the five proposed core prompts.

## Sources and exact overlap

Robert Morris, [*Minimal percolating sets in bootstrap percolation*](https://arxiv.org/pdf/math/0702370), introduction pp. 1–2, defines the process, states the n-seed minimum, and distinguishes inclusion-minimal sets from minimum size; Theorem 1 on p. 3 studies how large inclusion-minimal sets can be. The four-seed instance, elementary proofs and activity sequence here were worked out separately. The paper’s historical open questions are not asserted to remain open today.

Atlas AD-07 already teaches monotone closure, order-independent completion, smallest generating sets, and closed sets under if-then rules. P3 is a deliberate connection, **not a new kernel**. Week 26 already counts exposed sides and proves perimeter bounds. Here that quantity becomes a nonincreasing certificate for a growth process, and P5 changes the optimization question. Week 11 redistributes conserved chips and loses chips into a sink; this model adds occupied sites permanently and has no firing conservation law. Week 89 studies prescribed shape layers and accumulated totals, while these shapes emerge from a local threshold. Week 91 routes particles with persistent switches; it neither grows occupied sets nor optimizes seed sets. Week 77 tracks filled faces and surviving loops; no homology is involved here. These boundaries justify keeping P2, P4 and P5 central.
