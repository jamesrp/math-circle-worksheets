# Review: Week 97 K–1 adult guide (W97-K-FAC-v1), writer draft

I reviewed `draft/k1-guide.pdf` (4 pages) and its source `draft/src/k1-guide.tex` against the final K–1 pages, `plans/k1-drafts/week-97/k-1.pdf` (13 pages). I rendered and read every page of both. I also read:

- the outline `worksheet-workflow/outlines/week-97-k1.md`;
- the two page reviews (both describe the earlier 9-page draft);
- the Week 97 entry in `plans/k1-drafts/README.md`;
- the week's guide W97-FAC-v3 in full, and page 1 of the older packet W97-35-v2;
- the Week 98 model guide.

I did not edit the guide or the pages.

**How I checked.** I wrote `review-guide-check/verify.py` before opening the writer's checker. Its output is in `review-guide-check/verify.out`. The script does four things:

- **Answers.** It finds every leftover by literal take-away: a list of n × n tiles, with m removed at a time while at least m remain. From these it rebuilds every list and "find all" set the guide prints, plus the extension cards (6 in Problem 2, 7 in Problem 11).
- **General claims.** It tests the overview's claims for sides 0 to 2000:
  - the leftover sets for groups of 2, 3, 4, 6 and 8;
  - the repeat (sides n and n + m share a leftover) and the mirror (n and m − n share);
  - the 8k ring count;
  - the arithmetic printed in Problems 8 and 10.
- **The final student PDF.** It parses the drawings: the order and size of every square and rectangle, the cell count of each group card, the 26 mm cells, the 156 mm board, the 58 × 74 mm cut cards, and the ring colours on pages 9–10. It also counts the tiles each problem needs, as a timing check.
- **The guide.** It checks that each printed claim appears in the guide text and agrees with the computation. It also compares the older packet's page 1, which the shared launch reads aloud, with the K–1 answers.

Afterwards I ran a copy of the writer's `check_guide.py` in `/tmp`. It passes, and the PDF hashes match the writer's report. pdflatex is not installed here, so I reviewed the compiled PDF as delivered. The rendered pages show no overflow, clipping or overlap.

**Results.** Every answer, list, page number, problem number, board size, card size and group-card size in the guide is correct and matches the 13-page final packet, not the 9-page draft the reviews describe. For example, the guide gives Problem 3's rectangles in printed order, 4 × 3, 3 × 2, 5 × 2 and 5 × 3, with leftovers 0, 2, 2 and 3. The two FAIL lines in `verify.out` are the must-fix below, not errors in the script.

**Verdict.** This is a correct, compact guide with a real theorem-first overview, complete "find all" answers and a carefully hidden secret game. One must-fix: the K–1 table is sent into the shared launch without being told to leave before the older packet's printed collection is read aloud, and that collection states Problem 1's answer. The should-fix items are:

- how a pair shares packets, board, card and tiles;
- a thin "hiding" paragraph in the overview.

## Must-fix

### 1. The shared launch reads out Problem 1's answer, and the guide does not take the K–1 table out first (p. 2, "Launch together, then learn the table action")

- **What the guide says.** "Join the base guide's whole-group launch (p. 2): handle the tiles, see the 3 × 3 square in groups of 4 and the empty square, and make a legal attempt."
- **What that launch also contains.** Its second paragraph (W97-FAC-v3 p. 2) continues: "Now read the small printed collection for bundles of 4 and inputs 0–3." On the older packet's page 1, that collection reads: "Output 1 hides two possible inputs: 1 and 3. There are two different outputs: 0 and 1."
  - That is the answer to K–1 Problem 1 (groups of 4: circle 0 and 1).
  - It is also the core of Problem 2: leftover 1 hides 1, 3 and 5.
  - Problems 1 and 2 are the first-hour route.
