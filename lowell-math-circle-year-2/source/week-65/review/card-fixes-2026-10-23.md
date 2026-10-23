# Week 65 card fixes, October 23, 2026

The review card is `plans/review/week-65.md` (verdict keep). This pass made its four shoulds and its clear coulds. The student packet is now v3 (W65-S-v3, seven pages, Problems 1–6) and the guide W65-FAC-v3 (seven pages). The student pages were converted to problem files first, with no wording change (commit 136678c); these edits were made in the problem files afterwards.

| Card item | Change |
|---|---|
| should 1 | Guide item 1 states the rule: around a cluster of n rooms whose outside is one simple closed walk, left minus right quarter-turns is 4 + 4n on octagons and 4 on squares, with the add-a-room argument, as a discrete Gauss–Bonnet theorem; Weeks 56 and 61 are named as the positive-curvature side. The old "A general formula for larger clusters is not required" is gone. P2's section has the ready-pair question (no full return in fewer than 8 moves; no odd return, by two colours). P3's section has "A third case for a ready pair": Home, A and ⋆ on p. 5 give 17 left and 1 right; an L of three squares gives 5 left and 1 right. |
| should 2 | Guide p. 1 has a K–1 adult-led route on the existing pages (launch, P1's 4- and 6-move returns, P2's left-turn walk, P5's two-door routes with a coin; the adult reads and scribes) and a key in plain words. It is marked unpiloted. No K–1 student pages were added. |
| should 3 | P3: "Mark dots where you go straight." removed. |
| should 4 | New Problem 6 on p. 7: rooms reached in 2 door crossings but not fewer, on the octagon floor and on a printed 5 × 5 square floor, with two answer lines. Key: 48 and 8, in the guide's P6 section, with hints; the guide's p. 7 growth section is labelled "Behind Problem 6". |
| could 5 | P4's R label moved to (−0.66, 0): 8.5 mm from R, 16.1 mm from the nearest other street (was 16.1 mm from R, 8.9 mm from the v2v3 street). |
| could 6 | P2 says "facing the same way". P4 says "two different ordinary straight lines": "ordinary" was kept, since the question contrasts ordinary lines with the map's streets. |
| could 7 | P5's star is drawn 2.2 times larger, about the size of the room letters. |
| could 8 | p. 6 is headed "Problem 5 (continued)" instead of "Extra workspace ... Keep the board beside this sheet"; p. 5 keeps its one "beside" line. |
| could 9 | Guide P2 section: a child checks a corner with the corner of an index card. |

Checks: `review/verify_card_fixes_2026_10_23.py` rebuilds the tiling and checks the 4 + 4n rule on every simple connected cluster of up to four rooms around Home (and on squares), the named cases, the shortest full return (8, none odd, by search of every turn sequence up to 9 moves), the Problem 6 counts (layers 1, 8, 48; 56 routes with 8 rooms reached twice; squares 12 routes, 8 rooms), the R label distances, and the printed wording, numbering and footers. `student/build.py` records the Problem 6 counts in `checks.json`.

Not changed: the card's App-fit notes (the organizer's decision is recorded there). Nothing was physically rehearsed; the packet remains unpiloted.

## Critic follow-up, later on October 23, 2026 (v4)

An independent critic (Critic C) read the card-fix release and found two shoulds and two coulds, now made:

- **Should 8, Problem 6 (p. 7).** The page drew only the square floor, and the answer 48 rests on there being no overlaps beyond the 8 corner rooms, which a child could not see. The page now prints an octagon map beside a smaller square floor: Home, its 8 side neighbours and its 8 corner rooms, each drawn whole (`first_ring()` in `figures.py`, rooms listed in `student/geometry.py` as `ROOMS_AROUND_HOME`). Each neighbour visibly has one wall to Home, two to corner rooms and five on the map's outside; the prompt adds "Only the rooms around Home are drawn; the floor goes on."
- **Should 9, guide p. 1.** The rule "left minus right quarter-turns is 4 + 4n" was stated for any n rooms whose outside is one closed walk that does not touch itself. That is false for a ring around a hole: Home's 16 surrounding rooms have such an outside walk and give 72 = 4 + 4·17, not 68. The rule now adds "and encloses only those n rooms", with that ring as the example.
- **Could 10, readiness.** The guide said multiplication was not a prerequisite; it now says Problem 6 uses 8 × 7 or 8 × 5 + 8.
- **Could 11, "A third case".** The page-5 board's corners are unmarked, so the guide now says to dot them first before counting the 17 left turns and 1 right.

The Problem 6 key and its adult background now read the doors off the map. To keep the guide at seven pages, "can wait for another visit" became "can wait". Footers W65-S-v4 and W65-FAC-v4. Checks: `student/build.py` (the map's rooms and doors), `review/verify_card_fixes_2026_10_23.py` (now expecting v4 footers), and `plans/review/checks/week-65/check_critic_fixes.py` in the repository. The previous PDFs and ZIP are in the week's `archive-before-critic-fixes-2026-10-23/` folders. Still physically unrehearsed and unpiloted.
