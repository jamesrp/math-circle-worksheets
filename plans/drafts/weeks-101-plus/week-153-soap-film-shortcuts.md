# Week 153 (draft plan): Soap-film shortcuts

**Strand:** networks and shape (Maps and networks; Shapes and spaces). **Deep-math field:** geometric optimisation (Steiner trees, the Fermat point), minimal surfaces. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

To join given towns by roads of least total length, it can pay to add new junctions (Steiner points). In the shortest network the roads form a tree, every new junction has exactly three roads meeting at 120 degrees, two roads meeting at a town make an angle of at least 120 degrees, and n towns need at most n − 2 new junctions. For three towns whose triangle has all angles below 120 degrees, the best junction is the Fermat (Torricelli) point, where the three roads meet at 120 degrees; if one angle is 120 degrees or more, the best network is just the two sides at that corner. For an equilateral triangle with side 1, the two sides cost 2 and the Fermat network costs √3 ≈ 1.732; for a unit square, a spanning tree of three sides costs 3, the two diagonals 2√2 ≈ 2.828, and the best network 1 + √3 ≈ 2.732, with two junctions, and there are two such best networks (turned a quarter turn). Soap films between two parallel plates joined by pegs pull themselves short, so they show networks with 120-degree junctions; but a film settles into a locally shortest network, not always the shortest, so physical experiments suggest and illustrate rather than prove. Finding the shortest network is NP-hard as the number of towns grows. The Steiner ratio asks how much junctions can ever save: Gilbert and Pollak conjectured that the shortest network is never shorter than √3/2 ≈ 0.866 times the cheapest network without new junctions (equality for the equilateral triangle). Du and Hwang announced a proof in 1990, but a serious gap was later found, and current surveys treat the conjecture as open; it is proved for up to six towns, Chung and Graham (1985) proved a lower bound of about 0.824, and a 2026 conference paper claims a computer-certified bound of 0.8559. Children can discover that a middle junction beats any two sides, that the junction angles all look the same, and that soap sometimes finds a worse network than a cleverer drawing.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Steiner trees and spanning trees in six-pin soap films](https://arxiv.org/abs/0806.1340) — Prasun Dutta, S. Pratik Khastgir, Anushree Roy, arXiv 0806.1340, 2008 (read in full at ar5iv). Two parallel transparent plates about 1 cm apart joined by pins; films give Steiner trees with 120-degree junctions, but also longer, non-minimal trees depending on withdrawal and pin thickness; cites Courant and Robbins (read November 4, 2026).
- [The Steiner Minimal Tree](https://thatsmaths.com/2015/01/29/the-steiner-minimal-tree/) — ThatsMaths blog, January 29, 2015. Fermat point and the 120-degree rule, at most n − 2 Steiner points (Gergonne), two optimal networks for the square, soap films finding local minima, NP-hardness, and the gap in Du and Hwang's 1990 proof (read November 4, 2026).
- [Open problems on Steiner trees and maximal distance minimizers](https://arxiv.org/html/2511.18217) — Yana Teplitskaya, arXiv 2511.18217, November 2025. The Gilbert–Pollak conjecture (√3/2) is still open; 120-degree junctions and angles of at least 120 degrees (read November 4, 2026).
- [Towards Solving the Gilbert-Pollak Conjecture via Large Language Models](https://arxiv.org/html/2601.22365v2) — Yisi Ke, Tianyu Huang, Yankai Shu, Di He, Jingchu Gai, Liwei Wang, ICML 2026. Claims a certified lower bound 0.8559, improving Chung and Graham's 0.824 (1985); lists the cases proved for 3 to 6 points (read November 4, 2026).
- Prior use with children: [Mathematical Bubbles](https://u.osu.edu/ohio4hstem/2021/03/14/mathematical-bubbles) — Ohio 4-H STEM, tagged K–2 and 3–5, 30 minutes: wire-frame soap films and Plateau's three-city road problem with two plexiglass sheets joined by screws (read November 4, 2026).

## A kid-friendly way in

Two clear plastic sheets (cut from report covers or acrylic offcuts) held about 1.5 cm apart by bolts or dowels at the "towns", dipped in a tray of dish soap, water and a little glycerine; the film shows a road network between the pegs. On paper, the same towns as dots on a board with string and a ruler. Prep: make three or four frames (three towns as an equilateral triangle, a flat triangle with a wide angle, a square, a 2-by-1 rectangle), mix the solution; about 30 minutes, best done the evening before. Launch (2–3 minutes): three pegs on a board, two children each measure a string road joining all three, then dip the triangle frame and compare its shape with theirs.

## By band

- **K–1:** dip frames and draw what the soap makes; with string, join three pegs and compare the string used for "two sides" against "meet in the middle" by laying both strings side by side.
- **2–3:** for three towns, find the shortest middle junction by measuring (a protractor or a 120-degree card template helps); find the flat triangle where no junction helps; for the square, compare two sides plus one, the two diagonals, and the soap's network.
- **4–5:** explain why the angles must be equal (if one angle were smaller, sliding the junction shortens the roads); predict where junctions go for the rectangle and check against soap; meet a frame where the soap finds a worse network, and discuss why soap cannot prove a network is shortest.

## Checked facts

Computed in `check_networks_counting_2.py`, `check_week_153()`:

- equilateral triangle side 1: two sides 2, Fermat network √3 ≈ 1.732, ratio 0.866;
- triangle (0,0), (4,0), (1,3): Fermat point found numerically, all three angles 120 degrees, saves about 0.621 on the two shortest sides;
- flat triangle (0,0), (6,0), (3,1): angle at the top over 120 degrees, best junction is that corner;
- unit square: spanning tree 3, diagonals 2.828, best 1 + √3 ≈ 2.732 with all junction angles 120 degrees; both pairings equally good; ratio 0.911;
- 2-by-1 rectangle: best 2 + √3 ≈ 3.732 against spanning tree 4; pairing the long sides instead collapses to 4.472.

With pegs 10 cm apart these become 20 cm against 17.3 cm (triangle) and 30 cm, 28.3 cm and 27.3 cm (square). Cited, not computed: the n − 2 bound, NP-hardness, and the Steiner ratio results.

## Nearest existing themes

Week 53 (cheapest connected networks) chooses among given links only, and its research notes say "No Steiner points or unprinted new links are allowed"; this week is exactly the move Week 53 forbids, and the two should be named as a pair. Week 21 (shortest route touching a line) uses reflection to find a shortest path, Week 15 (nearest-site regions) has three regions meeting at a point, and Week 78 (three-armed lines) has tropical curves with three-armed junctions. New here: adding points to shorten a network, the 120-degree rule, physical minimisation by soap and its limits, and an open conjecture.

## App connection

Maps and networks: a "shortcut roads" family where the child places junctions and drags them, the app shows the total length and turns a junction green when it is at 120 degrees; puzzles ask to beat a given length, or to decide whether any junction helps. Week 53's cheapest-network family could offer a "now you may add junctions" second stage.

## Open questions

- Frame construction: whether a parent volunteer can make reliable frames without a drill (dowels glued to sheets, or clear cups and pins), and how far apart the plates should be.
- The status statements (Steiner ratio open, the 2026 bound, the exact 1985 bound) should be rechecked before publication; Teplitskaya's survey and Ke et al. quote different figures for the best bound since 1985.
- Whether 2–3 can measure angles well enough to see 120 degrees, or should compare with a cut-out three-armed template.
