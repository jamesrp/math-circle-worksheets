# Week 53 return visit: mathematical review of the draft

Reviewer: independent math check (CRITIC-MATH stage). I did not edit the draft.

## How I checked

- I read every map off the rendered pages and rebuilt it independently from the coordinates in `draft/src/*.tex`. For each map I recovered the place nodes, the link segments, every price label and, on K–1 pages, every dot. In all K–1 labels the number of dots matches the numeral. Every map carries the intended multiset of prices.
- I recomputed every answer with my own code and did not use `verify.py`. The code finds every cheapest network by brute force over all link subsets, with required places only, so it also covers the optional-place problems. It also lists all simple routes to find bottleneck values and cheapest trips, computes the groups as links open by price, does a breadth-first search over buy/return/swap moves for the stuck purchase, and enumerates the free-choice prices in 2–3 P6 and K–1 P7.
- I measured each label's distance to its own link and to the nearest other link from the TeX coordinates.

Every printed answer the pages rely on is correct as intended. The located problems are listed first. The verified answer key follows them.

---

## Located problems

### 1. Grades 4–5, pp. 2, 3, 4 and 6 (Problems 2, 3, 4 and 6): the general questions are false under the packet's own definition of a network

**Text.** The shared rules on p. 1 say: "A network is a set of bought links that lets the pawn walk on markers between every two circled places. A network may pass through places in squares or leave them out." The general questions then ask about "any map":

- P2: "Now take any two places on any map. Is the route between them along a cheapest network always a route whose most expensive link is as cheap as possible?" The intended answer is yes.
- P3: "Can two cheapest networks of one map use different prices? Can you tell the cost of a cheapest network from the groups, without choosing a network?" The intended answers are no and yes.
- P4: "Lee says that a network with no loop must be a cheapest network if, for every two places, no route on the map between them has a cheaper most expensive link than the route along the network. Is Lee right?" The intended answer is yes.
- P6: "Which ways of changing every price can change the cheapest networks of a map? Which can change its cheapest trips?" The intended answer is that adding to every price, doubling and squaring never change the cheapest networks.

**Evidence.** All four claims hold only when every place is circled. Once square places are allowed, as the packet's definition allows, the packet's own maps on p. 8 are counterexamples:

- **P2.** On P8's first map (spokes 3, triangle 4), the cheapest ways are the three pairs of triangle links, costing 8. Along AB+BC, the A–C route ABC has most expensive link 4. The route ASC on the map has most expensive link 3.
- **P3, first question.** On P8's second map (SA=SB=2, SC=4), the six cheapest ways include AB+BC with prices 4, 4 and SA+SB+SC with prices 2, 2, 4. These are different price lists.
- **P3, second question.** On P8's first map, the groups merge only at price 3, from 4 groups to 1. The group count therefore predicts 3 × 3 = 9, but the cheapest way costs 8.
- **P4 (Lee).** On P8's first map, take the network SA+SB+SC, which has no loop and costs 9. For every pair of the four places, its route has the lowest possible most expensive link: 3 for each pair of circles through S, and 3 for each spoke. Yet the cheapest way costs 8, so Lee's condition holds and the network is not cheapest.
- **P6, P8's second map.** Adding 2 to every price changes the cheapest ways from 6 to 3: only the triangle pairs remain, at 12.
- **P6, P8's first map.** Squaring every price makes SA+SB+SC (27) the only cheapest way, where before only triangle pairs were cheapest.
- **P6, P7's map.** Adding 2 creates a four-way tie at 12.
- **Smallest case.** With A and B circled, AB=5, AS=SB=2: the cheapest way is ASB (4). After adding 2 it is AB (7).

Doubling every price is the only one of the three changes that never alters a cheapest way when square places are allowed.

**Fix.** Restrict each general question to maps where every place is circled. For example:

- P2: "…on any map with no squares."
- P3: "…of one map with no squares…"
- P4: "Is Lee right for maps with no squares?"
- P6: "…of a map with no squares…"

