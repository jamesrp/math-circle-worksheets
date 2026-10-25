# Review of draft/k-1.pdf (Week 91 K–1, F91-K-v1)

Reviewer stage. I rendered all 7 pages at 110 dpi, plus zoomed crops (`review-render/p-1.png` … `p-7.png`). I read `draft/src/build.py`, `check.py` and the log, and re-simulated every answer independently (`review-render/verify91.py`, run with `python3 -I`). The draft was not edited.

## Summary

The packet follows the brief and the organizer's page standard closely. The header, footer, page numbers and consecutive "Problem N:" labels are correct. There are no titles, no encouragement, no hints and no exclamation marks, and no sentence describes a diagram. The one-move picture uses a blank board, as asked. The order of problems follows the outline: kernel 1 with the coin contrast (P1–P4), then kernel 2 on the four-exit tree (P5–P7), then kernel 3 late (P8–P9). Every possible/impossible answer is correct (details at the end). The packet also avoids the older band's problems: none of its targets match XYXY/XXYY/YXYX/XYYX, the D-first problem, or the older first pairs AC, BD, AB and DA. Its strongest features are the contrasting pile pictures with impossible cases (P2, P6, P9) and the prediction tables that compare card and coin (P4). Keep these.

One major problem affects five of the nine problems. Starting arrows are recorded after the counters have flipped the cards, and the board's final state usually shows a different start, often one that answers a different picture. Smaller issues: the coin experiment in P3 may not succeed often enough, the tree's main fairness fact is never asked, the "from every start" and "no start can" problems give no way to keep track of which starts were tried, two problems are too long to take in on one hearing, and several layout details need work.

---

## Major

### 1. The starting arrows have to be recorded before the counters go, but five problems ask for them after (P2, P6, P7, P8, P9)

Every counter flips the cards it passes. After the counters are sent, the board shows the starting arrows only when every card has flipped an even number of times. A child who builds the piles first and then copies the cards into the picture (the order the wording suggests) records the wrong start. In P6 and P7 that wrong start is often a correct answer to a different picture, so the adult checking the page cannot see the mistake.

Evidence from simulation (start → board after the trial):

- **P2** ("Make the piles … and draw a starting arrow that makes them"). Each possible picture except 3/3 needs an odd number of counters (3, 5, 9). After the trial the card shows the opposite of the start in every one of those cases. Example: X2 Y1 needs first arrow X, and the card ends on Y.
- **P6** (6 counters). The top card is back where it started, but both lower cards have flipped three times. LLL makes picture 1 (A2 B1 C2 D1) and ends on LRR, which is a start for picture 3. LRR makes picture 3 and ends on LLL, a start for picture 1. So copying the board after a success records an answer to the other possible picture.
- **P7** ("B the first exit to get two"). B's second counter is counter 5. If you stop there, LRL ends on RLL and LRR ends on RLR, and those are exactly the two "B last" starts. A child who stops at counter 5 and copies the cards writes a "B last" answer in the "B first" tree.
- **P8** (1 counter). RLL ends on LLR. **P9** (2 counters). A-then-D: LLR ends on LRL, which sends B then C.
- **P5** is the only safe problem: after four counters every card is back at its start. It is also the only problem worded in the safe order: "draw your starting arrows, and send four counters".

The brief names the remedy ("With the four spares, a pair can lay a copy of its starting arrows beside the board, a record that needs no writing"), but no page sets it up.

**Fix (smallest).** Add one sentence to the shared rules on page 1, for example: "Draw the starting arrows before the first counter." Or, as a no-writing alternative: "Lay a spare card beside each card to show its starting arrow." Then make P2 and P6 follow P5's order ("draw a starting arrow, then send the counters …"). Put a matching warning in the facilitator guide when one is written.

---

## Moderate

### 2. P3's second question depends on luck, and five rows is too few to settle it

