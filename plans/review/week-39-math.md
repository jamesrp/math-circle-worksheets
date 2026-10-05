# Week 39 (Road detours): math check

Scope: the current student packets in `lowell-math-circle-year-2/week-39/`:
- `week-39-k-1.pdf` (6 pp., Problems 1–7, footer F39-K-v2);
- `week-39-grades-2-3.pdf` (4 pp., Problems 1–6, F39-23-v2);
- `week-39-grades-4-5.pdf` (4 pp., Problems 1–6, F39-45-v2);
- the adult guide `week-39-facilitator.pdf` (7 pp.: six guide pages plus the appended route update).

The companion bonus packet (`week-39-bonus.pdf`, W39-BONUS-v1, with its own guide) got only a brief check, at the end. The `archive-before-fresh-review-2026-10-04/` folders were ignored, except to read the footer ID of the archived K–1 (item 3). I read the editable source in `lowell-math-circle-year-2/source/week-39/editable/src/`, and the `reference-pdfs/` copies are byte-identical to the delivered PDFs. Checked October 5, 2026.

**Result: every answer, map and theorem in the packet is correct. I found 4 minor problems, and none changes a printed answer:**
1. A K–1 question can be read two ways, and the guide accepts only one.
2. A Grades 4–5 instruction cannot be carried out for one of its three routes.
3. The guide gives the K–1 packet a version ID that the packet does not carry.
4. One loose phrase in the guide overview.

## How it was checked

- **`extract.py`** reads the delivered PDFs with PyMuPDF (`pip install pymupdf`), not the source. Its output is `extracted.json` and `out_extract.txt`. It rebuilds:
  - all 14 printed road maps: circle centres and radii, the letter inside each circle, and the black roads and grey road bands joined to circle centres;
  - the ten step tiles of the worked example: arrow direction from the arrowhead, the struck tiles, and the mini-map roads;
  - every printed route string;
  - the problem text.
- **`compare_source.py`** confirms that `make_packets.py` gives the same maps (centres within 0.05 pt, same edges), routes and problem wording as the PDFs (`out_compare_source.txt`).
- **`check.py`** uses only the standard library and its own code (`out_check.txt`). It has two independent reducers:
  - a breadth-first search over every deletion order;
  - a left-to-right stack.

  It enumerates every walk each problem allows. It then checks every route, chain, table row and count in the guide, transcribed by hand. It also checks the guide's general claims exhaustively on the printed maps:
  - confluence: every walk from every start, up to 10 steps on the ring, 8 on the two-ring map and 9 on the tree, has exactly one final route, equal to the stack result;
  - the key lemma of the guide's stack proof;
  - the ring length classes.
- **`bonus_check.py`** checks the bonus packet (`out_bonus_check.txt`).

## Diagrams (all bands): check out completely

- Every map has exactly the intended vertices and roads:
  - tree AB, BC, BD, DE, DF;
  - ring AB, BC, CD, DA;
  - two-ring map HA, AB, BH, HC, CD, DH.
- Each grey band lies under its black road. All node circles are round with r = 9.92 pt (3.5 mm).
- Shapes and scaling:
  - the rings are exact squares (equal sides and diagonals);
  - the trees sit on an equal-scale grid (unit roads AB, BC, BD; DE and DF √2 × unit);
  - the two-ring map is mirror-symmetric about H, with A and B on the left and C and D on the right.
- Every letter named in a problem is on that page's map.
- The worked example (p. 1, all bands):
  - The input tiles are A→B, B→C, C→B, B→D on a mini map with the tree's layout (C above B, D right of B). They chain to the legal walk ABCBD.
  - Only tiles 2 and 3 are struck, and they are one road in opposite directions.
  - The output tiles A→B, B→D are the reduced walk.

## K–1 (pp. 1–6, Problems 1–7)

Problems 1–6 check out. Problem 7 is item 1 below.

- **P1 (tree):**
  - The only three-step A→E trip is ABDE. It is already reduced, so "shorten it" correctly leaves it alone.
  - All 11 four-step B→B trips reduce to B.
  - All 5 four-step A→D trips (ABABD, ABCBD, ABDBD, ABDED, ABDFD) reduce to ABD.
- **P2 (ring):** there are 8 four-step home trips. Six shorten to staying at A. Two, ABCDA and ADCBA, keep all four steps, and no trip keeps only some.
- **P3:** there are 21 seven-step A→E trips, all reducing to ABDE, and 21 seven-step C→F trips, all reducing to CBDF.
- **P4:** there are 3, 11, 43 and 683 home trips of 4, 6, 8 and 12 steps. All of them shorten to A.
- **P5:**
  - Trips from C to F that use every road have 7, 9, 11, 13, … steps, numbering 1, 10, 68, 389, …
  - Every one reduces to CBDF. The answer is no.
