# Week 4 (stars and wheels): math check

Math check for the Week 4 review card, October 5, 2026. I opened no use logs or session records.

**What I checked**
- `week-04-k-1.pdf` (F04-K-v4, 10 pp., Problems 1–10).
- `week-04-grades-2-3.pdf` (F04-M-v4, 9 pp., Problems 1–9 and two wheel pages).
- `week-04-grades-4-5.pdf` (F04-U-v4, 11 pp., Problems 1–12 and two wheel pages).
- The adult guide `week-04-facilitator.pdf` (F04-FAC-v4, 10 pp.): overview, materials arithmetic, launch, every answer, hint and claim, and section 5.
- Sources in `source/week-04/src/` and `guide-src/`, read for coordinates and wording only.
- Not checked: `week-04-return-visit.pdf` and its guide. They are a separate companion with their own sources (`source/week-04-return-visit/`), and the Week 15 check also left its companion out.

**Scripts, in [checks/week-04/](checks/week-04/)**

Each script finds the repository from its own folder. `check_codes.py` needs `wordfreq` and `english-words` (pip). Run `extract_pdf.py` first: it writes `pdf_geometry.json` (about 670 KB, not committed), which `check_rings.py` and `check_times.py` read.
- `extract_pdf.py` reads every circle, segment and word from the three student PDFs into `pdf_geometry.json`.
- `check_rings.py` covers all 65 rings: dot count, equal spacing, x/y scale, top dot, black start dot and the label underneath. It also reads the K–1 Problem 5 pictures and the four 4–5 Problem 9 drawings from their line segments. Every answer comes from simulating the hop rule, and each is compared with the guide.
- `check_pictures.py` recognises each K–1 icon from its strokes. It reads the picture-ring order and every row of Problems 8–10 and checks the answers.
- `check_codes.py` reads both wheels: letter angles, diameters, and that the outer letters are not hidden. It simulates "set to D", reads each printed code, and tries all 26 settings against two English word lists (60k and 235k words). It also checks the setting tables.
- `check_times.py` checks the Problem 12 numbering, line counts and the envelope cusps. It draws `times_tables_completed.png`.
- `check_theory.py` brute-forces the general claims in the guide.
- `edge_cases.py` holds the counterexamples below.
- Saved outputs are the `*.out` files, `pdf_geometry.json` and `times_tables_completed.png`. The page renders were not kept.

## Results by band

**K–1 (Problems 1–10): every intended answer is right. Problem 5 (item 2) relies on a rule it does not restate.**
- Big rings of 4, 5, 6 and 7 dots: 4.10 in across, dots 0.8 in, spacing error under 0.01°, black start dot at the top. Every small ring matches its big ring and its "hop k" label.
- P1–P3 and P6–P7: the hops that land on every dot are 1 and 3 on 4 dots; 1, 2 and 3 on 5; only 1 on 6; and all six on 7.
- P4 starts: 2, 3, 2, 1.
- P5: the five pictures are regular, with a vertex at the top. Hops 1–5 that draw each: [1, 4], [2, 3], [1, 5], [2, 4], [3].
- Picture ring on pp. 8–10: sun, moon, heart, tree, fish, house, clockwise from the top, the same on all three pages and evenly spaced.
- P8: the rows are heart/house/sun, then fish/moon/heart, then sun/tree/fish. That uses 3 of the 5 blank rows.
- P9: the hops back are 5, 4, 3, 2, each unique among hops 1–5.
- P10: the secret hop is 3. Moon→fish, heart→house, fish→moon, house→heart.

**Grades 2–3 (Problems 1–9): checks out completely.**
- All 21 rings are regular and correctly labelled.
- Starts:
  - P1: 1, 2, 1, 4.
  - P2: 2, 1, 2, 5.
  - P3: 2, 3, 4, 1, 6.
  - P6: 1, 5, 2, 4.
- P7 (hops 4 to n − 1 with exactly 3 starts): 9 → 6; 16 → none, and no hop of any size works; 18 → 15; 15 → 6, 9, 12.
- The codes print exactly as intended, and the P4 decodes are STAR, FOX, WHEEL, PENCIL, I CAN DRAW A STAR.
- Each P8 code has exactly one all-English setting, H and Q, in both word lists.
- P9: X, T, N, E.
- Wheels: 5.500 in and 4.000 in. The 26 letters run clockwise from A at the top in 13.846° steps. Set to D, CAT → FDW and every letter moves 3. The outer letters' glyphs come no closer than 2.13 in to the centre, outside the 2.00 in inner wheel.

**Grades 4–5 (Problems 1–12): every answer is right. The Problem 12 wording is item 3.**
- All 16 rings, numbered or not, are regular.
- Pieces:
  - P1: 1, 2, 3, 4, 1, 6.
  - P2: 2, 3, 5, 4, 2, 3.
  - P3: 4, 2, 6, 9, 1, 5, 15. Its two check rings are 20 dots and 24 dots, matching the first two cases.
