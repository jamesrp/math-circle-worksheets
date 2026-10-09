# Week 46 (Two boards forget their starts): math check

Scope:

- Base packet in `lowell-math-circle-year-2/week-46/`: `week-46-k-1.pdf` (4 pp., Problems 1–7), `week-46-grades-2-3.pdf` (4 pp., Problems 1–7), `week-46-grades-4-5.pdf` (4 pp., Problems 1–7) and `week-46-facilitator.pdf` (6 pp.).
- Bonus companion in the same folder: `week-46-bonus.pdf` (3 pp., Problems 1–3) and `week-46-bonus-facilitator.pdf` (2 pp.).

I ignored the archive folders. Sources read: the three student TeX files and `write.py`/`common.py` in `source/week-46/editable/src/`, and `source/week-46-bonus/student/build.py` and `support.py`. My scripts and their outputs are in [checks/week-46/](checks/week-46/). Checked October 5, 2026.

**Result: every diagram matches its text, and every answer, example, table and overview claim in both guides is correct. I found 1 minor problem. In Grades 2–3 Problem 3 (and 4–5 Problem 3), two identical boards are a legal but trivial answer to "match before all three slots have markers", and nothing steers children past it.**

## How it was checked

- **The PDFs match their sources.** All six delivered PDFs are byte-identical (MD5) to the reference copies in `source/week-46/editable/reference-pdfs/` and `source/week-46-bonus/reference-pdfs/`.
- **`extract_diagrams.py` reads every diagram from the TeX and checks it against the PDFs** (`extract_diagrams.out`: 399 checks, 0 failures; data in `diagrams.json`).
  - It parses every slot box, token, instruction card and highlighted slot from the TikZ coordinates. It groups them into boards, stacked pairs and card stories, and assigns each to its rule or problem.
  - Every token's fill matches its letter. On every page, each R/B letter in the PDF text layer sits exactly on its TeX token (offset 0.00 pt). A 100-dpi raster sample inside each token shows the right colour.
  - Every card's label "i→c" matches its bold slot and its token colour, and the token lies inside that slot.
  - Each problem statement in the TeX appears in the PDF text. Problems run 1–7 in every band and 1–3 in the bonus.
  - **Launch picture (all bands):** RBR/BRB, then card 2→B, then RBR/BBB.
  - **Toggle picture (2–3, 4–5):** RBR/BRB, then "toggle slot 2", then RRR/BBB.
  - **Draw cards:** K–1 p4, 2–3 p3 and 4–5 p4 each show exactly 1R, 2R, 3R, 1B, 2B, 3B, all the same size.
  - **Problem boards:**
    - K–1 P1 and 2–3 P1: RBR over BRB.
    - K–1 P2 and 4–5 P1: RBR/RRR, RRB/BRR, BRB/BRB and RRR/BBB.
    - K–1 P5: story 1→R, 3→B, with two blank pairs.
    - K–1 P6: RRR over BBB.
    - 2–3 P2 and 4–5 P2: stories 1→R 1→B 3→R; 2→R 3→B 1→R; 2→B 2→R 2→B.
    - 2–3 P6: RBR/RRR, RRB/BRR, BRB/BRB.
  - **Bonus.** The P1 picture is RBR/BRB, then COPY 1 to 2, then RRR/BBB. The P3 picture is RBB, then T, then BBR. The working circles have radius 31 pt, so they are 21.87 mm across, as the guide says (21.9 mm).
- **`check_base.py` enumerates every base task** (`check_base.out`: 112 checks, 0 failures).
  - A breadth-first search finds the fewest shared setting instructions for all 64 ordered pairs.
  - It checks every setting story up to length 5 (all 8 starts each) and every toggle story up to length 6 on every pair.
  - It checks all 66,430 mixed setting/toggle stories up to length 5.
  - It computes the exact matching-time law from RRR/BBB, every colour story for the 4–5 P6 slot story, and every covering slot story of length 3–7.
  - It computes all 6^m random draw sequences for m = 3–6, conditioned on coverage.
  - Each guide example is first checked to be printed in the guide's text layer and then recomputed.
