# Week 40 (Loop colors): math check

Scope: the current student packets in `lowell-math-circle-year-2/week-40/`:
- `week-40-k-1.pdf` (5 pp., Problems 1–6, footer F40-K-v2);
- `week-40-grades-2-3.pdf` (4 pp., Problems 1–6, F40-23-v2);
- `week-40-grades-4-5.pdf` (4 pp., Problems 1–7, F40-45-v2);
- the adult guide `week-40-facilitator.pdf` (7 pp.: six guide pages plus the appended route update).

The bonus companion in the same folder (`week-40-bonus.pdf`, W40-BONUS-v1, 3 pp., with `week-40-bonus-facilitator.pdf`, 3 pp.) was also checked in full, at the end. The `archive-before-fresh-review-2026-10-04/` folders were ignored. I read the generator in `lowell-math-circle-year-2/source/week-40/editable/src/` for intent only. All six delivered PDFs are byte-identical to their `reference-pdfs/` copies in the two source folders. Checked October 10, 2026.

**Result: every count, colouring, table and theorem in the packet is correct, and every diagram is the knot or tangle it is meant to be. I found 4 minor problems, and none changes a printed answer:**
1. A K–1 question can be read as "one colour per strand", which changes the answer from four cases to one.
2. The end dot named R clashes with R for red in every band.
3. The before/after arrow in Grades 2–3 and 4–5 reads as "R → L".
4. The guide's trefoil preparation cannot be carried out if the overhand knot is tied in the other hand.

## How it was checked

All scripts are in this folder. They use only Python 3 with pdfplumber, and none trusts the author's checker (`check_math.py`, `knot_geometry.py`, `verify.py`).

- **`diag.py`** reads the delivered PDFs, not the source. It converts every vector path to millimetres and rebuilds each cord diagram from the drawn outlines:
  - each wide black outline stroke is a drawn piece of cord, and pieces that meet end to end are merged into one arc;
  - two arc ends that face each other across a gap form an underpass when the segment joining them crosses exactly one other arc exactly once (the overstrand);
  - unmatched ends are open ends;
  - any intersection between drawn arcs would be a crossing with no gap, and there are none anywhere.

  It then counts R/B/G colourings by brute force, counts cords (components), lists the over/under events along each cord and computes crossing signs.
- **`check_main.py`** (output `out_check_main.txt`, 264 checks, all pass) covers all three main packets and the guide:
  - page by page and band by band, the diagrams, colours and letters read from the PDF;
  - the guide's lists and tables, transcribed by hand;
  - the crossing-rule algebra and the Reidemeister identities over Z/3, exhaustively;
  - reference trefoil and figure-eight knots built from PD codes, independent of the packet;
  - the printed trefoil fitted to the space curve the guide names.
- **`check_bonus.py`** (output `out_check_bonus.txt`, 68 checks, all pass) does the same for the bonus packet. It adds an abstract two-strand model as a second, independent count.

## Diagrams (all bands): check out completely

- **Page 1:**
  - X example:
    - the long horizontal piece (x = 50–160 mm) passes over the broken middle vertical and under the two full verticals at x = 45 and 165;
    - the blue output trace runs 51–159 mm, exactly that arc, from "start" to "stop".
  - Isolated crossings: each vertical is unbroken and is the overstrand, and every stroke colour matches its printed letter. R/R/R and R/B/G are valid, and R/R/B is invalid, as printed.
- **Page 2 (trefoil):**
  - Shape:
    - three drawn arcs and three underpasses, with no gapless crossing;
    - the travel order is O U O U O U, so the diagram is alternating;
    - all three crossings have the same sign (writhe +3), so it is a reduced alternating 3-crossing diagram, the trefoil;
    - every crossing involves all three arcs.
  - Size and gaps:
    - the centerline is 148.00 mm wide;
    - the white gap between an underpass end and the overstrand outline is 2.30 mm.
  - Labels and curve:
    - labels 1, 2, 3 sit 7.2–7.3 mm from their own arc and at least 54.8 mm from the others;
    - every drawn point lies within 0.08 mm of the stated curve (sin t + 2 sin 2t, cos t − 2 cos 2t), and at each crossing the over branch has the larger depth −sin 3t, as the guide says.
  - Recording area: 12 labelled triples of circles, so the count of 9 is not revealed.
