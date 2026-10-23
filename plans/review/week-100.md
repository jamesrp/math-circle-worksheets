# Week 100: Distance in nested worlds

**Verdict: keep.** No must. Every answer, diagram and proof checks; P2, P4 and P5 are catalog-grade tasks with their own cards and boards, and the guide opens with the theorems. The fixes are a sharper P4 question, a P10 end rule and a K–1 route.

Reviewed October 23, 2026 by Claude, with math.md. Packet: week-100-grades-3-5.pdf (W100-G35-v1, Grades 3–5, 8 landscape pp., Problems 1–10). Adult guide: week-100-facilitator.pdf (W100-FAC-v1, 5 pp.). Companions noticed but not reviewed: none. Status: unpiloted. The organizer chose the topic on October 17; the source README says "Prepared for organizer review. Unpiloted", with printing, cutting and timing unrehearsed. No K–1 packet, by design.

## The mathematics

Cards sit in nested loops whose labels grow outward, and two cards' distance is the label of their smallest common loop. This is an ultrametric: among any three cards the largest distance occurs at least twice (P2 by cases, P6 in general). Balls are nested or disjoint and every member is a centre (P3, P7). Complete consistent clues rebuild the loops, and one bad triangle proves a table impossible without saying which clue is wrong (P4, P5). Cards 0–7 under a scaled 2-adic distance form such a world (P8, P9). A mathematician would enjoy it: non-Archimedean geometry reached by building and rebuilding.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Strong triangle inequality, ball nesting, reconstruction, inconsistency certificates, a 2-adic example; the guide proves each by nesting or divisibility. |
| Problems | strong | P2's six contrasting triples (two impossible, two equilateral), P4's inverse rebuild and P5's every-repair each hold five minutes or more. The order runs read, build, invert, repair, prove. P4 ends thinly (fix 1). |
| Student pages | strong | Spec header and footer, rules once, a non-task worked example (X and Z, the group checked, X–Z = 6), no slop or hints. Cut-outs sit apart from tasks, so cutting a working copy loses nothing. |
| Concreteness | adequate | Cards and loops show every membership; the guide's launch (p. 2) shows the X–Z reading and a ball test; P4's partner checks clues. Nothing checks the smallest-loop reading in P1–P3, and loops are never counted or sized (fix 9). |
| Correctness | strong | math.md: 81 checks, no student error. I agree, and rate its one guide finding a could (fix 5). |
| Adult guide | strong | Theorem-first with hypotheses and limits; launch, first-visit timing, full keys, the repair completeness argument and the 15-question proof. Gaps: fixes 2, 3. |
| Age fit, K–1 | weak | No route: "No younger-table session is implied by the shared demonstration" (guide p. 2). |
| Age fit, grades 2–3 | adequate | Third graders can likely do P1–P4 with the mathematician reading (prediction). The ten-sentence opening, P3's letter r and P8's remainders are heavy; the guide's first visit stops at P4. |
| Age fit, grades 4–5 | strong | P4–P7 and P10 suit the organizer's table; P8–P9 need remainders by 4, which they have. |

## Keep

- p. 1: the X/Y/Z arrow chain and "X–X = 0"; "A group may contain three or more smaller groups", which makes 2,2,2 and 4,4,4 buildable; four 2-labels, so a child can try 2,2,4 and watch two loops cross.
- P2: the six triples in this order, and one explanation, not six.
- P3: radii 1, 3 and 7 that are not labels, and "balls that contain B" with no fixed centre, so any centre gives the same answer.
- P4: ten movable clue cards and "Your partner checks each clue against the loops"; the hidden world is not p. 1's (C and D swapped).
- P5: the A–C = 2 card, and "Find every repair … Explain why your list is complete", whose answer is a short three.
- P10's secret-world game and the guide's all-8 adversary proof.
- Guide: the overview, launch and first-visit route.

## Fix

1. **should**, P4, p. 4: "Draw two different-looking worlds with exactly these distances." A mirror image does it, as P1's "Rearrange the cards and loops" already did, and the destination the guide's overview names, that complete clues determine the groups, is never asked. Replace it with "Could loops around different sets of cards fit the same ten clues?" (No: one structure of 358 fits, math.md. An extra loop labelled 4 around D and E holds the same cards; guide p. 4 already covers it.)
2. **should**, P10, p. 8, and guide p. 5. Nothing says what happens when the asker's drawing is wrong, so "as few questions as possible" rewards guessing. In the guide, or one page sentence: the builder reveals the world, and any wrong distance loses the round.
3. **should**, K–1, guide p. 2. The K–1 table has no route after the launch. A should, as on the Week 87, 96 and 97 cards, since the plan declines a K–1 packet. Add a route: picture cards in small and big yarn loops; the parent reads P2's triples as close and far ("cat and dog close, cat and fish close, dog and fish far: can you make it?"). That K–1 keeps the rule is a prediction.
4. **could**, P5: "Change exactly one of these ten clues, with A–C = 2," removes math.md's second reading.
5. **could**, guide p. 5: "on page 1" (twice) means the overview, not student p. 1 (math.md); little is lost, since the overview is the guide's first page.
6. **could**, p. 1: delete "Each card is also a one-card group."; no task uses it.
7. **could**, p. 1: P1's two recording lines sit under the X/Y/Z example; move them under the P1 world.
8. **could**, p. 7: P8's box is 43 mm tall for eight cards, three loop levels and six balls, and P9 has about 2.5 cm; rebalance.
9. **could**, guide p. 2: give loop counts and rough lengths (P8 needs seven), name p. 8 as the workmat from P1 on, and note that 15 secret worlds in P10 need a third 4-label.
10. **could**, P8: restore the plan's "Find a pair far apart on the number line but close here"; the 0-and-4 surprise is only in the guide.
11. **could**, guide, P7: suggest hunting for partly overlapping balls in the P4 world before arguing in general.

## Overlaps

Weeks 67 and 69 use road length on trees, an ordinary metric that breaks this rule (1, 1, 2). Week 6's yes/no tree on 0–7 is P8's parity loops. Week 19 nests sets, with no distance. No merge.

## App fit

Not in themes.md. I propose Fit B, size M, a new family.

- Board: drag loops around cards and pick labels 2, 4, 8; the app refuses crossing loops and labels that do not grow outward, which paper cannot enforce.
- Rebuild (P4): fit a clue set; each clue lights when it holds.
- Can't (P2, P5): tap three clues whose largest is unique, and the app checks the certificate. Then every one-clue repair, ended with "That's all" and no slot count.
- Pin it down (P10): choose the fewest clues that force a hidden world; if a second world fits, the app shows it. Avoid the all-8 adversary, which always forces 15.

Pitfalls: no predict-a-distance or watch-a-ball rounds, and no tap that reveals a distance in rebuild puzzles. Draw on P2, P4, P5 and P10, with P8 as a later group.

## Classroom evidence

None reported. The source README says "Unpiloted; printing, preparation, material handling, adult procedures and timing have not been physically rehearsed."
