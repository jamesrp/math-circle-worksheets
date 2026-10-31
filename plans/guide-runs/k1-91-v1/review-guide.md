# Review: Week 91 K–1 adult guide, draft v1 (F91-K-FAC-v1)

**What I read.** I read the guide (`draft/k1-guide.pdf`, 4 pages, and its `.tex` source), and the final student pages (`plans/k1-drafts/week-91/k-1.pdf`, 7 pages). I rendered and read every page of both. I also read:

- the outline, both page reviews and the draft's entry in `plans/k1-drafts/README.md`;
- the week's guide (F91-FAC-v3) and materials file (F91-M-v1);
- the Week 98 model guide.

I did not edit the guide or the pages.

**How I checked.** I wrote `review-guide-check/check91.py` before looking at the writer's checker. Its output is in `review-guide-check/check91.out`. The script:

- reads the pile dots, counter labels, numbered exits, recording boxes and tree counts directly from the student PDF;
- simulates the switch from both starts, and the four-exit tree from all eight starts up to counter 48;
- lists every coin word;
- measures the boards, cards, strips and scale bar in the materials file;
- finds where the K–1 route sits in the week's guide.

Every printed answer agrees with my checks:

- P2 and P6 tables;
- P4 same/other pattern;
- P3's 42/128 and 9.2%;
- the eight-start key;
- P7 (LRL/LRR at counter 5; RLL/RLR at counter 8);
- P8 (RLL, RRL);
- P9 (LLR; impossible; RRL; impossible).

All page numbers, problem numbers, tree counts (9, 2, 3, 4), row counts (4 × 10, 6 × 7) and material sizes match. Those sizes are 32 mm circles on p. 1, 24 and 30 mm circles on p. 2, 18 × 22 mm cards, and strips of twelve 15 mm squares. Afterwards I ran a copy of the writer's checker in `/tmp`, and it passes.

**Verdict.** This is a correct and well-keyed guide, and nearly ready. It has one must-fix: one sentence in the overview misstates what counts as proof of impossibility. The should-fix items are about running the K–1 table:

- moving onto the three-card tree;
- a first route that fits the hour;
- how much writing and drawing the pages ask for;
- what to record from this first, unpiloted use.

## Must-fix

### 1. "A failed search alone does not prove impossibility" is false here (p. 1, "Destination and evidence")

**The problem.** The switch has two starts and the tree has eight. Trying every start and failing *is* a proof for these machines, and the guide relies on this itself:

- p. 2: "The two starts exhaust the choices";
- p. 4: "The start list proves these are all the choices".

At K–1 the most natural proof that P2's picture 4 or 6 cannot be made is "we tried this arrow and that arrow and neither worked." Read plainly, the sentence tells the adult not to accept that proof. The sentence also blurs the coin contrast. A coin failing to show 5 and 2 proves nothing because the coin has no list of starts to exhaust. That is a different situation from a search that has tried every start.

**Fix.** Replace the last sentence of the paragraph with:

> "Successful trials prove possibility. Failure proves impossibility only when every start has been tried: both arrows on one switch, or all eight starts on the tree, pooled across pairs. Tosses that never show a result prove nothing."

## Should-fix

### 1. Problem 7's closing sentence reads as a false claim, and the rule the problem turns on is never stated (p. 4)

