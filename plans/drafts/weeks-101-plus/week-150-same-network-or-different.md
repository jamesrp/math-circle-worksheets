# Week 150 (draft plan): Same network or different?

**Strand:** networks (Maps and networks). **Deep-math field:** graph theory (isomorphism, invariants), complexity of algorithms. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Two drawings show the same network (are isomorphic) when the dots of one can be renamed as the dots of the other so that two dots are linked in the first exactly when their new names are linked in the second; where the dots sit and how the links bend do not matter. An invariant is any count that every renaming keeps: the number of dots and links, the list of how many links meet at each dot (the degree list), the number of triangles or four-link loops, whether the network is in one piece. A difference in any invariant proves two drawings are different networks. Equal invariants prove nothing: a hexagon and two separate triangles both have six dots each with two links, but only one has triangles; the cube network and an 8-ring with its four diameters (the Möbius ladder) both have 8 dots, every dot with 3 links and no triangles, yet the cube has 6 four-link loops and the ladder has 4; two six-bead trees with the same degree list (3, 2, 2, 1, 1, 1) differ because the three-link dot touches two leaves in one and one leaf in the other. To prove two drawings are the same, show a renaming that works. Checked by computer here: the numbers of different networks on 1 to 5 dots are 1, 2, 4, 11, 34, and the 125 labelled trees on 5 dots and 1296 on 6 dots fall into 3 and 6 shapes. No short list of invariants is known to decide sameness in general: colour refinement (repeatedly sorting dots by their neighbours' colours) separates almost all networks but cannot separate any two regular networks of the same size and degree (Grohe and Neuen). Whether sameness can be decided in polynomial time is open, and it is not known to be NP-complete; Babai (2015) gave an algorithm running in quasipolynomial time, exp((log n)^c), the first big improvement on Luks's 1983 bound (Babai found and repaired an error in January 2017). Children can discover that a pentagon and a five-pointed star are the same network, that matching counts are a useful first test but not a proof, and that a renaming is the proof of sameness.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Graph Isomorphism in Quasipolynomial Time](https://arxiv.org/abs/1512.03547v2) — László Babai, arXiv 1512.03547, December 2015, v2 January 2016. The quasipolynomial bound and the previous best exp(O(√(n log n))) from Luks 1983 (read November 4, 2026).
- [Algorithm Solves Graph Isomorphism in Record Time](https://www.quantamagazine.org/algorithm-solves-graph-isomorphism-in-record-time-20151214/) — Erica Klarreich, Quanta Magazine, December 14, 2015. Plain-language statement of the problem, its open status (not known in P, not known NP-complete), and the note on the January 2017 retraction and repair (read November 4, 2026).
- [Recent Advances on the Graph Isomorphism Problem](https://ar5iv.labs.arxiv.org/html/2011.01366) — Martin Grohe and Daniel Neuen, arXiv 2011.01366, 2020. Colour refinement identifies almost all graphs but cannot distinguish regular graphs of equal degree and size; the complexity of the problem is a major open question (read November 4, 2026).
- [Comparing Graphs](https://oer.xyzhomework.com/ebooks/html/contemporary-math/ch12/12-3-comparing-graphs.html) — adapted from OpenStax, Contemporary Mathematics, section 12.3. A textbook treatment of invariants as quick difference tests, with an example of two graphs with equal degree counts that are still different (read November 4, 2026).
- Prior use with children: none found for K–5. Searches for math circle, NRICH and JRMF activities on "same graph" and graph isomorphism found a Waterloo CEMC grade 7–8 math circle lesson (could not be opened, so not cited) and the [Plus maths minute](https://plus.maths.org/content/maths-minute-graph-isomorphism-problem) (Plus magazine, January 18, 2017), which uses the London tube map against a geographic map as the example of one network drawn two ways (read November 4, 2026).

## A kid-friendly way in

String-and-bead networks: wooden beads (or paper fasteners on card) tied together with short strings, so a network can be picked up and laid down in a new shape without changing who is joined to whom. Then a deck of drawn networks, three or four drawings of each of several networks, to sort into same-network families. Prep: tie four or five bead networks (pentagon, five-pointed star, two six-bead trees, hexagon), print and cut a 24-card deck; about 25 minutes. Launch (2–3 minutes): hold up a bead pentagon, drop it on the table as a crumpled tangle, then lay it out as a star; ask whether it is still the same network, and show that every bead still holds the same two strings.

## By band

- **K–1:** rearrange a bead network to match a drawing, then decide by trying whether a second bead network can be laid out to match it. Count strings at each bead with stickers as a first "same or different" check.
- **2–3:** sort the deck of drawings into families; for two cards in different families, find a count that proves the difference (links, dots with three links, triangles). Meet a pair where every count agrees and the drawings still differ.
- **4–5:** prove sameness by writing a renaming (letters on one drawing, numbers on the other) and checking every link; find all 6 tree shapes on 6 beads and argue none is missing; discuss why trying all 720 renamings of six beads is slow and how counts cut the search.

## Checked facts

Computed in `check_networks_counting_2.py`, `check_week_150()`:

- networks on 1 to 5 dots: 1, 2, 4, 11, 34; the 64 drawings on 4 labelled dots fall into 11 families;
- labelled trees n^(n−2): 16, 125, 1296 on 4, 5, 6 dots, in 2, 3 and 6 shapes;
- pentagon and five-pointed star are the same network;
- hexagon versus two triangles, K3,3 versus the triangular prism, cube versus Möbius ladder (four-link loops 6 versus 4), and the two spider trees with degree list (3, 2, 2, 1, 1, 1): equal degree lists, different networks;
- renamings to try: 120 for five beads, 720 for six.

Cited, not computed: Babai's bound, the open complexity status, and the colour refinement facts.

## Nearest existing themes

The scouting draft untangling-networks uses the same physical move (drag dots, links follow) to ask whether crossings can be removed; this plan uses it to ask whether two drawings are one network, so the two share a launch and should be scheduled apart or as a pair. Week 10 counts links at each island (the degree idea), Week 52 and 53 meet trees, Week 37 counts labellings up to symmetry, and draft Week 103 names an isomorphism between tower maps and Sierpiński graphs. New here: sameness as the existence of a renaming, invariants as one-way proofs, the six tree shapes, and an honest open problem in computing.

## App connection

Maps and networks: a "same network?" family. The child drags dots of one drawing (links follow) to make it look like a target, or taps "different" and must point to a count that differs (the app highlights a three-link dot, a triangle). A second puzzle type gives a renaming table to fill so that every link checks. The untangling family, if built, could share the drag engine.

## Open questions

- Whether K–1 can keep strings untangled enough to compare; card networks with brass fasteners and paper strips may be easier than beads.
- How large the deck should be: 4-dot networks (11 families) are small but some are dull; six-bead trees (6 families) may be the better main deck.
- Whether a pair with equal counts but different shape (cube versus Möbius ladder) is too hard to see at 8 dots for grades 2–3.
