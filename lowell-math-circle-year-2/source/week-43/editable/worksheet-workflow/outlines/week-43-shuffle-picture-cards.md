Week 43: Shuffling picture cards

Mathematical kernels

1. To make a uniformly random order of three distinct cards, choose the first card uniformly from all three, the second uniformly from the two remaining, and place the last. Six equally likely choice histories yield the six orders once each. An in-place equivalent chooses uniformly from positions 1–3 to swap into slot 1, then positions 2–3 to swap into slot 2. Choosing the current slot is legal. This is the Fisher–Yates mechanism; general uniformity follows by continuing the shrinking choice set.

2. A tempting alternative swaps slot i with a uniformly chosen one of all three slots, for i=1,2,3. Its 27 equally likely histories cannot split equally among six orders; exact counts are ABC 4, ACB 5, BAC 5, BCA 5, CAB 4, CBA 4. A divisibility argument avoids a 27-row worksheet. Show an explicit input/process/output example for a new swap convention: ABC, choose slot 3 for slot 1, obtains CBA; choose slot 2 for slot 2, remains CBA. Keep the fairness question open. A short random sample does not prove or refute exact fairness.

Sources: Princeton Algorithms, Knuth/Fisher–Yates: https://algs4.cs.princeton.edu/11model/Knuth.java.html; wrong-range comparison in https://www.cs.princeton.edu/courses/archive/fall13/cos226/lectures/21ElementarySorts-2x2.pdf. Three-card distributions independently enumerated. Fall repeating machines/perfect shuffles concern deterministic iteration, not random uniformity.

Suggested emphasis by level:

K–1: make different picture orders and use a concrete chooser; distinguish a picture order from its choice history.
Grades 2–3: connect each of six fair choice histories to one final order with movable cards.
Grades 4–5: design and certify a uniform method and find a structural obstruction to the naive method.

Materials

Per child: three distinct picture cards about 40×55 mm, a three-slot mat with slots at least 45×60 mm, choice tickets for positions 1,2,3, and a second two-ticket set for positions 2,3, plus an opaque cup. Ten identical kits; no 52-card deck. Draw tickets uniformly and replace/reset according to the demonstrated chooser. Supply six loose final-order cards if useful; no mandatory exhaustive tally of random trials. Use letters only as secondary labels so nonreaders can manipulate the same mathematics.