- **`check_bonus.py` enumerates every bonus task** (`check_bonus.out`: 49 checks, 0 failures).
  - It tracks stories symbolically and runs a BFS over copy/reset stories. It checks all 64 directed copy graphs on 3 sites and all 4,096 on 4 sites for the reset extension.
  - It counts covering ticket stories and searches all S/T words for n = 2–6 slots.
  - It checks the guide's kit arithmetic.

## K–1: checks out completely

- **P1.** RBR/BRB differs in all three slots, so it needs 3. Over all pairs the minimum is the number of differing slots, never more than 3.
- **P2.** The pairs need 1, 2, 0 and 3, so the four pairs show each possible value once.
- **P3.** Twelve unordered pairs need exactly 2. No pair needs 4.
- **P4.** A story makes all 8 starts match exactly when it names all three slots. None of the 36 two-instruction stories does. There are 48 such three-instruction stories.
- **P5.** Under 1→R, 3→B, two starts finish alike exactly when their middle colours agree: 12 different-start pairs match, and 16 stay different.
- **P6.** From RRR/BBB the chance of matching within 3 draws is 2/9. The chance of still being unmatched after 6 draws is 7/27 ≈ 0.26, and after 10 it is about 0.05, so "more than three" happens often.
- **P7.** No. A shared setting instruction never turns an agreeing slot into a disagreeing one.

## Grades 2–3: every answer correct; one minor wording problem (Problem 1 below)

- **P1.** The answer is 3, as in K–1.
- **P2.** Only story 2 (2→R, 3→B, 1→R) guarantees a match; every start ends RRB. Story 1 finishes BRR or BBR, leaving slot 2 free. Story 3 finishes RBR, RBB, BBR or BBB, leaving slots 1 and 3 free. The markers are {1,3}, {1,2,3} and {2}.
- **P3.** Yes. A pair matches under a setting story exactly when every initially differing slot has been named. 360 (pair, story) cases of length ≤ 2 match with fewer than three slots named.
- **P4.** 168 of the 216 three-draw stories fail some pair, and ten draws of 1→R fail too.
- **P5.** The answer is 3. No story of length ≤ 2 works.
- **P6.** Only BRB/BRB, which already matches. Toggles keep the set of differing slots fixed.
- **P7.** A mixed story makes every start agree exactly when each slot gets at least one setting instruction.

## Grades 4–5: every answer correct (see Problem 1 below for P3's second question)

- **P1.** The pairs need 1, 2, 0 and 3. The rule is the number of differing slots.
- **P2.** The stories give 2, 1 and 4 finishes. In general, a story that leaves u slots unnamed has exactly 2^u finishes (all setting stories up to length 5).
- **P3.** The story forgets every start exactly when all three slots are named. Two particular boards can agree sooner, for example RRR/BRR after 1→R.
- **P4.** No. Every toggle story keeps every pair's set of differing slots, and is a bijection of the 8 boards.
- **P5.** The condition is the same as in 2–3 P7. Both directions were checked over all mixed stories up to length 5.
- **P6.** With slots 1, 3, 1, 2, the final board is (c3, c4, c2). From every start, each of the 8 boards comes from exactly 2 of the 16 colour stories, so all eight tie at 1/8.
- **P7.** Yes, for every slot story that names all three slots (checked up to length 7). No for random draws: only 36 of 81 four-draw slot stories cover. After four random draws the result still depends on the start: P(RRR) is 11/54 from RRR but 1/18 from BBB.

## Adult guide (base): checks out completely

- **Overview.**
  - The 2^u count, the minimum equal to the number of differing slots, and that agreement persists are all true.
  - So are "every pair agrees iff every slot is visited", with shortest length 3, and the iff for a particular pair.
  - Toggles keep the set of differing slots fixed. The mixed criterion is correct, with the right hypothesis: at least one setting instruction per slot, not merely one visit.
  - Conditional on any covering slot story, each final board has probability 1/8.
  - The union bound 3(2/3)^m is valid; the exact chance of a missing slot is 3(2/3)^m − 3(1/3)^m.
  - The warning about colour-inspecting stopping rules is right. Stopping at the first covered board with slot 1 red reaches only 4 of the 8 boards.
