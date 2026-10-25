# Review of draft/k-1.pdf (Week 81, Buckets of Fish, K–1, W81-K-v1)

Reviewer stage. I rendered all 7 pages (80 dpi, plus 150 to 200 dpi crops of pages 1 and 3), read `draft/src/k-1.tex` and `build.py`, compared the kit against the shared packet `lowell-math-circle-year-2/week-81/week-81-students.pdf` (W81-S-v3), and checked every answer with my own solver (`moves`, win/lose labels, all game lengths, board peak, winning moves, and the "must refill" misreading). I did not use the author's `check.py`.

## Verdict

This is a strong draft that is close to final. The mathematics on the pages is correct, the sequence follows the outline, and the page format matches the standard. K–1 gets real game theory and a real termination question with few words. Four problems need changes before it goes to the organizer. Fix 1 and 2 first, because each one can make a child get a wrong answer or have no answer to find:

1. The rule picture shows only the refill, which supports the misreading "may" = "must". Under that misreading, five printed tasks change answer or have no solution.
2. In Problem 9, "at one time" can mean "in one move".
3. Problem 5 has four answer rows for three partner moves, and nothing links the start to the rows.
4. Problem 6 has four slots for "4 counters", which has three answers, and four slots for "6 counters", which has exactly four.

The rest is moderate or cosmetic.

## What works (keep it)

- **Rule wording.** It meets every constraint in the outline. The refill is optional ("may"), the refill bucket is named by number, a counter can never go back where it came from, and the removed counter goes to Removed while new ones come from Supply. A partner can check a move by watching it.
- **Order of ideas.** One bucket comes first as the base case (P1). Then two buckets: who can always win (P2), the winning first move (P3), against the adult (P4), and every partner reply from (2,2), which is the copy without naming it (P5). Then the children use pairs (P6) and explain an impossibility (P7). Kernel 2 follows: shortest and longest games (P8), the board growing (P9), the longest three-bucket game (P10), and whether a game can go on forever (P11). Three buckets come late, as the outline asks.
- **Targets the children already know.** Every target of P12 is a position from an earlier problem: (2,0,0) is P1's "2", (0,2,0) and (2,2,0) are from P2. Most targets in P3 were met earlier too: (4,0) is P1's "4", and (2,0), (0,2), (2,2) are from P2. Keep these.
- **Contrasting cases.** P3 contrasts (1,1), won only by refilling, with (2,1) and (2,3), won only by not refilling. P12's four starts are all won from bucket 3, with no refill, one refill or two.
- **Sizes stay in range.** Two-bucket longest games are at most 9 moves (P8) and three-bucket ones at most 12 (P10). Sorting cards are not copied, and no older-band problem is reused.
- **Format.** Header and footer are correct and there are no extra headings, exclamation marks, hints or follow-up prompts. "Explain" appears only where explanation is the point (P7, P11, and "show the adult how" in P4).

## Mathematics: every answer checked independently

| P | Starts | Verified answer |
|---|---|---|
| 1 | 2, 3, 4, 5, 6, 7, 10, 11 in one bucket | 2nd, 1st, 2nd, 1st, 2nd, 1st, 2nd, 1st (forced games) |
| 2 | (1,1) (2,0) (0,2) (2,1) (1,2) (2,2) | 1st, 2nd, 2nd, 1st, 1st, 2nd |
| 3 | (1,1) (2,1) (1,2) (3,1) (2,3) (3,3) | Each has exactly one winning move: (2,0), (2,0), (0,2), (4,0), (2,2), (4,2) |
| 4 | (4,2), (3,4) | 2nd wins (games last 6–8 moves); 1st wins only by moving to (2,4), taking from bucket 1 (7–11 moves, at most 7 counters) |
| 5 | (2,2) | The partner has exactly **3** moves: (1,2), (2,1), (3,1). The only winning replies are (0,2), (2,0), (4,0), and each one is the copy |
| 6 | 4 and 6 counters | 4: (0,4), (2,2), (4,0), so **3** ways. 6: (0,6), (2,4), (4,2), (6,0), so **4** ways |
| 7 | 5 counters | Impossible: any split leaves an odd bucket |
| 8 | (0,1) (0,2) (0,3) (1,1) (2,2) (3,3) | Shortest / longest: 1/2, 2/4, 3/6, 2/3, 4/6, 6/9 (every length in between can occur) |
| 9 | (0,0,1) (0,0,2) (0,0,3) | Most counters on the board at once: 2, 4, 6 |
| 10 | same starts | Longest game: 4, 8, 12 |
| 11 | (3,3,3) | No game goes on forever. Longest is 21 moves; the board can reach 12 counters |
| 12 | (2,0,1) (1,0,1) (0,1,1) (1,1,1) | Each has exactly one winning move: (2,0,0), (2,0,0), (0,2,0), (2,2,0) |

