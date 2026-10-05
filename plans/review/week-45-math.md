# Week 45 (The visible side): math check

Scope:

- Base packet in `lowell-math-circle-year-2/week-45/`: `week-45-k-1.pdf` (4 pp., Problems 1–7), `week-45-grades-2-3.pdf` (4 pp., Problems 1–6), `week-45-grades-4-5.pdf` (4 pp., Problems 1–7) and `week-45-facilitator.pdf` (6 pp.).
- Bonus companion in the same folder: `week-45-bonus.pdf` (3 pp., Problems 1–3) and `week-45-bonus-facilitator.pdf` (4 pp.).

I ignored the archive folders. My scripts and their outputs are in [checks/week-45/](checks/week-45/). Checked October 5, 2026.

**Result: every student problem in every band is correct, with the intended answer and the right number of answer slots. No answer in either guide is wrong. I found one problem, in the bonus guide: its overview prints the count of histories as "322=12".**

## How it was checked

- **The PDFs match their sources.** All six delivered PDFs are byte-identical (MD5) to their reference copies in `source/week-45/editable/reference-pdfs/` and `source/week-45-bonus/reference-pdfs/`.
- **`pdf_extract.py` reads every diagram from the PDFs.** It uses PyMuPDF to read the drawing and text layers of the delivered PDFs and writes `pdf_geometry.json`. Output: `pdf_extract.out`, 97 checks, 0 failures.
  - **Card faces (all bands).** Each of the 48 faces shows one letter, R or B, that matches its fill. All faces are the same size, 2.10 × 2.80 cm. Each face shows either one mark or a black cover, never both and never neither.
  - **Catalogue diagrams.** These read 1–6 from left to right in one row, with "same card" brackets under 1–2, 3–4 and 5–6. The colours are R, R, R, B, B, B. All bands use the same catalogue.
  - **Launch picture.** Ticket 4 leads to a covered B face, then "turn over" leads to an R face marked 3. This matches the catalogue: face 3 is the partner of face 4.
  - **Chooser picture.** Tickets 1 and 3 each lead to a covered red face.
  - **Answer slots.**
    - K–1 P5 has three groups of three boxes.
    - K–1 P7 has two boxes.
    - 2–3 P1 has tickets 1–6.
    - 4–5 P6 has tickets 1–6, with no colours given away.
  - **Problem numbering** runs consecutively in every packet.
  - **Bonus.**
    - All 16 tokens are circles, and each label letter matches its fill.
    - The P1 launch card is G|B, and the outputs are G then B. "L face" sits under G.
    - The P1 table has rows RR, RB, BB, with RB's red face on the L side. Its columns are L/L, L/R, R/L, R/R.
    - The P2 picture shows P (with the choice dot), Q and R (with the prize star). After "Host A opens Q", it shows P, empty, R, with the dot still at P.
    - Both host tables list all six prize/ticket stories.
    - The P3 example shows hidden B, then F, then report R. The P3 table has rows R1, R2, R3, B, and columns H1, H2, F. There are four numbered redesign slots.
- **`check_base.py` enumerates every base task exactly.** It reads the card model from the extracted diagrams, not from the author's text. Output: `check_base.out`, 45 checks, 0 failures.
  - It checks every one-ticket removal, every added ticket, every 3-ticket and 2-ticket cup, every card removal, and all 63 non-empty ticket subsets. It also checks every card selection and all 64 six-round sequences.
  - It parses the guide's overview table, the 2–3 P1 table, the K–1 lists and the 4–5 P6 T-list, and compares each with the enumeration.
  - A 60,000-round simulation of the printed protocol gives 0.662 for the six-ticket rule and 0.500 for chooser {1,3}.
- **`check_bonus.py` enumerates every bonus history.** It covers the 12 same-card histories, 6 prize/ticket histories for each host and 12 reporter histories, and all 16 honest/flip assignments of four tickets. Output: `check_bonus.out`, 27 checks, 1 failure (the problem below).
  - It checks the n-clue extension for n ≤ 8.
  - It checks the "door 3 opened" and "always open 2" extensions.
  - It checks the b·h = r·f extension by enumerating histories for r, b, h, f ≤ 4.
  - It checks the guide's P1, P2 and P3 tables and the kit arithmetic: 14 tickets per kit, 70 tickets, 20 cards, 15 doors, 20 counters and 10 cups.

## K–1: checks out completely