Alternatively, move the sentence "A network may pass through places in squares or leave them out" from the shared rules into Problem 7, where squares first appear, and still add the qualifier. Children at P8 can look back at earlier problems.

The contrast is good facilitator material: P8's maps break P2, P3, Lee's claim and P6. This is the kernel-3 point that the base week's tools fail once places are optional.

K–1 asks no general questions. The 2–3 definition ("between every two places") has no squares, so 2–3 P7 is correct as written.

### 2. K–1, p. 6, Problem 7: "with the square" has two readings, and one of them makes the task trivial

**Text.** "Draw dots on the links to the square so that joining A, B and C costs the same with the square as without it." The triangle links are 4, 4, 4.

**Evidence.** Spoke prices tried: 1–6 dots each.

- **Reading A** (intended, matching P4/P5's "once without the square and once using it"): the cheapest join that uses S costs 8. The solutions, in any arrangement, are (1,3,4), (1,3,5), (1,3,6), (2,2,4), (2,2,5), (2,2,6) and (2,3,3). No choice with three equal spokes works: 2,2,2 gives 6 and 3,3,3 gives 9.
- **Reading B** (the square is on the map, and the cheapest join still costs 8): 42 sorted triples work, including 4,4,4 and 6,6,6. Under this reading, "make the spokes expensive" solves it at once.
- **A trap even under reading A.** A child who copies P4's pattern and buys all three spokes may choose spokes that add to 8, such as (1,1,6) or (1,2,5). On those maps the cheapest join using S is 1+1+4 = 6 or 1+2+4 = 7, so the square does save counters. The parent volunteer is unlikely to catch this.

**Fix.** Use the P4/P5 wording and make "cheapest" explicit: "Draw dots on the links to the square so that joining A, B and C as cheaply as you can costs the same using the square as without it."

### 3. Star maps in K–1 (pp. 4, 5, 6) and grades 4–5 (pp. 7, 8): each spoke's price label sits nearer an outer triangle link than its own spoke

**Diagrams.**

- K–1 P4 (p. 4)
- K–1 P5, top two maps (p. 5)
- K–1 P7, the three blank boxes (p. 6)
- 4–5 P7 (p. 7)
- 4–5 P8, top two maps (p. 8)

**Evidence.** Measured from the TeX coordinates, label box to link:

| Map | Label | Distance to an outer link | Distance to its own spoke |
|---|---|---|---|
| K–1 P4 | SC "2" | 3.0 mm to BC (centre 6.0 mm) | 3.5 mm (centre 8.9 mm) |
| K–1 P4 | SB "2" | 3.3 mm to AB | 3.5 mm |
| K–1 P4 | SA "2" | 3.0 mm to AC | 3.5 mm |
| K–1 P5, SA=SB=2, SC=4 | SC "4" | centre 6.9 mm from BC | centre 9.3 mm |
| K–1 P7 | SB box | 2.6 mm to AB | 3.5 mm |
| 4–5 P7 | SC "2" | 2.7 mm to BC | 3.5 mm |
| 4–5 P8, second map | SC "4" | centre 6.6 mm from BC | centre 7.3 mm |

On the page, BC appears to have one label above it and one below it, and SC appears unlabelled.

This matters most on the map with SA=SB=2, SC=4, where the odd spoke is the whole point. If SC is read as 2, by symmetry with the other spokes, the cheapest join becomes SA+SB+SC = 6. K–1 P5's middle answer then flips from "same, 8" to "the square saves". 4–5 P8's middle answer becomes one way at 6 instead of six ways at 8.

**Fix.** Place each spoke label on the inner half of its spoke, beside S, in the wide 120° gap between spokes where the triangle sides are far away. Do the same for the K–1 P7 boxes. Then confirm that every label's nearest link is its own; the builder's clearance report does not test this.

### 4. K–1, pp. 2–3, Problems 2 and 3 (the six-place K–1 map): the CD label "3" is nearer BC than CD

**Evidence.** The "3" label box is 2.9 mm from the BC diagonal and 3.5 mm from CD, inside the wedge between them. This happens on both large maps and, more mildly, on the small copies.

A misreading here flips both answers. If CD is taken for a 2-dot link, the 2-dot links already join all six places. P2's answer ("the pawn first walks from A to F at 3 dots") becomes 2, and P3's "Can you buy a network that has no link with 3 or 4 dots?" becomes "yes".

**Fix.** Move CD's label low on the left side of CD, near D, where the BC diagonal is farthest away.

### 5. Six-place map in 2–3 P5 (p. 4), 4–5 P6 (p. 6) and 4–5 P8 (p. 8): the EF label sits nearer DE than EF

**Evidence.** On every printed copy (as printed, +2, doubled and squared), the EF label box is 2.6 mm from DE and 3.5 mm from EF. On the 4–5 P8 map it is 3.2 mm from DE and 3.5 mm from EF. The label sits near E, where DE and EF converge.

The outline warns that the base week's first print misplaced labels on this same map. I checked the effect: swapping the DE and EF prices happens not to change any answer on these pages. All network costs, trip sets and the 4–5 P8 answer stay the same. So this is a legibility fix, not a wrong answer.

**Fix.** Slide the EF label down toward F, or put it outside the map to the right of EF.

### 6. Minor: the number of record boards does not match the answer count in "find all" tasks

- K–1 P1 (p. 1): "How many different networks cost just that much? Draw each one." There are 4 small boards; the answer is 3.
- 2–3 P1 (p. 1) and 4–5 P2 (p. 2): there are 8 small boards; the answer is 6.

A child may keep hunting for a 4th or 7th network or fill a board with a non-cheapest one. This is low priority, since spare boards are normal. If it matters, set the extras visibly apart, using whatever convention the organizer accepts.

---

## Verified answer key, by band

### K–1: correct apart from items 2, 3, 4 and 6

- **Shared examples.** Buy AB, then BC: tray 2, then 3. The rings example gives {A,B}{C}{D} at 1 dot and one group at 2 dots. The square example costs 2, then 4 through S, against 3 for AB alone. All trays and rings are correct.
- **P1.** The cheapest network costs 4. There are 3 cheapest networks: CD plus any two of AB, BC, AC.
- **P2.** Groups on the six-place K–1 map:

  | Links open | Groups |
  |---|---|
  | 1 dot | {A,B} {C} {D} {E,F} |
  | up to 2 dots | {A,B,C} {D,E,F} |
  | up to 3 dots | one group |
  | up to 4 dots | one group |

  The pawn first walks from A to F at 3 dots.
- **P3.** The cheapest network costs 9, in 2 ways: AB, AC or BC, CD, DE, EF. No network avoids every 3- and 4-dot link, because the links of 1 and 2 dots leave {A,B,C} and {D,E,F} apart.
- **P4.** Without the square: 8, in 3 ways. Using it: 6, by SA+SB+SC only.
- **P5.**

  | Map | Without the square | Using it | Does the square save? |
  |---|---|---|---|
  | Spokes 3 | 8 | 9 | no |
  | SA=SB=2, SC=4 | 8 | 8, in 3 ways | no, the same |
  | Diamond | 12, in 4 ways | 8 | yes, by 4 |

- **P6.** Cheapest is 6, uniquely: AS, BS, ST, TC, TD.
- **P7.** See item 2 for the solutions.
- All dot prices are at most 4, every total is at most 12, and markers needed are at most 9.

### Grades 2–3: the mathematics checks out completely; only diagram items 5 and 6 apply

- **P1.** The cheapest network costs 9. There are 6 cheapest networks: two of AB, AC, BC, plus CD, plus CE or DE, plus EF.
- **P2.** Lowest most-expensive link:

  | Pair | Lowest top price | Routes that achieve it |
  |---|---|---|
  | B to D | 2 | BCD, BACD |
  | D to F | 4 | DEF, DCEF, … |
  | A to F | 4 | ACEF, ACDEF, … |

- **P3.** Groups:

  | Links open | Groups |
  |---|---|
  | priced 1 | {A,B,C} {D} {E,F} |
  | up to 2 | {A,B,C,D} {E,F} |
  | up to 3 | unchanged |
  | up to 4 | one group |

  B and D first share a ring at 2, D and F at 4, A and F at 4. These agree with P2.
- **Trip example.** ABC costs 3, matching the tray.
- **P4.**

  | Prices | Cheapest network | Cheapest A–D trip |
  |---|---|---|
  | as printed | AB, BC, CD, cost 3 | ABCD, 3 |
  | every price 1 more | cost 6 | AD, 5 |
  | every price 2 more | cost 9 | AD, 6 |

  Each answer is unique.
- **P5.** In every version the cheapest network is AB, BC, CD, DE, EF.

  | Prices | Network cost | Cheapest A–F trips |
  |---|---|---|
  | as printed | 8 | ABCDEF and ACDEF, 8 each |
  | every price 2 more | 18 | ACDF only, 15 |
  | doubled | 16 | ABCDEF and ACDEF, 16 each |

  Every payment is at most 18.
- **P6.** It is possible, for example AB=1, BC=1, AC=3. With whole-number prices, the prices work exactly when AB + BC = AC − 1. I checked all 55 solutions with prices up to 12.
- **P7.** The answers are no and no. Every cheapest network has no loop, so all have the same number of links and each gains the same amount. Every trip's cost doubles.

### Grades 4–5: the answers check out; item 1 makes the general claims in P2, P3, P4 and P6 false as worded

- **P1.** A to D: 2 (ACD, ABCD). B to D: 2. D to F: 4. A to F: 4.
- **P2.** The same 6 cheapest networks as 2–3 P1. Yes when every place is circled (see item 1).
- **P3.** The groups are as in 2–3 P3. All six networks use prices 1, 1, 1, 2, 4. The group counts 6, 3, 2, 2, 1 give a cost of (6−1)+(3−1)+(2−1)+(2−1) = 9. The general answers are correct only with no squares.
- **P4.** All four networks with no loop have most expensive link 3. BC+CD+DA costs 9 and the others cost 7, so Sam is wrong. Lee is right only with no squares.
- **P5.** As in 2–3 P4.
- **P6.** The network AB, BC, CD, DE, EF is the same in all four versions.

  | Prices | Network cost | Cheapest A–F trips |
  |---|---|---|
  | as printed | 8 | ABCDEF and ACDEF, 8 each |
  | every price 2 more | 18 | ACDF, 15 |
  | doubled | 16 | ABCDEF and ACDEF, 16 each |
  | squared | 14 | ABCDEF only, 14 |

  So adding to every price and squaring change the trips; doubling does not. Every payment a child makes is at most 29.
- **P7.** The cheapest is SA+SB+SC = 6. Starting from AB+BC, moves that keep the total at most 8, or even at most 9, reach only the three triangle pairs. The answer is "no". At least one step must cost 10 or more.
- **P8.**

  | Map | Cheapest cost | Number of cheapest ways |
  |---|---|---|
  | Spokes 3 | 8 | 3 (triangle pairs) |
  | SA=SB=2, SC=4 | 8 | 6 (3 triangle pairs; SA+SB plus SC, AC or BC) |
  | Only A and F circled | 8 | 2 (ABCDEF, ACDEF) |

- **P9.** Cheapest is 6, uniquely. A square place never has just one bought link: returning it keeps everything joined and is cheaper. With four circled places, at most 2 square places can have three or more links. Every leaf of a cheapest way is circled, and a tree has at least 2 + Σ(degree − 2) leaves over its branch points. The map attains 2 (S and T).
