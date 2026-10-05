# Week 53 (connecting networks): math check

Scope: `lowell-math-circle-year-2/week-53/week-53-students.pdf` (one combined packet, 9 pages, Problems 1–9; pp. 1–4 headed Grades 2–5, pp. 5–9 headed Grades 4–5) and `week-53-facilitator.pdf` (8 pages). Sources read: `source/week-53/student/` (`students.tex`, `networks.json`, `diagrams.py`, notes) and `source/week-53/guide/facilitator.tex`. I did not run or import the writer's or guide's `verify_*.py`. My scripts and their outputs are in this folder. Checked October 5, 2026.

**Result: every answer, count and theorem in the packet and guide is correct. I found 3 problems, all on the student pages: one diagram-labelling problem on the six-place map (pp. 6 and 8), plus two minor ones. The adult guide has no mathematical errors.**

## How it was checked

- `pdfgeom.py` is a standard-library reader for the delivered PDF's content streams. It reads back every stroked link, every place circle, every white price-label box, every price numeral, every price dot and every answer blank.
- `check_diagrams.py` (output `out_check_diagrams.txt`) rebuilds all 27 printed graphs from that data and compares them with my own transcription from the rendered pages. It checks places, links, thick (bought) links, numerals, dot counts and the 12 blanks on p. 7. All of these match, and `networks.json` matches the printed maps. For every price label it also measures the distance to its own link and to the nearest other link, and checks whether the label's white box paints over another link or is covered by a place circle. Main place circles are 10.4 mm across. Nearest centres are 56.8 mm (p. 1), 67.5 (pp. 2–4), 64.6 (p. 5), 51.0 (p. 6), 40.3 (p. 7), 37.5 (p. 8) and 98.6 mm (p. 9), exactly as the guide states. The p. 5 and p. 9 squares have equal sides and diagonals (64.60/91.36 mm and 98.60/139.44 mm).
- `check_math.py` (output `out_check_math.txt`) enumerates every edge subset of every fixed map: the connected purchases, the trees, the minimum and every optimum. It also lists every legal and illegal one-link swap from the four printed thick inputs. On p. 6 it finds the every/some/none status of each link, the bridges, and the cut and cycle certificates. It runs all 4^6 = 4096 price assignments for p. 7. As finite sanity checks of the general claims on pp. 8–9, it compares local and global optimality on all 152 trees of the fixed maps and on 86,417 trees of random positive-price graphs (0 mismatches), and tests uniqueness on 2,413 random distinct-price graphs (0 failures).
- `check_label_fix.py` (output `out_check_label_fix.txt`) tests replacement label positions for Problem 1 below at both printed scales.

## Grades 2–5 (pp. 1–4): the mathematics checks out. Diagrams are correct.

- **Convention (p. 1):** prices XY=2, YZ=4, XZ=3, with dots matching the numerals. Six coins are drawn, and 2+4=6 is correct. XY/YZ is deliberately not the cheapest choice (the cheapest is XY/XZ=5). That is acceptable for a demonstration.
- **P1:** on the left, the minimum is 3, uniquely AB/BC (the two-link totals are 3, 4, 5). On the right, the minimum is 3 with two optima, AB/BC and AB/AC (totals 3, 3, 4).
- **P2:** the minimum is 4 with exactly 3 optima: CD plus any two of AB, AC, BC. Three record maps are printed. AD=3 is in no optimum.
- **P3:** the minimum is 7, uniquely AB/BC/CD. The three cheapest links AB/BC/AC cost 6 but leave D out, and no connected purchase costs less than 7. The next costs are 8 and 9.
- **P4:** the minimum is 6 with exactly 3 optima: CD/DE plus two of the triangle links. The four cheapest links (AB, AC, BC, CD) omit E.

## Grades 4–5 (pp. 5–9): the mathematics checks out. See Problems 1–3 for the p. 6 and p. 8 diagrams and wording.

- **P5 demo:** cost 6, then 9 after buying UW, then 5 after returning VW. All correct.
- **P5 left:** input AB/AD/AC costs 10. Exactly 3 cheaper legal swaps exist: return AC/buy BC gives 7, return AC/buy CD gives 8, and return AD/buy CD gives 9. One cheaper-looking swap is illegal (return AD/buy BC gives 8 but isolates D). Five answer rows are printed, which is enough.
- **P5 right:** input AB/BC/CD costs 6. No cheaper swap exists, and this input is optimal.
- **P6:** the unique optimum is AB/BC/CD/DE/EF with cost 8. Those five links are in every optimum, and AC, BD, CE and DF are in none. Each forced link has a cut where it is the unique cheapest link: {A}, {A,B}, {A,B,C}, {E}, {F}. Each excluded link is the unique dearest link on a cycle: ABC, DEF, BCD, CDE. The map has no bridges.
- **P7:** both goals can be met. Of the 4096 assignments, 1956 give exactly one optimum and 2140 give several. Distribution: 1:1956, 2:936, 3:768, 4:144, 5:96, 6:96, 8:72, 9:24, 16:4. The K4 map has 64 subsets, 38 connected purchases and 16 spanning trees.
- **P8:** with positive prices, an optimum has no loop. The top input (cost 8) has no cheaper swap and is the optimum. The bottom input AB/AC/BD/DE/DF costs 14 and has exactly 4 cheaper legal swaps: 13, 13, 11, 12. Five more swaps would cut the total but disconnect a place. The general answer is no: a connected purchase with no loop and no improving swap is always cheapest. The all-bought price-1 triangle (cost 3, no swaps possible, minimum 2) shows that the loop-free condition is needed.
- **P9:** the minimum is 6, uniquely AB/BC/CD. The general answer is no: distinct positive prices on a connected map give one optimum.

