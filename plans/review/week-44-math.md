# Week 44 (The bag that copies): math check

Scope:
- Student packets in `lowell-math-circle-year-2/week-44/`:
  - `week-44-k-1.pdf` (W44-k-1-v2, 4 pp., Problems 1–4)
  - `week-44-grades-2-3.pdf` (W44-grades-2-3-v2, 4 pp., Problems 1–6)
  - `week-44-grades-4-5.pdf` (W44-grades-4-5-v2, 4 pp., Problems 1–6)
  - the encore `week-44-bonus.pdf` (W44-BONUS-v1, 3 pp., Problems 1–3; pp. 1–2 Grades 2–5, p. 3 Grades 4–5)
- Adult guides: `week-44-facilitator.pdf` (6 pp.) and `week-44-bonus-facilitator.pdf` (W44-BONUS-FAC-v1, 3 pp.).
- Sources read: `source/week-44/editable/src/*.tex`, `facilitator-src/guide.json`, and `source/week-44-bonus/student/build.py` and `guide.md`. The six reference PDFs in the sources are byte-identical to the delivered PDFs.

Archive folders were ignored. Checked October 5, 2026. My scripts and outputs are in [checks/week-44/](checks/week-44/): `common.py`, `extract.py` and `check.py`, with `extracted.json`, `out_extract.txt` and `out_check.txt`.

**Result: every answer key is right, and every student problem has the outcome its guide intends.** All three base bands are correct, and so is the encore. I found 4 problems:

1. **Bonus guide p. 3:** two printed formulas are garbled ("123=6" and "34...*(n+2)"). This is the only place the packet prints something false.
2. **K-1 P1:** the page asks for "draw stories" and the key answers for colour stories. The launch shows the two reds as different counters, and on that reading the answer changes.
3. **K-1 P2:** the page asks "Which bags can you make after three draws?", but one possible bag (3R/2B) is not printed and has no space.
4. **Base guide p. 2 kit:** five counters of each colour per pair is one short of laying out all three K-1 P1 bags at once. It is also one short of a five-draw single-colour story, which the 4–5 P6 exploration invites.

Items 2–4 are minor. None of them changes a printed answer.

## How it was checked

- **`extract.py`** reads the delivered PDFs, not the sources (PyMuPDF vector data). For every page it records:
  - every counter disc, with its centre, size, fill colour and label;
  - every answer box, bag box, story cell and history card, and which discs each box holds;
  - every line segment;
  - the page text.

  It also compares the delivered PDFs with the sources' reference copies by SHA-256. All six are identical.
- **`check.py`** uses only my own code (`common.py`) and the standard library. It enumerates every marked history with exact fractions: each draw is uniform over the counters present, and every draw is returned. The rules are copying, return-only and add-the-other-colour, with two or three colours. It then tests:
  - every claim on the student pages and in both guides;
  - the printed bags and cards from `extracted.json`.
- **Base model, n = 1–8:**
  - there are (n+1)! marked histories, and all are equally likely;
  - the red total is uniform at 1/(n+1);
  - the final bag is (r+1, n−r+1), so neither colour vanishes;
  - every colour word has probability r!(n−r)!/(n+1)!;
  - P(next red | previous red) = 2/3 and P(next red | previous blue) = 1/3 at every position.
- **Three colours, n = 1–6:**
  - there are (n+2)!/2 histories and C(n+2,2) count vectors, with n! histories per vector;
  - every word has probability 2·r!b!g!/(n+2)!.

## K–1 (pp. 1–4, Problems 1–4): correct answers; items 2 and 3 below are reading problems

- **Launch figure** (same in all three bands): R B → draw R → R R B. It matches the copying rule and gives away no task answer.
- **P1:** there are exactly three two-draw bags: 3R/1B, 2R/2B and 1R/3B. The page has 3 bag boxes and two two-cell story rows.
  - With colour stories, only 2R/2B has two (RB, BR), as the key says.
  - With marked stories, every bag has two. See item 2.
- **P2:** the printed bags are 4R/1B, 2R/3B, 5R/0B and 1R/4B.
  - 4R/1B, 2R/3B and 1R/4B are possible (RRR; RBB, BRB, BBR; BBB). 5R/0B is impossible.
  - The fourth possible bag, 3R/2B (RRB, RBR, BRR), is not printed. See item 3.
- **P3:** six four-draw colour stories end at 3R/3B, and the page has six 4-cell rows. The blue-majority four-draw bags are exactly 1R/5B (BBBB) and 2R/4B (four stories).
- **P4:** the bags before the last draw are as follows. They match the key's table, and every one is reachable in three draws:
  - 5R/1B ← 4R/1B (R);
  - 4R/2B ← 3R/2B (R) or 4R/1B (B);
  - 3R/3B ← 2R/3B (R) or 3R/2B (B).

  Blue can never be lost.

## Grades 2–3 (pp. 1–4, Problems 1–6): checks out completely

- **P1:** RR→3R/1B, RB→2R/2B, BR→2R/2B, BB→1R/3B. Only 2R/2B has more than one colour story.
- **P2:**
  - The marked example (R1 → R1 B1 R2 → "next draw could be R2") is legal.
  - The tree has two roots, three branches each and six colour boxes, matching the six marked histories.
  - Each final colour count has exactly two histories, so all are tied.
