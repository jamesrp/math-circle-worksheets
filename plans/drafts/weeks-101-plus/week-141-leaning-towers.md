# Week 141 (draft plan): Leaning towers off the table

**Strand:** analysis, with shape (app region "Shapes and spaces"). **Deep-math field:** statics (centre of mass), infinite series, optimisation. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

With n identical blocks of length 1, stacked one per level, the greatest overhang past a table edge is (1/2)(1 + 1/2 + 1/3 + … + 1/n) = H_n/2 (the "harmonic stack"; in print at least since Paul B. Johnson's "Leaning Tower of Lire", 1955). Building from the top down shows why: the top block can stick out 1/2 past the block below; then the top two together have their centre of mass 1/4 past the top block's support edge, so they can stick out 1/4 past the third block; in general the top k blocks, whose combined centre sits at the average of their centres, can stick out 1/(2k) past the next. One block reaches 1/2, two 3/4, three 11/12, and four 25/24, so four blocks put the top block entirely past the edge. Because the harmonic series diverges (Oresme's grouping: 1/3 + 1/4 > 1/2, 1/5 + … + 1/8 > 1/2, and so on), any overhang is possible with enough blocks, but slowly: overhang 2 needs 31 blocks and overhang 3 needs 227, and the growth is about (1/2) ln n. Every harmonic stack is a knife-edge balance; a real one must give up a little. Allowing several blocks per level changes everything. Three blocks reach 1 (one block centred on the edge with two blocks side by side on top), four reach (15 − 4√2)/8 ≈ 1.168 (Ainley), and Paterson and Zwick (SODA 2006, American Mathematical Monthly 2009) built stacks with overhang of order n^(1/3), exponentially better than the harmonic stack. Paterson, Peres, Thorup, Winkler and Zwick then proved that any balanced n-block stack has overhang at most 6n^(1/3), so order n^(1/3) is optimal; the best constant is open. Children can discover the four-block milestone by building, the halving-then-thirds pattern of each new block's slide, and in grades 4–5 why the overhang never stops growing, and that cleverer stacks beat one-per-level.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Overhang](https://ar5iv.labs.arxiv.org/html/0710.2357). Mike Paterson and Uri Zwick, arXiv 0710.2357 (preliminary version SODA 2006; full version for the American Mathematical Monthly). Harmonic stacks give (1/2)H_n; Ainley's four-block optimum (15 − 4√2)/8; optimal stacks for n ≤ 19 by search; parabolic stacks with overhang of order n^(1/3) (read November 3, 2026).
- [Maximum Overhang](https://ar5iv.arxiv.org/html/0707.0093). Mike Paterson, Yuval Peres, Mikkel Thorup, Peter Winkler, Uri Zwick, arXiv 0707.0093. Theorem: a balanced n-block stack has overhang at most 6n^(1/3), so order n^(1/3) is best possible (read November 3, 2026).
- [Maths in a Minute: the Leaning Tower of Lire](https://plus.maths.org/maths-minute-harmonic-series-and-leaning-tower-lire). Ben Watkins, Plus magazine, July 22, 2025. Johnson 1955, the centre-of-mass method, harmonic overhang and its divergence (read November 3, 2026).
- [Solution: 'Hanging Far Out Over the Edge'](https://www.quantamagazine.org/the-overhang-puzzle-solution-20161202/). Pradeep Mutalik, Quanta Magazine, December 2, 2016. H_n/2 with five blocks giving 137/120, and the note that multi-block levels do better (read November 3, 2026).
- Prior use with children: [Centre of Gravity Grade 7: Form and Function (lesson plan)](https://www.sciencenorth.ca/sites/default/files/2018/April%2021%20-%20Grade%207%20-%20Centre%20of%20gravity%20-%20lesson%20plan%20ENG.pdf). Science North, 2018: stack at least four identical blocks, books or cards one per level until the top one is fully past the table edge; use a low table (read November 3, 2026). No K–5 math-circle handout was found.

## A kid-friendly way in

Materials per table: 8 identical wooden blocks (Jenga-type or cut 2 × 4 offcuts), a low table or a sturdy box with a straight edge, masking tape to mark the edge, a "block ruler" (a card strip one block long marked at 1/2, 3/4, 11/12 and 25/24 for adults, or plain halves and quarters for children), and a pillow or tray below the edge. Prep: gather blocks and make the strip, about 15 minutes. Launch (3 minutes): slide one block out until it is about to tip and mark where its middle is; then ask whether, with more blocks, the top block could be completely past the edge, with no part above the table.

Suggested hour: 0–5 launch; 5–25 one-per-level stacking toward "top block fully past the edge"; 25–45 band questions; 45–60 compare the best stacks, then show the three-block side-by-side stack as a surprise.

## By band

- **K–1:** How far can one block stick out? Two blocks? Make the top block hang all the way past the tape. Children check "past the edge" by sighting down from above.
- **2–3:** Find the fewest blocks that put the top block fully past the edge, one block per level. Then measure each block's step with the block ruler; what pattern do the steps make from the top down?
- **4–5:** Explain the top-down method with centres (each block's middle, then the middle of a pair, of three). Will 8 blocks reach two block lengths? Will any number? Group the steps 1/3 + 1/4, then 1/5 to 1/8, as in atlas GA-12. Then free the rule: with two blocks allowed on a level, how far can three or four blocks reach?

## Checked facts

- `check_week_141()`: H_n/2 = 1/2, 3/4, 11/12, 25/24, 137/120 for n = 1 to 5; three blocks fall short of 1 and four pass it.
- `check_week_141()`: with exact fractions, for n up to 11, the centre of mass of the top k blocks of the harmonic stack sits exactly over the edge of block k + 1 (or the table edge), so every harmonic stack balances on knife edges.
- `check_week_141()`: overhang 2 first needs 31 blocks and overhang 3 needs 227; a 52-card deck gives about 2.27 card lengths; H_1000/2 − (1/2) ln 1000 ≈ 0.289.
- `check_week_141()`: the three-block stack (bottom block centred on the edge, two blocks side by side above) balances and reaches 1 > 11/12; Ainley's (15 − 4√2)/8 ≈ 1.16789 exceeds 25/24 (the formula is cited from Paterson and Zwick).
- `check_week_141()`: Oresme groups 1/(2^m + 1) + … + 1/2^(m+1) are each at least 1/2 for m = 1 to 7.
- The n^(1/3) order and the 6n^(1/3) bound are cited, not computed.

## Nearest existing themes

Atlas GA-12 (harmonic machine against halving machine) is the same series with fraction strips; this week gives it a physical body and a reason to care. Week 89 (Growing shapes and totals) builds running totals. Week 131 (coupon collector) is a chance home for the same harmonic numbers. The word "overhang" in Week 32 (squares must not overhang a rectangle) and Week 91 (card corners extending past circles) is about drawing fit, not stacking, so there is no overlap. Week 20 (Averaging) and atlas AP-01 use balance-point averages in a different way. New here: centre of mass as an average, a divergent series met with the hands, and an optimisation question whose answer is a 2009 research result.

## App connection

Region "Shapes and spaces", possible family "Leaning tower": a side-view board where a child drags blocks onto a stack; the machine shows each partial stack's balance point as a dot and topples unbalanced stacks. Puzzle 1: "Get a block fully past the edge with as few blocks as you can." Puzzle 2: "Beat 1 block length with 3 blocks" (requires two blocks on one level). A physics-free version can check balance exactly with fractions, so no simulation engine is needed.

## Open questions

- Material fit: knife-edge stacks topple; rehearse with real blocks to see how close children get to 25/24 with four (expect less) and whether the five-block margin is a better target.
- Do 2–3 children need the block ruler, or is "past the edge or not" enough for their question?
- Is the side-by-side three-block stack buildable by hand without glue, given it is also a knife-edge balance?
- Whether the n^(1/3) result should appear in the guide only as an adult note.
