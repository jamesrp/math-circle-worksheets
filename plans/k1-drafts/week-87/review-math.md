# Math review: Week 87 K–1 draft (W87-K-v1)

Reviewed `draft/k-1.pdf` (5 pages, identical to `draft/src/k-1.pdf`) and `draft/src/k-1.tex`.
Every card set was read from the `\card` calls in the source and checked against the rendered pages.
My own script, `review-math-work/check.py`, recomputed every vote, knockout and build count. It does not use the author's `verify.py`.

**Verdict: all the mathematics is correct.** Every printed answer exists and is unique where the page expects one. All diagrams match their text and the intended cards. No problem is impossible, and none has an answer different from the one intended.
I found two minor problems that do not stop the packet working: a shortcut that solves Problem 6, and a gap in wording for Problems 7–8. Both are listed below with small fixes.

## Per-problem verification

| Problem | Asks | Intended outcome | Independent check |
|---|---|---|---|
| Opening rules, p. 1 (launch picture) | Shows a pair vote on DFE, EFD, FED | D or E: V1 votes D; V2 and V3 vote E; E wins 2–1 | Ballots D, E, E. The picture puts the V1 token under D and the V2 and V3 tokens under E, and E is circled: it matches. V3's top letter F is not on offer and V3 still votes E, which matches the rule. F beats D and F beats E (each 2–1), so the launch does not give the circle away. |
| 1, p. 1 | Cards ABC, BCA, CAB: circle the winner of A/B, B/C, C/A | A, B, C | A beats B 2–1 (V1, V3). B beats C 2–1 (V1, V2). C beats A 2–1 (V2, V3). The card pictures match the cut cards. |
| 2, p. 2 | Knockouts with the first pair and waiting letter given: BC wait A, CA wait B, AB wait C | A, B, C (the waiting letter always wins) | First winners are B, C, A; final winners are A, B, C. The diagrams match the outline's three knockouts. |
| 3, p. 3 | Printed cards CBA, BAC, CBA: which letters can win a knockout? | C only | B beats A 3–0. C beats A 2–1 and beats B 2–1. All three knockouts give C (A waits: C; B waits: C; C waits: C). A loses both of its votes, and B loses to C. |
| 4, p. 4 | Printed cards ABC, BAC, CAB: which letters can win? | A only | A beats B 2–1 and beats C 2–1; B beats C 2–1. All three knockouts give A. C loses both of its votes. |
| 5, p. 5 | One swap on one fixed card so that B wins whoever waits | Possible: 3 of the 9 swaps work | V1 ABC→BAC, V3 CAB→BAC and V3 CAB→CBA each make B the only winner. All 9 swaps make the letter that moved up the only winner. None of V2's swaps work, so trying them gives children cases that fail. |
| 6, p. 5 | Build three cards (each with A, B, C once) on which C wins whoever waits | Possible | 68 of the 216 ordered card sets work. Every set with C on top of 2 or 3 cards works (56 sets). |
| 7, p. 5 | Can C win whoever waits with C on top of exactly one card? | Yes, but rarely | Only 2 of the 20 card sets (repeats allowed; 12 of 96 orderings) work: {ACB, BCA, CAB} and {ACB, BCA, CBA}. C must be second on both other cards, one topped by A and one by B. |
| 8, p. 5 | Can C win whoever waits with C on top of no card? | No | 0 of 20 card sets (0 of 64 orderings) work. C has to beat A on two cards and beat B on two cards. A card without C on top puts C above at most one letter, so three such cards give at most 3 of the 4 wins needed. |

The script also confirmed, over all 216 card sets, that "wins whoever waits" means exactly "beats both other letters in pair votes" when there are three voters. Problems 3–8 depend on this. No pair vote ties, and no count goes above three (the largest is Problem 3's 3–0).
Neither printed set (Problems 3 and 4) repeats upper Problem 1's sets {ABC, ACB, BAC} or {ACB, CBA, BAC}.

## Located problems

### 1. K–1, page 5, Problem 6: copying an earlier set solves it (minor)

Text: "Build three cards V1, V2 and V3 from blank cards and letter slips, with one A, one B and one C on each card. Make C win, whoever waits."

Evidence: Problem 3 (page 3) prints V1 CBA, V2 BAC, V3 CBA, and C wins all three knockouts on those cards. A child can solve Problem 6 by copying the Problem 3 picture onto the blank cards. The outline says children should never copy a printed set onto blank cards, and copying skips the building that leads into Problems 7–8.
Changing only Problem 6's letter does not help. A wins on Problem 4's printed set, and B wins on the set the child just made in Problem 5, so each letter already has a set to copy.

Smallest fix: change Problem 3's cards so that its only winner is B, and leave everything else as it is. For example, use **V1 BCA, V2 CAB, V3 BCA**.
- On these cards B beats A 2–1, B beats C 2–1 and C beats A 3–0. All three knockouts give B. A loses both of its votes, and C loses only to B.
- The set keeps the draft's features: one repeated card, one 3–0 vote, and only one letter that can win.
- It contains neither BAC nor CBA, so it does not print an answer to Problem 5.
- After this change no printed set on the pages makes C win, and the only winners of Problems 3, 4 and 6 are B, A and C.

Other sets that pass the same checks: {ABC, BCA, BCA} and {ACB, BCA, BCA}.

### 2. K–1, page 5, Problems 7 and 8: the card rule is not repeated (low)

Text: "Problem 7: Can C win, whoever waits, if C is on top of just one card?" and "Problem 8: Can C win, whoever waits, if C is not on top of any card?"

Evidence: the rule "one A, one B and one C on each card" appears only in Problem 6, and the opening rules do not state it. A child might read Problem 8 as "keep C off the top row" and leave the top row empty. Cards (empty), C, A / (empty), C, B / (empty), C, A then give C 3–0 against A and 3–0 against B. Under that reading the answer to Problem 8 changes from No to Yes.

Smallest fix: begin each problem with "Build three cards the same way." For example: "Problem 8: Build three cards the same way. Can C win, whoever waits, if C is not on top of any card?" Another option is to move "Each card has A, B and C once" into the opening rules.

## Notes (no change required)

- Problem 4's set is the fixed cards with V2's C and A swapped (BCA→BAC), and A, the letter that moved up, wins. This shows Problem 5's method in advance with a different letter. The sequence is legitimate, but the facilitator guide should say so.
- Putting C on top of every card solves Problem 6 at once. That is a reasonable entry point, and Problems 7–8 carry the depth. Problem 7's answer is Yes, but only 2 of the 20 card sets work. Children who try at random may decide "no", so the adult notes should give an example such as BCA, ACB, CAB.
- Not a math issue, but the brief should know: Problem 6 is close to the first half of shared Problem 3 ("Make three different cards so that the same letter wins every knockout"). It is not a reprint: K–1 allows repeated cards and fixes the letter as C.