"Can 7 tosses put 5 counters on X and 2 on Y?" One row of 7 tosses gives 5 X and 2 Y with probability 21/128 ≈ 16%. Over the five printed rows (35 tosses, a long job for K–1), the chance of seeing it at least once is only 59%. About 4 pairs in 10 will fill every row without seeing it. They will then reasonably answer "no" for the coin, which is the same answer they gave for the card in P2. That reverses the contrast the problem exists to show (the kernel's point is that the coin can make any order).

**Fix options.**
- (a) Ask for "5 on one exit and 2 on the other": 33% per row, 86% over five rows. P2's 5/2 picture can still be the reference.
- (b) Use a 4-toss case, which matches the kernel's 4-toss counts: "Can 4 tosses put 3 counters on X and 1 on Y?" (25% per row, 76% over five rows). Shorter rows also mean less to write.
- (c) Keep the question but drop the fixed five-row frame, so tossing continues until it happens, and note in the guide that "I didn't see it" is not "it can't happen".

The first question ("two counters in a row on the same exit") is fine: 126 of the 128 possible 7-toss orders have such a pair.

### 3. The tree's main fact, fair sharing from every start, is never asked

Kernel 2's title fact is "the four-exit tree shares fairly from any start": eight counters give 2 to each exit, and counters 5–8 repeat 1–4. P5 checks the first four counters, P6 asks about the uneven state after six, and P7 asks about second arrivals. No problem has children send 8 (or 12) counters and decide whether the piles always come out even. That would be the tree's counterpart of P1 and P2, and it is a possible/impossible decision K–1 can make. P7's "B last" trial happens to reach 8 counters, but the question there is about B.

**Fix.** Add two pile pictures for 8 counters to P6, one possible (2/2/2/2) and one impossible (for example 3/1/2/2), or change one existing picture. Or add a short problem before P6: "Send 8 counters from different starting arrows. Can one exit end with more counters than another?" A tree version of P4 ("Your partner sets the cards and sends four counters. Guess where counter 5 lands …") would also bring out the repetition, if there is room for it.

### 4. Problems about every start, and about no start, give no way to keep track of the starts already tried (P5, P6)

- **P5** asks "Can two of the four counters land on the same exit?" The answer is "never, from any start", and there are 8 starts. The page gives 6 recording trees, so a pair cannot record every start on its own sheet. **Fix:** give 8 trees, in two rows of four compact trees (the compact tree already used for P8 fits). The guide can then suggest that the table's two pairs pool their starts.
- **P6** asks the children to cross out pictures "that no starting arrows can make". Settling that by trial means knowing that all 8 starts have been tried (48 counters). The page has only the four target trees, so failed starts go unrecorded and children cannot tell which starts they have covered. Fixing item 1 helps, because a drawn start then really is the start. Beyond that, either give a row of small blank trees as extra workspace, or point back to the P5 record, which already lists the starts tried (once item 1 is fixed, every start drawn in P5 is a true start).

### 5. Two problems need more than one hearing (P3, P4)

The standard says K–1 problems should be one or two short sentences that make sense after one hearing.

- **P3** has three sentences, and the first holds the whole coin rule after a colon. The brief already says the adult says which face sends a counter to X, so a shorter version would be: "Put the card away and toss the coin to choose X or Y for each counter. Can the coin put two counters in a row on the same exit? Can 7 tosses put 5 counters on X and 2 on Y?" Or simply drop the clause naming the faces.
- **P4** has three sentences and packs in two games and four rounds ("Play again for counters 8, 7 and 4, and then play with the coin."). The tables already show the rounds (5, 8, 7, 4) and the second game (the "coin" label), so the text can lean on them. For example: "Your partner sets the card and sends one counter. Guess where each counter in the table will land, and then send counters to see." The coin table then explains itself once the adult points to it.

---

## Minor

### 6. The circles children draw arrows in are at the small end, although the pages have room for bigger ones

All tree circles, including the compact ones, are 18 mm across (`r = 9.0` in `tree()`), and the P2 circles are 21 mm. Drawing 18 slanted arrows in 18 mm circles (P5) is a real fine-motor job for kindergartners. Pages 2, 5, 6 and 7 leave about 56, 69, 60 and 69 mm empty above the footer. Enlarging the circles in P6, P7 and P9 toward 24 mm (the board's own size) would use that space and make drawing easier. Also, keep page circles visibly different from the board's 24 mm card circles, so children are not tempted to set cards on the sheet.

### 7. Shared-rules wording

- "set each card to point either way" is ambiguous when read aloud ("either way" can sound like "both ways" or "it doesn't matter"). Suggest: "point each card the way you choose".
- The rules and the picture show a counter waiting beside the top card only. The brief stresses "A counter waits beside a card, not on it". On the tree, the counter's stop beside the lower card is neither stated nor drawn. It can be shown in the launch, but "At each card it waits beside the card, moves where the arrow points …" would cover it in a few words. Optional.

### 8. The one-move picture is misaligned

The three panels are bottom-aligned on their bounding boxes. The "flip" label has a descender, so the whole third panel sits about 1 mm higher than the other two, which is visible in the rendered page (exit boxes and labels not level). Fix: give the tikzpictures a common `baseline=(0,0)`, or set the labels with `anchor=base` at a fixed y.

### 9. P8 has three trees for two answers

The answer is exactly two starts (RLL and RRL; the left card is never touched). A spare tree is a defensible way not to give away the count, but K–1 children tend to treat empty frames as things to fill, and may "find" a third way by repeating one. Consider four trees (still not suggesting the count), or make sure the guide anticipates this. This is a judgement call, not an error.

### 10. Bold "card" and "coin" labels

The labels above the P4 tables are set in bold `\large`, so they look like section headings. In normal weight they would read as table labels.

### 11. `check.py` checks the wrong counter

`check.py` checks counter 11 for P4, but the page asks for counter 7. This is harmless, since both are odd, but the check should match the page.

### 12. Staffing and writing load (for the guide, not the page)

P1, P3 and P4 each call for letters written in order. With one parent volunteer for two pairs, the adult can become the bottleneck if they write for both pairs. Most first graders can write X and Y, but the guide should say who writes. Physical rehearsal of the kit with K–1 has not been done; the pages cannot establish it, and nothing here claims otherwise.

---

## Answer check (independent simulation, all correct as posed)

| Problem | Answer |
|---|---|
| P1 | From either start the arrivals alternate (XYXYXYXYXY or YXYXYXYXYX). Two in a row never happens. |
| P2 | X2 Y1: start X. X3 Y3: either start. X2 Y3: start Y. X5 Y2 (7 counters): impossible. X5 Y4: start X. X3 Y5 (8 counters): impossible. |
| P3 | Two in a row on the same exit: possible (126/128 of 7-toss orders). 5 X and 2 Y in 7 tosses: possible, probability 21/128 (see item 2). |
| P4 | After counter 1, counters 5 and 7 land where counter 1 did, and counters 8 and 4 land on the other exit. The coin gives no prediction. |
| P5 | From all 8 starts the first four counters reach four different exits, so two never share an exit. |
| P6 | A2 B1 C2 D1: LLL or RLL. A2 B2 C1 D1: impossible (always 3 go left and 3 go right). A1 B2 C1 D2: LRR or RRR. A1 B1 C2 D2: impossible. |
| P7 | B first to get two: LRL or LRR (at counter 5). B last to get two: RLL or RLR (at counter 8). |
| P8 | Two ways: RLL and RRL. |
| P9 | A then D: LLR only. D then C: impossible. C then B: RRL only. B then A: impossible. |

Cards are listed top, left, right, with L meaning the arrow points down-left.