- **Launch.** Both examples are correct: RBR/BRB under 2→B gives RBR/BBB, and toggling slot 2 gives RRR/BBB.
- **Materials and pages.** The arithmetic holds: 5 pairs, 10 strips, 30 counters and 5 cups. Each band has four pages.
- **Answer keys.** Every table and example on pp. 3–5 matches the enumeration. That includes the K–1 P2 table and repairs, the K–1 P5 examples (RRB/RRB; RRB/RBB), the 2–3 P2 counterexample finishes and the 2–3 P7 stories (BBR, and RBR/RRB). It also includes the 4–5 P2 table and the 4–5 P6 (c3, c4, c2) argument.
- **Route note.** The note on p. 6 cites the right problem numbers.

## Bonus pages and bonus guide: check out completely

- **P1.**
  - Copies alone can reach 22 of the 27 slot maps, and they keep RRR and BBB fixed.
  - The pairs that copies can never make alike are exactly the four complementary pairs: RRR/BBB, RRB/BBR, RBR/BRB and RBB/BRR.
  - No story of two or fewer instructions works. With exactly one RESET the shortest story has length 3. All 12 such stories begin with the RESET, and the guide's RESET 1; COPY 1 to 2; COPY 1 to 3 is one of them.
  - The directed-graph extension is true for every graph on 3 and 4 sites: one reset synchronises the boards exactly when the reset site reaches every site.
- **P2.**
  - 6 of 27 three-draw stories cover, and 36 of 81 four-draw stories, giving 2/9 and 4/9. The guide's 3 × 6 × 2 count is right.
  - All 6 stories without replacement cover, and 1,1,…,1 never covers.
  - The (2/3)^m figure and the 3(2/3)^m bound are correct. So is the fresh-colour extension, with or without replacement.
- **P3.**
  - STSTS is the unique shortest synchronising word, with the trajectory printed in the guide.
  - Every synchronising word up to length 8 has at least three S and at least two T.
  - The extension holds for n = 2–6: the shortest length is 2n − 1, uniquely S(TS)^(n−1).
- **Guide arithmetic.** The circle size (21.9 mm) and the kit totals for KK11 / 3333 / 445 are correct: 10 rows, 30 counters, 15 tickets, 5 cups, 15 markers and 5 pencils.

## Problems found

### 1. Grades 2–3, page 2, Problem 3 (also Grades 4–5, page 2, Problem 3): identical boards answer the "does" half trivially

- **Quoted text (2–3):** "Problem 3: Can some starting pairs match before all three slots have markers? Make one example that does and one that does not."
- **Quoted text (4–5):** "…Could two particular boards agree before that happens?"
- **Evidence:**
  - Any pair of identical starts, such as RRR/RRR, already matches before any instruction, with no markers at all. Each of the 8 identical pairs works (`check_base.out`).
  - Nothing on the page excludes identical starts. A literal-minded child can answer "yes, RRR and RRR" and never meet the intended case.
  - The intended case is two different boards that match early because every slot where they differ has been named. An example is RRR/BRR after 1→R, which is the guide's example in both bands.
  - The guide does not mention the trivial reading. The stated answers stay correct under both readings, so this is a wording issue, not a wrong answer.
- **Smallest fix:**
  - 2–3: "Can two different starting boards match before all three slots have markers?"
  - 4–5: "Could two particular different starts agree before that happens?"
  - Alternatively, leave the pages and add one guide sentence: "If a child offers two identical boards, accept it and ask for two boards that start different."

## Notes (not errors)

- **Bonus guide, P1 key.** The key gives only RRR/BBB, with an argument ("every copy leaves each board monochromatic") that covers only that pair.
  - The complete answer is any pair that differs in every slot. That includes the pictured RBR/BRB.
  - The reason: every slot always holds the colour of some original slot, and such boards differ at every original slot.
  - A sentence saying so would help an adult confirm the other three pairs.
  - Also, the page-1 picture shows RBR/BRB turning into RRR/BBB, which displays one answer pair. Children still have to explain "never".
- **Base guide, p. 1.** "Even ten draws can revisit one slot" is true but weaker than intended. The point is that all ten draws can name the same slot. A clearer wording: "Even ten draws can all name the same slot."
- **K–1 Problem 5.** Two identical boards also "end matching". That is harmless here, because the "ends different" half carries the idea (only the middle colour survives).
- **Citations not checked.** I could not check the cited Gautam Iyer CMU notes ("Coupling", Proposition 9) or the *Math Circle by the Bay* preface, because neither is in the repository. The mathematics attributed to them was checked independently above.
