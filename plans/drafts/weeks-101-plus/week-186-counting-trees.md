# Week 186 (draft plan): How many trees on numbered pegs?

**Strand:** networks (Maps and networks), with counting. **Deep-math field:** enumerative combinatorics (labelled trees, bijections, symmetry). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot. **Overlap warning:** the Prüfer-code core of this topic is already atlas family AD-04, and its counts appear in AD-05 and drafts 107 and 150; this plan proposes a different angle and recommends using it as a return visit, not a new week.

## The deep idea

Cayley's formula (stated by Cayley in 1889; Borchardt had it earlier): the number of trees on n numbered points (networks with n − 1 links, all points joined, no loop) is n^(n−2): 1, 3, 16, 125, 1296 for 2 to 6 points. Prüfer's code (1918) proves it by a one-to-one match with words: remove the smallest-numbered leaf, write down its neighbour, repeat until two points remain; the word has n − 2 letters from n labels, every word comes from exactly one tree, and each label appears (its number of links − 1) times. A second route counts by shape. A tree shape with s symmetries (ways to move its pegs that keep it the same drawing) can be numbered in n!/s different ways, and adding over shapes must give n^(n−2): on 4 points, the path (2 symmetries) gives 24/2 = 12 and the star (6) gives 4, so 16; on 5 points, path 60, fork 60, star 5, so 125; on 6 points six shapes give 6, 90, 120, 360, 360 and 360, so 1296. Why these sums always land on a power of n is the theorem, not the computation: Feldman (2024) gives a proof that builds trees path by path and uses only the distributive law, and Joyal's proof matches "everyone points at someone" pictures (n^n of them) with trees that have a chosen start and finish (n^(n−2) · n · n). Proved for all n by several methods. Checked here: n^(n−2) by listing all trees for n ≤ 7, the shape sums for n = 4, 5, 6, and the Prüfer match for n = 4, 5, 6. Children can discover that the same shape can be numbered many ways, count those ways by symmetry, and see the totals 16 and 125 appear.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Cayley's Formula](https://mathcircle.berkeley.edu/sites/default/files/handouts/2021/Caleys_Formula_Espen_Slettnes.pdf) — Espen Slettnes, Berkeley Math Circle handout, February 3, 2021. Five proofs (double counting, birooted trees and functions, matrix-tree theorem, Prüfer sequences, parking functions) and the exercise to verify n = 1 to 5. Prior use with circle students, level not stated (read November 4, 2026).
- [Cayley's formula from middle school math](https://arxiv.org/html/2408.04676v1) — Victoria Feldman, arXiv 2408.04676, August 2024. A short proof that builds each tree from paths and sums over shapes with the distributive law (read November 4, 2026).
- Prior use with children: the BMC handout above (age not stated). No K–5 use found (searched circle handouts and classroom pages for Prüfer codes and counting labelled trees). The repository's own atlas family AD-04 (grades 2–3 and 4–5) is the nearest classroom-ready material.

The Cayley 1889 and Borchardt dates and Prüfer's 1918 are classical attributions not confirmed from a page read today.

## A kid-friendly way in

Pegs and straws. A board with 4 (later 5) numbered pegs, or numbered paper cups, and straws or pipe cleaners as links. Rule: use one straw fewer than pegs, and every peg must be reachable. Children build every different tree they can and lay each one on a recording card (a peg diagram to draw on). Then sort the cards by shape. Prep: peg boards or cups, straws cut to length, printed recording cards; about 20 minutes. Launch (2–3 minutes): three numbered cups; build a tree with two straws, then a second one, and ask whether the second is "different"; agree that it is different when a different pair of numbers is joined, not when it is turned.

## By band

- **K–1:** three cups (3 trees) and four cups with three straws: find trees, and sort them into "line" and "star" piles. Spot that three straws can also make a triangle that leaves a cup alone (not allowed).
- **2–3:** find all 16 trees on 4 pegs as a pooled class collection, sorted by shape: 12 lines and 4 stars. Why 4 stars (choose the middle)? Why 12 lines? Then 5 pegs by shape: how many stars, lines and forks?
- **4–5:** count numberings of a shape as 4! or 5! divided by its symmetries; total 125; then meet Prüfer's two-number message on 4 pegs (AD-04) as the proof that 16 is no accident.

## Checked facts

Computed in `check_networks_3.py`, `check_week_186()`:

- trees on 2 to 7 numbered points: 1, 3, 16, 125, 1296, 16807, each n^(n−2);
- 3 straws on 4 pegs: 20 choices, 16 trees and 4 triangle-plus-lonely-peg; 4 straws on 5 pegs: 210 choices, 125 trees;
- by shape: 4 points 12 + 4; 5 points 60 + 60 + 5; 6 points 6 shapes with 6, 90, 120, 360, 360, 360; each count divides n!;
- the Prüfer code matches trees and words one to one for n = 4, 5, 6; path 1–2–3–4 has code (2, 3), the star at 1 has code (1, 1); each label appears (links − 1) times (n = 5);
- 4^4 = 256 = 16 · 4 · 4 and 5^5 = 125 · 25 (Joyal's pointing pictures).

Cited, not computed: Cayley's formula for all n and Feldman's and Joyal's proofs.

## Nearest existing themes

This substantially overlaps existing material. Atlas AD-04 ("Send a whole tree in two numbers") is the Prüfer code on four labels with the 16 trees; AD-05 lists the spanning trees of a small network and notes that K4 has 16; draft 150 counts 16, 125 and 1296 labelled trees in 2, 3 and 6 shapes; draft 107 counts spanning trees of grid mazes; Week 53 prices trees and Week 12 proves counts by forced bijections. What would be new: counting numberings by symmetry (n!/s, the orbit idea of Week 37 and draft 162) and a K–1 straw entry, which AD-04 lacks. Recommendation: do not run this as its own week; use the pegs-and-shapes hour as a return visit that leads into AD-04, or fold the shape count into draft 150.

## App connection

Maps and networks (or Counting and arranging): a "tree catalogue" family. The child links numbered dots with n − 1 links; the app rejects loops and lonely dots, files each new tree into a shape drawer, and flags repeats. Puzzles: find all 16 four-dot trees; find the 5 five-dot stars; send a tree to a friend as two numbers (AD-04's code), and rebuild a tree from a message.

## Open questions

- Whether this should exist at all beside AD-04 and draft 150; the organizer should choose one home for labelled-tree counting.
- Whether 2–3 children see two drawings with the same joined pairs as "the same tree" without long discussion; a sticker-on-each-straw recording ("1–3") may settle it.
- The classical dates (Borchardt, Cayley 1889, Prüfer 1918) need a source read before any guide is written.