**The problem.** "Thus B must be first or last in that first round" reads as a general statement. It is false: from LLL, B is third, and from RRL, B is second (p. 3's own table). The fact children can use is missing:

- counter 5 always lands where counter 1 did, so the first exit to reach two is counter 1's exit;
- counter 8 repeats counter 4, so the last exit to reach two is counter 4's exit.

**Fix.** Replace the last two sentences before the hint with:

> "Counter 5 lands where counter 1 did, and no exit gets a second before all four have one. So the first exit to reach two is counter 1's, and the last is counter 4's (at counter 8). B first needs B as counter 1; B last needs B as counter 4."

### 2. There is no move onto the three-card tree, and no recovery from a slip (pp. 2–3)

**The problem.** The only demonstrated move is on a single switch. Problem 5 starts the tree, where each counter stops twice and two different cards flip. The page review noted that the stop beside the lower card is neither stated nor drawn on the pages. The outline names the slips that silently change answers:

- flipping the wrong card;
- resetting a card "to help";
- setting the counter on a card.

The guide says neither how to show one tree move nor what to do after a slip during a trial.

**Fix.** Add two sentences before Problem 5's answer, or in the first-route paragraph:

> "Before Problem 5, a child sends one counter on the four-exit board while the adult names each step: wait beside the top card, move, flip it; wait beside the lower card, move, flip that card. If a card is flipped wrongly or reset during a trial, clear the exits, set the cards from the saved copy and start again."

One counter from any start answers nothing in Problem 5.

### 3. The first route gives no priority within Problems 1–2, and the 15 minutes is tight (p. 2, "A one-hour first route")

**The problem.** Problem 2 alone needs at least 53 counter moves, and up to 76 (check output). That minimum assumes each possible picture is made at the first try and both arrows are tried for the two impossible ones. On top of the moves come:

- clearing exits;
- laying saved cards;
- drawing six arrows.

Problem 1 adds 20 moves and 20 letters for one row from each arrow. All of this is at K–1 pace, with a partner check on every move. The guide hedges ("adjustable estimates") but does not say which pictures matter most. The two-minute table demonstration is also missing from the 60-minute budget.

**Fix.** Give Problems 1–2 about 20–25 minutes. Name a first subset of Problem 2: pictures 1 (2,1), 3 (2,3) and 4 (5,2), which give one picture for each arrow and one impossible picture. Make Problem 5 "if 15 minutes remain" rather than a fixed slot, and count the table demonstration in the setup time.

### 4. The writing and drawing load is not stated, and neither is which answers need no record (p. 1, "Prerequisites and staffing"; p. 2)

**The problem.** The guide says the adult writes "when needed". It does not say how much writing the pages can ask for:

- P1: up to 40 letters;
- P3: up to 42 letters;
- P4: 16 entries;
- P2 and P5–P9: 78 circles for drawn arrows, 18–21 mm across.

With one adult for two pairs, the adult becomes the scribe for all of it.

**Fix.** Add a sentence:

> "Writing is optional where the board shows the answer: P3's five-and-two question can be read from the exit piles, and the two-in-a-row questions can be watched. One written row from each arrow is enough. A child who cannot yet draw a slanted arrow can draw a slanted stroke, or point to the saved card while the adult draws it."

### 5. The guide does not say what to record from the first use (whole guide)

**The problem.** Everything here is unpiloted, and the guide lists many physical steps that are untested. Yet it never asks the adult to note what happened. The Week 98 model ends with what to record, and AGENTS asks that observed experience change the design.

**Fix.** Add one line before "Where it goes":

> "Record preparation time, which problems were reached, missed or wrong flips, whether the saved cards were laid and copied correctly, who did the writing, and which pictures children crossed out and why."

## Minor

1. **Overview, "what children discover" (p. 1).**
   - "Small possible/impossible programs" uses "programs" as jargon.
   - Two facts the pages turn on appear only in the solutions: the extra counter goes to the first arrow's exit (which picks the arrow in P2), and after counter 1 every later counter is known (P4).
   - **Fix:** "K–1 finds that the switch never repeats an exit, so the piles differ by at most one and the extra counter goes to the first arrow's exit. After one counter, every later counter can be predicted. Four counters on the tree always reach four exits. Setting two cards sends the first counter where you choose."
2. **Launch figure (p. 2).**
   - It redraws the student p. 1 picture but labels it "Input / Move / Flip", where the page says "start / move / flip".
   - **Fix:** Use the page's labels. Alternatively, drop the figure and write "as in the picture on student p. 1; the card at its left is the saved copy." Also say the scrap-paper circle must be at least 24 mm across so a card fits.
3. **"Bring scissors, glue and scrap paper for the demonstration" (p. 1).**
   - Scissors and glue are for making cards; only the scrap paper is for the demonstration.
   - **Fix:** Split the sentence.
4. **Arrival strips (p. 1).**
   - Two strips per pair are listed, but only Problem 4 mentions one ("if needed").
   - **Fix:** Say they are an optional counting aid for Problems 4 and 7, or drop them.
5. **Sentences that read like notes to a reviewer, and repetition (pp. 1, 3, 4).**
   - Cut these sentences:
     - "no special object is missing from the print kit";
     - "Coins, counters and stationery are supplied, not printed";
     - "The cups, if used, are additional supplied objects";
     - "A proposed sequence is not a claim that those tosses actually occurred";
     - "These reasons cover every start, as does the complete eight-start list".
   - The saved-card instruction appears six times. Keep the launch statement and the specific P2, P6 and P7 warnings.
   - The card-word convention is defined on p. 3 and again on p. 4.
   - The section runs to 2,313 words. The whole Week 98 guide is 3,025.
6. **Wording that puts the adult in charge of the explanation (pp. 3–4).**
   - P5: "before giving the full argument" → "before asking why".
   - P8: "then show its two settings" → "then ask the child to draw both settings".
7. **"Where it goes" (p. 4).**
   - The replaced section is correctly identified: p. 2, "K–1 route, adult-read", through two lines at the top of p. 3.
   - The week's guide p. 1 still says K–1 has an adult-read route, "not an independent packet". After replacement, that sentence contradicts the new section.
   - **Fix:** Add: "and update the p. 1 overview sentence on K–1 to point to this section."

## What works and should be kept

- **Correct, current answers.** Every answer is correct and keyed to the final pages:
  - ten counters in P1;
  - five and two "in either direction" in P3;
  - P4's 5, 8, 7, 4 order;
  - nine trees in P5;
  - the added 8- and 12-counter pictures in P6.

  Every "find all" list (P2, P6, P7, P8, P9) has a reason why it is complete.
- **A theorem-first overview.** It states the assumptions (no resets, one counter at a time, an equal-depth tree) and the limit (not arbitrary trees or roads). Its explanations a child can give with objects are the paired arrivals and the two-and-two split. It separates experiment, conjecture and explanation, and points to the week's guide rather than repeating the road mathematics.
- **The saved-card hazard, handled concretely.** P2: after an odd number of counters the card points the other way. P6: the lower cards have flipped three times. P7: draw before testing, even when stopping at B's second counter.
- **The coin contrast.** It gives the face-by-face witness, the 9.2% chance of missing the split across all six rows, and a hint that is a question ("What faces would make the piles?").
- **P4's out-of-order rows.** Guess all four first, then fill in the arrivals in order within one trial.
- **Spare frames.** The spare frames in P5 and P8 are explained, and the guide accepts "the left card doesn't matter" as the structural answer in P8.
- **Staffing.** "Rather than let the adult run either machine" keeps the choices with the children. Every hint is a question.
- **Kit and layout.** The kit additions match the outline and the week's materials (14 cards, 32 counters, 2 coins, about 30 minutes). Headers, footers and layout are clean.

## On the writer's report

- **Issues 1–4 (preserving starts, coin misses, P4 row order, spare frames).** I agree, and the guide handles each well.
- **Issue 5 (writing load).** I agree it is a risk, but the guide only names the bottleneck. Should-fix 4 asks it to quantify the load and say which answers need no writing.
- **Issue 6 (the p. 1 sentence).** I agree. Put it in the guide's own "Where it goes" sentence, since the report will not travel with the guide.
- **What the report misses.** It does not flag the overview's sentence about failed searches (must-fix 1), the P7 closing sentence, or the missing demonstration for moving onto the tree.
