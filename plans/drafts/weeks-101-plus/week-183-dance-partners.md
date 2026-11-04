# Week 183 (draft plan): Can everyone get a partner?

**Strand:** networks (Maps and networks). **Deep-math field:** matching theory, min–max duality. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Hall's theorem (Philip Hall, "On representatives of subsets", 1935): n children each list the partners (dance partners, helper jobs, seats) they will accept. Everyone can be paired with a different acceptable partner exactly when every group of children, taken together, accepts at least as many partners as the group has members. One direction is obvious: three children who between them accept only two partners cannot all be served. The surprise is the other direction: if no such "small group with too few friends" exists, a full pairing always exists, so the stuck group is a complete certificate of impossibility, as checkable as a pairing is a certificate of possibility. König's theorem (König and Egerváry, 1931) is the counting form: in a grid with some squares marked "acceptable", the most rooks that can sit on marked squares with no two in a row or column equals the fewest rows and columns that together cover every marked square. Both are proved for all sizes; each follows from the other, and both are special cases of max-flow min-cut (Week 13). A corollary children can test: if every child accepts exactly k partners and every partner is accepted by exactly k children (k ≥ 1), a full pairing always exists. A working method (proved): when a pairing is stuck, follow a chain that swaps partners along "accept, paired, accept, …" to free a partner; when no chain exists, the children reached by the search form the stuck group. Checked here on all 512 three-by-three and 65,536 four-by-four acceptance tables: a full pairing exists exactly when no group is short (247 and 37,823 tables have one), and König's equality holds on every 3-by-3 table and 2,000 random 5-by-5 tables. Children can discover that equal totals are not enough, find the stuck group, and fix a pairing by a chain of swaps.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Hall's marriage theorem](https://arxiv.org/html/2503.23159v1) — Peter J. Cameron, arXiv 2503.23159, 2025. Hall's 1935 paper in the *Journal of the London Mathematical Society*, the statement and inductive proof, König and Egerváry's 1931 matrix form, the equivalence with König's max matching equals min vertex cover, and earlier related work by van der Waerden and Sperner (read November 4, 2026).
- [Term rank](https://encyclopediaofmath.org/wiki/Term_rank) — Encyclopedia of Mathematics. The 0/1 grid form: the most 1s with no two in a line equals the fewest lines covering all 1s; reference to König, *Mat. Lapok* 38 (1931) (read November 4, 2026).
- [The Mathematics of Marriage](https://mattbaker.blog/2014/06/25/the-mathematics-of-marriage/) — Matt Baker, Matt Baker's Math Blog, June 25, 2014. The Halmos–Vaughan inductive proof, the 13-piles card solitaire application and links to max-flow min-cut (read November 4, 2026).
- Prior use with children: [Hall's Matching Theorem: warmups and followups](https://mathcircle.berkeley.edu/sites/default/files/handouts/2022/SMC-HallsMatchingTheorem--warmups-and-followups.pdf) — T. Malper, Stanford Math Circle, spring 2022, hosted by the Berkeley Math Circle; a high-school handout with a card-choosing warm-up, the rooks problem and König's regular case (read November 4, 2026). No K–5 use found (searched NRICH, JRMF and circle handouts for marriage, matching and distinct representatives).

## A kid-friendly way in

Partner mats. A printed mat shows children's faces on the left and partner animals (or job cards) on the right, with a drawn line for every acceptable pair. Children lay a paper clip or ribbon on lines to pair everyone, one clip per face and per animal. Some mats work, some do not. Prep: print 8 to 10 mats (sizes 4 and 5) and gather clips or ribbons; about 20 minutes. Launch (2–3 minutes): a 3-face mat on the board; a volunteer pairs two, gets stuck on the third, and someone swaps a pair to free a partner; then show a mat that cannot be done and ask how we could ever be sure.

## By band

- **K–1:** pair up on 3- and 4-face mats with clips; on a stuck mat, point to the faces that all want the same few animals ("these three only like these two").
- **2–3:** sort a stack of 5-face mats into "works" and "cannot", proving each: a full set of clips, or a ring drawn round a short group. Fix a stuck pairing by a chain of swaps. Design a mat where every face has two lines but it still fails.
- **4–5:** the rook grid. A 5-by-5 grid with marked squares: place the most rooks on marked squares with no two in a line, and cover all marks with the fewest whole rows and columns; find that the two numbers always match and that the cover proves the rook count is best. Test the "everyone exactly k" rule.

## Checked facts

Computed in `check_networks_3.py`, `check_week_183()`:

- Hall's condition matches full pairing on all 512 three-by-three and 65,536 four-by-four tables; 247 and 37,823 of them allow a full pairing;
- König's equality (most rooks = fewest lines) on all 3-by-3 tables and 2,000 random 5-by-5 tables;
- the plan's five-child example A {1, 2}, B {2}, C {1, 2}, D {3, 4, 5}, E {3}: no full pairing; the smallest stuck group is A, B, C; at most 4 pairs, matched by the 4 lines (columns 1 and 2, rows D and E); letting C also accept 4 fixes it;
- every 4-by-4 table where each row and column has the same number k ≥ 1 of marks has a full pairing.

Cited, not computed: Hall's theorem and König's theorem for all sizes.

## Nearest existing themes

Week 27 (Stable pairings) has full preference rankings and asks for stability; here acceptance is yes or no and the question is existence. Week 1's extension uses Hall's obstruction once (two spaces competing for one partner in a tiling) and its gem names Hall's theorem; draft 118 uses Hall's theorem inside the five-card trick only as an adult remark. Week 13 (Route packing and bottlenecks) is max-flow min-cut, of which König is the bipartite special case; the augmenting chain here is Week 13's change-walk, so run this after Week 13 or frame it as Week 13's sibling. Week 25 (Row and column shadows) also works in 0/1 grids, with a different question. New: the stuck group as a certificate, and the rooks-versus-lines duality in a grid.

## App connection

Maps and networks (or Codes and logic): a "partners" family. The child drags a link from each face to an animal; links light up only on accepted pairs. When stuck, the child can tap a group of faces, and the app shows how many animals that group accepts; a short group wins the "prove it cannot" star. Puzzle one: 5 faces, one stuck group of 3. Puzzle two: the rook grid, with a lines slider that must cover every mark.

## Open questions

- Framing: "marriage" is the classical name but children should see helpers and jobs, buddies or dance partners; check the organizer's preference.
- Whether 2–3 can search for a short group without adult prompting on 5-face mats; a 6-face mat may be too many groups to scan.
- How to show the chain of swaps physically (coloured ribbons that are moved one at a time) so it does not become a long recording task.
