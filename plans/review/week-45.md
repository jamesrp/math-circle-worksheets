# Week 45: The visible side

**Verdict: keep.** Every answer checks, the problems run in a sound order, and nothing printed leaves anyone stuck. Every fix is a should or a could.

Reviewed October 5, 2026 by Claude in two independent reviews, reconciled, with the math check in [week-45-math.md](week-45-math.md). Packets: week-45-k-1.pdf (W45-k-1-v2, 4 pp., Problems 1–7), week-45-grades-2-3.pdf (W45-grades-2-3-v2, 4 pp., Problems 1–6) and week-45-grades-4-5.pdf (W45-grades-4-5-v2, 4 pp., Problems 1–7). Adult guide: week-45-facilitator.pdf, 6 pp. Companions noticed but not reviewed: week-45-bonus.pdf (W45-BONUS-v1, 3 pp.) and its guide (W45-BONUS-FAC-v1, 4 pp.). Status: unpiloted; the October 4 revision left the student pages unchanged and added the route page (guide p. 6).

## The mathematics

Cards RR, RB and BB have six faces; a secret ticket picks the face that shows. Given red showing, tickets 1, 2 and 3 survive and two hide red: chance 2/3, not the 1/2 of counting cards (Bertrand's box). A cup of tickets 1 and 3 gives the same clue with chance 1/2, so the answer depends on how the clue was produced. A red clue ties exactly when the cup holds ticket 3 and one of tickets 1 and 2, with any of tickets 4–6: 16 cups, none of whole cards. A mathematician would enjoy the mechanism point; the object is small. The chooser contrast (2–3 P4, 4–5 P2, P4) and the design problems carry it.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Conditioning with stated hypotheses, a mechanism contrast, a characterisation, an obstruction. All on six faces. |
| Problems | adequate | Each band runs sort, clue, second chooser, design. Thin: 2–3 P1, 4–5 P3. |
| Student pages | adequate | Header, footer, numbering right; no slop; a non-task visual (ticket 4) first. Faults: fixes 1–4, 6. |
| Concreteness | strong | Tickets are the cases; flipping a card checks a hidden color. One short launch (guide p. 2), but children never play the screen game (fix 7). |
| Correctness | strong | math.md: 169 checks, one failure, in the bonus guide (fix 8). Both reviews' enumerations agree. |
| Adult guide | adequate | Theorem-first overview with hypotheses and band map; keys with completeness proofs. Wrong hour, generic hints, no extensions (fix 7). |
| Age fit, K–1 | adequate | Flip, sort, remove, compare to three, at full length. Read aloud, the rule paragraphs won't land in one hearing (prediction). |
| Age fit, grades 2–3 | strong | Small counts, tickets hold the state, no fractions; P5–P6 are real design. |
| Age fit, grades 4–5 | adequate | Exact fractions, a refutation, a characterisation. P3 takes a minute. |

## Keep

- The card strip with "same card" brackets, the ticket-4 visual (p. 1) and the tickets-1-and-3 chooser (p. 3).
- Face tickets as the complete case list instead of long trials.
- K–1 P1–P3's "red underneath / blue underneath" boards; P5–P7.
- 2–3 P4's two boards; P5, whose third question is impossible; P6.
- 4–5 P2's friend's argument; P4; P6's open ticket row; P7.
- Guide: the p. 1 overview, the K–1 P4 note (p. 2), the completeness arguments.

## Fix

1. **should**, K–1 p. 3. The rule says "show its red face with the mark covered"; P4 says "show the face named by each draw". Under the rule, adding ticket 4 flips P4 to blue 2–1, and P5 gains a fourth cup, {4,5,6}. Not a must: P4's wording and guide p. 2 settle it. Fix: p. 3 in every band, "Only tickets 1 and 3 are in the cup." under the p. 1 rule; cut P4's "and show the face named by each draw".
2. **should**, all bands, pp. 1 and 3. "Each pair below is the two faces of one card." narrates the brackets; "Use matching-size cards." and "Choose and orient behind the screen" are operator procedure, already on guide p. 2. Fix in `src/write.py`, p. 1: "The small numbers match the six tickets. A secret ticket picks the face that shows, with its number covered. You see only the color." p. 3 as in fix 1.
3. **should**, method on the page. 2–3 P2's "Explain using the tickets that could have produced that clue." and P3's "Account for every ticket that could give this clue." name the conditioning step. 4–5 P5's "Give a possible set of hidden-color results that both chooser rules can produce." presumes the answer. Fix: P2 ends "Which hidden color is the better guess, and why?"; cut P3's and P5's second sentences.
4. **should**, 2–3 p. 1, P1. Both questions, the six showing and hidden colors and "Which tickets show the same color on both faces?", are read off the strip above. Fix: ask "Find every pair of tickets that show the same color but hide different colors." (four pairs). The first review rated this a could about wording; it is a should because CARD.md counts a thin problem as one.
5. **should**, 4–5 p. 2, P3: "If the chooser also reveals the face mark, what happens to the uncertainty?" A minute's thought. Fix: "The chooser also tells you one fact about the covered number: the number, whether it is odd or even, or whether it is 3 or less. After a red clue, what does each fact do to the better guess?" Key: the number decides; odd ties; even means red; "3 or less" changes nothing.
6. **should**, K–1 P5 (three groups of boxes) and P7 (two boxes): the slots match the answers. Fix: five groups, four boxes.
7. **should**, guide p. 2, "A flexible hour and optional hints", runs "0-8 minutes" to "57-60: reset kits."; context.md gives thirty-five to forty minutes at tables. Hints are generic; no problem has an extension. Fix in `facilitator-src/guide.json`: p. 6's first routes in 35–40 minutes, pairs first playing four to six rounds as chooser and guesser (guess, flip, no tally); a hint and an extension per problem.
8. **should**, bonus guide p. 1 (companion): "There are 322=12 equally likely histories." `source/week-45-bonus/guide.md` line 3 has `3*2*2=12`; write 3 × 2 × 2 = 12 and rebuild.
9. **could**, 4–5, a P8: allow copies of whole cards. Which make a red clue fair, and which hide red 3 times in 4? (One RR with two RB; three RR with two RB.)
10. **could**, K–1 and 2–3 p. 4: lay each card's tickets on it, so removing a card takes them.
11. **could**, guide p. 2: "For ten children" → eleven. The second review put this in fix 7; one word is a could.
12. **could**, guide p. 6: name the bonus as the 4–5 continuation. The second review folded this into a should; p. 6 already gives 4–5 a return route.
13. **could**, K–1 P7: "the same chance" → "a tie", as P2–P3 say. 4–5 P2's quotation marks print straight, and justified lines split words (bet-ter).
14. **could**, guide p. 2: give the slide number for the Mintz source.

Both reviews agree with math.md, which read K–1 P5 under the p. 1 rule only (fix 1).

## Overlaps

In Week 44 one visible colour word merges equally likely histories; Week 42 conditions by discarding outcomes and designs fair rules. Neither has a clue whose production changes the answer. Atlas AP-02, "The clue that changes the bag", reaches the same 2/3 against 1/2 contrast with bags. No merge; the guides could cross-refer.

## App fit

Change B to A, size S. themes.md rated it before the case engine existed; `docs/cases.md` now says Week 45 needs "Nothing new", and the solve is an obvious tap. The board is three cards that flip on a tap, whose six faces toggle into a cup; drop tickets and the screen. cases.md's "(ticket, side) pairs" are here just the six faces. The engine has `groupCases` (hides-red and hides-blue bins), `evenGroups`, `keepCase`, `claimCases` and `catalogHTML`. `evenGroups` is true for two empty bins, as in 8 of the 64 cups, so the family must require a red face.

- **Sort.** Red-showing faces into the bins (K–1 P1–P3, 2–3 P2–P3).
- **Design, checked on a claim.** Tying removals (K–1 P2: 1 or 2); red always hides blue (K–1 P5: three cups); a card removed for certain red or blue (K–1 P6, 2–3 P5); fair pairs (K–1 P7, 2–3 P6: {1,3}, {2,3}).
- **Find every.** The 16 fair cups of 64 (4–5 P6), with That's all; the certificate is the catalog by red-showing part.
- **Can't.** Whole cards never tie (4–5 P7): over seven selections the hides-red bin holds 0 or 2, the hides-blue bin 0 or 1.
- **Hard.** Copies of cards (fix 9); bonus P1's twelve histories (a card, then `sequences(['L', 'R'], 2)`).

Pitfalls: no live tie meter or greying of blue faces while designing, as the second review's live panel would give: that is the conditioning, and six toggles invite trial and error; no "k of 16"; no typed probabilities or colour guessing. The chooser contrast stays in grown-up notes. Thin, as themes.md says: a short set, or a group beside Weeks 42 and 44.

## Classroom evidence

None reported; the theme is unpiloted. The source README says "The theme remains unpiloted", and the guide's footers read "Unpiloted".