- **Why the guide's wording does not prevent it.** Its summary lists only the first paragraph's actions, but nothing tells the K–1 adult or the lead to split the launch. Under AGENTS ("Launch together"), the launch must not reveal the main theorem or a target answer.
- **Fix.** Replace the first sentence with:

  > "Join the first part of the base guide's whole-group launch (p. 2): handle the tiles, see the 3 × 3 square in groups of 4 and the empty square, and watch a legal attempt. Then take the K–1 children to their table, before the lead reads the older packet's bundles-of-4 collection. That collection ('two different outputs: 0 and 1'; 'output 1 hides 1 and 3') answers Problem 1 and starts Problem 2."

  In "Where it goes" (p. 4), add that the base launch's printed-collection paragraph is read after the K–1 table has left.

## Should-fix

### 1. How a pair shares packets, board, group card and tiles is not stated (p. 1 "Per pair" and "Print"; p. 2 "Before a secret round")

- **What is missing.** "Print" says to print pages 1–11, page 12 "separately" and "one copy of page 13 per pair". It never says how many packets (one per child?) or how many boards (one per pair or one per child).
- **Why the counts matter.**
  - **Tiles.** A pair has 64 tiles. If each child builds on their own board, two 6 × 6 squares need 72 tiles. The pair has to build one square at a time.
  - **The secret game.** On page 2 the group-of-4 card and the record rows are on the same page. The maker needs a group card behind the folder while the guesser keeps the rows. That works only if each child has their own page 2, which the guide does not say.
  - **Hiding.** "Before a secret round" hides the deck, square, spare tiles and cup, but not the board or the group card the maker is using.
- **Fix.** In "Print", add:

  > "Print one packet (pages 1–11) per child, and one board (page 12) and one card sheet (page 13) per pair. A pair builds one square at a time on its board and fills one child's group card; both children record on their own page."

  In "Before a secret round", add: "The maker takes the board, the allowed cards, the cup and the group card from their own page behind the folder; the guesser keeps their page to record."

### 2. The overview's "hiding" paragraph states no fact about which squares share a leftover (p. 1, "One result can hide several squares")

