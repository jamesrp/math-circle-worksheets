# Week 87 independent mathematical review

Reviewed the actual draft packets: shared (3 pages, Grades 2–5), line (4 pages, Grades 3–5), upper (2 pages, Grades 4–5), materials (5 pages). All 14 pages were rendered and individually inspected. No K–1 packet was expected under the specific outline. No source or draft was edited.

**Mathematical verdict:** All student problems and displayed numerical/ranking examples check out. Shared Problems 1–3, line Problems 1–4, and upper Problems 1–2 have the intended outcomes under their stated conventions. The median proof, even-voter weak/strict distinction, and real-line impossibility argument are valid; retain their substance. Details and reproducible independent checks are in `math-audit/verification-notes.md`, `independent_check.py`, `results.json`, `check_pdf_geometry.py`, and `geometry.json`.

## Located material-operation defects

### 1. Tally target geometry has no handling clearance

**Location:** materials pages 1 and 4, used by every voting problem. Exact objects: 18 mm vote-token circles versus 17 mm target circles in the 54×54 mm wells.

**Independent evidence:** Actual PDF-vector measurements give token diameter 18.000 mm, target diameter 17.000 mm, horizontal target-center pitch 18.000 mm, and outer target centers 9.000 mm from the well edges. Placing three actual tokens on the top row makes neighboring tokens and both side boundaries tangent. Tiny 0.0001 mm PDF coordinate rounding is not usable clearance. Five votes in the same well are mathematically legal and must be physically supported. The present digital fit does not supply the requested practical clearance.

**Smallest fix:** Adjust target arrangement or token size/well size to make all five votes fit each destination with positive inter-token and boundary clearance, with matching target outlines. Re-measure the rebuilt PDF. This independently confirms adversarial review item 3. Retain “physical cutting/placement untested” until rehearsed.

### 2. Line proposals cannot simultaneously label their fixed positions and tally wells

**Location:** materials page 4, “Place the two current option tiles above the first two wells,” and materials page 5, the sole X/Y proposal pieces. Relevant rule: line page 1, “Favorites stay still. Each voter chooses the nearer proposal, X or Y.”

**Evidence:** The supplied line set has one X and one Y; each must remain on the line to define the unchanged comparison. The tally has only “Option / Option / Tie” labels and requires tiles above the first two wells. Using those same pieces to label the tally removes the proposals from the reference line. The fixed-card route has duplicate A/B/C pieces and does not have this shortage. This is a missing state representation, not an arithmetic error.

**Smallest fix:** Supply a second X/Y pair specifically for tally labels, or persistent X/Y labels on a line tally. Verify the complete state with both proposals on the board, all five fixed favorites present, and all five votes identifiable in the tally. This independently confirms adversarial review item 2.

## Other reviewer concern and verification limits

The two one-voter line demonstrations are individually correct. The adversarial review's request for one complete five-voter operation is supported by the outline; it is a teaching/representation fix rather than a mathematical counterexample. Its suggested non-task example, favorites 0,1,5,8,10 and proposals 2/8, was independently checked: X,X,Tie,Y,Y, so 2–2 with one tied voter.

Independent finite verification covers all 20 unordered sets of three distinct cards, all 216 labelled three-card profiles, all 3,003 five-favorite tick multisets against every different tick, and all 1,001 four-favorite tick multisets. General arguments, rather than these finite experiments, justify the median theorem and arbitrary-real-line impossibility. Physical preparation, actual-size printing, and classroom operation remain untested.