- **Page 3:** the plain loop is one closed, crossing-free stroke, 148.00 mm wide.
- **Pages 1–3** are identical in all three bands (arcs, labels, colours).
- **K–1 p. 4:** nine crossings, each with a vertical overstrand, a coloured left piece and an uncoloured right piece with "?". Rows are left colour R, B, G and columns are over colour R, B, G. Stroke colours match the printed letters.
- **K–1 p. 5, Grades 2–3 p. 4, Grades 4–5 p. 4:**
  - The P–Q bend is one arc and the overstrand at both crossings, and the L–R strand has three arcs. The gaps are 1.8 mm clear.
  - In the "after" picture the strands do not cross, and the four end dots are in the same places (shifted 96.0 mm). It is a type II move.
  - K–1 case discs: each fill matches its letter.

## K–1 (pp. 1–5, Problems 1–6)

Problems 1–5 check out. Problem 6 is correct as the guide reads it, but see items 1 and 2.

- **P2:** exactly 9 colourings in arc order 1, 2, 3: RRR, BBB, GGG and the six permutations of RBG. This equals the guide's list (p. 3). None uses exactly two colours.
- **P3:** one arc, so 3 colourings, all one colour. The answer is "no".
- **P4:** physical. The guide's expectation is right: two unknots and the plain loop open, and the trefoil cannot.
- **P5:** each "?" has exactly one answer, and all nine equal the guide's table (p. 3).
- **P6:**
  - The six printed cases (L, P, R, Q) are RBRB, RRBR, GBGB, BGBR, BBBB, RGRG.
  - Cases 1, 3, 5, 6 work, with middle colours G, R, B, B. Case 2 fails because the second crossing forces R = R, not B. Case 4 fails because P ≠ Q on one arc. This matches the guide's table exactly.
  - Over all 81 end assignments, exactly the 9 with P = Q and L = R work, as the guide says.

## Grades 2–3 (pp. 1–4, Problems 1–6): checks out

- **P2:** 9 colourings, as above.
- **P3:** 3 colourings, and none uses more than one colour.
- **P5:** all 9 ordered pairs (L, P) work.
  - Before: there is one completion, with middle = L if L = P and the third colour otherwise, R = L and Q = P.
  - After: L–R and P–Q are single arcs.
- **P6:** no choice of (L, P) has two completions of either picture.

Items 2 and 3 apply to page 4.

## Grades 4–5 (pp. 1–4, Problems 1–7): checks out

- **P2 and P3:** 9 versus 3.
- **P5:** all 9 pairs, each with exactly one completion.
- **P6:** 9 ≠ 3, so with the supplied invariant the trefoil cannot become the plain loop.
- **P7:** the figure-eight (from its PD code) has exactly 3 three-colourings, all constant, and it is knotted. Its non-constant m-colourings exist exactly for m = 5, 10, 15, 20, 25, 30 (m ≤ 30), matching the guide's "exactly when 5 divides n".

Items 2 and 3 apply to page 4.

## Adult guide (7 pp.)

The overview and every solution check out, except item 4 (p. 2). Checked:
- **Overview (p. 1):**
  - the definitions;
  - 9 total and 6 non-constant for the trefoil, and 3 for the plain loop;
  - the one-way certificate;
  - the figure-eight as the counterexample to the converse.
- **Proof (p. 6):**
  - the rule is equivalent to c = 2b − a (mod 3), checked on all 27 triples;
  - each crossing has a unique completion;
  - Types I, II and III, including both sides of Type III equalling a − 2b + 2c;
  - the bijection argument and the invariance of the total and non-constant counts.
- **Keys:**
  - the K–1 tables (p. 3);
  - the 2–3 crossing table "Upper left 3 / 1, 2; Upper right 2 / 3, 1; Lower center 1 / 2, 3", which matches the reconstructed diagram (p. 4);
  - the 4–5 keys (p. 5).
- **Other pages:** the "Key alignment" line (p. 6) and the route update (p. 7).
- **Citation:** the Bestvina citation's content is confirmed (§4, Problem 11: "the figure eight knot is n-colorable precisely when n is divisible by 5"). I could not pin down its page from a text conversion. The Kauffman citation was not checked.

## Bonus packet and bonus guide: check out completely

- **P1 (machine):**
  - Layout: the printed crossing takes (R, B) to (B, G). The six-crossing machine has 8 arcs and 6 crossings, all of the printed type.
  - Read level by level from the PDF, every input pair follows (a, b) → (b, third colour).
  - Equal pairs return after 1 crossing and the others after 3. None fails, and the cycles are RB→BG→GR and RG→GB→BR. The guide is right.