- P4: settings J, S and X are each the unique all-word setting. For MROOB, CHEER (K) and JOLLY (D) are the only common words.
- P6: R, I, F, A, and the missing setting is T.
- P8: 5, 7, 11, 13, 17, 19.
- P9 drawings, read from the segments: 15 endpoints with hops {6, 9}; 20 with {5, 15}; 14 with {6, 8}; 21 with {6, 15}. No other hop draws the same lines.
- P10: every double coding is one setting. Twenty-five pairs of non-A settings leave the message uncoded.
- P11: setting C visits 13 letters. Twelve settings visit all 26: B, D, F, H, J, L, P, R, T, V, X, Z.
- P12: labels 0–23 sit clockwise beside the right dots, and 13 → 2.
  - ×2: dot 0 is fixed, 8–16 is drawn twice, and there are 22 distinct lines.
  - ×3: dots 0 and 12 are fixed, 3–9, 6–18 and 15–21 are drawn twice, and there are 19 distinct lines.

**Guide: apart from items 1–4, every statement I checked is true.**

Shapes and counts:
- Overview: starts = gcd, with the 12-dot hop 8 example.
- Every shape name in the K–1, 2–3 and 4–5 tables, including {12/5}, {9/4}, {8/3} and "four five-pointed stars".
- The restarts-only reading 1, 2, 1, 0.

Proofs and arguments:
- The section 5 proof: g pieces of n/g dots, multiples of g, and rotations.
- The polygon case j ≡ ±1 (mod m).
- Hop k and n − k give the same lines, and no other hop does.
- One piece for every hop exactly when n is prime.
- φ(n) one-piece hops and φ(n)/2 pictures.
- 26/gcd(26, s) letters per setting, φ(26) = 12, and the affine-code criterion.
- "Counting connected parts would give 1 every time." Brute force for n ≤ 30 found no drawing with two or more pieces that falls apart.
- The P7 and P8 arguments.
- The counter games: pass 2 of 5 reaches everyone, pass 2 of 4 misses two, and passes 1 and 3 reach all 4.

Materials and setup:
- Every materials total: 61 counters, 6 pencil sets, 14 pencils, 9 rulers, 8 scissors, 10 fasteners, 3 whiteboards, 20 sheets of scrap.
- "6+ colours": no ring a child draws needs more than 6 starts.
- Hopper plus 7 markers covers the 8-dot ring.
- 0.8 in K–1 dots. A 1 in counter clears the next dot by at least 0.88 in, on the 7-ring.
- Wheel sizes, and the CAT/FDW and VWDU→YZGX checks.

## Located problems (4: one wrong mathematical statement in the guide, three wording or reading issues)

### 1. Guide p. 9, Problem 12 answer and section 5 "Times tables": the dents (cusps) are put at the fixed dots, where the curve touches the circle

- **Where:**
  - The Problem 12 answer: "×2: a heart shape (cardioid) with its dent at dot 0, at the top. … ×3: a two-lobed shape (nephroid) with dents at dots 0 and 12."
  - Section 5: "The cusps sit at the fixed points, (k − 1)m ≡ 0 (mod n): dot 0 for ×2 and dots 0 and 12 for ×3 on 24 dots."
- **Evidence** (`check_times.py`, `edge_cases.py` §4, `times_tables_completed.png`):
  - The chord from e^{iθ} to e^{ikθ} touches its envelope at X(θ) = (k e^{iθ} + e^{ikθ})/(k + 1). The derivative X′ = 0 exactly when e^{i(k−1)θ} = −1.
  - So the cusps are at (k − 1)θ ≡ π, not at the fixed points (k − 1)θ ≡ 0. At the fixed points X has length 1, so the curve touches the dot circle there.
  - For ×2 the only cusp is at θ = 180°: inside the circle, R/3 from the centre, toward dot 12 (below the centre on the page). The curve touches the circle at dot 0.
  - For ×3 the cusps are at θ = 90° and 270°, R/2 from the centre, toward dots 6 and 18. The curve touches the circle at dots 0 and 12.
  - On the printed 24-dot rings, 7 of the 22 ×2 chords pass within 0.08R of (0, −R/3). That is the visible dent. At dot 0 only the diameter and the two short chords 1–2 and 22–23 come near.
  - For ×3, 5 chords pass within 0.08R of each of (±R/2, 0). No chord passes near dots 0 or 12 except those that end there.
  - An adult following the guide will look for the dent at the top and tell a child with a correct drawing that it should be at dot 0.