### 1. Pages 6 and 8: the prices of CD and DE are printed against link CE

- **Diagram:** the six-place map (`SixCert`, `SixGood` and `SixBad`). CD's "2" is printed above the CD link, and DE's "1" on the upper-left side of the DE link. Both face CE, which runs just above them from C to E.
- **Evidence (`out_check_diagrams.txt`):**
  - **p. 8, both maps:** the centres of the CD "2" and the DE "1" are each 1.5 mm from link CE and 3.2 mm from their own links. Both white label boxes paint over CE, so the CE line is visibly broken around each numeral. In a 300 dpi render the CE line is broken at the "2" and at the "1", so both numerals read as sitting on CE, while the thick CD and DE links carry no numeral of their own.
  - **p. 6:** the same two numerals are 3.1 mm from CE and 3.2 mm from their own links. If each numeral is given to its nearest link, CE gets three prices {6, 2, 1} and CD and DE get none. A child can recover the intended prices only by elimination: every link needs a price, and CE already has "6".
  - The mathematics depends on these two prices. CD=2 is the forced non-bridge link of Problem 6 (cut {A,B,C}; cycles BCD and CDE), and DE=1 enters the {E} cut and the DEF and CDE cycles. Page 8 does not say that its map is the p. 6 map, so a child cannot rely on cross-referencing.
- **Smallest fix:** move the two labels in `diagrams.py`/`networks.json` (it changes both pages):
  - Put DE's price on the F side of DE (reverse its perpendicular offset). This passes at both scales: 3.2 mm from DE, and the nearest other link is at least 7.7 mm away.
  - CD lies in a narrow wedge between CE and BD. No 0.32 cm offset works on p. 8: the best is 3.2 mm from CD against 3.7 mm from another link. Either centre the price on CD itself (CE and BD are then 4.6 mm away on p. 8 and 6.2 mm on p. 6), or move it toward D (label fraction about 0.75) with a 0.2 cm offset. That gives 2.0 mm from CD against at least 4.2 mm from any other link at both scales.
  - Neither box then crosses another link (`out_check_label_fix.txt`).

### 2. Page 8 (minor): BD's price "5" is partly hidden under circle C

- **Diagram:** in both p. 8 maps, BD's label sits at the midpoint of BD, directly below place C. The circle is drawn after the label with a white fill.
- **Evidence:** the top 0.50 mm of the 3.0 mm numeral, including part of the top bar that distinguishes 5, is covered by circle C. The label is also 3.3 mm from BD and only 5.2 mm from BC. The same label is clear on p. 6, where the larger scale leaves room.
- **Smallest fix:** put BD's price below BD (reverse its offset). It is then 3.2 mm from BD, at least 11.6 mm from any other link and clear of all circles at both scales. This can be done together with Problem 1.

### 3. Page 6 (minor wording): the answer label "Cannot be bought:" does not match the question

- **Quoted text:** the question asks "Which links are in no cheapest purchase?", but the answer area is headed "Cannot be bought:" (with "Must be bought:" beside it).
- **Evidence:** every link can be bought in some connected purchase. For example, AB/AC/CD/DE/EF, AB/BC/BD/DE/EF, AB/BC/CE/DE/EF and AB/BC/CD/DE/DF are connected purchases containing AC, BD, CE and DF respectively. Read literally, "Cannot be bought" has the answer "none", while the intended answer is AC, BD, CE, DF.
- **Smallest fix:** head the areas "In every cheapest purchase:" and "In no cheapest purchase:".

## Adult guide: checks out completely

- **Overview:** the claims are true with the stated hypotheses (finite, connected, strictly positive prices). These include: optima are spanning trees; the cut and cycle rules require a unique cheapest or dearest link, while a tied cheapest crossing link lies in some optimum; the local swap test is equivalent to global optimality for loop-free purchases, but not for purchases with loops; distinct prices are sufficient but not necessary for uniqueness; and the remarks on zero, negative and real weights.
- **Keys:** every key matches my enumeration. P1–P4 catalogs and lower-bound arguments: correct. P5 swap table, path arguments and the illegal AD/BC swap: correct. P6 cut table, cycle list and the no-bridge claim: correct. P7 witnesses, the 16/38/64 counts and the full 4096 distribution: correct. Coverage table and the 152-tree total: correct. P8 top path table and bottom four-row table (including CE's path prices 3, 1, 5, 1): correct. P9 key: correct.
- **Proofs:** the necessity and sufficiency proof on p. 7 (ties allowed), the Kruskal remark, the certificate proof and the distinct-price uniqueness proof are all valid.
- **Page references and material claims:** the page references hold (cuts on p. 4, proof on p. 7). Spacing, the price-sum bound of 26, the 24-counter bound and the ten-marker count match the PDF.
- The guide does not mention the p. 6 and p. 8 label placement in Problem 1. The student fix makes a guide note unnecessary.
