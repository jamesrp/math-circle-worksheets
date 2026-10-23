# Week 88 (Packing and kissing circles): math check

Scope:
- `lowell-math-circle-year-2/week-88/week-88-students.pdf`: one shared Grades K–5 packet, 8 pages, Problems 1–11.
  - p. 1: shared rules and Problem 1 (actual-size 40 mm middle disk). p. 2: Problem 2 (160 × 112 mm tray).
  - p. 3: Problems 3 and 4. p. 4: Problem 5. p. 5: radius bridge and Problem 6 (actual-size 40 mm middle disk).
  - p. 6: Problem 7 (160 × 110 mm tray). p. 7: Problems 8 (160 × 108 mm tray) and 9. p. 8: Problems 10 and 11.
- `week-88-facilitator.pdf`: 6 pages. Both PDFs are byte-identical to the copies in `source/week-88/reference-pdfs/`.

Sources read: `source/week-88/student/students.tex`, `guide/facilitator.tex`, `build.py`, `README.md`, `QA.md`, `SOURCES.md`. I did not run or import the package's `check_math.py`. My scripts and their outputs are in this run folder, for `plans/review/checks/week-88/`. Checked October 23, 2026.

**Result: every answer, construction, bound and proof in the packet and guide is correct. I found 4 problems, all minor:**
1. One false sentence in the guide's Problem 5 hint.
2. Problem 10 assumes the child's rings from Problems 3–5 were the largest possible.
3. Problem 4's half-scale sketch has no "not actual size" caption.
4. Problem 6's actual-size middle disk sits too close to the problem text for a full ring.

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 0 failures). Standard library only.
  - **Least centre angles.** For every pair of outside sizes around each middle disk, computed two ways: by the cosine rule, and by bisection on the real centre distance.
  - **Equal-size rings.** Largest n with n·α ≤ 360°. An equally spaced construction is checked on every pair. The guide's ⌊π/arcsin(r/(R+r))⌋ is compared with the gap count on 40,000 radius pairs.
  - **Mixed rings.** Every cyclic order of small (S) and large (L) outside disks, lengths 2–14, is tested by its sum of least gaps. Every order that passes is realised explicitly and checked on every pair. This gives the true maxima with and without the both-sizes rule.
  - **Guide witnesses.** Both mixed witnesses, with angles parsed from the guide source.
  - **Trays.** The guide's 11-centre table is parsed from the source and checked in exact arithmetic (numbers p + q√3): all 55 pairs, the walls, and 108/110/112 mm. The row-constrained minimum for Problems 8–9 is found by sweeping every middle-row position. Oler's inequality gives a proven bound for any packing in each tray.
  - **Guide numbers.** Every number the guide quotes.
- **`check_packing.py`** (output `check_packing.py.out`). A numpy multi-start search for unrestricted tray packings: 12 disks at 112 mm, and 11 disks at 108 mm in any arrangement. This is numerical evidence, not proof. Two sanity cases with known answers show the search's accuracy (about 0.02 mm).
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 0 failures, 2 findings). Reads the delivered student PDF with PyMuPDF:
  - headers, footers and problem numbers 1–11;
  - every circle's printed diameter and roundness, its nearby label and the page's sketch captions;
  - the tray interiors between the inner edges of the border strips;
  - the radii, tangency and joining segments of the p. 5 bridge;
  - the clear room around both actual-size middle disks.

  It re-reads every quoted guide sentence with pdftotext.

## Problem-by-problem verification