- **P2 (closures of 1, 2, 3, 4, 6 crossings):**
  - From the PDF: colourings 3, 3, 9, 3, 9 and cords 1, 2, 1, 2, 2. The abstract model agrees, and so does the guide's table.
  - Each picture's labels are correct, and the returns join left to left and right to right.
  - Equal counts with different cords: 1 against 2 or 4, and 3 against 6.
- **P3 (joined pictures):**
  - Top: 6 same-sign crossings, one cord, 27 colourings.
  - Bottom: 3 crossings, one cord, 9 colourings.
  - Three joined three-crossing loops give 81 in the model. All of this matches the guide.

## Problems found

### 1. K–1 p. 5, Problem 6: "whole strands" invites one colour per strand

- **Printed:** "Which color choices let you color both whole strands and obey both crossings?"
- **The clash:** page 1 teaches "Give each whole arc one color". A child can carry "whole … one color" over to "whole strands" and give the L–R strand a single colour.
- **Evidence (`check_main.py`, last line of the K–1 p. 5 block):**
  - Under that reading a case works only if L = R = middle and P = Q, with the crossing rule then forcing L = P. That leaves case 5 (BBBB) alone.
  - The intended reading gives cases 1, 3, 5, 6, which is what the guide (p. 3) marks.
  - So the wording changes the answer, and an adult may be checking a different question from the one the child answered.
- **Smallest fix:** "Which color choices let you color every arc of both strands and obey both crossings?" Optionally add a note to the guide's Problem 6 key: the L–R strand has three arcs.

### 2. All bands: the end dot "R" clashes with R for red

- **Where:**
  - K–1 p. 5 (Problem 6 picture, and the case headings "L P R Q" over coloured discs);
  - Grades 2–3 p. 4 (Problems 5–6);
  - Grades 4–5 p. 4 (Problem 5);
  - the guide: "(L,P,R,Q)" p. 3, "R-end color equal to L" p. 4, "hence R=a" p. 5.
- **The clash:** page 1 of every band fixes R = red.
- **Evidence:** K–1 case 2 prints the heading R over a blue disc lettered B, and case 4 does too. A pre-reader sees "R" above a blue dot, in a problem whose whole content is matching colours to the letters R/B/G.
- **Smallest fix:** rename the end dots with letters that are not colour codes, for example L, P, Q, S, or W, X, Y, Z. Change both pictures, the K–1 case headings and the guide's tables.

### 3. Grades 2–3 p. 4 and Grades 4–5 p. 4: the before→after arrow reads "R → L"

- **Where:**
  - the arrow shaft runs x = 98–110 mm at y = 121 mm;
  - the before picture's label "R" is at x = 101 mm and the after picture's "L" at x = 113 mm, both at y = 117 mm.
- **Evidence:** the arrow sits under and between those two labels, so it reads as a map from end R to end L. That contradicts "matching end dots", which pairs L with L and R with R.
- **Smallest fix:** move the arrow up between the "before" and "after" titles (y ≈ 68–70 mm), or below the pictures, clear of the end labels.

### 4. Guide p. 2, adult model preparation: the overhand knot has a handedness

- **Printed:** "form a loose overhand knot in an open cord and securely join its ends … then lay it out to match the printed three-crossing model. Verify … every over/under relation."
- **Evidence:** the printed trefoil is right-handed. All three crossings are positive, writhe +3, consistent with the page mirroring the stated space curve, whose writhe is −3. The trefoil is chiral, so a closed overhand knot tied in the other hand cannot be laid out to match all three printed over/under relations. Every crossing comes out reversed. Without a warning, an adult may think the cord is wrong or keep trying.
- **Smallest fix:** add a sentence. "An overhand knot can be tied in two mirror-image ways; if all three crossings come out reversed, retie it the other way round. The mirror trefoil also has nine colorings and cannot become a plain loop, so either serves Problem 4, but only the matching one fits the printed picture."

## Not checked

- Physical fit of cords, markers and tracing paper, and classroom use. The packet itself marks these as untested.

## Noticed in passing (not mathematics)

- **Bonus guide p. 1:** the text is garbled and appears in the source `guide.md` as well. It reads "For six full pair kits across KK11 /3333 /445" and "KK11 may revisit", presumably meaning K–1 / 2–3 / 4–5. Spaces are missing in "at100%", "the5 pt", "two25 mm", "packets,12" and "Grades2–3".
- **Grades 4–5 p. 4:** Problems 5 and 7 ask for an explanation but have no answer box (for the card).
