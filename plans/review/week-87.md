# Week 87: Voting and agendas

**Verdict: keep.** No must: every answer, diagram and proof checks, every problem has its pieces and board, and the guide opens with the theorems. The fixes are line stems that mark each answer, a printed median conjecture, a short agenda route, no K–1 plan and one guide overclaim.

Reviewed October 23, 2026 by Claude, with math.md. Packets: week-87-shared.pdf (W87-S-v1, Grades 2–5, 3 pp.), week-87-line.pdf (W87-L-v1, Grades 3–5, 4 pp.), week-87-upper.pdf (W87-U-v1, Grades 4–5, 2 pp.), week-87-materials.pdf (5 pp.). Adult guide: week-87-facilitator.pdf (W87-F-v1, 6 pages). Companions noticed but not reviewed: none. Status: unpiloted. Cutting, token fit, resets and timing are unrehearsed. No K–1 packet, by design.

## The mathematics

The rankings ABC, BCA, CAB give a majority cycle, so the letter that waits always wins a two-round knockout. A letter that beats both others wins every knockout. When voters prefer the nearer location on a line, the middle of five favorites beats every other location (Black's median voter theorem). Four voters leave an unbeaten interval but no winner. The cycle cannot come from one line, because the middle candidate is never anyone's last choice. A mathematician would enjoy it. Shared P1–P3 and upper P1 carry the cycle, line P1–P4 the median, and upper P2 the impossibility.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Condorcet's paradox and the median theorem, joined by an impossibility, each provable with markers. |
| Problems | adequate | Line P1–P4 contrast in order: plain, then repeats and median ≠ midpoint, then why, then four voters. Upper P2 is a real impossibility. The agenda visit has three problems on one given profile (fix 3). |
| Student pages | adequate | Headers, footers and numbering are right, and a worked visual precedes each convention. Line stems cue the answers (fix 1); line P3 prints the conjecture (fix 2). |
| Concreteness | adequate | Cards, tokens, lanes and a Tie well hold the state; each visit has a short launch. The vote is applied by reading, checked by a partner against the unchanged card. |
| Correctness | strong | The math check confirms every answer; one guide overclaim (fix 5). I agree. |
| Adult guide | strong | Theorem-first, with assumptions, limits and a band map. Every problem is keyed with reasons, plus launch, prep, pacing and hints. Gaps: K–1 and a same-visit continuation. |
| Age fit, K–1 | weak | No route: "There is no independent K–1 edition" (guide p. 1). |
| Age fit, grades 2–3 | adequate | Adult reads; counts stay at five or below; the knockout mat holds the state; line P1–P2 is tick counting. The agenda route runs short. |
| Age fit, grades 4–5 | strong | Upper P1, line P3–P4 and upper P2 are proofs a child can do with markers. |

## Keep

- The non-task worked examples. Shared pp. 1–2 has the D/E/F vote and knockout (F beats both, so the cycle stays hidden). Line p. 1 has the five-lane launch, with distances, a tied voter and a 2–2 tally. Upper p. 2 has the distance-to-card conversion.
- Shared P1's cyclic cards, P2's three targets and P3's two contrasting constructions.
- Line P2's sets. (0, 0, 0, 8, 10) keeps a stacked majority at zero, and (0, 1, 6, 9, 10) separates the median from the midpoint and the mean. Keep "Voters sharing a favorite still get one vote each."
- Line P4 after P3, and upper P2's "or explain why it cannot be done".
- One token per voter, separate lanes and the Tie well.

## Fix

1. **should**, line pp. 1–2, P1 and the three P2 lines. Stem height is 8 + 7·(index mod 3) mm (build.py `numberline`), and voters are labelled left to right. So V3, the median, always has the tallest stem: at 4, 0, 4 and 6, every answer. A child can answer by "the tall line". Use equal stems with staggered labels, and number one P2 set out of order.
2. **should**, line p. 3, P3: "Does the third favorite from the left always beat every different location?" prints the discovery that P1–P2 build. Keep the first two sentences and replace the rest with "How can you tell which location wins without trying every vote? Explain why your way always works." Move the third-favorite question to the guide as a held prompt.
3. **should**, shared packet and guide p. 2. The agenda visit has three problems, and a letter that beats both others first appears when children must build one (P3). Upper P1 supplies that contrast without line conventions, but the guide files it as a return investigation (p. 5). Name it as the same-visit continuation.
4. **should**, K–1, guide p. 1. Nothing says what the K–1 table does. As on the Week 68 card, name another week's K–1 packet, or an adult-led shared P1–P2: the parent reads the cards and the children move the tokens.
5. **should**, guide p. 3, shared P3: "or invent another and test their claim." Only Problem 1's set and its mirror ACB, CBA, BAC work (math check, all 20 sets). Use the math check's replacement text, and change "The cards need not have identical first choices" to "Three different cards cannot share a first choice."
6. **could**, shared p. 3: move "Each ranking card must contain A, B and C once" into P3, and drop the repeated "Keep each set of cards unchanged".
7. **could**, shared p. 2: drop "The same cards stay visible in both rounds."
8. **could**, upper p. 2: drop "Favorite markers above; letter tiles below".
9. **could**, upper P1: "for each set"; "Explain how you can tell" rather than "from the pair votes", which names the method.
10. **could**, upper p. 2: add 0–10 ticks to the P2 work line, as in the worked example.
11. **could**, materials p. 4: widen Out and Winner from 29 mm to 34 mm for 28 mm tiles.
12. **could**, line p. 1: "Keep X/Y proposals on the board; use the separate X/Y tally labels" belongs in the launch.
13. **could**, materials pp. 2–3: replace the 36 slips per kit with pencil on the blank cards.

## Overlaps

Week 24's decks make a chance "beats" cycle, with no agenda. Week 27 uses ranking cards for stable pairs. Week 15's bisector is what a line voter computes. Week 67's middle-value dot minimizes path length. No other theme has voting. No merge.

## App fit

Not in themes.md yet. I propose Fit B, size M.

- **Agendas.** Fixed cards are on screen. The child taps the first pair and tokens fly to the tally; the goal is to make a named letter win. When one letter beats both others, "can't" is certified by its two pair wins. With four or five letters and longer chains, a target can win exactly when no group of other letters beats every letter outside it (the top cycle). That group is the checkable "can't".
- **Design.** Fill blank cards so that one letter always wins, or the waiting letter does.
- **Line.** Use reverse goals: move the fewest favorites so that 7 wins, or add a voter so that 5 wins. Avoid predict-the-winner and drag-until-green.
- **Impossibility.** Drag A, B, C and three favorites, and the cards update live. Certify "can't" for ABC/BCA/CAB by pointing at the card where the middle letter would be last.

Draw on shared P1–P3, upper P1, line P1–P4 and upper P2.

## Classroom evidence

None reported. Not yet taught.