| Problem | Asks | Intended answer | Verified |
|---|---|---|---|
| 1 | Most 40 mm disks touching a 40 mm middle | 6 | Least gap exactly 60°; 7·60 = 420 > 360. The equally spaced six-ring is legal and every neighbour touches. The printed middle is 40.000 mm, with ≥ 74.7 mm clear around it. |
| 2 | Most 40 mm disks in 160 × 112 mm | Open; guide proves 11, claims no maximum | 11 (rows 4-3-4) fit with 2.718 mm spare. The square baseline of 8 fits; a third straight row of four would need 120 mm. Oler proves ≤ 12. The search finds no 12 (see the note below). Interior measures 160.001 × 112.001 mm. |
| 3 | 40 mm ring about 80 mm middle | 9 | α = 2 arcsin(1/3) = 38.942°, so 10 would need 389.42°. The nine-ring's neighbours are 41.04 mm apart. |
| 4 | 80 mm ring about 40 mm middle | 4 | α = 83.621°, so 5 would need 418.10°. The four-ring's neighbours are 60√2 = 84.85 mm apart. |
| 5 | Mixed ring, at least one of each size | 8 (80 mm middle), 5 (40 mm middle) | Exhaustive over cyclic orders. The maxima are reached with 1 or 2 large disks only. Both guide witnesses are legal (least clearance 1.042 mm and 0, touching). |
| bridge | Centre distance = sum of radii | – | Radii 7.5 and 12.5 mm, drawn at half scale for 15 and 25. Centres are 20.00 mm apart, so the disks are tangent. The segments join the centres, and the dot is at the contact point. |
| 6 | Largest ring, why not one more, must neighbours touch | 6; 420° > 360°; yes | The equality case is forced: six gaps of at least 60° that sum to 360° are each exactly 60°. |
| 7 | 4-3-4 rows in 160 × 110 mm | Fits, with 0.718 mm spare | Exact: 20 pairs touch, none overlap, 40√3 < 70. Oler also proves 11 is the most any arrangement can hold here. |
| 8 | 4-3-4 rows in 160 × 108 mm | No | The rows of four are forced to x = 20, 60, 100, 140. Every middle x is within 20 of one of them, so each row gap is ≥ 20√3 and the height is ≥ 40 + 40√3 > 108. |
| 9 | Smallest height for those rows | 40 + 40√3 ≈ 109.282 mm | The sweep gives the least offset 20√3, only at x = 40, 80, 120, which are 40 apart, so the bound is attained. |
| 10 | Explain why the rings in Problems 3–5 can't be beaten | The bounds above | The bounds are correct, with wide margins: 389° (P3), 418° (P4), 369° and 381° (P5), each against 360°. See problem 2 below for the wording. |
| 11 | Rule for equal outside disks | ⌊π / arcsin(r/(R+r))⌋, depends only on the ratio | Formula and scale invariance confirmed. |

Diagram scaling: every circle is round to 0.001 mm. The sketches on pp. 3, 4 and 8 keep the 80 : 40 ratio exactly, at 0.5, 0.5 and 0.3 scale.

## Located problems

### 1. Guide p. 3, Problem 5: a false sentence in the hint (minor)

> "Changing the central disk can change which size consumes the most room."

**Evidence** (`check_math.py.out`, Guide p. 3 section). Least gaps between outside centres:
- 80 mm middle: S–S 38.94°, S–L 48.19°, L–L 60.00°.
- 40 mm middle: S–S 60.00°, S–L 70.53°, L–L 83.62°.

Around either middle, a large outside disk needs more angle than a small one. Swapping one small disk for a large one costs +18.49° around the 80 mm middle and +21.06° around the 40 mm middle. So changing the middle never changes which size takes the most room. It changes how much room each size takes. An adult reading this hint would expect a reversal that never happens.

**Fix.** "Changing the central disk changes how much extra room the large disk takes: about 18° more than a small one around the 80 mm middle, about 21° more around the 40 mm middle." Or delete the sentence.

### 2. Student p. 8, Problem 10: assumes the earlier rings were the largest (minor)

> "Return to your rings in Problems 3–5. For each one, can you explain why a ring with more outside disks is impossible?"

**Evidence.** The guide (p. 3) explicitly accepts non-maximal rings: "A legal eight-disk construction remains valid evidence, even if not best." For a child whose Problem 3 ring has eight disks, the statement to be explained is false. A legal, non-maximal eight-ring exists, with 5.92 mm between neighbours (`check_math.py.out`, Problem 10 section). The same applies to a four-disk mixed ring in Problem 5, and so on. Such a child is asked to prove something false.

**Fix.** "Return to Problems 3–5. For each one, what is the largest possible ring? Explain why no ring can have more outside disks." This keeps the upper-bound task. A child who finds a bigger ring along the way has made progress, not hit a contradiction.

### 3. Student p. 3, Problem 4: half-scale sketch with no "not actual size" caption (minor)

