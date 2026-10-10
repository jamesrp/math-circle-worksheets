# Week 27 (stable pairings and deferred acceptance): math check

Scope: everything current in `lowell-math-circle-year-2/week-27/`, archive folders excluded:

- `week-27-k-1.pdf` (W27-K-v3, 7 pp.: a worked example on p. 1, then P1–P6 one per page)
- `week-27-grades-2-3.pdf` (W27-23-v3, 6 pp.: the same example on p. 1, then P1–P5)
- `week-27-grades-4-5.pdf` (W27-45-v2, 6 pp., P1–P6)
- `week-27-facilitator.pdf` (19 PDF pages: an unnumbered overview, printed pp. 1–17, and an appended route note numbered 19). Guide page numbers below are the printed ones.
- The bonus companion `week-27-bonus.pdf` (W27-BON-v1, 4 pp., P1–P4) and its guide `week-27-bonus-facilitator.pdf` (W27-BON-FAC-v1, 5 pp.).

Sources read: `source/week-27/editable/src/k-1.tex`, `grades-2-3.tex` and `grades-4-5.tex` (exact token coordinates), `build_packets.py` and `examples.py` (layout only), and `source/week-27-bonus/student-src/bonus.tex`. The delivered PDFs are byte-identical to the reference copies in both source folders. I did not use the packet's answer files (`math_checks.json`, `math-checks.json`, `checks.json`), its checkers or its review notes. Checked October 10, 2026.

**Result: no mathematical errors on any student page in any band, including the bonus. The bonus guide checks out completely. The base guide's overview, theorems, proofs, answers, request logs and all 16 answer figures are correct. It has three located problems, all minor: a "full audit" table that lists one blocker per row while saying all are recorded (problem 1), a Grades 4–5 key that calls 16 the "exact expected answer" when 13, 14 and 15 are also correct (problem 2), and a shared launch that works through, in full, one printed case of K–1 Problem 1 and of Grades 2–3 Problem 1 (problem 3).**

## How it was checked

My scripts and their saved outputs are in this folder (to be committed as `checks/week-27/`). Each script finds the repository from its own location. Run `extract.py` first; the check scripts run it themselves if `extracted.json` is missing.

- `common.py`: my own stable-matching tools. These find blocking pairs (with incomplete lists, an unlisted partner is unacceptable and any acceptable partner beats being unpaired), enumerate perfect and partial matchings, and list every complete strict profile. They also run the printed asking rules over every choice of which free asker moves next, memoised, with an option for the "keep the first asker" rule. A replayer checks a given request log for legality.
- `extract.py` → `extracted.json`, `extract.out`: reads every preference strip, drawn pairing and blank board from the student PDFs with pdfplumber. A circle is a curve and a square a filled square rect. A strip row is an owner token, a colon and a box. Drawn pairings are line segments whose ends sit on token centres; shading is read from the fill colour. Every one of the 722 tokens matches a node in the TeX source in kind, letter, position (within 1 pt), size and shading.
- `check_students.py` → `check_students.out`: every student problem. It also runs a census of all 46,656 complete three-pair profiles (every stable pairing; the asking rules from both sides in every order; the changed rule in every order) and a hill-climbing search over four-pair profiles for the most requests.
- `check_guide.py` → `check_guide.out`: every profile, candidate table, reversal table, request log and answer figure in the guide, read from the PDF and checked against the student pages and my own enumeration. Figures are read as vector lines, and each one's matching is compared with its caption. The script also checks the overview's theorems on all three-pair profiles and Extension B for n = 1–4.
- `check_bonus.py` → `check_bonus.out`: bonus P1 scores and blockers, P2 partial matchings and P3 roommate pairings. For P4, it searches for two stable matchings that leave different objects unpaired: exhaustively over every 2×2, 2×3 and 3×2 incomplete-list market (64,625 markets), and over 100,000 random 3×3 markets.

**Results common to every band.** Every strip in every band lists only opposite-side letters, each once, with one slot per letter. Every circle and square token is drawn with equal width and height. K–1 task icons are 20.1 mm; the page-1 example uses 12.7–14.0 mm icons in both K–1 and Grades 2–3. The Grades 2–3 and 4–5 task icons are 9.7–13.0 mm, and the 4–5 hold/release example uses 7.6 mm icons. The page-1 example (K–1 and Grades 2–3) is correct: current pairs P–V and Q–U, dashed P–U, shading on each strip's current partner. Left panel: P prefers U to V and U prefers P to Q, so they block. Right panel: U ranks Q first, so "no" and no block. No page has fewer blank boards than the stable pairings it asks for.

## K–1: checks out completely

- **P1:** in the top case only AX / BY can stay (all four have first choices; the crossed pairing is blocked by AX and BY). In the bottom case only AX / BY can stay; AY / BX is blocked by AX alone.
- **P2:** top: both pairings stay. Bottom: only AY / BX (AX / BY is blocked by AY and BX). Each case has two blank boards.
- **P3:** both drawn pairings are AX / BY.
  - Top: the only blocker is AY. Reversing A or Y alone makes it stable; reversing B or X leaves AY.
  - Bottom: the blockers are AY and BX, with disjoint ends, so no single reversal works: cross it out.