The worked move (0,2) → (1,1) is legal. If a counter may go back into its own bucket, (1,0) and (1) can cycle forever; the printed rule correctly rules this out.

Outline error, not on the pages: the outline lists "(1, 2, 1) 3 and 9". The shortest game is **4** (a + b + c = 4); the longest, 9, is correct. Pass this on to whoever writes the guide.

## Issues, in order of priority

### 1. The rule picture shows only the refill, which supports "may" = "must" (page 1, shared rules). Must fix.

The only worked example is (0,2) → take from bucket 2 → put one in bucket 1 → (1,1). A kindergartner who sees only that move will copy it. The outline warns that this misreading changes answers. I checked what happens to the printed tasks when every move must refill:

- P2: (2,1) becomes a second-player win.
- P3: (2,1) and (2,3) have **no** winning first move, so the child is asked for something that does not exist.
- P12: (2,0,1) and (0,1,1) have **no** winning first move.
- P8: the "shortest" and "longest" games become the same length.

**Fix.** After the removal panel, branch into both results. Draw (0,1) with Supply unchanged and (1,1) with one counter taken from Supply, with two arrows or a small "or" between them. Three-plus-one panels fit the existing 40 mm strip if the panels shrink slightly. This also shows the partner what they must accept as legal. Using a start that is not a task instance would be slightly better than (0,2), which appears in P2 and P8. That is optional, because showing one move from (0,2) reveals nothing about who wins.

### 2. Problem 9: "at one time" is ambiguous, and the problem is long for one hearing (page 5). Must fix.

"Work together to get as many counters into the buckets at one time as you can." A child can hear "at one time" as "in one move". The answer would then be 2 for every start, since the most one move can add is two counters, from bucket 3. "Get as many counters into the buckets" can also be heard as "put in as many counters as you can", which counts refills rather than what is on the board. The problem is also four sentences long and introduces a new rule. That is the longest K–1 prompt in the packet, against the standard of one or two short sentences.

**Fix.**
- Separate the rule from the task.
- Show the bucket-3 move in a small three-panel picture, as page 1 does for bucket 2, using a start that is not a task (for example (1,0,2) → take from bucket 3 → (2,1,1)). This is the first use of a new procedure. The parent volunteer is not a mathematician, and the session-2 lamp failure came from a rule that existed only in words.
- Reword the task without "at one time", for example: "Work together to make the buckets hold as many counters as you can. Write the most they hold."

### 3. Problem 5: four rows for three moves, no link from the start, and "draw a move" (page 3). Should fix.

- From (2,2) the partner has exactly three moves, but the page gives four row pairs. K–1 children, and a parent without a guide, will try to fill the fourth row. The likely results are a repeat or an illegal move such as (1,3), taking from bucket 1 and adding to bucket 2, which is the misreading the outline warns about. Either print three rows, accepting that this reveals the count (the real task here is the replies), or keep four rows and make sure the guide says one row stays empty. I lean toward three rows for K–1.
- The start sits alone at the left, vertically centred, with no arrows to the rows. A pre-reader cannot tell that column 1 means "after your partner's move" and column 2 means "after your reply". Draw a fan of short arrows from the start to each left-column pair. That is a visual connection, not a sentence describing the diagram.
- "Next to each, draw a move that lets you always win" should say what P3 and P12 say: "draw the buckets after a move that lets you always win". As written, a child may try to draw the move itself, with arrows or a hand.

### 4. Problem 6: the slot counts hint at a wrong count, and empty buckets are ambiguous (page 4). Should fix.

- The "4 counters" row has 4 slots for 3 answers, and the "6 counters" row has 4 slots for 4 answers. A child who has found (0,4), (2,2) and (4,0) is invited to add a fourth, which will be (1,3) or (3,1), both first-player wins. **Fix:** give both rows the same number of slots that matches neither answer. Five slots per row works: 4 counters has five splits in all, so a child who draws every split and circles the winners fits too. Seven slots for the 6 row is also fine.
- Readings that change the answer: if "put 4 counters into buckets 1 and 2" is heard as "some in each bucket", the answers drop to 1 and 2. If (2,4) and (4,2) are heard as "the same way", they drop further. P2 already shows empty buckets, (2,0) and (0,2), as legal starts, which supports the intended reading. The guide must say to accept empty buckets and to treat (2,4) and (4,2) as different. Nothing needs to be added to the page.

### 5. Problem 11's start (3,3,3) is larger than the outline's three-bucket bound (page 6). Moderate.

The outline caps three-bucket starts at (2,2,2) and calls its 14-move longest game "more than K–1 should count". (3,3,3) starts with 9 counters, can reach 12 on the board, and allows a 21-move game. The question does not require counting, but the natural way for a child to test "forever" is to play a long game. The kit's 30 counters per pair are enough, since at most 21 counters are used. **Fix:** use (2,2,2) (longest game 14, peak 8), which keeps the "could this go on and on?" feel inside the stated bound. Alternatively, keep (3,3,3) deliberately and note in the guide that a test game can run to 21 moves.