- **P1.** Red underneath: 1, 2, 4. Blue underneath: 3, 5, 6. Exactly four pairs show the same colour but hide different colours: {1,3}, {2,3}, {4,5}, {4,6}.
- **P2.** With red showing, hidden red has 2 ways and hidden blue 1. Removing 1 or removing 2 makes a tie. Removing 3 gives 2–0, and removing 4, 5 or 6 changes nothing.
- **P3.** With blue showing, hidden red has 1 way and hidden blue 2. Removing 5 or removing 6 makes a tie.
- **P4.** Before any addition: 1–1. Adding 2 gives 2–1 for red. Adding 4, 5 or 6 leaves 1–1. The page's "show the face named by each draw" overrides the page rule "show its red face", and the guide says so.
- **P5.** Exactly three cups: {3,4,5}, {3,4,6}, {3,5,6}. The page prints three slots.
- **P6.** Removing RB makes a red clue always hide red. Removing RR makes it always hide blue.
- **P7.** Exactly two cups: {1,3} and {2,3}. The page prints two boxes.

## Grades 2–3: checks out completely

- **P1.** Tickets 1, 2, 5 and 6 have the same colour on both faces.
- **P2.** Given red showing, guess red: 2/3.
- **P3.** Given blue showing, guess blue: 2/3. The guess changes colour, but the rule "guess the showing colour" stays the same. The guide covers both readings.
- **P4.** No. The two-ticket chooser gives 1/2; the six-ticket rule gives 2/3.
- **P5.** Yes (remove RB), yes (remove RR), no. Removing BB leaves 2/3.
- **P6.** {1,3} and {2,3}.

## Grades 4–5: checks out completely

- **P1.** Red showing: hidden red 2/3, hidden blue 1/3. Blue showing: hidden red 1/3, hidden blue 2/3.
- **P2.** The friend's argument fails: after a red clue, RR has probability 2/3 and RB 1/3.
- **P3.** A revealed mark fixes the hidden colour: 1, 2, 4 hide red; 3, 5, 6 hide blue.
- **P4.** Yes: 1/2 against 2/3.
- **P5.** No. All 64 six-round sequences have positive probability under both rules.
- **P6.** Exactly 16 subsets: {1,3} or {2,3}, together with any subset of {4,5,6}.
- **P7.** No. With whole cards only, the red-clue counts are (2,0), (0,1), (0,0), (2,1), (2,0), (0,1) and (2,1), so there is never a positive tie.

## Adult guide (base): checks out completely

- **Overview.** The ticket table, the 2/3 and 1/2 conditional probabilities and the RR double weight are all correct. So is the exact design condition: a red clue is fair exactly when ticket 3 is in the cup with exactly one of tickets 1 and 2. That gives 2 × 2³ = 16 fair subsets, two of them two-ticket cups, and none made of whole cards. The hypotheses are stated: uniform tickets, replacement, and only the colour is public.
- **Answers, hints and extensions.** Every answer agrees with the enumeration. That includes the K–1 P4 all-rounds alternative (adding 2 or 4 gives 2–1 for red; adding 5 or 6 gives 2–1 for blue) and the 4–5 P5 values (2/3)⁶ and (1/2)⁶.

## Bonus student pages: check out completely

- **P1.** Red, red: RR has 4 histories and RB has 1, so the best guess is RR at 4/5. Red, blue: only RB with L then R, so RB is certain.
- **P2.** With Host A, switching wins 4 of 6 histories, or 2/3. With Host B, 2 of the 6 histories are discarded, and switching wins 2 of the remaining 4, or 1/2. So the host's knowledge changes the answer.
- **P3.** A blue report has 5 histories, and 3 of them hide red, so red is the better guess at 3/5. A tie needs exactly 3 honest tickets and 1 flipping ticket, in any order.

## Problem found

### 1. Bonus guide, page 1, Mathematical overview, first paragraph: the history count prints as "322=12"

- **Quoted text:** "…independently choose L/R faces with replacement for each of two clues. There are 322=12 equally likely histories."
- **Evidence:**
  - The PDF text layer has "322=12" in a single DejaVuSans span. No multiplication sign or italic font tells the digits apart, and 322 ≠ 12.
  - The source `source/week-45-bonus/guide.md`, line 3, reads `3*2*2=12`.
  - `guide_renderer.py`, line 31, turns `*…*` into `<i>…</i>`, which here wraps the middle 2. The font family maps italic to the regular font, so the asterisks disappear and leave "322".
  - The intended statement, 3 × 2 × 2 = 12 histories, is correct; the enumeration in `check_bonus.py` gives 12.
- **Smallest fix:** in `guide.md`, line 3, write `3×2×2=12` (or `3 × 2 × 2 = 12`), then rebuild the bonus guide.
- **Optional:** the same renderer rule turns `b*h=r*f` on line 73 into "bh=rf" on page 3. That still reads correctly as products, so it needs no fix, but writing `b×h=r×f` would stop it depending on the rule.

Not counted, because it is not a mathematical-correctness issue: the base guide's materials paragraph says "For ten children". The current group in `worksheet-workflow/context.md` is eleven children.