- **P3:** copying gives 1/3, 1/3, 1/3, all tied. Return-only gives 1/4, 1/2, 1/4, so one red is the most likely.
- **P4:** a 3R/2B finish has the stories RRB, RBR and BRR. Each has chance 1/12, and each is 2 of the 24 marked histories.
- **P5:** 5R/1B has only RRRR. 4R/2B has 4 stories and 3R/3B has 6.
- **P6:** no colour can vanish.

## Grades 4–5 (pp. 1–4, Problems 1–6): checks out completely

- **P1:** six marked histories, two per total.
- **P2:** return-only gives 1/4, 1/2, 1/4.
- **P3:** RRB, RBR and BRR are each 1/12.
- **P4:** 24 histories, 6 per total. RRR and BBB have 6 each; each of the six mixed words has 2.
- **P5:** 120 histories, 24 per total, so 1/5 each. "Without making a 120-row list" is right, since 5! = 120.
- **P6:** five draws give 720 histories with 1/6 per total, and n draws give 1/(n+1).

## Encore packet (pp. 1–3, Problems 1–3): correct

- **Demo figure, p. 1:** R0 B0 → draw R0, add the other colour → R0 B0 B1. This is legal under the page's own labelling rule.
- **P1:**
  - Copying gives one red and one blue with chance 2/6. The add-other rule gives 4/6, and add-nothing gives 2/4, so add-other is the answer.
  - The add-other histories with one red are (R0,B0), (R0,B1), (B0,R0) and (B0,R1).
  - The add-other finals are RR 1R/3B, RB and BR 2R/2B, and BB 3R/1B.
  - Each of the three columns has six lines, and the add-nothing column needs four.
  - The extension stays open. Add-other at three draws gives 1/24, 11/24, 11/24, 1/24, and at four draws it gives 1/120, 13/60, 11/20, 13/60, 1/120.
- **P2:** after four draws the forecast is (r+1)/6.
  - The most likely red is 5/6, from RRRR only. The least likely is 1/6, from BBBB only.
  - The tie at 1/2 comes from exactly the six 2R2B words.
  - Forecasts 1/6 to 5/6 come from 1, 4, 6, 4 and 1 stories, so different stories can give the same forecast.
  - The forecast equals the red share of the actual bag after every one of the 120 marked histories.
- **P3:**
  - The 12 printed cards are exactly the 12 marked two-draw histories from R0, B0, G0, each with chance 1/12.
  - There are six final bags with two cards each, but the colour words differ: RR is 1/6 and RG is 1/12.
  - Three draws give 10 bags, each with 6 of the 60 histories.

## Adult guides

**Base guide:** correct throughout. I checked:

- **Overview:**
  - after n draws, n+2 counters and the composition (r+1, n−r+1);
  - the uniform total 1/(n+1);
  - the word probability r!(n−r)!/(n+1)! and n!/[r!(n−r)!] words;
  - (n+1)! equally likely histories, with 6 (two per total) for n=2 and 24 (six per total) for n=3;
  - RR, RB, BR and BB at 1/3, 1/6, 1/6, 1/3, and return-only at 1/4 each with totals 1/4, 1/2, 1/4;
  - "after red, the next red chance is 2/3; after blue, it is 1/3". This is true at every position as the one-step conditional, though not given a full history.
- **Every key:**
  - the K-1 P3 position pairs and the P4 table;
  - the 2–3 P2 six-row table and the P4 factor products;
  - the 4–5 P4 word groups;
  - the 4–5 P5 transition table: 6×4 | 6×3 + 6×1 | 6×2 + 6×2 | 6×1 + 6×3 | 6×4;
  - the 4–5 P6 proof.
- **Other figures:**
  - "counting to six" (K-1 bags hold at most 6);
  - "four pages per band";
  - 120 rows for four draws.

Item 4 concerns the kit.

**Bonus guide:** the mathematics is correct throughout. I checked:

- the three two-draw distributions, the history weights 1/6 and 1/4, and the next-red forecast (r+1)/(r+b+2) with its 1/6 to 5/6 range;
- the three-colour theorem with its hypotheses, which holds by enumeration for n ≤ 6 with 1/C(n+2,2) per vector, 2r!b!g!/(n+2)! per word, (n+2)!/2 histories and n! per vector;
- 12 histories, 6 vectors and 2 each for n=2; 60, 10 and 6 for n=3;
- the P3 word classes 6, 3×2 and 6×1;
- 60 = 12 × 5 third identities, and 27 colour words;
- the kit, where six per colour covers every task (at most 5, 3 and 4 of one colour), and the eleven-child totals (30 per colour, 50 cards, 150 slips, 10 sheets).

Two formulas on p. 3 are misprinted; see item 1.

## Located problems (4)

### 1. Bonus guide p. 3, "Problem 3 (page 3)": two printed formulas are garbled

- **Quoted text (as printed):**
  - "For (3,0,0), the one color word has 123=6 identity histories"
  - "Total histories are 34...*(n+2)=(n+2)!/2, yielding 1/C(n+2,2)."
