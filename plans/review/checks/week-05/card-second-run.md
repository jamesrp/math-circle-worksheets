# Week 5: Tower cities

**Verdict: revise.** One must, in the adult guide: 204 of the 576 4-by-4 cities share all sixteen numbers with another city, so 4–5 Problem 5 cannot be finished for them, and the guide's entry neither warns nor says what to do. The pages and problems are at the bar; the verdict hinges on this one finding.

Reviewed 2026-10-10 by Claude, with math.md. Packets: week-05-k-1.pdf (F05-K-v4, 7 pp., Problems 1–7), week-05-grades-2-3.pdf (F05-M-v4, 9 pp., Problems 1–7), week-05-grades-4-5.pdf (F05-U-v4, 8 pp., Problems 1–9). Adult guide: week-05-facilitator.pdf (F05-FAC-v4, 9 pp.). Companions noticed but not reviewed: week-05-return-visit.pdf (F05-RV-v1, 3 pp.) and its guide. Status: unpiloted.

## The mathematics

A row of towers is a permutation, and the towers seen from an end are its records. Seeing 1 from an end puts the tallest there, so (1,1) is impossible, and L + R ≤ n + 1; counting rows by records gives Stirling numbers. A city is a Latin square with skyscraper clues. Clue sets fit one city, several or none; every 3-by-3 city's numbers total 22; the fewest clues that fix a city are 2 for 3-by-3 (a swap proof) and 3 for 4-by-4 (by computer); two 4-by-4 cities can share all sixteen numbers. A mathematician would enjoy it. K–1 P2–P7, 2–3 P1 and P3–P7, and 4–5 P1 and P3–P9 carry it.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Records, which clue sets fix a Latin square, a sum invariant, critical sets, twin cities. |
| Problems | strong | Cards that work beside cards that can't (K–1 P3, P7; 4–5 P1); puzzles with one city, none (2–3 P3) and several (P4) before children make puzzles. |
| Student pages | strong | Spec header and footer, one rule paragraph, no hints or slop. Spare slots hide the counts (8 frames for 6 rows). 1-inch grids where cubes stand. |
| Concreteness | strong | The eye at the table enforces the count; a partner checks hidden rows and cities; colour by height shows a repeat. One launch shows the look and the folder. |
| Correctness | strong | Math check: 124 checks, 0 mismatches; guide slips only. I re-ran the 204 and puzzles E, F. |
| Adult guide | adequate | Counted materials, a scripted launch, roles, fallbacks, ordered hints, proofs, a record sheet. Fixes 1–3. |
| Age fit, K–1 | strong | One or two read-aloud sentences, counting to 4, a hiding game; four towers come late. |
| Age fit, grades 2–3 | strong | Building a city is itself a puzzle; P5's "why fewer cannot work" has a cube argument; P7's 22 comes late. |
| Age fit, grades 4–5 | strong | P1–P3 start at once; puzzles E and F need trying cases; P6, P8 and P9 are for the quickest. |

## Keep

- All bands: "You see a tower when it is taller than every tower in front of it", eye at the table; pre-built towers coloured by height.
- K–1: P2's six rows; P3 and P7, each with two impossible cards; P4's hidden-row game as the main activity; P5's "How do you know you have them all?".
- 2–3: P1's never-pairs; P3's impossible 2, 2, 2; P4–P6; P7's open "Which totals can a city have?".
- 4–5: P1's eight cards; the P3 ladder from 12 clues to 4; P4, whose A and D seed P9; P5 asking for no proof of a computer result; P6–P9.
- Guide: the launch, roles, fallbacks, the swap argument, section 5.

## Fix

1. **must**, guide p. 7, 4–5 Problem 5 (student p. 6: "so that your city is the only one that fits"). 204 of 576 cities share all sixteen numbers with another (math check item 1; recomputed), among them Problem 4's A and D, which the children have just built. A pair hiding one can never finish, and the entry doesn't say so. Hint (1), "Problem 4 had two numbers and four cities. Add one number.", fails for A and D; hint (2), "Which edge number differs between the two?", has no answer for twins. Guide fix: "About a third of cities (204 of 576, including Problem 4's A and D) share all sixteen numbers with another city, so no puzzle singles them out. If the solver finds a second city that fits every number, the builder made no mistake: that is Problem 9. Keep both cities and hide a new one." Add "(B or C, not A or D)" to hint (1) and "If none, see Problem 9" to hint (2). Leave the student page, so Problem 9 keeps its discovery.
2. **should**, guide pp. 2 and 4, K–1 Problem 4 and launch step 4. Nothing says which number goes with which end. Partners facing across a folder have opposite lefts, so a builder who hears "2 and 1" may build the hider's row turned round, which an adult reading Problem 3's key (2 and 1: 213) may call wrong (prediction). Hint (2), "Find the card in Problem 3 with these numbers", fails for 3 and 1. Fix: "The hider points to each end as they say its number; a row turned round counts." Hint (2): "Find these numbers on your Problem 2 page."
3. **should**, guide p. 1, section 1. It states the row facts and mentions the 22 as something a child may notice; L + R ≤ n + 1, fewest clues 2 and 3, and the twins first appear on pp. 5–7. These are the upper bands' destinations, and fix 1 shows an adult needs them before Problem 5. Add a line for each from section 5, marking the 4-by-4 results "by computer", with the band that meets it.
4. could, guide p. 8: "≈ ln n" → "≈ ln n + 0.58" (math check item 4).
5. could, guide p. 1: "(fewer numbers each time)"; C and D both have 6.
6. could, K–1 P1: two rows, the left one being the page-1 picture's 132. Use 213, or add a row.
7. could, P3 in 2–3 and 4–5: label the puzzles 1–4 and A–F, as the guide, the record sheet and the Week 2 upper catalog do.
8. could, guide p. 2, launch step 3: "Ask what the other end shows now (1)" previews K–1 P3 and 2–3 P1; drop it.
9. could, the source README links a missing plans/fall-forecast-2026-10-03.md; plans/week-05-redesign.md describes v3.
10. could, return-visit guide p. 3: "forced to be b, a" should be "a, b" (math check item 6).

## Overlaps

Week 25 also asks which edge counts fix a grid and meets an undetectable 2-by-2 switch, as 152 of the 262 twin pairs here do, but on 0/1 pictures. Week 3 meets records only through Foata's bijection. The app's Symbol Orchard already has these Latin squares with entry clues and leaves visibility out by design. No merge.

## App fit

A, confirmed; size M, not S, since heights need towers and a side view. A group in Symbol Orchard, reusing its board.

- Board: tap a cell to cycle its height. Tapping a full line's clue shows its side view, hidden towers greyed; don't light clues on partial lines.
- Solves: a row for a card, or a checked "No row" (K–1 P3, P7; 4–5 P1). One-city puzzles (2–3 P3; the 4–5 ladder, E and F Hard) and a checked "No city". Every city, then one more clue, ending with "That's all", not slots (P4). Make a puzzle while the app plays the partner, showing a second city (2–3 P5, 4–5 P5–P6). Twin cities (4–5 P9).
- Pitfalls: 3-by-3 has 12 cities, so check on submit, not freely. Don't ask why 3 clues are fewest on 4-by-4. Accept "can't be singled out" as a checked claim for a twin. Leave the counting tables and the 22 on paper.

## Classroom evidence

None reported. The source README marks v4 "Unpiloted"; themes.md lists only Weeks 1, 2 and 15 as taught. Nothing records the guide's evening-before tests, so the sight lines and folders are unrehearsed.
