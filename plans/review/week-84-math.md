# Week 84 (Public knowledge): math check

Scope:
- `lowell-math-circle-year-2/week-84/week-84-students.pdf`: one shared packet headed "Grades 2–5", 8 pages. The band-views menu gives K–1 no pages and Grades 2–3 and 4–5 the whole packet, so this one packet is every band.
  - p. 1: café rules, a two-person worked example, then Problem 1 (four conversations).
  - p. 2: headband rules, a two-doll worked example, then Problem 2 (Deals 1–3).
  - p. 3: Problems 3 and 4.
  - pp. 4–8 are materials: eight YES/NO deal cards (p. 4), eight headband cards (p. 5), private YES/NO cards and B/R headbands (p. 6), reply cards (p. 7), and the staging labels with three doll slots (p. 8).
- `week-84-facilitator.pdf`: 5 pages. They cover the overview, setup, café and headband solutions, the optional bounded hidden-number grid, and provenance.

Sources read: `source/week-84/student/students.tex`, `guide/facilitator.tex`, `README.md`, `SOURCES.md`. I did not run or import the package's `check_math.py` or `build.py`. All printed data come from the delivered PDFs. My scripts and their outputs are in this run folder, for `plans/review/checks/week-84/`. Checked October 23, 2026.

**Result: every answer, diagram and card set is correct, and so is every guide solution. I found 3 minor problems and nothing that makes a task wrong or impossible:**
1. Problem 3's "the same three replies" has a second reading that turns the answer from yes to no.
2. The reply cards include only one NO, but two printed conversations have two and three NOs.
3. One sentence of the guide overview says the opposite of what it means.

## How it was checked

