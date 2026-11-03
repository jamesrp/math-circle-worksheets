# Week 115 (draft plan): Wallpaper patterns

**Strand:** symmetry (Patterns and symmetry). **Deep-math field:** geometry, group theory (plane crystallographic groups). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A wallpaper pattern repeats by slides in two different directions, and its symmetries (slides, turns, mirrors, glides) form one of exactly 17 types: the plane crystallographic or wallpaper groups, first listed by Evgraf Fedorov in 1891 and found again independently by George Pólya in 1924. Two theorems carry the classification. The crystallographic restriction: a turn that keeps a wallpaper pattern can only be a half, third, quarter or sixth turn (orders 2, 3, 4, 6). One proof uses a shortest slide t: turning t by the spin angle gives another slide, and for 5-fold spins the sum t + (t turned by 144°) is a slide about 0.618 times as long as t, while for 7-fold and higher t minus its turned copy is shorter; either way t was not shortest. The second is Conway's "magic theorem", from John Conway's orbifold notation (Conway, Burgiel and Goodman-Strauss, *The Symmetries of Things*, 2008): list each kind of spin point by its order n, each kind of mirror line by *, the spin orders where mirrors cross after the *, a glide not explained by mirrors by x, and a pattern with only slides by o; charge (n − 1)/n for a spin point, 1 for each * or x, (n − 1)/(2n) for a mirror corner, 2 for o. Every wallpaper pattern costs exactly 2, and the signatures that cost exactly 2 are exactly the 17 groups. Children can discover that spin points come only in orders 2, 3, 4 and 6, that patterns with spins and no mirrors fall into four families, and why a 5-fold spin never appears; the "costs add to 2" rule becomes a find-all-ways puzzle. Proved: the 17, the restriction, the magic theorem (its proof is an Euler-characteristic argument, adult reading). Checked here: the cost-2 enumeration returns exactly the 17 signatures, and the four spin-only ones (2222, 333, 442, 632). Nothing in the plane classification is open; the limits are the assumptions: discrete symmetries and slides in two independent directions. Note the hard part for adults: the notation counts each kind of point once, where "same kind" means one is carried to the other by a symmetry.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [A Brief Survey on Wallpaper Groups](https://math.mit.edu/research/highschool/primes/circle/documents/2023/Angela_Zhao.pdf). Angela Zhao, MIT PRIMES Circle, May 2023. Orbifold notation, the cost table, the magic theorem (stated, proof deferred to Conway et al. ch. 7), the casework giving exactly 17, and the four rotation-only groups 2222, 442, 333, 632 (read November 3, 2026).
- [The Crystallographic Restriction](https://mathpages.com/home/kmath547/kmath547.htm). MathPages, no author named on the page. A lattice argument that 2cos θ must be an integer, leaving orders 2, 3, 4, 6 (read November 3, 2026).
- [Wallpaper group](https://en.wikipedia.org/wiki/Wallpaper_group). Wikipedia, used only as a pointer for the history: Fedorov 1891, Pólya 1924, and the statement of the restriction (read November 3, 2026).
- Prior use with children: [UW Math Circle, Week 24: Wallpaper Patterns](https://sites.math.washington.edu/~mathcircle/circle/files/25sp-week24.pdf). University of Washington Math Circle, spring 2025; level not stated. Students extend patterns, mark mirror and rotation points, find glides, name signatures such as *632 and 22x, and draw a wallpaper for a partner to classify (read November 3, 2026).

## A kid-friendly way in

Hunt for spin points with tracing paper and a pushpin. Each table gets 6 to 8 printed wallpaper samples (gift wrap, fabric photos or printouts the volunteer makes from a free symmetry drawing tool), tracing paper, a pushpin on a piece of cardboard, and a small craft mirror. Trace a patch of the pattern, pin the tracing at a point, and turn it: if the tracing matches again before a full turn, the pin is on a spin point, and the number of matches in a full turn is its order. A second station stamps patterns: an asymmetric stamp (a footprint or flag cut from a sponge, as in Week 35) on a square or triangle grid, following a rule card such as "turn a quarter at every corner". Prep: printing and cutting, about 25 minutes. Launch (2 to 3 minutes): on a large printed pattern, trace, pin and turn in front of everyone; count the matches in a full turn together; then show a mirror held on a line that reflects the pattern into itself.

## By band

- **K–1:** spin-point hunt on two or three bold patterns; put a coloured sticker on each spin point by how many matches it makes (2, 3, 4 or 6); sort samples into "has a 4-spin" and "does not". Then stamp a pattern by turning a stamp a quarter at each corner and find its spin points. No reading beyond the sticker key.
- **2–3:** on every sample, find all the kinds of spin points and mirror lines; make a wallpaper with a stamp that has a 3-spin but no mirror; then try to build a pattern with a 5-spin from paper regular pentagons (three pentagons leave a 36° gap). The facilitator should say plainly that the pentagon failure motivates the restriction but is not its proof, since a 5-fold spin could in principle come from other shapes.
- **4–5:** the price list game. Spin points cost beads from a purse of 24: a 2-spin costs 6, a 3-spin 8, a 4-spin 9, a 6-spin 10 (these are (n − 1)/n of 12). Find every way to spend exactly 24 (2222, 333, 442, 632) and match each to a sample. Then the shortest-slide proof drawn with arrows: why a 5-spin or 8-spin would make a slide shorter than the shortest one. Optional: add mirrors and glides to the price list and check the samples' full signatures.

## Checked facts

Computed in `check_symmetry_games.py`, `check_week_115()`:

- enumerating Conway signatures with total cost 2 gives exactly 17: o, 2222, 333, 442, 632, *2222, *333, *442, *632, 4*2, 3*3, 2*22, 22*, **, *x, xx, 22x;
- with prices 6, 8, 9, 10 the ways to spend exactly 24 are 2+2+2+2, 3+3+3, 4+4+2, 6+3+2;
- 2cos(360°/k) is an integer only for k = 1, 2, 3, 4, 6 (k up to 24);
- the shortest-slide argument: some t ± (t turned) is strictly shorter than t for k = 5 and 7 to 12, never for 2, 3, 4, 6; for k = 5 the short slide has length about 0.618;
- only triangles, squares and hexagons fit around a point; three pentagons leave 36°.

Cited, not computed: the classification (17 groups, Fedorov 1891, Pólya 1924) and the proof of the magic theorem.

## Nearest existing themes

Week 35 (Footprint borders) classifies frieze patterns, which slide in one direction only (7 types); this week is its two-dimensional sequel and should reuse its footprint stamp and slide/flip/glide vocabulary. Week 1 and 1e (tiling) use pattern blocks but not the symmetry of the tiling; Week 34 (Hidden turns) and Week 37 (Mirror twins) study turns and mirrors of finite objects. New here: two independent slides, the crystallographic restriction (a real impossibility theorem children can see), and the cost-adds-to-2 accounting. The draft for Week 116 (kaleidoscopes) produces three of the 17 (*333, *442, *632) from triangle mirrors and could run as its return visit.

## App connection

Patterns and symmetry. A "Wallpaper workshop" family extending Footprint borders from a strip to the plane: the child drops spin pins and mirror lines on a pattern and the app animates the move, accepting it when the pattern lands on itself. Example puzzles: "Pin every kind of spin point in this pattern (there are three kinds)"; "Edit the motif in one cell so the pattern keeps its 4-spins but loses every mirror". A purse puzzle (spend exactly 24 beads on spin points) has four answers and an easy checker. Fit B: a new mechanic, clear checkable solves.

## Open questions

- Can K–1 children manage tracing paper and a pin without an adult doing the turning? Rehearse with one child.
- Sample choice: patterns must be large enough to trace and must cover several groups, including at least one with a 3-spin and one with a glide; the volunteer may need a printed set rather than found gift wrap.
- The orbifold "same kind of point" idea is probably adult-only; the full signature task should stay an optional 4–5 extension.
- Whether the price list should use beads (whole numbers) or fractions for 4–5.
