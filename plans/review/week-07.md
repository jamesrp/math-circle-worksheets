# Week 7: Take-away games

**Verdict: keep.** No must. Every answer checks and partners enforce the rules. The guide's one false statement touches no printed problem; the fixes are guide repairs and K–1 wording.

Reviewed October 5, 2026 by Claude, reconciled from two independent card runs, with the math check in [week-07-math.md](week-07-math.md). Packets: week-07-k-1.pdf (F07-K-v4, 6 pp., P1–9), week-07-grades-2-3.pdf (F07-M-v4, 5 pp., P1–9), week-07-grades-4-5.pdf (F07-U-v4, 8 pp., P1–14). Adult guide: week-07-facilitator.pdf (F07-FAC-v4, 9 pp.). Companions noticed but not reviewed: the return visit and its guide; archived v3. Status: unpiloted (October 3 revision).

## The mathematics

A pile is one to hand over when every move from it reaches one that is not; working up from 0 labels them all. Moves 1 to k give the multiples of k + 1; 1, 3 or 4 gives 0 and 2 mod 7. Each label depends on the few below it, so every finite menu ends up repeating (pigeonhole, 4–5 P14). Equal piles lose by copying, and with 1 or 2 two piles lose exactly when their remainders mod 3 match, the smallest case of Sprague–Grundy. A mathematician would enjoy it. K–1 P1–P7, 2–3 P1–P6 and 4–5 P1–P8 carry the one-pile core.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Backward induction, periodicity with a proof, menu design, greedy failing, misère, copying. |
| Problems | strong | Several piles or games per question. 2–3 meets 1, 3 or 4 as piles, a chart and adult games before Lena and Omar. New rules contrast: 1, 3 or 5 is parity; 2, 5 or 6 has period 11. |
| Student pages | adequate | Spec headers and footers, walled 0.68 in tracks, no neg.md item, no hints. Three K–1 problems leave the next action unclear (fixes 4, 5). |
| Concreteness | strong | The partner or the 4–5 referee checks each move; the launch (guide p. 2) moves counters and token together. Token fit is unrehearsed; the guide's five-minute test covers it. |
| Correctness | strong | The math check finds all 32 answers and hints right; my solver agrees on spot checks. Guide errors count under Adult guide. |
| Adult guide | adequate | Counts, a scripted launch, pairings, three held hints per answer, a record sheet. One false statement, a thin overview, reply-table slips (fixes 1–3). |
| Age fit, K–1 | strong | One or two sentences, read aloud. Lose to the grown-up as a team, then use the secret on a partner. |
| Age fit, grades 2–3 | strong | Counting to 20; sevens only in P6. Prediction: colouring all of 0–20 (P2) is steep; the guide's struggling route skips it. |
| Age fit, grades 4–5 | strong | Play opens each new game (P1, P3, P10, P12). Kai (P5) is the densest reading. P8–P14 come late. |

## Keep

- The launch: the adult plays from 7, lands on 6 and 3 without explaining, and ends with "find the secret".
- K–1's secret hunt: P2 records the grown-up's 9, 6, 3, 0, P3 uses it, P6 and P7 break it. P8's pairs: three equal, two that one move makes equal.
- 2–3 on 1, 3 or 4 throughout P1–P7, with Lena (P4) and Omar (P5) testing every reply.
- 4–5 P5 (Kai), P7's three rules, P9's design question, P13's chart, P14's 2, 5 or 6 track.
- "Until you are sure" on the first/second rows; the record sheet's tried / guessed / checked in some cases / explained scale (guide p. 9).

## Fix

1. **should**, guide p. 8: "(The shift by one is special to moves 1 to k.)" False: for one pile the last-counter-loses squares move up one for every menu (1, 3 or 4: 1, 3, 8, 10, 15, 17; math check item 1, 255 menus). Not a must: every printed last-counter-loses problem (K–1 P9, 4–5 P10–P11) uses 1 to k, so no answer is wrong. But a 4–5 child who tries 1, 3 or 4 finds the p. 9 claim "every coloured square moves up 1" true, and this sentence would lead the adult to deny it. Use the math check's replacement.
2. **should**, guide p. 1: "The pattern always repeats" needs a finite menu and may start late (2, 4 or 7; math check item 2). The overview omits the multiples of k + 1, copying and the last-counter shift, and does not separate experiment (charts), conjecture ("every 7") and explanation (Lena, copying, 4–5 P8). Move four sentences up from Section 5.
3. **should**, guide p. 3, reply table (math check items 3–5). "the second column" should be "the 'Squares to leave' column". "take 1 and wait" should be "take the smallest number allowed"; 1 is illegal under 2 or 3, and under 2, 5 or 6. Row 1 or 4: "remainder 1: take 1 or 4", as the 2–3 P8 answer accepts. Rows 1 or 2 and 1, 2 or 3 give only replies; begin "take the remainder on dividing by 3 (4)".
4. **should**, K–1 p. 6, P8 and P9: every row prints "1st 2nd", but neither problem asks for a choice, and P8 never says to play (math check item 6). End both with "Circle whether you would rather go 1st or 2nd."; in P8 put "Play each pair of piles many times with your partner." first.
5. **should**, K–1 p. 2, P3: "Now you go first from 10 against your partner. Colour your own squares." Both partners' pages say it, but each game has a second player. A child who colours as second player gets no 9, 6, 3 (prediction), and the guide's check "colours exactly 9, 6, 3, 0" fails. Borrow P6 and P7's colouring rule: "Now play your partner from 10, and take turns going first. Colour the first player's squares."
6. **could**, 2–3 P2: label the second 0–20 track extra workspace.

## Overlaps

Week 8 (Rook race and Nim) shares two-pile copying, which K–1 P8, 2–3 P7 and 4–5 P12 preview. Week 7 owns one pile with a menu; Week 8 owns free takes, XOR and the queen game. Keep both, Week 7 first. Week 60 shares only backward induction. No merge.

## App fit

Confirm A, size S. Pebble Duel has a Menus group for this theme. The port should contain:

- Take buttons for the menu against a perfect opponent. Solves: a win, or choosing who starts and winning from drawn starts (K–1 P1–P3; 2–3 P1, P3).
- Every reply as the certificate for "go second" (2–3 P4): the app plays each first move in turn, and the child must win them all.
- The track as a solve: mark the squares to leave on 0–30 and declare done. The app checks the set without showing a count; from a wrong square it plays the child and wins (2–3 P2, 4–5 P4, P7).
- A design goal (4–5 P9): a menu whose squares to leave are exactly 0, 5, 10, …. Reverse goals resist guessing.
- 2, 5 or 6 (4–5 P14), with period 11, and the two-pile chart (4–5 P13).

Pitfalls: a "which squares are coloured" quiz is predicting, which children enjoyed less. A hint that names the winning take gives the game away. Big piles should push to the repeat, not to counting. The one-pile shift fails for two piles.

## Classroom evidence

None reported for these packets. The source and year-2 READMEs say the October 3 version is untaught, plans/week-07-redesign.md records no Week 7 observations for v3, and the private use log is not in this checkout.

The core game met an earlier group. In the organizer's year-1 Handout 2.3 (Fall 2025) children played 1, 2 or 3 from 20 stones; Handout 3.1 recaps that they "found that the copying strategy was pretty good" and that 4 left loses for the player to move. That is a handout, not evidence about these pages. Year 1 used 1 to 3 and 1 to 5, so returning children may know the 1-to-k pattern.