- **P6:** the 128 eight-step home trips give exactly 5 results:
  - stay at A (70 trips);
  - ABCDA and ADCBA (28 each);
  - ABCDABCDA and ADCBADCBA (1 each).
- **P7:** the 32 six-step A→C trips give exactly 4 results:
  - ABC and ADC (15 each);
  - ABCDABC and ADCBADC (1 each).

## Grades 2–3 (pp. 1–4, Problems 1–6): checks out completely

- **P1:**
  - The printed routes ABABDFDE, ABDFDE and CBCBDF are legal and reduce, in every order, to ABDE, ABDE and CBDF.
  - There are 21 seven-step C→F trips, and every one finishes as CBDF.
- **P2:** 48 twelve-step home trips use every road, and all reduce to A. Every closed A-walk of 0–14 steps reduces to A.
- **P3:** the five results are as in K–1 P6. The fewest steps in a nonempty survivor is 4.
- **P4:**
  - ABABCBADCDA is legal (10 steps) and has 4 possible first reversals.
  - All 50 complete deletion orders end at A, so the answer is no.
- **P5:**
  - "Go around the left ring through A" does not fix a direction, since both directions pass A.
  - All four direction readings give two journeys that are already reduced and different, so the answer is no.
- **P6:**
  - At 12 steps, 27,624 home trips use both rings. Of these, 15,080 vanish and 104 lose no steps.
  - A vanishing trip needs even length, and a no-loss home trip needs a multiple of 3 steps, so 12 serves both.

## Grades 4–5 (pp. 1–4, Problems 1–6)

All answers are correct. Item 2 below concerns P4's instruction.

- **P1:** as in Grades 2–3.
- **P2:** every closed A-walk of 0–14 steps reduces to A. The guide's farthest-vertex proof is valid for all lengths:
  - the farthest visited vertex is not A;
  - it can only be entered from its parent, and the next step must go back.
- **P3:** every C→F walk of 0–14 steps reduces to CBDF. The guide's proof is valid: a reduced tree walk with a repeated vertex would contain a nonempty reduced closed walk, so a reduced walk is the unique simple path.
- **P4:**
  - ABABCBADCDA ends at A in all 50 orders, ABADCBC at ADC in 2 orders, and ABCDABCBA at ABCDA in 1 order.
  - The answer "no, on any map" is true. It is confirmed by the exhaustive confluence check, and the guide's p. 6 proof is correct.
- **P5:** the commutator HABHCDHBAHDCH (12 steps) has no immediate reversal, so it cannot disappear. This holds for all four direction readings of "through A / through C".
- **P6:** of the 24 orders of the whole loops a, a⁻¹, c, c⁻¹, 16 vanish and 8 survive. So the counts alone do not decide, and for example aa⁻¹cc⁻¹ is a valid "different result".

## Adult guide

Every route, count and chain is correct. I checked:
- **Overview:** the overview is accurate, with the right hypotheses: unique reduction, the tree theorem, the ring direction argument, the commutator, endpoint-fixed homotopy, and the remark about parallel edges.
- **K–1 key, p. 3:**
  - P3 examples ABABDFDE and CBABDEDF;
  - the P4 alternating witnesses;
  - P5: CBABDEDBDF is 9 steps, uses all roads, and its three deletions in the stated order are legal;
  - all five P6 table rows (each input 8 steps, reducing as listed) and the completeness argument;
  - P7: the inputs ABABABC and ABABADC, and the "length ≡ 2 mod 4" claim (checked to 14).
- **Grades 2–3 key, p. 4:**
  - the three distinct 12-step P2 trips, each covering every road;
  - both P4 chains, each arrow being one legal deletion;
  - P5 and P6 (HABHBAHCDHDCH vanishes; HABHCDHBAHDCH has no reversal).
- **Grades 4–5 key, p. 5:** the P4 chains, P5 = aba⁻¹b⁻¹, and P6's equal zero signed counts.
- **Stack proof, p. 6:** correct. Its lemma (reading e then e⁻¹ after any reduced stack S returns S) holds for every reduced stack up to 8 steps on all three maps.
- **Route update, p. 7:** BABAB → B, ABABD → ABD, and the three four-step ring results.
- **Page cross-references:** pp. 3, 4, 5 and 6 are all right.

The guide's problems are items 1, 3 and 4 below.

## Problems found

### 1. K–1 p. 6, Problem 7: "same roads" has two readings, and the guide accepts one

- **Text:** "Can two of your remaining trips visit exactly the same roads in a different order?"
- **Guide (p. 3):** "Yes, the two six-step survivors both use all four roads, but in different orders. They do not have the same directed-edge multiset; the question only asks for the same roads."
- **Evidence (`check.py`, K–1 P7):** the four results use these roads:

  | Result | Roads |
  |---|---|
  | ABC | AB, BC |
  | ADC | AD, CD |
  | ABCDABC | AB×2, BC×2, CD, AD |
  | ADCBADC | AD×2, CD×2, AB, BC |

