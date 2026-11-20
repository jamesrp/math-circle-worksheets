# Week 58 return visit writer report

## Deliverable and stage

- `draft/facilitator.pdf`: **8 US Letter pages**, W58-RV-FAC-v1.
- Portable source: `draft/src/` with `facilitator.tex`, `checked-tables.tex`, independent `check_guide.py`, `build.sh`, and source README.
- Writer stage only. No formal guide critic or reviser stage was run, no student/material PDF or source was changed, and nothing was committed, pushed or published by this writer. The separate Claude critic is next.
- **Unpiloted and physically unrehearsed.** The guide does not claim child testing, successful staffing/timing, or actual material fit.

## Mathematical destination

The opening overview proves the two-cut bound for even-count two-colour trains using a half-length moving window, distinguishes impossibility from needing more cuts, gives exact half-colour sharing under additive uniform-within-colour values, states the three-panel obstruction, proves the proportional marking invariant, and bounds split cards by the selected cut locations. The solutions establish uniqueness of the 60/180 mm strip cuts, the three required panel half-cuts, every finite train answer, all marking outcomes and envy comparisons, and both upper card obstructions.

For upper Problem 3's actual question about other numbers on the same two uniform-colour cards, the direct half-of-each-colour argument suffices (including zero values). The guide does not import an unnecessary continuous two-knife theorem for arbitrary varying density. General necklace-splitting and connected envy-free results remain explicitly unproved background.

## Independent mathematical checks

`check_guide.py` was written independently, not copied from the student checker. It binds the three final student PDFs by SHA-256 and checks every numbered problem's page against `pdftotext`.

Checks passed:

- Every displayed train was transcribed against the final rendered diagrams and solved by all card-to-tray assignments; the number of assignment transitions is the exact minimum number of gaps. All minimum cut sets are retained. Middle Problem 2 row 6 has exactly two minimum sets, `(2,7)` and `(3,8)`; both are printed.
- All six two-red/two-blue orders are listed. All 70 four-red/four-blue orders confirm 36 one-cut and 34 two-cut orders, with the complete first-half criterion and counts by class.
- All 790 nonempty trains using at most six reds and four blues: 441 impossible, 179 requiring one gap, 170 requiring two.
- All 10,922 even-count binary trains of even length 2 through 14 pass a separate half-length-window scan. The general proof, not this finite scan, establishes the unlimited claim.
- Exact fractional strip values, 80/160 mm individual half points, the 60/180 mm exact split, and the three-panel half system with determinant 576.
- All six panel orders: both rounds' marks, selected takers, all nine observer-versus-tray values, own-share bounds, and every strict envy relation. Tables are generated from these exact Fraction computations and checked again at the end of the build.
- All 120 labelled arrangements of three reds/two blues have their 5.5 half point inside a red; ten colour orders. The printed R3 midpoint and two-red/three-person obstruction are checked.
- Both non-task launch examples, the changed-total counterexample, and other printed arithmetic/counts are asserted.

## Final-page and build checks

- Personally rendered and inspected **all 17 final student pages** (K–1 5, middle 6, upper 6) at 100 dpi. Compared train words, cards, diagrams, problem numbering and page locations with the source and the guide key. No student edits.
- Inspected all eight base-material pages, the base adult guide, the outline, both earlier student reviews, the draft README, and the Week 8/Week 98 model guides. Materials sizes and print-page descriptions match the base kit.
- Compiled twice with pdfLaTeX in the coordinator-provided isolated TeX environment. No errors or overfull boxes; `build.sh` rejects overfull boxes. Cleaned TeX intermediates automatically.
- Personally rendered and inspected **all eight final guide pages** at 120 dpi: no clipping, overlap, broken tables or footer collisions. An initial isolated spill paragraph was fixed before final QA by placing the two short K–1 answer tables side by side.
- Clean-copied only `draft/src/` and the three unchanged student PDFs to a new directory outside the repository. Rebuilt there with no repository dependency; checker found the PDFs beside `src/` and passed. `pdftotext -layout` matched exactly. The rebuilt PDF was also byte-identical.
- Final PDF SHA-256: `5c21b93a5045bd9628c804d1c27569986ff21ce87f74a501bfd0d0ec721ee415`.
- QA records live only under this run's `tmp/`: student/material renders, final guide renders, extracted text, `build-check.log`, `clean-build-check.log`, `clean-facilitator.txt`, and `clean-path.txt`. These are not deliverables for the branch.

## Student-page risks and adult workarounds

1. **Upper Problem 6, student page 5:** “whatever values the cards give” follows rules that fix the target at 4. That universal statement needs “one third of each person's original total”; keeping 4 fails when totals change. For example, three panels each worth 8 give total 24, so a first share of 4 is below the required 8. Guide page 7 flags this explicitly and requires personal target `T_i/3`, unless each total remains 12. This is a newly identified wording risk for the critic/organizer, not a silent student edit.
2. **Middle Problems 5–6, student pages 5–6:** although selected cuts use half-panels, a non-taker's second-round mark is 112.5 mm in every middle game. The guide supplies the exact mark and explains that showing it lies beyond 75 mm is enough to decide the taker. Do not describe the game as needing only half-panel reasoning.
3. **K–1 Problem 3, student page 3:** the revised prompt is interpreted as recording successful partner challenges actually played, not an all-34 catalogue. The guide gives the complete 34-order characterization and tells the adult that seven rows are not a promised total.
4. **Middle Problem 1, student page 1:** eight recording rows intentionally accommodate only six colour orders plus spare space. The guide warns against hunting for two nonexistent answers.
5. **Strip pictures:** the printed student strips are schematic. All physical measuring/cutting uses the separate 240 mm materials strip. All cuts are straight across; a longitudinal fold/cut is not allowed.
6. **Two kinds of A/B:** the guide asks adults to put away two-person cards before using three-person A/B/C. Comparisons always keep one observer fixed across trays.
7. **Upper Problem 4:** three observers judge two trays; this is an exact-bisection test, not a complete allocation into three recipients' own shares. The guide keeps the two-tray comparison and does not claim unique physical arrangements of already-separated panel halves.
8. **Open-length train records:** middle Problem 4 prints twelve slots but does not require twelve cards. The per-pair ten-card kit handles every fixed train; children can sketch larger invented cases. Adding two cards is not silently claimed as part of the kit.

The earlier reviews' main page defects (cut direction, more than one piece per tray, and K–1 counting places rather than motions) are visibly corrected in the final student PDFs. The common example is now RBR|BRR, not the earlier repeated-order example; upper P5 has its printed first-round example, and upper P8 now calls for paper reds. The guide follows those final versions.

## Materials and unavailable evidence

Every object needed by the **student pages** has a printable base-kit shape. Longer trains require the named extra unmounted page-1 copies; panel games consume additional page-5 sets; upper P8 requires two fresh paper reds. The guide gives a stock plan rather than assuming two shared pair kits let both pairs work simultaneously. The optional neutral 30 mm launch strip is made from scrap and is not a base-kit printable; it is only a non-task demonstration.

The original private reference books were not available in this checkout and are not claimed as reread. Procaccia's author-hosted chapter was consulted online, especially sections 13.2 and 13.3.1–13.3.3; the other outline references are transparently labelled bibliography not newly consulted. No claim about physical readiness or age fit is inferred from that literature. Cutting, replacement handling, table footprints, preparation time and all classroom outcomes remain unverified.
