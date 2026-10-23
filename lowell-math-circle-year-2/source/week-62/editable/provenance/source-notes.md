# Week 62 research and provenance

Prepared October 4, 2026. Research/outline stage only; no student or adult PDF is authored by this stage. The library contains established mathematics, not claims of newly invented theorems. Draft classroom adaptations, preparation estimates and physical procedures remain unpiloted and unrehearsed.

## Mathematical source trail

- Eric Lehman, F. Thomson Leighton and Albert R. Meyer, *Mathematics for Computer Science*, revised June 6, 2018, MIT. [Primary PDF](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf), local `external-resources/new-themes-52-63/week62-63/mit-6042-mathematics-for-computer-science-2018.pdf`. Section **12.6.1**, printed **pp. 514-516** (PDF **pp. 522-524**), explicitly models pairwise scheduling conflicts by edges and time slots by vertex colors. Section **12.6.2**, printed **pp. 516-517** (PDF **pp. 524-525**), includes complete graphs, cycle bounds and **Theorem 12.6.3**, the maximum-degree-plus-one upper bound. The outline's first-fit failure on P4 is an independently constructed and checked example, not the source's scheduling diagram or its star example.
- Alan Frieze, CMU Discrete Mathematics, **D18, “Paths, Walks and Bipartite Graphs,” “Characterisation of bipartite graphs,” Theorem 1, pp. 8-10**. [Primary PDF](https://www.math.cmu.edu/~af1p/Teaching/DM/D18.pdf), local `cmu-frieze-D18-bipartite.pdf` in the same reference folder. It proves bipartiteness iff there is no odd cycle, component by component, using BFS layers. Source definitions of paths and cycles are on pp. 1-2. This gives the general theorem beyond ring alternation.
- MIT 18.310, **Lecture 14, “Some Graph Theory,” Section 1, “Definitions and Perfect Graphs.”** [Primary HTML](https://math.mit.edu/~djk/18.310/Lecture-Notes/some_graph_theory_2007.html), local `mit-18310-some-graph-theory-2007.html`. The paragraphs immediately following the clique-number definition state the clique lower bound and its strictness for odd cycles of length at least five. Later perfect-graph material is adult context, outside this outline's core.
- Igor Pak, MIT 18.315, Spring 2005, notes by Amanda Redlich, **Lecture 9, p. 1**, definition and first theorem/proof under “Chromatic Polynomial.” [Primary PDF](https://ocw.mit.edu/courses/18-315-combinatorial-theory-introduction-to-graph-theory-extremal-and-enumerative-combinatorics-spring-2005/d1f49cd743278b91cb580542cc51bc3b_lec09.pdf), local `mit-18315-lec09-chromatic-polynomial.pdf`. It gives counting with named colors and deletion-contraction. The local path and diamond formulas are derived by choosing colors at their vertices and verified by enumeration; no source figure is reused.

The downloaded Lecture 4 note was inspected but is **not** relied on for the first-fit upper bound: its opening is a recoloring-connectivity theorem, despite “Greedy Algorithm” in the course index. This avoids overstating what that page actually proves.

## Precise facts and finite checks

`verify.py` is standard-library code independent of a future worksheet builder. It exhausts all color assignments for seven explicit graphs and separately compares BFS, exhaustive two-colorings, and exhaustive odd-simple-cycle search for all **1,099 labeled simple graphs on one through five vertices**. It writes `small-instances.json`; run `python3 plans/new-themes-52-63/week-62/verify.py` from the repository root.

| Graph, with fixed vertex labels | Edges | Minimum colors | Largest clique | Named 3-colorings |
|---|---|---:|---:|---:|
| P4 | AB, BC, CD | 2 | 2 | 24 |
| C4 | AB, BC, CD, DA | 2 | 2 | 18 |
| Diamond | AB, AC, BC, AD, BD | 3 | 3 | 6 |
| K4 | every pair of A,B,C,D | 4 | 4 | 0 |
| K2,3 | every pair from A,B to C,D,E | 2 | 2 | 30 |
| C5 with a leaf | AB, BC, CD, DE, EA, AF | 3 | 2 | 60 |
| C4 with one diagonal | AB, BC, CD, DA, AC | 3 | 3 | 6 |

P4's first-fit order A,D,B,C uses 3 colors; the optimal bipartition is {A,C}/{B,D}. Exhausting all 24 vertex orders supplies an extra check on the procedure, not an assigned student catalog. A proper coloring is an upper bound, a clique/odd cycle is a lower-bound certificate, and a matching pair proves the minimum. The finite code check does not prove the theorem for arbitrary n; the source proof does. Loops are excluded, parallel edges add no new restriction, and edge crossings in a drawing do not add a vertex unless explicitly marked.

## Actual prior-packet overlap

The current `BONUS-AND-RETURN-VISITS.md` and `WEEKS-11-51.md` were read; relevant final student PDFs were text-extracted and every page of the targeted student packets was rendered and inspected. The extracted notes and 51-page contact review are in `tmp/worksheet-runs/week-62-new-v1/prior-review/`. This is a targeted novelty assessment; root's collection-wide inventory supplies broader coverage.

- **Week 14 return visit, student pp. 3-4, Problem 2** already colors triangulation corners with three colors so each triangle has all three, then seeks a minimum corner cover. Its adult p. 1 proves the special three-color construction and the smallest-class cover. General proper vertex coloring is therefore not a novel term or action on its own.
- **Week 33 bonus, student pp. 2-3, Problems 2-3** already asks for two-color rings and all proper three-color five-rings up to rotation. The adult **p. 3** gives the even/odd obstruction, six rotation classes, 30 fixed-position words, and the general cycle-coloring formula. **Week 35 bonus**, indexed as closing an alternating necklace, is another related ring entry. A simple ring, parity alone, or its count does not distinguish Week 62.
- **Week 36 bonus, student p. 2, Problem 2**, already compares two and three ownership colors avoiding monochromatic allowed triples; adult pp. 1-2 explains the cap bound. Those constraints are on **triples**, not pairwise graph edges. It is not the proper graph coloring/scheduling theorem, but reuse of “two versus three colors” alone would be shallow.
- **Week 19** base and bonus packets were also inspected as relevant set/graph-adjacent background. Their containment, pairwise intersection, complement and chain arguments do not investigate arbitrary pairwise conflict scheduling or the first-fit ordering gap.

The distinct core is minimum simultaneous slot assignment on **arbitrary pairwise conflict networks**, general odd-cycle certificates in networks with branches/chords/components, and **first-fit order versus optimum**. Use C5-with-leaf for the clique gap and non-ring networks throughout. Optional path/diamond assignment counts provide a new graph family; counting ring colorings alone does not.

## Local teaching precedents and proposed adaptation

Actual local source: Givental, Nemirovskaya and Zakharevich, *Math Circle by the Bay*, **Preface printed pp. viii-x (PDF pp. 9-11)**. The authors choose themes with mathematical depth, supply manipulatives, encourage independent attempts and explanations, and vary depth and pace rather than prescribing one timing for all groups. Actual local source: Rozhkovskaya, *Math Circles for Elementary School Students*, **Lesson 7, “At the lesson,” item 1**, EPUB `OEBPS/part0017.xhtml`, reports unexpected game outcomes probably caused by missed legal moves. **Lesson 8, “At the lesson,” item 2**, `part0018.xhtml`, reports uneven copying/coloring times and reduced transcription for a later table.

Our inference: use fixed endpoint conflict marks and a partner who checks every edge; give several meaningful graph structures before abstraction; preserve one candidate coloring instead of maintaining several tallies. These are proposed adaptations, not classroom evidence from the books. In the organizer's actual prior-year **Handouts 7, Problems 7.2-7.3**, pairwise handshakes model every pair and adding one participant; **Handouts 6, Problems 6.2-6.6** connects concrete arrangements and representations. These are local format precedents, not sources of the new scheduling tasks. The current worksheet context, October 3, gives eleven children at fixed KK11 / 3333 / 445 tables and one anchored adult per table; it takes precedence over README's older September 28 count.

## Novelty and band recommendation

**Proceed as a substantive Grades 2-5 theme.** Entry requires matching vertex/card labels, retaining pairwise endpoint restrictions, and counting through eight; adult reading is routine assistance. Older continuations require certificates and following an ordering, with small products only for optional counting. K-1 can try placements with adult reading if children retain the rule, but full K-1 coverage is not recommended. Do not claim a new K-1 investigation merely by repeating ring alternation.

`outline.md` follows the workflow template (kernels, one-line band emphases, materials/physical constraints) without prescribed numbered problems. The generator and prompt blocks were not edited. Root's `../STAGE-ROUTING.md` applies one combined `students.pdf` output with honest page headers. Read `REPUBLISHING.md`; new wording and figures must be original, and source ZIPs should omit generated workflow prompts and borrowed exemplars. No existing packet, global index, AGENTS.md or republication note was modified by this stage.