- **P4:** top: Y: A, B is the only fill that keeps both pairings stable (Y: B, A lets BY block AY / BX). Bottom: impossible; BX blocks AX / BY whatever Y says.
- **P5:** of the 16 two-pair profiles, exactly 7 make only the left (straight) pairing stable, so two different sets exist.
- **P6:** exactly 2 profiles make both pairings stable, and two cases are printed.
- (Not an error: P4's top case is P2's top profile with Y blanked, and it is also one of the two P6 answers, so a child who looks back can copy it. The guide's route places P3–P6 on a later visit.)

## Grades 2–3: checks out completely

- **P1:** top: only AX / BY stays; on AY / BX the only pair to join is A–X. Bottom: both stay, so nothing is joined.
- **P2:** only AY / BZ / CX of the six candidates is stable; six blank boards are printed.
- **P3:** exactly three are stable: AY / BX / CZ, AZ / BX / CY and AZ / BY / CX.
- **P4:** exactly 4 of 24 pairings are stable: AW / BX with either CY / DZ or CZ / DY, and AX / BW with either. No pairing gives all eight letters a first choice. Four boards are printed.
- **P5:** of the 46,656 complete profiles, 34,080 have one stable pairing, 11,484 exactly two and 1,092 three. No profile has more than three, so the task is possible. Two boards are printed.

## Grades 4–5: checks out completely

- **P1:** top (the K–1 P2 top profile) has two stable pairings, with two boards printed. Bottom (the 2–3 P2 profile) has one, with three boards printed; nothing on the page asserts three.
- **P2:** in every order of free askers, A–D asking gives AW / BY / CZ / DX in 8 requests, and W–Z asking gives AZ / BY / CW / DX in 7. Both results are stable and they differ, so the answer is yes. These are the only 2 stable pairings of the 24. The hold/release example is consistent with its text: P–U before, Q–U after.
- **P3:** under "keep the first asker", every order ends with everyone paired, on all 46,656 three-pair profiles. In 36,288 of them some order ends unstable, so the task is possible.
- **P4:** n² = 16 can never be exceeded. The least such bound is 13, and a four-pair profile that needs 13 requests in every order exists (`check_guide.out`). The printed rules always finish with everyone paired.
- **P5:** on all 46,656 three-pair profiles, from both sides and in every order, the rules end in the same stable pairing.
- **P6:** the most last-choice letters in a stable three-pair pairing is 3 (exhaustive).

## Bonus companion: checks out completely

- **Opening example:** current pairs are U–P and V–Q. V lists P before its current Q, and P lists V before its current U, so V and P block.
- **P1:** the six totals are AX/BY/CZ 15, AX/BZ/CY 13, AY/BX/CZ 11, AY/BZ/CX 10, AZ/BX/CY 11 and AZ/BY/CX 12.
  - The unique lowest total is 10 (AY / BZ / CX), and BX blocks it.
  - The only stable pairing is AY / BX / CZ, total 11. The table has six rows.
- **P2:** first lists: only AX is stable, leaving B and Y unpaired (two rows printed). Second lists: exactly AX / BY and AY / BX are stable, both leaving C and Z unpaired (three rows printed).
- **P3:** with the left lists every one of the three pairings is blocked (by BC, AB and AC respectively). With the right lists only AB / CD is stable. Six boards are printed for 3 pairings × 2 lists.
- **P4:** the requested pair of stable pairings does not exist. No stable pairing set ever changed the unpaired objects in the exhaustive or random search above.

## Bonus guide: checks out completely

Every total, every "full blockers" list in P1, both P2 profiles and the depth variant (without A–X, BX is uniquely stable, leaving A and Y unpaired) are correct, and so are all roommate blockers. The alternating-path proof that the unpaired set cannot change is correct under its stated hypotheses: strict lists, mutual acceptability, and any acceptable partner preferred to being unpaired.

## Base adult guide

The overview is correct and states its hypotheses:

- the n² request bound;
- termination with a perfect stable pairing for equal sides and complete strict lists;
- the improving-hold invariant and the stability proof;
- asker optimality and order independence, checked on all three-pair profiles from both sides;
- "reversing the proposing side can change it" (4–5 P2);
- the bound of three last-choice letters for three pairs.

All of the following match the delivered student pages and my enumeration:

- every "exact strips" profile;
- the K–1 P3 reversal table;
- the seven K–1 P5 profiles and the two P6 profiles, with the completeness arguments;
- the 2–3 P4 block argument and the 2–3 P5 construction;
- both 4–5 P2 request logs, replayed step by step, every "keeps" and "released" entry;
- the 4–5 P3 counterexample, with the stable result of the ordinary rule;
- the P4 and P5 proofs and the P6 construction;
- the census numbers on p. 15 (46,656 profiles, 279,936 candidates, 60,324 stable, maximum 3);
- Extension A's first-rejection proof;
- Extension B (n for n ≥ 2, and 2 for n = 1).

All 16 answer figures show the matching named in their caption or text.

## Located problems

### 1. Guide p. 6, Grades 2–3 Problem 2 (and the 4–5 P1 reference to it): the "full audit" lists one blocker per row but says all are recorded (minor)

- **Quoted text:** "Only AY / BZ / CX stays. Here is a full audit. One witness is enough to reject a candidate; the checker records all blockers." The table is headed "Blocking pair(s), or stable", with rows "AX / BY / CZ — BX" and "AZ / BY / CX — AY". Guide p. 10 sends the 4–5 P1 key to this audit.
- **Evidence (lists A: X>Y>Z, B: X>Z>Y, C: Y>X>Z; X: C>B>A, Y: A>C>B, Z: B>A>C):**
  - AX / BY / CZ is also blocked by:
    - BZ: B prefers Z to Y, and Z prefers B to C.
    - CX: C prefers X to Z, and X prefers C to A.
    - CY: C prefers Y to Z, and Y prefers C to B.
  - AZ / BY / CX is also blocked by:
    - BZ: B prefers Z to Y, and Z prefers B to A.
    - CY: C prefers Y to X, and Y prefers C to B.
  - Read as the complete list, the table would lead an adult to tell a child who names CY or BZ that they are wrong. The same pattern appears on p. 7 (2–3 P3), where AY / BZ / CX lists only AX, though BX also blocks (B prefers X to Z, and X prefers B to C); that page does not claim completeness. The p. 9 table already carries the right caveat.
- **Smallest fix:** on p. 6 replace "the checker records all blockers" with "the table shows one; a child may find another." Alternatively, print the full lists: "BX, BZ, CX, CY" and "AY, BZ, CY", and on p. 7 "AX, BX".

### 2. Guide p. 13, Grades 4–5 Problem 4: "Exact expected answer: 16" (minor)

- **Quoted text:** "Exact expected answer: 16 requests; 100 with ten per side … These are valid upper bounds; neither is asserted to be the smallest possible upper bound."
- **Evidence:** the task asks for "a number of requests that can never be exceeded", so any number from 13 up, with a reason, is correct. The least such number is n² − n + 1: 13 for four per side, 91 for ten.
  - Why: when an asker makes its n-th request, each of the other n − 1 receivers has rejected it and so holds someone. That request fills the last receiver and ends the run. So at most one asker uses all n requests, and 4 + 3·3 = 13.
  - It is reached: A: Z>Y>X>W, B: X>Z>Y>W, C: Z>X>Y>W, D: Y>X>Z>W; W: B>C>D>A, X: A>C>D>B, Y: B>C>A>D, Z: D>A>B>C takes 13 requests in every order (`check_guide.out`).
  - The guide's hedge is accurate, but under the heading "exact expected answer" an adult has nothing to judge a child's sharper "13" by, and could mark it wrong.
- **Smallest fix:** retitle the heading "A sufficient answer: 16 requests; 100 with ten per side". Add: "Any number of at least 13 with a correct reason is right. 13 = 4 × 3 + 1 is the least: once an asker makes its fourth request, every other receiver already holds someone, so that request ends the run (91 for ten)."

### 3. Guide p. 2, shared launch: the demonstration is a printed task, solved in full (minor)

- **Quoted text:** "Use A: X > Y; B: X > Y; X: A > B; Y: A > B. Place AX and BY. Ask, 'B would rather have X. Does X also want B more than A?' … no, so BX does not block. Now change the pairing to AY and BX without changing strips. A and X both want one another: they block."
- **Evidence:** this is exactly the profile of K–1 Problem 1's bottom case and of Grades 2–3 Problem 1's top case (p. 2 of each packet), with the same two pairings drawn. The launch shows the whole answer to those cases: AX / BY stays, and AY / BX is blocked by A–X, the pair the 2–3 page asks children to join. The tie between launch and task is confirmed by `check_guide.py`. AGENTS.md asks for a non-task instance.
- **Smallest fix:** use a profile printed nowhere, with the same two-step script, for example A: Y > X; B: X > Y; X: A > B; Y: A > B.
  - Place AY and BX first: X would rather have A, but A prefers Y, so XA does not block.
  - Then place AX and BY: A and Y both want each other, so they block.
  - `check_guide.py` confirms the profile is unused and both steps behave as described.

## Notes (not errors)

- Guide p. 11: "This instance-specific count is not a claim that all markets have fixed request counts under every scheduling variant." Under the printed rules the count is in fact always fixed. Each asker asks exactly its choices down to its final partner, and Extension A shows that partner does not depend on the order. This held on every three-pair profile from both sides. If "variant" means the changed P3 rule, the hedge is apt.
- Guide p. 12 (4–5 P3): the counterexample depends on A asking X before B does. With B first, the changed rule gives the stable AY / BX / CZ. The guide asks for "one legal asking order", so this is consistent. If an order-proof example is wanted, use A: X>Y>Z, B: X>Y>Z, C: Y>X>Z; X: C>A>B, Y: A>B>C, Z: A>B>C. Every order of the changed rule ends unstable there (1,296 of the 46,656 profiles have this property).
- The route note is numbered 19; there is no printed page 18. This is a label only.