- **`pdf_extract.py`** (output `pdf_extract.out`, data `pdf_geometry.json`) reads the delivered student PDF with PyMuPDF. On every page it records:
  - the header, the footer and the problem labels;
  - every solid or dashed box, with its size in inches and the text inside it;
  - every filled disk, with its fill colour (matched to the source's `hatblue`/`hatred` RGB values) and the letter printed on it.
- **`check_math.py`** (output `check_math.out`) uses possible-worlds models written from the page's rules, not hand-coded answers.
  - **Café.** A person answers YES if every deal that is still publicly possible and agrees with their own card is all-YES. They answer NO if none is, and NOT YET otherwise. After each answer, the public set keeps the deals in which that person would have said the same thing.
  - **Headbands.** In each round, every doll compares the unchanged shared set with what it sees. After the simultaneous reveal, the set keeps the arrangements that would have produced the same three replies.
  - **Hidden-number grid.** Alice and Bob alternate turns. The speaker names the larger person if every public world agreeing with their own number gives the same comparison. Otherwise they say "don't know".
  - **What the script runs:**
    - all 8 café deals, and all 7 or 8 headband arrangements, for up to 10 rounds;
    - the k-round theorem for every arrangement of 1–6 dolls;
    - a sequential-reveal protocol, for comparison;
    - the 0–6 and 0–5 grids;
    - the card counts and sizes;
    - every guide sentence it tests, matched against the guide PDF's text.
- **Results:** 58 checks pass. The one failure is item 2 below, and is reported on purpose.

## Student packet, Grades 2–5 (pp. 1–8): correct except items 1 and 2

- **p. 1 example.** "Before" lists all four 2-person deals. After "Person 1 says NO", exactly NY and NN remain, as printed.
- **P1.** Exactly 4 conversations are possible, and they are the 4 printed. The deals that fit each one (4 + 2 + 1 + 1 = 8) are:

  | Conversation | Replies | Deals that fit |
  |---|---|---|
  | 1 | NOT YET, NOT YET, NO | YYN |
  | 2 | NO, NO, NO | NYY, NYN, NNY, NNN |
  | 3 | NOT YET, NO, NO | YNY, YNN |
  | 4 | NOT YET, NOT YET, YES | YYY |
- **p. 2 example.** From {BB, BR, RB}, doll 1 seeing R on doll 2 matches only BR, so it shows PROVE BLUE.
- **P2.** The deals print as BRR, BBR and BBB. Each disk's colour matches its letter, and the disks are numbered 1 2 3.
  - **Deal 1 (BRR).** Round 1: doll 1 proves; dolls 2 and 3 show NOT YET.
  - **Deal 2 (BBR).** Round 1: all NOT YET. Round 2: dolls 1 and 2 prove; doll 3 shows NOT YET.
  - **Deal 3 (BBB).** Rounds 1 and 2: all NOT YET. Round 3: all three prove.
  - No red doll ever proves. Every deal has a blue doll, so "until every blue doll can show PROVE BLUE" always ends.
- **P3, reading replies per doll.** Round 1 gives four groups: {BRR}, {RBR}, {RRB} and {BBR, BRB, RBB, BBB}. In round 2, BBR, BRB and RBB give PPN, PNP and NPP, and BBB gives NNN. So all 7 reply histories differ by round 2, and the answer is "yes". See item 1 for the other reading.
- **P4.** With all 8 cards and no announcement, every doll in every arrangement always has an own-red match. So every reply is NOT YET in every round, nothing is ever removed, and no doll can ever prove blue. The answer is "no".
- **Materials (pp. 4–8):**
  - p. 4 has the 8 YES/NO deals once each, and p. 5 the 8 B/R arrangements once each. All 16 cards measure 3.45 × 1.85 in and label positions 1 2 3.
  - p. 6 has 3 YES and 3 NO cards, and 3 B and 3 R headbands. That is enough for any deal.
  - p. 7 has 3 PROVE BLUE and 3 NOT YET cards, enough for any headband round, but only 1 YES and 1 NO (item 2).
  - The three doll slots on p. 8 are the size of a reply card (2.18 × 2.30 in).
- **Pages.** All 8 headers are identical, and the problems are numbered 1–4.

### 1. p. 3 Problem 3 (minor): "the same three replies" can mean "the same three reply cards", and then the answer is no

- **Quoted text:** "Put deals into groups that give the same three replies in round 1. Can later rounds separate every group?"
- **Evidence.** The intended reading compares the reply of each doll. It gives the four groups above, all separated by round 2, and the guide (p. 3) answers on that basis: "all seven deals have distinct public response histories by round 2".
  - **The other reading.** A child can instead compare which replies were given, not who gave them: one PROVE BLUE and two NOT YETs. Round 1 then gives two groups, {BRR, RBR, RRB} and {BBR, BRB, RBB, BBB}.
  - **What changes.** Under that reading, later rounds never separate BRR, RBR and RRB, which give one PROVE BLUE and two NOT YETs in every round. Nor do they separate BBR, BRB and RBB, which give two PROVE BLUEs and one NOT YET from round 2 on (`check_math.out`, "unordered reading"). The child's correct answer would be "no", but the key says "yes".
  - **Why the reading is natural.** The round-1 replies of the three one-blue deals really are "the same three replies", just shown by different dolls.
- **Smallest fix:** "Put deals into groups in which each doll gives the same reply in round 1. Can later rounds separate every group?"

### 2. p. 7 reply cards (minor): one NO reply card, but Conversations 2 and 3 have three and two NO replies

- **Quoted text:** p. 7 prints PROVE BLUE ×3, NOT YET ×3, YES ×1 and NO ×1.
  - The guide (p. 2) says: "Print cafe and headband configuration cards (pages 4–5), reply cards (pages 6–7)".
  - p. 1 prints Conversation 2 as "1 NO / 2 NO / 3 NO" and Conversation 3 as "1 NOT YET / 2 NO / 3 NO".
- **Evidence.** Laying out a printed café conversation needs up to 3 NO, 2 NOT YET and 1 YES reply cards, and p. 7 has one NO (`check_math.out`).
  - p. 6's YES and NO cards are the people's private cards, not replies. The guide's own list calls them "cafe YES/NO cards", separate from "public response cards". p. 6 also holds the B/R headbands, so "reply cards (pages 6–7)" is wrong for p. 6.
  - Problem 1 can be solved from the printed transcripts without reply cards. So this matters only if a table acts out a conversation with cards, or deals a fresh café round.
- **Smallest fix:** in the guide, write "private cafe cards and headbands (page 6), reply cards (page 7); cafe replies are spoken aloud, or print page 7 twice". Optionally, fill p. 7's empty ninth slot with a second NO, which is enough for Conversation 3. p. 7 has no room for a fourth row of cards.

## Guide (pp. 1–5): correct except item 3

- **Overview (p. 1):**
  - The definition of knowledge as agreement across every compatible possibility is right.
  - "A personally NO player can answer NO immediately" and "A first 'not enough information' therefore proves that first preference is YES" are true.
  - The theorem is true: with k ≥ 1 blue headbands, exactly the blue dolls first prove blue in round k. I checked it for every arrangement of 1–6 dolls, not only k = 1, 2, 3. Its hypotheses (public announcement, perfect simultaneous reasoners) are stated.
  - "A red doll who knows red still reports 'not yet'" is true: after the blues prove, every red doll's matches are all red.
- **Setup (p. 2):**
  - The BBR private views are right: doll 1 has BBR/RBR, doll 2 BBR/BRR, doll 3 BBR/BBB.
  - Sequential elimination does leak information. If BBR's dolls reveal one at a time, doll 1's NOT YET removes BRR, and doll 2 then proves in round 1.
  - The display size is right: 4 × 3.45 + 3 × 0.25 = 14.55 in, and 2 × 1.85 + 0.25 = 3.95 in.
- **Solutions (p. 3).** The key "YYN; NYY/NYN/NNY/NNN; YNY/YNN; YYY" is right, and so are its explanations, including "a later YES-preferring speaker … also says NO". The guide's statements on Problems 2–4 are also right:
  - the red doll's two possibilities in BRR before round 1;
  - the red doll's BBR/BBB after round 1 of BBR;
  - "all three declare round 3";
  - the Problem 3 separation (under the per-doll reading);
  - "No blue proof ever follows" for Problem 4.
- **Grid (p. 4).** Every step is reproduced for the 0–6 domain and the deal Alice = 3, Bob = 2:
  - Alice's first "don't know" removes rows 0 and 6.
  - Bob's removes columns 0, 1, 5 and 6.
  - Alice's second leaves (3,2) and (3,4), since rows 1–2 know Bob is larger and rows 4–5 know Alice is larger.
  - Bob with 2 then knows both numbers, while the audience does not, and "Alice is larger" leaves (3,2).
  - The claim about the 0–5 domain is true: with the same deal, Alice knows at her second turn.
  - The grid has 49 cells, 42 after the diagonal.
- **Encore (p. 5).** Two café arrangements with the same conversation exist (Conversations 2 and 3).

### 3. Guide p. 1, overview (minor): "Later NO need not mean the later speaker personally says NO"

- **Quoted text:** "A first 'not enough information' therefore proves that first preference is YES. Later NO need not mean the later speaker personally says NO."
- **Evidence.** Every later NO speaker does say NO, so the sentence as printed is self-contradictory.
  - The intended fact is about the speaker's own card. In NYY and NYN, person 2 holds a YES card and says NO because person 1 already said NO (`check_math.out`).
  - Page 3 states it correctly: "Do not infer every NO speaker has preference N."
  - The overview also asks "Does everyone want a drink?" where the student page asks "a cup?". That changes no mathematics.
- **Smallest fix:** "A later NO need not mean the later speaker's own card is NO." Optionally, also change "drink" to "cup".