- **Evidence:** `check.py`, section H (the only two FAIL lines).
  - `guide.md` has `1*2*3=6` and `3*4*...*(n+2)`. `guide_renderer.py` turns `*text*` into italics (line 31: `re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', s)`). Its italic face is mapped to the regular font, so the asterisks vanish.
  - The PDF text and a rendered crop both read "123=6" and "34...*(n+2)".
  - The intended statements, 1·2·3 = 6 and 3·4·…·(n+2) = (n+2)!/2, are true (checked for n ≤ 6). As printed, though, the first reads as "one hundred twenty-three equals six". The second reads as 34 times … times (n+2).
- **Smallest fix:** in `guide.md`, write `1×2×3=6` and `3×4×...×(n+2)` (the base guide already uses ×), then rebuild. `1/(3*4)` earlier in the same section prints correctly but could use × for consistency.

### 2. K-1 p. 1, Problem 1: "draw stories" has a second reading, and on it the answer changes

- **Quoted text:**
  - Student: "Which bags can come from two different draw stories?"
  - Guide p. 3 key: "Only the middle bag has two different two-draw *color* stories."
  - Guide p. 2 launch (shared by all bands): "Do a second draw so children see that both red identities can be selected."
  - The materials give every kit identity labels R1, B1, R2, ….
- **Evidence:** `check.py`, section C.
  - Counted by colour, only 2R/2B has two stories (RB, BR).
  - Counted by which counter was drawn, which is the distinction the launch has just shown, each bag has exactly two: RR as R1R1 or R1R2, BB as B1B1 or B1B2, and RB and BR once each. So "every bag" is a defensible answer, and the key does not say whether to accept it.
  - The same reading gives 24 stories, not 6, for K-1 P3's 3R/3B. That page's six 4-cell rows do signal colour stories there.
- **Smallest fix:**
  - On the page, write "two different color stories", which is the 2–3 page's wording.
  - In the key, add: "If a child counts which red was drawn, RR and BB also have two stories each. Accept this, then ask which bags have two different colour orders."

### 3. K-1 p. 2, Problem 2: one possible bag is not printed, though the question asks for all

- **Quoted text:**
  - Student: "Which bags can you make after three draws? Make a story for each possible bag, and cross out any impossible bag." The four printed bags are 4R/1B, 2R/3B, 5R/0B and 1R/4B, each with three story cells.
  - Guide p. 3: "For the printed choices: … The full collection of possible three-draw bags also includes 3R/2B, via RRB, RBR, or BRR."
- **Evidence:** `extract.py` reads exactly those four bags and 12 story cells (`check.py`, section C).
  - The possible three-draw bags are 1R/4B, 2R/3B, 3R/2B and 4R/1B.
  - So the page's layout implies three possible bags out of the four printed. The literal question has four answers, and the fourth has no box. A child who answers only from the printed bags is wrong on the literal reading but right on the key's "For the printed choices".
- **Smallest fix:** "Which of these bags can you make after three draws? …". Keep 3R/2B in the key as the follow-up "Is there another three-draw bag?" Alternatively, if finding all bags is the intent, add a blank fifth bag box with three story cells.

### 4. Base guide p. 2, "Materials and readiness": the kit is one counter of each colour short for two uses the packet invites

- **Quoted text:**
  - "per pair, five red plus five blue counters of equal size and feel" and "supply pencils plus a small tray for each ending bag".
  - K-1 P1: "Make every different bag you can reach after two draws."
  - 4–5 P6: "What do you predict about red-draw totals after five draws, or after more draws? Explore your prediction".
- **Evidence:** `check.py`, section F.
  - Any story of at most four draws needs at most 5 of one colour, so five each covers every printed bag built one at a time.
  - Building all three K-1 P1 bags at once (one per tray) needs 6 red and 6 blue.
  - In a random five-draw story, the first four draws are one colour with chance 2/5. The fifth then repeats that colour with chance 5/6. So 1/3 of five-draw stories (RRRRR or BBBBB) need a sixth counter of one colour for the last copy, and any sixth draw would come from an incomplete bag.
  - The guide does not say to draw rather than build kept bags.
- **Smallest fix:** "per pair, six red plus six blue counters". In general, an n-draw story needs n+1 of each colour, so six covers every five-draw story and all three K-1 P1 bags at once. Alternatively, keep five and add "record finished bags by drawing them; for runs longer than four draws add counters".

## Not checked

- **Source:** the citation of Janko Gravner, UC Davis MAT 235B slides 12–14 ("Pólya's urn") and the bonus guide's *Math Circle by the Bay* reference, because neither is in this checkout. I verified the mathematics they are cited for independently above.
- **Physical handling** (both guides already mark it untested):
  - mixing, blind draws, and counters of equal feel;
  - removable labels;
  - cutting the bonus p. 3 cards.
- **The packets' own checkers:** `src/check.py`, `verify.py`, `verify_math.py`, `verify_revision.py`, `facilitator-src/check_math.py` and the bonus `student/verify.py`, which I did not run, by design.