- **The two readings:**
  - As road sets, ABCDABC and ADCBADC match, so the answer is yes.
  - As the children's step tiles, counted with repeats (with or without arrows), no two results match, so the answer is no.
- **Why it matters:** "exactly", together with the tile-based recording the page prescribes, invites the tile reading. A K–1 child who compares tiles and says "no" is right, but an adult following the key would correct them.
- **Smallest fix:** add to the guide's P7 key: "A child who compares tiles and answers no is also right: ABCDABC crosses A–B and B–C twice, ADCBADC crosses A–D and D–C twice. Accept either answer with its reason." Optionally, also drop "exactly" from the student question.

### 2. Grades 4–5 p. 3, Problem 4: one printed route has only one deletion order

- **Text:** "Shorten each recorded trip in different orders." The third route is A→B→C→D→A→B→C→B→A.
- **Evidence:** ABCDABCBA has exactly one available reversal (B→C→B). After removing it, ABCDABA again has exactly one (A→B→A), so there is only 1 complete deletion order. The other two routes have 4 and 2 first choices. A child cannot do what the instruction asks for this route.
- **Smallest fix:** change the instruction to "Shorten each recorded trip, in different orders when you can." Alternatively, replace the route with A→B→C→B→C→D→A→B→A. It is also 8 steps, has 3 first choices and 4 complete orders, and still ends at ABCDA (checked).

### 3. Guide p. 6: the K–1 version ID disagrees with the packet

- **Text:** "Key alignment: K-1 has six pages, Problems 1-7, F39-K-v3".
- **Evidence:**
  - All six K–1 pages print "Bellingham Math Circle / Week 39 / F39-K-v2". `common.py` hard-codes `-v2` for every band.
  - The archived four-page K–1, numbered Problems 1–5, also prints F39-K-v2. So the footer cannot tell an adult which numbering the continuation key (Problems 3–7) refers to.
  - The guide's pages 1–6 are footed "n / 6", but the PDF has 7 pages.
- **Smallest fix:** give the K–1 band the footer F39-K-v3 in `common.py` `page()` and rebuild the K–1 PDF. Otherwise, change the guide line to v2 and accept the ambiguity with the archived version.

### 4. Guide p. 1 and p. 7: "zero-net-count obstruction" points the wrong way

- **Text:**
  - p. 1: "Grades 4-5: prove unique reduction and find the zero-net-count obstruction."
  - p. 7: "Grades 4-5 can separate unique reduction (P4) from zero-net-count obstructions (P5-6)".
- **Evidence:** in P5–6 net counts are the thing that fails to obstruct. The commutator has zero net count around each ring and still cannot disappear, and 16 of the 24 orders of a, a⁻¹, c, c⁻¹ vanish. The obstruction is the reduced order, as the guide's own "Order can survive" paragraph says correctly. Read as "net count is the obstruction", the phrase states the opposite lesson.
- **Smallest fix:** "… and find a zero-net-count trip that still cannot disappear" (p. 1). On p. 7, use "… from trips with zero net count that cannot disappear (P5-6)".

## Bonus packet (brief): checks out completely

`bonus_check.py`:
- **P1 (four-arm star):**
  - Searching every multiset of up to three added outer roads, the fewest additions is 2. The optimal pairs are exactly AB+CD, AC+BD and AD+BC.
  - The shortest surviving tour is 6 steps (H-A-B-H-C-D-H).
  - Closing either added road leaves no surviving tour that visits all four stops (searched to 20 steps).
  - The extension's 5-step tour with three additions exists.
- **P2:** 27 six-step returns on the unit star and 48 on the extended star, all reducing to H. The four-step counts are 9 and 12, and the guide's split 27 + 9 + 9 + 3 is correct.
- **P3:**
  - Of the 21 card pairs, compared at the level of individual road steps, exactly three commute: a & aa, ab & abab, and abA & abbA. Their common reductions are aaa, ababab and abbbA.
  - The worked example aAb reduces to b.
- **Bonus guide:** the overview and the kit arithmetic (24/12/144/42/36; a longest pair of 8 loops = 24 steps) are correct.

## Files

All in this run folder, with their saved outputs:
- `extract.py` → `extracted.json`, `out_extract.txt`;
- `compare_source.py` → `out_compare_source.txt`;
- `check.py` → `out_check.txt`. Its one FAIL line is item 3;
- `bonus_check.py` → `out_bonus_check.txt`.

`extract.py` and `compare_source.py` find the repository four folders up from `plans/review/checks/week-39/`, or by searching upward. The `png/` folder holds 100-dpi page renders used for visual inspection.