- **Fix:**
  - Problem 12 answer: "×2: a heart shape (cardioid) that touches the circle at dot 0, with its dent inside, a third of the way from the centre toward dot 12. ×3: a two-lobed shape (nephroid) that touches the circle at dots 0 and 12, with its two dents halfway from the centre toward dots 6 and 18."
  - Section 5: "The curve touches the circle at the fixed points, (k − 1)m ≡ 0 (mod n). Its k − 1 cusps lie midway between them in angle, at (k − 1)/(k + 1) of the radius: R/3 toward dot 12 for ×2, and R/2 toward dots 6 and 18 for ×3."

### 2. K–1 p. 5, Problem 5: two of the five pictures need the restart rule, which is stated only inside Problem 4

- **Where:** "Problem 5: Find every hop from 1 to 5 that draws each picture." The page shows the six-pointed star and three crossing lines, and four trial rings with the black start dot of Problems 1–3.
  - The guide's answer (p. 4) is "Six-pointed star: 2, 4. Three crossing lines: 3", with no word about starting again.
  - Its Hint 2 sends children to "your drawings on pages 2–4". On page 3, hop 2 and hop 3 on 6 dots are one triangle and one line.
- **Evidence** (`edge_cases.py` §1, `check_rings.py`):
  - On 6 dots, hopping from the black dot until back, as in Problems 1–3 and 6–7, gives these drawings:
    - hops 1 and 5: the hexagon;
    - hops 2 and 4: one triangle {0, 2, 4};
    - hop 3: one line 0–3.
  - So no hop 1–5 draws either printed picture. The answers 2, 4 and 3 hold only with Problem 4's "If a dot has no line, start again there with the same hop."
  - The guide's suggested route reaches Problem 5 after Problems 8, 6 and 7, none of which needs a restart.
- **Fix:** add to the prompt: "Find every hop from 1 to 5 that draws each picture. Start again if a dot has no line, as in Problem 4." Alternatively, add one line to the guide: "The six-pointed star and the three lines need the Problem 4 restart. A child who only hops from the black dot will find no hop for them."

### 3. Grades 4–5 p. 9, Problem 12 (and guide p. 9): "A dot that lands on itself gets no line"

- **Where:** Student page: "A dot that lands on itself gets no line." Guide: "Dot 0 gets no line" (×2) and "Dots 0 and 12 get no line" (×3).
- **Evidence** (`edge_cases.py` §3): read literally, these dots have no line at all. But other dots' lines end at them:
  - ×2: 12 → 0.
  - ×3: 8 → 0, 16 → 0, 4 → 12 and 20 → 12.
  
  The guide's own counts include those lines (22 and 19 distinct lines). A child, or an adult checking with the guide, may leave out 12–0 or the four ×3 lines into 0 and 12. That also removes the lines that run to where the curve touches the circle.
- **Fix:** student page: "A dot that lands on itself draws no line of its own." Guide: "Dot 0 draws no line of its own (dot 12's line still ends there)", and the same for ×3 (lines from 8 and 16 end at 0, and lines from 4 and 20 end at 12).

### 4. Guide p. 3, K–1 definition: "every dot gets a marker" can never happen

- **Where:** "'Lands on every dot' means every dot gets a marker before the counter is back on the black dot."
- **Evidence** (`edge_cases.py` §2): in the pair protocol on the same page, the partner "puts a marker on each dot it lands on and says 'back' when it reaches the black dot". The black dot holds the counter and is never marked before the counter returns. So, read literally, no hop on any ring qualifies.
  - "Every other dot marked" gives exactly the guide's answers: hops 1 and 3 on 4 dots, all three on 5, hop 1 on 6, and all six on 7.
  - Hint 2 ("is any dot bare?") already uses the right test.
- **Fix:** "…means every other dot gets a marker before the counter is back on the black dot."

## Notes (not counted as problems)
- **"The only other dictionary word is DIFFS" (guide p. 7, 4–5 P4):** this depends on the dictionary. Webster's Second (web2) also lists PURRE (setting X), and DIFFS is rare slang (wordfreq Zipf 1.7). CHEER and JOLLY are the only common words, so the student task is unaffected. Possible wording: "the only other candidates are rare words (DIFFS, PURRE)".
- **K–1 P8 has five blank rows; three are needed.** The guide says the last two stay empty. This is a layout point only.
- **Guide P7 explanation (4–5):** "the same two steps work for any ring and hop" is right in outline. Step 2 gives the piece size as the first whole number of laps, lcm(n, k)/k hops. Equating that with "biggest common number" needs lcm·gcd = n·k, which the child-level sketch leaves implicit. Section 5 gives the complete proof.
- **The 2–3 and 4–5 rule allows hops of n/2:** hop n/2 draws each diameter twice ("there and back"). The guide's tables count these correctly as one piece per diameter.
