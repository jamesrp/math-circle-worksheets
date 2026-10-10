# Week 36 (Making threes): math check

Scope:
- Student packets in `lowell-math-circle-year-2/week-36/`:
  - `week-36-k-1.pdf` (W36-k-1-v2, 4 pp., Problems 1–4)
  - `week-36-grades-2-3.pdf` (W36-grades-2-3-v2, 4 pp., Problems 1–5)
  - `week-36-grades-4-5.pdf` (W36-grades-4-5-v2, 5 pp., Problems 1–5)
  - the bonus companion `week-36-bonus.pdf` (W36-BONUS-v1, 3 pp., Problems 1–3; pp. 1–2 headed Grades 2-5, p. 3 Grades 4-5)
- Adult guides: `week-36-facilitator.pdf` (6 pp., including the p. 6 route note) and `week-36-bonus-facilitator.pdf` (W36-BONUS-FAC-v1, 3 pp.).
- Sources read: `source/week-36/editable/src/{k-1,grades-2-3,grades-4-5}.tex`, `facilitator-src/guide.md` and `route-note.json`, and `source/week-36-bonus/student/{build.py,common.py}` and `guide.md`. All six delivered PDFs are byte-identical (`cmp`) to the reference copies in `source/week-36/editable/reference-pdfs/` and `source/week-36-bonus/reference-pdfs/`.

I ignored the archive folders. I did not run or import the packets' own checkers (`verify.py`, `verify_math.py`, `verify_revision.py`, `check_revised_cases.py`, the bonus `student/verify.py`). I rendered every student page and read each one. Checked October 10, 2026. My scripts and outputs are in this folder (`common.py`, `extract_pdf.py`, `check_pages.py`, `compare_source.py`, `check_math.py`, `check_bonus.py`, `check_guide_text.py`, with `extracted.json` and the `out_*.txt` files). All 370 checks pass.

**Result: every answer, count, diagram and theorem in the three bands, the bonus and both guides is correct. K–1, Grades 2–3, Grades 4–5, the bonus student pages and the base guide check out completely. I found 1 minor problem, in the bonus guide's P3 extension; no printed answer changes.**

## How it was checked

