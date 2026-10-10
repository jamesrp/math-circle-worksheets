# Week 54: Partitions and rebuilding

**Verdict: keep.** No must. Children reach Euler's odd-equals-distinct theorem by physically joining and halving strips, every answer checks, and the guide is at the bar. The missing K–1 route is a should, as on the Week 60, 62 and 76 cards: the outline says "K–1: no standalone packet recommended", and no adult is left stuck.

Reviewed October 10, 2026 by Claude, with the math check in [week-54-math.md](week-54-math.md). Packets: week-54-students.pdf, W54-S-v1, 9 pages (pp. 1–5 Grades 2–5, Problems 1–5; pp. 6–9 Grades 4–5, Problems 6–9). Adult guide: week-54-facilitator.pdf, W54-FAC-v1, 8 pages. Companions noticed but not reviewed: none exist. Status: unpiloted. It was written October 4 under the 52–63 routing, which allows Grade 3–5-only themes.

## The mathematics

A collection is a partition: unordered strips adding to a total. Joining equal pairs turns an only-odd collection into one with all sizes different, and halving even strips undoes it. Each odd size u keeps its own family u, 2u, 4u, …, and within a family the pairing is forced. So the order of joins doesn't matter (P6), both round trips return (P4), and the two catalogs match for every total (P5, P9). Separately, exchanging rows and columns is an involution that swaps "at most k strips" with "sizes at most k" (P7–P8). A mathematician would enjoy both.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Two genuine bijections. The domain is respected (P4's inputs all differ), and order-independence is posed as a question. |
| Problems | strong | The cases contrast. Nine 1s carry to (8,1); (5,5,3,3,3,1,1) leaves one 3; (5,3,1) needs no join; (12,6,3) halves to seven 3s. P7 has the rectangle (4,4) and P8 the self-conjugate (3,3,2). P3 is execution, and P7 is light. |
| Student pages | strong | Spec header and footer, no slop, rules stated once. Non-task worked visuals come before P1, P3, P4 and P7. Spare boxes hide the counts: 6 for 5 and 8 for 7 (P1), 8 for 6 (P5), 12 for 10 (P8). |
| Concreteness | strong | Cubes hold every state, and each starting state is printed so it can be rebuilt. A partner checks joins side by side. The launch on guide p. 3 is whole-group: 2 + 1, reordering, a split. Loose squares would weaken this (fix 2). |
| Correctness | strong | math.md finds no failures and no diagram mismatches, and my own checks of P1–P8 agree. I accept both of its guide findings (fixes 3 and 4). |
| Adult guide | strong | Theorem-first p. 1 with hypotheses, limits, a band map and evidence levels. Keys with completeness arguments, held hints, a launch, a timetable, kit counts, pretests, and a uniqueness proof without binary. |
| Age fit, K–1 | weak | No route in this theme. Guide p. 2: "K–1 resumes Week 1 Problem 1 (sailboat/cat) or Problem 2". |
| Age fit, grades 2–3 | strong | Short rules third graders can read. Counting to 24 and halving to 12. The page holds each before-state. P5 comes late. |
| Age fit, grades 4–5 | strong | P6 and P7 are concrete; P8's rule and P9's proof come last. The guide's first hour keeps this table on pp. 1–4, which may go quickly (prediction). |

## Keep

- p. 1's three rules and the 3-unit visual (loose strips, longest first, "2 + 1"); P1.
- P2's chosen total and two separate catalogs, so "odd" and "different" never merge and equal counts are left to notice.
- The p. 3 and p. 4 visuals; P3's and P4's cases; "Does each starting collection return?"
- P5's eight box pairs for six pairs. P6 as revised ("until all sizes are different", then "from any all-odd collection").
- p. 7's column outlines labelled 4 3 3 1 1; P7, P8's twelve rows, P9.
- Guide: the overview, the launch, the P2/P5/P8 completeness arguments, P6's two checked routes, the p. 6 proofs, the pretest list.

## Fix

1. **should**, K–1, guide pp. 1–2: "K–1 has no Week 54 packet." The K–1 table joins the strip launch, then tiles Week 1 boards. P1, P3's nine ones and the odd check by pairing are cube work a non-reader can do, and the outline proposed "an adult-supported entry". Head pp. 1 and 3 "Grades K–5". Route K–1 through P1 (the parent records sizes), P3's first and third cases, and P2's odd side at total 6. Add two 12-cube kits. That K–1 sustains this is a prediction.
2. **should**, guide p. 2, kit and pretests: "unit squares or snap cubes … use loose touching squares if necessary". Loose strips touching end to end look like one strip, so a join leaves no trace and P4's ten-strip state scrambles easily (prediction). Specify linking cubes. Standard 2 cm cubes fit: the longest strip, 12, is 24 cm.
3. **should**, guide p. 4, P3 bridge: "(3, 3, 1, 1, 1, 1) has one legal join 3 + 3 → 6". The ones can be joined first too (math.md item 1). An adult may stop a child who joins them first, just before P6 asks whether order matters. Write "one legal join is".
4. **could**, guide p. 4, P2: say why largest size 3 fails for 7 (3 + 2 + 1 = 6), per math.md item 2.
5. **could**, p. 1: "Use all the units in a collection of straight strips" → "A collection uses all the units, in straight strips."
6. **could**, p. 6, P6: the words "four 3-unit strips and six 1-unit strips" repeat the picture beside them, and "all-odd" should read "only odd sizes".
7. **could**, p. 7, P7: the grid cells are 4.6 mm, smaller than the 5.6 mm input squares. 5×5 grids at 6.5 mm hold every result.
8. **could**, p. 9, P9: "Explain how joining and splitting can decide this" names the method. "Explain why." does not.
9. **could**, P4: add (6,6,1), which comes back as (12,1), as a contrast for 4–5, and drop "again".
10. **could**, guide p. 8: "guide-src/check_answers.py" is guide/check_answers.py.

## Overlaps

Week 38 lists the partitions of four in passing. Week 30 shares the uniqueness of a power representation behind P6, but in base 3. Week 12 is the other bijection theme, on Catalan objects. None takes partitions or Euler's theorem as its object. No merge.

## App fit

Fit B, size M, confirmed. The app gives a strip workbench: tap two equal strips to join them, or an even strip to halve it. The app refuses unequal joins, which paper can't. A free mode cuts anywhere for unrestricted catalogs.

- **Catalogs (P1, P2, P8):** every collection to total 8, odd-only or all-different to about 12, at most k strips. Point to the existing copy of a duplicate. The child declares "done", with no visible count.
- **Matching (P5):** pair each odd collection with its partner by joining it.
- **Reach or refute (new):** reach a target by joins and halvings, or show it can't be done. The certificate is that halving everything gives different odd collections. For totals 10–16, my search found 12–21% of reachable pairs need both kinds of move, such as (8,1,1,1,1,1,1) → (2,2,2,2,2,2,2) in 6. Use those for Hard, against Plume.

Pitfalls: "predict the final collection", because joining is forced and that is the theorem; auto-running joins; visible counts. Exchange is one tap, so use it only inside P8's catalog. Leave P6's general question and P9 on paper.

**Decision, October 10, 2026.** Port, in Wave 7 (sets and numbers): the strip workbench above, with catalogs the child declares complete and reach-or-refute targets whose "can't" certificate is the two halved, all-odd collections. The missing K–1 route stays a should, following the Week 60, 62, 69 and 76 cards, where the design records no K–1 edition; the Week 53 and 63 musts were K–1 bands that exist but are too thin. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported. The source README says "These adaptations are unpiloted", and guide p. 2's cube pretests have not been run.