**Diagram.** Problem 4's figure labels a circle "40 mm" but prints it 20.0 mm across, and labels a circle "80 mm" but prints it 40.0 mm across (`check_diagrams.py.out`). The only caption on the page, "Sketches, not actual size", sits at y = 85 mm. That is under Problem 3's figure and above Problem 3's answer line, so it reads as belonging to Problem 3. Elsewhere in the packet, uncaptioned circles are actual size: the 40 mm middles on pp. 1 and 5 measure 40.000 mm. Under that convention Problem 4's "80 mm" circle is exactly the size of a real 40 mm disk. A child who checks a disk against it will find the label contradicted.

**Fix.** Add "Sketches, not actual size" under Problem 4's figure, as under Problem 3's.

### 4. Student p. 5, Problem 6: actual-size middle disk too close to the text for a full ring (minor)

**Diagram.** The actual-size 40 mm middle disk is centred at y = 176.2 mm. The last line of Problem 6's text ends at y = 120.5 mm, which leaves 55.7 mm. A ring of six 40 mm disks reaches 60 mm from the middle centre. If one outside disk sits straight above the middle, it covers the problem text by 4.3 mm. Only rotations with two disks straddling the top clear it, by 1.1 mm (`check_diagrams.py.out`). The source reserves only ±45 mm vertically: `\path[use as bounding box] (-65,-45) rectangle (65,45)`. Page 1 reserves ±67 mm and has 74.7 mm clear.

**Fix.** Enlarge the vertical bounding box to at least ±62 mm, as on p. 1. There is 91 mm of free space below the disk.

## Adult guide

Apart from problem 1 above, the guide checks out completely. Points confirmed:
- **Overview.**
  - The equal-disk theorem has the right hypotheses: planar, nonoverlapping, external tangency, equal radii, local not density.
  - The ⌊π/arcsin(r/(R+r))⌋ formula is stated for congruent outside disks only.
  - The mixed maxima are 8 and 5.
  - The 4-3-4 minimum height is stated only for those rows.
  - The overview separates construction (lower bound), failed attempts (conjecture) and proof.
- **Problem 6 proof.** The least-gap triangle argument, the gap larger than a half turn, rigidity, and the 4×60 + 120 versus 5×72 flexibility contrast are all correct.
- **Problems 7–9.** The row argument is correct and complete: the rows of four are forced, there is the 20 mm horizontal bound, and both row gaps are ≥ 20√3.
- **Problems 10–11.**
  - The chord formula holds for θ ≤ 180°.
  - The converse construction is right: ⌊2π/α⌋ equally spaced disks fit.
  - The cosine-rule bound for mixed radii is correct.
  - β = arccos(2/3) and γ = arccos(1/3) are correct.
  - 2β + 7α ≈ 368.976° and 2γ + 4·60 ≈ 381.058° are correct. The "every other gap is at least α, or at least 60°" step holds because those are the smallest of the three pair angles.
- **Materials.** 13 small and 5 large disks per pair let a child try one more than every maximum (12 in the tray, 10 around the 80 mm middle, 5 large around the 40 mm middle). The largest ring the materials allow reaches 120 mm from its centre, which is within the 260 × 260 mm mat. The totals are 65 small and 25 large for five kits.

## Facts the guide may want (not errors)

- **Problem 2, 112 mm tray.** Oler's inequality (N ≤ 2A/√3 + P/2 + 1 for centres at least one unit apart in a convex region) proves that 13 disks never fit. The search finds no 12: its best minimum centre distance is 37.05 mm against the 40 mm needed (`check_packing.py.out`). For twelve, the search first succeeds at 120 mm, the height of three straight rows of four; it still fails at 118 mm (39.06 mm). So 11 is almost certainly the answer. The guide is right not to claim it as proved.
- **Problem 7, 110 mm tray.** Oler proves 11 is the most any arrangement can hold, not just the 4-3-4 rows.
- **Problem 8, 108 mm tray.** In any arrangement, the search's best is 39.45 mm. That is the 4-3-4 pattern squashed to rows 34 mm apart, against the 40 mm needed. So the "no" very likely holds without the row restriction, though only the row version is proved. The guide's "No claim is made here about arbitrary 11-disk packings in 108 mm" is appropriately cautious.

Physical fit, printing and disk accuracy are outside a math check and remain untested, as the package says.