- **`extract_pdf.py`** reads the delivered PDFs, not the sources.
  - It takes every tile glyph from the vector data with pdfplumber: four Bézier arcs make a circle, a closed three-point path a triangle, a filled black-outlined rectangle a square.
  - It classifies each fill twice: from the vector fill (white, black or gray, or a TikZ pattern, or ReportLab's clipped gray stripes) and from 150-dpi pixels inside the glyph. The two classifications agree on all 264 glyphs.
  - It groups the glyphs into 3×3 boards (nine centres on a square lattice), launch triples, pairs and number examples. It attaches each printed number to the tile above it.
- **`compare_source.py`** checks that every glyph drawn in the three `.tex` files is printed with the same shape, fill and centre (within 0.1 pt), with none extra, on every page. Each problem statement in the sources appears verbatim in the PDF text.
- **`check_pages.py`** checks every diagram against the rule and the text:
  - both launch triples, with their shape and fill icon rows and labels;
  - the four Problem 1 pairs in each band and the guide's key for them;
  - all 20 printed 3×3 boards, which each show the nine tiles once, in rows circle/triangle/square and columns open/striped/solid;
  - the bonus number examples and the three number layers;
  - the cell sizes the bonus guide quotes;
  - that every circle and square has equal width and height.
- **`check_math.py`** (base packet and base guide) builds the 12 allowed threes from the printed attribute test alone. It then checks, by enumeration:
  - unique completion for all 36 pairs, and the guide's rule z = −x−y (mod 3) under all 36 ways of coding the values as 0, 1, 2;
  - incidence: four threes through each tile, and two threes meet in 0 or 1 tile;
  - the four splits, and the guide's direction argument;
  - every subset of the nine tiles: legal-subset counts, extension counts, the maximal collections, and both lemmas of the ten-pair proof on every 5-set;
  - all 1,296 legal plays of the shared adding game;
  - every key in the guide.
- **`check_bonus.py`** (bonus pages and bonus guide):
  - an exact minimax of the private-ownership game;
  - every branch of the guide's centre-and-opposites strategy for all nine centres;
  - the shared-three variant;
  - all 512 two-colour and 19,683 three-colour ownership assignments;
  - all 19,683 number choices for P3, every single-number change of every design, and all line-free nine-card sets of the 27-card deck.
- **`check_guide_text.py`** confirms that each guide claim I tested is printed, word for word, on the page the guide cites.

## K–1 (pp. 1–4, Problems 1–4): checks out completely

- **Launch (same in all three bands):**
  - "allowed three" is open circle, solid triangle, striped square: shapes all different, fills all different. It is allowed.
  - "not allowed" is open circle, open triangle, solid square. It fails only on fills ("two the same").
  - The icon rows under each example match their tiles in order. The lowered triangle and the arrow do not change anything, since positions do not matter.
- **P1:** each printed pair has exactly one completion. In page order these are solid circle, open square, open square and solid circle. Every pair a child can invent also has exactly one completion.
- **P2:** there are 4 splits, ignoring group order. The page asks only for different ways.
- **P3:** the most tiles you can keep is 4, for example the 2×2 rectangle of open and striped circles and triangles. No 5 tiles avoid an allowed three, and every collection that cannot be extended has exactly 4 tiles.
- **P4:** there are 4 threes through every middle tile. They pair off the other eight tiles.
- **Diagrams:** the P1 tiles match the text, and the P3 board is the full nine-tile board on 60 mm cells.

## Grades 2–3 (pp. 1–4, Problems 1–5): checks out completely

- **P1:** no pair has two answers.
- **P2:** exactly 4 unordered splits.
- **P3:** the maximum is 4. From any 4-tile collection, changing one tile and then adding another never works: I checked all 54 such collections, every swap and every addition. With fewer than 4 tiles you can always add one.
- **P4:** 4 threes through any tile.
- **P5:** every legal play lasts exactly 4 moves. I enumerated all 9·8·6·3 = 1,296 plays: legal collections of size 0, 1, 2, 3 and 4 always have exactly 9, 8, 6, 3 and 0 legal additions. The second player always makes the last move and wins, so choices cannot change the length.
- **Diagrams:** all four small boards on p. 4 are complete and in the standard order.

## Grades 4–5 (pp. 1–5, Problems 1–5): checks out completely

- **P1:** the completions are as in K–1, and every pair has exactly one completion.
- **P2:** the maximum is 4 (54 four-tile collections avoid a three; none of 5 tiles does). The ten-pair argument holds: for every 5-set S and every tile x outside it, the pairs of S completed by x are disjoint, so there are at most 2 of them.
- **P3:** two different threes share at most one tile (12 disjoint pairs of threes, 54 sharing one tile). There are four threes through each tile.
- **P4:** exactly four splits, and four boards are printed.
- **P5:** you can never stop before 4 tiles (see Grades 2–3 P5).

## Bonus student pages (pp. 1–3, Problems 1–3): check out completely

- **P1 (private ownership, first to own an allowed three loses):**
  - The game always ends, because the first player would own 5 tiles and every 5 tiles contain a three.
  - Exact minimax: the first player can force a win, and every one of the nine first claims wins.
  - So "Can either player guarantee a win?" has the answer: yes, the first player.
- **P2:**
  - Two colours are impossible (0 of 512 assignments).
  - Three colours work: 3,762 assignments with named colours, with class sizes 4/4/1 (162), 4/3/2 (2,592) and 3/3/3 (1,008).
- **P3:**
  - Both convention examples are labelled correctly. 1, 1, 2 is not allowed; 1, 2, 3 is allowed.
  - Each of the three layers numbers all nine tiles with its own number.
  - Exactly 162 of the 19,683 number choices contain no allowed three.
  - Changing only the numbers can make an allowed three appear: from any design, every single-number change does so (all 2,916 changes).
- **Diagrams:**
  - The 108 pt (38.1 mm) and 58 pt (20.5 mm) boards are full nine-tile boards in standard order.
  - The two 56 pt record boards carry no numbers.
  - The striped and solid (gray) fills are distinct in the pixels.

## Base guide (pp. 1–6): correct throughout

I checked these statements:

- **Overview:**
  - the keep-or-missing completion rule, and z = −x−y (mod 3), under any coding of the values;
  - 12 threes, four through each tile, and 0 or 1 shared tile;
  - exactly four partitions;
  - a maximum of 4, with any 2×2 attribute rectangle as a witness (all 9 rectangles work);
  - the ten-pair capacity argument (8 < 10);
  - extension counts 9, 8, 6, 3, 0, the forced four-move game, and the second player winning;
  - the limits paragraph.
- **Readiness check and launch:** the printed triple and near miss.
- **Keys:**
  - the four completions, in page order;
  - the four pairs through the open circle;
  - the K–1 and 2–3 witness, and the claim that every triple of it has two of some shape or fill;
  - the 2–3 P3 and P5 keys;
  - the 4–5 P3 examples (circles versus triangles are disjoint; circles versus open tiles share one);
  - the four splits on p. 4, which are exactly the 12 threes, each once;
  - the 3 + 3 + 6 count;
  - "disjoint iff same direction", with three threes in each of the four directions;
  - the P5 argument.
- **p. 5:**
  - the dish lemma;
  - the three distinct forbidden fourth tiles for every legal triple;
  - the subset counts 1, 9, 36, 72, 54, 0;
  - every maximal collection has size 4.
- **Cross-references:** "page 4 lists all", "page 5 explains", the route note on p. 6 and "4 / 5 / 5 problems" all match the packets.

## Bonus guide (pp. 1–3): correct, apart from Problem 1 below

I checked these statements:

- **Overview:**
  - the four wrap-around threes, which are not straight on the printed board;
  - the first-player win;
  - the two-colour bound;
  - unique completion for the 27 numbered cards.
- **P1 strategy:**
  - claim any centre c, then answer x with the third tile of {c, x};
  - the response is always free, and the first player never owns a three;
  - over all nine centres there are 3,024 terminal branches: 432 losses on the second player's third claim and 2,592 on its fourth;
  - the four opposite pairs about the open circle;
  - in the shared-three variant the first player loses, so the winner changes as stated.
- **P2:**
  - the witness RRB/RRB/BBG;
  - 3,762;
  - 9 > 4 + 4;
  - a 3/3/3 design exists, as the extension needs.
- **P3:**
  - the witness 122/233/233, which equals number − 1 = x² + y² (mod 3);
  - d₁² + d₂² ≠ 0 for every nonzero direction;
  - shifting all numbers, or renaming the values of any attribute, gives another design;
  - all numbers 1 gives exactly the 12 shape/fill threes.
- **Materials:**
  - the quoted 108 pt and 58 pt cells match the PDF;
  - 27 cards and 12 counters per colour per pair cover every task.

Facts the guide does not state, which are not errors but could help an adult:

- Every one of the 162 P3 designs uses one number exactly once and the other two four times each. So the page's "All three numbers must appear" is automatic: two numbers would be a two-colouring, which P2 shows is impossible.
- The P3 designs are exactly the 4/4/1 colourings of P2. The guide's own P2 witness, read as numbers, is a P3 design.
- Changing any single number of any design creates an allowed three.

## Located problems (1, minor; no incorrect answers)

### 1. Bonus guide p. 2, P3 extension: the hint about repeated tiles points the wrong way

- **Quoted text:** "Extension: diagnose a proposed design that has two copies of the same shape/fill tile in different layers; different coordinates may create cross-layer triples."
- **Evidence:** `check_bonus.py`, last section.
  - Take two copies of one tile, say numbers a ≠ b. A third card completes them only if it has the same shape, the same fill and the remaining number, which is that tile's third copy. So two copies of a tile never lie in an allowed three unless the third copy is also chosen. The repetition creates no triple by itself.
  - Among all nine-card sets of the 27 cards with no allowed three (2,106), 1,944 repeat some shape/fill tile. An example: CO1, CO2, CH1, CH2, TO1, TO2, TH3, TF3, SH3.
  - So a child's design with a repeat usually has no allowed three. What is wrong with it is only that it breaks the page's rule "one numbered version of every shape-fill tile" (some tile is missing). An adult following the sentence may hunt for a cross-layer triple that is not there.
- **Smallest fix:** replace the sentence with: "Extension: a nine-card set with two copies of one shape/fill tile breaks the one-version rule but usually has no allowed three. Two copies of a tile are completed only by its third copy. Ask why the page insists on one version of each tile."

## Not checked

- **Sources:** the citations, because none of the cited works is in this checkout:
  - Carney, *SET and Finite Affine Geometry*, §§1–3 and §5, pp. 15–16;
  - Khovanova, *SET Tic-Tac-Toe*;
  - *Math Circle by the Bay*, Preface pp. viii–ix.

  The mathematics they are cited for is standard, and I verified it independently above.
- **Triangles:** the triangle glyphs are isosceles, not equilateral: height/base 0.975 on the base pages and 0.891 in the bonus, against 0.866 for an equilateral triangle. No page calls them regular, and "triangle" is only a shape category, so I do not count this as a problem.
- **Physical fit:** both guides mark it untested. One geometric note: on the bonus 38.1 mm cells the glyphs are 14.1 mm across. A 15 mm counter pushed into a cell corner overlaps a square glyph's corner by about 1.1 mm and a triangle's base corner by about 0.5 mm; shape and fill stay visible.
- **The packets' own checkers:** not run, by design.