### 6. Circle choices "goes first / goes second" (P1, P2, P4). Moderate.

Kindergartners cannot read these words, so the adult must tell them which is which 16 times. "1st" and "2nd" are readable by K–1 children, shorter, and keep the same meaning. Consider replacing the words.

### 7. Problems 9 and 10 use the same three starts. Judgment call.

The longest game in P10 is the same always-refill play that reaches P9's peak, so a pair that finishes P9's game has mostly done P10. The identical starts do give the clean patterns 2, 4, 6 and 4, 8, 12, with each bucket-3 counter worth 2 on the board and 4 moves, which is the kernel-2 insight. That argues for keeping them. If the reviser wants more contrast, P10 could use (0,1,1), (1,1,1) and (0,0,3) (longest 6, 7 and 12), which also checks that children refill on bucket-2 takes in a three-bucket game. Either way, do not lengthen P9.

### 8. Bridge from picture to board. Low.

No problem says to set up the pictured counters on the kit board. "Play from each start" assumes the launch showed this. Since this is the children's first contact with the pictures, P1 could say "Put counters in bucket 1 like each picture, and play." Otherwise make sure the guide's launch covers it.

### 9. Supply and Removed in the rule picture look like buckets. Low.

They are drawn as rounded boxes the same width as the buckets, placed directly under buckets 1 and 2. The bucket numerals sit between each bucket and the box below, so "1" could be read as labelling Supply. On the kit board (W81-S-v3, page 2), Supply and Removed are wide square-cornered boxes spanning the board below all three buckets, labelled inside. Drawing them that way, with a little more vertical gap, matches what the children see and keeps Supply visibly "not a bucket", as the outline requires.

### 10. Typesetting. Low.

Justified 12 pt text stretches spaces, and LaTeX's sentence spacing adds wide gaps. In the render, "Problem 5:␣␣Your partner goes first from this start.␣␣Draw…" shows this, as do P8 and P10. Add `\raggedright` and `\frenchspacing` to the preamble.

### 11. Smaller notes, at the reviser's discretion

- **P1 order.** 2, 3, 4, 5, 6, 7 strictly alternates, so a child can fill in the circles by continuing the alternation rather than thinking about pairs. 10 and 11 at the end do test the idea. A mild shuffle such as 4, 3, 6, 2, 7, 5, then 10, 11 would make the pairs reason more necessary. Keeping the ordered version for accessibility is also defensible.
- **P12 after P11.** The packet ends on an easier competitive task after the deepest question. Stopping anywhere is fine, so this is acceptable. Ordering P9, P12, P10, P11 would end on "forever".
- **P4 (3,4).** It has 4 in bucket 2 and 7 counters, slightly beyond the outline's "up to three per bucket, six or fewer counters". This is fine for counting to 10–12 and needs no change.
- **Answer sizes.** P3's answer buckets (16×22 mm) must hold up to 4 drawn dots in bucket 1, for (4,0) and (4,2). That is tight for kindergarten drawing, but workable.

## Notes for the facilitator guide (not page changes)

- **P4.** The page assumes an adult who plays perfectly and copies quietly. The parent volunteer needs the copy reply for every position reachable from (4,2) and the move (3,4) → (2,4). Playing each child from 2 starts in both orders is up to 16 games for one adult, so the guide should suggest a subset.
- **P5.** The partner has three moves. The copy is the answer, and naming it is the children's discovery.
- **P6 and P7.** Answers are 3 and 4 ways; empty buckets count, and (2,4) differs from (4,2). P7 is impossible because 5 cannot be split into two even piles.
- **P11.** An adult-level explanation: bucket 3 never gains counters, so it empties after its 3 takes. After that, bucket 2 never gains, and bucket 1 only shrinks once bucket 2 is empty.
- **Outline correction.** (1,2,1) runs from 4 to 9 moves, not 3 to 9.
- **Status.** The week is unpiloted. The board, counters and the fit of the pages have never been handled with K–1 children.

## Format compliance checklist

- **Header** "Week 81 / Buckets of Fish / K–1" on every page: yes.
- **Footer** "Bellingham Math Circle / Week 81 / W81-K-v1" with page number: yes.
- **No Name/Date fields, no titles, no encouragement, no exclamation marks, no dashes used as asides, no hints:** yes.
- **Problems numbered 1–12 consecutively:** yes.
- **Rules unnumbered at the top of page 1:** yes. The three-bucket rule lives in P9 and is used by P10–P12, which is acceptable.
- **Overflow and overlap:** none on any page. P3's right column ends exactly at the right margin.
- **Prompt length.** P9 (four sentences) is over the K–1 one-or-two-sentence standard; P5 and P8 (three each) are borderline.
