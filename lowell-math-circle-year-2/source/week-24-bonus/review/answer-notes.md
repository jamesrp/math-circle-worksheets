# Week 24 revised answers and assumptions

This is one shared Grades 2–5 companion, with three distinct directions: a simultaneous three-way champion, the change caused by summing two replacement draws, and concealed deck choice. It deliberately does not repeat cycle-building, deck edits, duplication or certainty from a lucky run. All material is unpiloted; bag independence/mixing and physical fit are unrehearsed. Routine reading/recording help is expected. P1 and P2 are the concrete route; exact distribution comparisons and minimax reasoning require readiness. The base outline supplies the fixed deck model; the new counts were recomputed by `src/check.py`, whose results are in `writer-checks.json`. This writer computation is not an independent reviewer computation.

## Problem 1

There are 3×3×3=27 equally likely triples, no ties. A wins 10, B wins 10, C wins 7. Champion counts for each card are A2:0, A4:1, A9:9; B1:0, B6:4, B8:6; C3:1, C5:2, C7:4. Each count is the product of the numbers of lower cards in the other two decks. The answer is that A and B tie for the largest chance, each 10/27; C has 7/27. The tables do not prescribe an enumeration order.

## Problem 2

Ordered draws matter: (2,4) and (4,2) are two physical outcomes even though their sum agrees. Each deck has nine equally likely ordered draws.

- A, first-card rows 2,4,9: totals (4,6,11), (6,8,13), (11,13,18). Multiplicities: 4:1, 6:2, 8:1, 11:2, 13:2, 18:1.
- B, rows 1,6,8: (2,7,9), (7,12,14), (9,14,16). Multiplicities: 2:1, 7:2, 9:2, 12:1, 14:2, 16:1.
- C, rows 3,5,7: (6,8,10), (8,10,12), (10,12,14). Multiplicities: 6:1, 8:2, 10:3, 12:2, 14:1.

## Problem 3

Each pair has 9×9=81 equally likely four-card outcomes. A–B: A wins 37, B wins 44, 0 ties. A averages 74/81 points, B 88/81. B–C: B wins 39, C wins 38, 4 ties; points 82/81 and 80/81. C–A: C wins 39, A wins 38, 4 ties; points 82/81 and 80/81. The one-draw A advantage over B reverses. A chart matching each of nine ordered draw cards to each of the other's nine, or multiplying sum multiplicities, is valid. The facilitator may offer this method when needed; the student page leaves the organization open.

## Problems 4 and 5

The label bag must be nonempty. A or B or C may individually have no slips. Each individual equal-sized slip is an equally likely physical choice; duplicate labels therefore contribute multiplicity. The printed average is the exact average over all equally likely independent label-slip and card draws, not the mean of a short play sample.

The added convention visual is a single legal round: You draw label B, select deck B=(1,6,8), and draw 6; the opponent draws label A, selects deck A=(2,4,9), and draws 4. Since 6>4, points are 2 and 0. Both selected cards belong to the shown decks. This illustrates only the procedure; it provides no mixture expectation.

Slips have equal size and concealment; labels and numerals are drawn independently, replaced and remixed. Same-deck draws use separate copies and remain independent. Point expectation is a long-run/theoretical average, not a guarantee of a finite score. Against fixed A,B,C respectively, pure A earns (1,10/9,8/9); pure B earns (8/9,1,10/9); pure C earns (10/9,8/9,1). Uniform A,B,C earns (1,1,1). Any bag with equally many A,B,C labels does the same. Child-designed alternatives have no single answer; evaluate with these payoffs.

For label proportions a,b,c (nonnegative, summing to one), expected points against A,B,C are 1+(c−b)/9, 1+(a−c)/9, 1+(b−a)/9. Their sum is 3, so no bag earns more than 1 against all three fixed decks. Having all scores at least 1 forces c≥b, a≥c, b≥a, hence a=b=c. Therefore equal mixing uniquely maximizes the worst expected score. It also earns 1 against any independently selected opponent mixture, by averaging its three fixed-deck scores. A finite game only supplies experiments; the check of all draws supplies the explanation.

## Build and QA

Standalone `src/bonus.tex`, `src/build.py` and `src/check.py`. `build.py [output-directory]` finds pdflatex on PATH or via PDFLATEX, with output/intermediates in the chosen directory. Rendered every draft page and inspected it; no physical-readiness or classroom claim. The exact source references in the outline are background only: Conrey et al., *Intransitive Dice* (2016), pp. 1–2 models the base game, not these new conclusions. AP-22 is related but uses different payoffs/tasks.