- **What it says.** "A secret is not always recoverable … The group size and the allowed cards both matter." These are true, but an adult cannot tell from them what children will find in Problems 2, 6 and 11, or why.
- **The K–1 view of the week's destination is missing.** Problem 6's answer, {1, 5} and {2, 4} with 3 and 6 alone, is the K–1 version of the older tables' x and p − x pairing. Problem 11's 1, 3, 5 (and 7) all leaving 1 is the base guide's own composite example ("With bundles of 8, output 1 has four possible inputs").
- **What else is missing.** The overview never says that groups of 2 leave 0 or 1 (by the side's evenness), or that groups of 8 leave only 0, 1 or 4. Both are needed for Problems 7 and 11.
- **Fix.** Add to that paragraph (all checked in `verify.out`):

  > "Sides n and m − n always leave the same: in groups of 6, cards 1 and 5 and cards 2 and 4 hide each other, while 3 and 6 are alone (Problem 6). With objects: take a 1 × 1 corner off a 5 × 5 square and the L re-forms as a 4 × 6 rectangle, whole groups of 6 (the base guide's p. 5 picture). Groups of 8 hide more: every odd side leaves 1, and squares leave only 0, 1 or 4 (Problem 11), which is the older tables' composite surprise. Groups of 2 leave 0 or 1, as the side is even or odd."

  Then change "K–1 reaches restricted leftovers, ambiguity, and a first geometric explanation" to name these two links to the base overview.

## Minor

1. **The table demonstration shows only one card-fill (p. 2).** Side 3 in groups of 5 is a good non-task instance. It also shows the stranded tiles on a partly filled mat counting as the leftover, which is the case the page review's major item 1 was about. But 9 = 5 + 4 fills the mat once, so the demonstration never shows "fill, empty, fill again". The math review warned that this misreading turns a 6 × 6 in groups of 3 into 33.
   - **Fix:** use side 4 with the same five-space mat: three fills, then one tile stranded on the mat, leftover 1. This is still not a task.
   - **Figure changes:** a 4 × 4 start, the middle caption "Fill five spaces, three times", one tile on the last mat, and a record of 1 under side 4.
2. **Problem 3's first hint has no answer (p. 3).** "Which of these has a different number of tiles along the two edges?" fits all four printed rectangles (4 × 3, 3 × 2, 5 × 2, 5 × 3).
   - **Fix:** "Which number on page 1 did no square leave? Can a rectangle leave it?"
3. **"Problem 7 is an alternative entry" is unclear (p. 1 "Print", p. 2 "A first hour").** It does not say what Problem 7 replaces or for whom. The page has 26 card-fills against Problem 1's 22, so it is easier to count but not shorter. The Problem 7 note on p. 4 compares it with Problem 1, which needs Problem 1 done.
   - **Fix:** "For a child who struggles to fill a card of four, start with Problem 7's sides 1–3, then go to Problem 1."
4. **Problem 9 has one confusing sentence and one directed step (p. 4).**
   - "With one color, remove one ring at a time, rebuilding before the next whole-square trial" is hard to follow. Write: "With one color, build and take away one ring at a time, so each ring stays visible."
   - "Have children show full rings going into the cup before naming a pattern" prescribes the explanation as a method. Make it a hint: "Can you take the ring away in whole groups?"
5. **Problem 10's "ready child" argument is algebra (p. 4).** The 2k + 1 and 2k − 1 counts are adult notation.
   - **Fix:** give the child's version first: "the outside ring of the 7 × 7 is rows of 7 and 7 and sides of 5 and 5: 24 tiles, three cards of 8; or eight straight runs of 3". Keep the 8k line for adults.
6. **Some hint and note wording is opaque for a parent volunteer (p. 3).**
   - Problem 5: "Where could an unchecked side fit in your collection?" Use "Which squares haven't you built yet?"
   - Problem 4: "rather than let repeated handling displace comparison". Use "so the table has time to compare".
7. **"Where it goes" omits other base-guide sentences that will contradict the section (p. 4).** Besides the launch paragraph (must-fix 1), these need to change:
   - W97-FAC-v3 p. 1: "There is no K–1 packet (page 2 gives an adult-led K–1 route)".
   - p. 2 Staffing: "The K–1 table takes the K–1 route below with its adult".
   - p. 2 Staffing: "There is no required cutout deck or exact material fit". The K–1 table now cuts cards and needs 26 mm fit.
   - **Fix:** list them in one sentence so the integrator does not miss them.
8. **The packet is named as "the draft `k-1.pdf`" (p. 1).** That name goes stale on approval.
   - **Fix:** "the K–1 packet W97-K-v1 (`week-97-k-1.pdf` once approved)".
9. **Two small wording slips (p. 1).**
   - The week's kit is "64 counters or square tiles", not "the week's 64 square tiles". Write "64 counters or square tiles (1-inch square tiles if the room has them)".
   - "The little square pictures are records, not tile mats": they show which square to build. Write "show which square to build; they are not mats".
10. **Light repetition (pp. 2–3).**
    - The grey 1 is explained twice: "do not treat its grey 1 as a new puzzle" on p. 2 and "The prefilled side-3 answer is correct" on p. 3. Keep one.
    - The card's shape is explained twice, on p. 2 ("Tiles may come from anywhere") and under Problem 4. Keep the Problem 4 note to one clause.

## The writer's flagged issues

**Agree.** I agree with every page risk the writer lists, and with how the guide handles each:

- the straight three-cell card read as a rigid strip;
- a partly filled card mistaken for a group;
- Problem 4's 12 fills for side 6;
- the ways a secret can leak (deck gap, cup, number of fills, shape of the leftover);
- the 9 × 9 and 10 × 10 being too big for the kit;
- Problem 9 built on the table, and Problem 10 borrowing page 9's card.

**Disagree on two points.**

1. The report says the table demonstration "gives away none of their answers". That is true of the demonstration, but the shared launch the guide sends the table to does (must-fix 1).
2. "The task pages already supply the needed group cards" is true, but the guide never says how many packets and boards a pair needs, and the secret game depends on that (should-fix 1).

The writer chose to leave the base guide's stale "no K–1 packet" sentences for integration. That is reasonable, but the launch paragraph cannot wait: it affects the first hour.

## Checklist results

1. **Correctness.** All printed answers verified (`verify.out`):
   - **Problems 1, 3, 4, 5, 7.** P1 1, 0, 1, 0, 1, 0. P3 0, 2, 2, 3. P4 1, 1, 0, 1, 1, 0. P5 1, 4, 3, 4, 1, 0. P7 1, 0, 1, 0, 1.
   - **Problems 8–10.** P8 1 and 0. P9 1, 1, 1 (rings 8 and 16). P10 1 (24 = 3 groups; 49 = 1 + 8 + 16 + 24).
   - **Secret games.** P2 0:{2, 4}, 1:{1, 3, 5}. P6 0:{6}, 1:{1, 5}, 3:{3}, 4:{2, 4}. P11 0:{4}, 1:{1, 3, 5}, 4:{2, 6}, with 2, 3, 5, 6 and 7 impossible.
   - **Extensions.** Card 6 joins leftover 0 in groups of 4, and card 7 joins leftover 1 in groups of 8.
   - **Overview.** Its leftover sets and repeat argument hold through side 2000.
   - **Kit and demonstration.** Two colours of 32 suffice (7 × 7 uses 32 and 17). The demonstration leaves 4.
2. **Agreement with the pages and the week.** Every problem and page number, the rectangle order, group-card sizes (4, 4, 4, 3, 6, 6, 2, 8, 8 cells of 26 mm) and the 156 mm board match the 13-page final PDF. The 58 × 74 mm cards and "pages 8 and 10 have no card" also match. Nothing contradicts W97-FAC-v3. The launch omission is must-fix 1, and the stale base sentences are minor 7.
3. **Overview.** It passes.
   - Theorem-first, with assumptions (filled square, any m tiles, leftover 0 allowed) and limits (squares, not piles or rectangles).
   - A followable repeat proof and a child-sized blocks-and-corner explanation.
   - A clear ladder from experiment to conjecture, finite proof and explanation.
   - Its hiding paragraph is thin (should-fix 2).
4. **Launch.** The table demonstration is brief, concrete, not a task, and gives nothing away, and it has a worked visual. The shared part leaks Problem 1's answer (must-fix 1), and the demonstration shows only one fill (minor 1).
5. **Usability and age fit.**
   - **Strengths.** Staffing is honest: the adult reads and scribes, and the children build, choose secrets and circle. The one-hour route sums to 60 minutes, with pooling and the game protected, and later visits are mapped. Hints are nearly all questions, and the secret-round procedure is careful.
   - **Gaps.** Per-pair sharing is not stated (should-fix 1). A few hints and notes need rewording (minors 2, 4–6).
6. **Brevity.** The guide is 2,446 words for one band (Week 98: 3,025 words for two). It has no generic encouragement and does not narrate the pages, and its repetition is light (minor 10).

## What works and should be kept

- **The overview's spine.** "Sides n and n + m have the same leftover" is proved by the two strips and corner. "Sides 1 through m cover every possibility" follows, and the blocks-and-corner explanation for groups of 4 is in words a child can use.
- **The evidence ladder.** "Checking every allowed card proves a finite game answer", and "merely testing more squares does not" explain a general pattern. Each problem keeps to it: "An earlier pattern predicts the answers; the blocks and arms explain them" (Problem 8), and "the even cards must also be tested" (Problem 11).
- **The demonstration's partly filled mat.** "Those four are the leftover, whether on the board or the partly filled mat", together with "Full groups go in the cup; partial groups never do." This closes the trap the page review found.
- **"Before a secret round."** Lay out only the allowed cards and remove card 6. Hide the deck, cup and spare tiles. Bring the leftover forward as a rearranged pile. The four rows are four rounds. Rebuild only disputed candidates.
- **Complete "find all" answers, each with its completeness reason.** Also the note that the revealed card "belongs in the answer but need not be the only answer".
- **Staffing.** It states what the adult does and does not do, and "If the adult is choosing every move, stay with a smaller concrete collection."
- **The first-hour route.** It sums to 60 minutes, pools square cases and protects time for the game.
- **The practical notes.** Problem 8 is honestly "without building" (beyond one kit), Problem 9 is built on the table, and Problem 10 borrows page 9's card. The "filled in, or only outlined?" hint and the side-6 fill count (12) for Problem 4 are useful too.
- **The Status line.** It names exactly what is physically unrehearsed.
