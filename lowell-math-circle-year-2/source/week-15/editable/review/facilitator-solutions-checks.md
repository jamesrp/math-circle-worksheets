# Week 15 facilitator guide checks

Status: draft and unpiloted. Week 15 is a library label, not a scheduled event. Checked October 3, 2026. The mathematical review here is an independent computational method and written derivation, not a separate human or classroom review.

## Coverage and fidelity

- All 24 final numbered problems are covered: Problems 1–8 in each of K–1, grades 2–3 and grades 4–5. Each has a solution diagram, explanation, adult-only held hint and optional extension.
- Guide: 14 US Letter pages. Pages 1–2 are preparation, flexible one-hour teaching menu, mathematical reference, source citations and limits. Pages 3–6 cover K–1; 7–10 grades 2–3; 11–14 grades 4–5. There are 24 equal-scale TikZ answer maps.
- Student PDFs remain eight pages each. Their SHA-256 hashes are unchanged; see `reference-pdf-sha256.txt`. The student writer is parsed as data, never executed or edited.
- The final wording is honored: K–1 Problem 4 keeps every nearest letter, and grades 2–3 Problem 7 forbids any contact with C, including a single point.
- Coordinates are adult-only checks, with frame [-3,3] × [-3,3]. Reduced guide diagrams are not full-size measurement sheets. Ties are retained in all closed cells. The frame is not mistaken for a whole-plane boundary.

## Independent exact checks

Run `check_solutions.py` with Python 3. The builder uses exact rational polygon clipping. The checker independently enumerates intersections of pairs of supporting lines and tests every inequality, then compares the vertex sets for every shown construction. This checks 82 site cells underlying the 24 maps. Direct squared distances independently check all 50 original student probe points. The reported solution keys agree.

Key exact results:

- K–1 Problem 1: 7 A, 6 B and 3 AB answers. Problem 4: 3 A, 3 B, 1 C, 2 AB, 1 AC, 1 BC and 1 ABC.
- Grades 2–3 Problem 1: 4 A, 6 B and 4 AB. In both P/Q triangle tasks, P=(0,1) is C only; Q=(0,-1) is AB. At P the squared lengths are 5,5,1; at Q, 5,5,9.
- Triangle map: A has x≤0,y≤−x; B x≥0,y≤x; C y≥|x|. Only the nonpositive half of the A/B bisector survives.
- Collinear maps have their adjacent midpoint boundaries. The unequal middle strip is −5/4≤x≤3/4. No three-way tie is possible for three distinct collinear sites.
- The square has closed quarter-plane cells and a four-way tie at the origin. With center E added, its cell is |x|+|y|≤2. The four diamond vertices retain three-way ties; open central axis pieces cease to be boundaries between old sites.
- K–1 Problem 7: midpoint C gives |3x−2y|≤39/10. The strip and corner inverse constructions use reflected sites, respectively (−2,0),(2,0) and (2,0),(0,2).
- Grades 2–3 Problem 5: sharing pairs AB, AD, BC, BD, CD; AC has no shared point. ABD vertex (0,−1/2); BCD vertex (3/8,0). BD segment length 5/8.
- Grades 2–3 Problem 7: D=(0,−5/2) has y≤−4|x|/5−9/20, with ABD vertex (0,−9/20). It shares rays with A and B, and no point with C. D=(0,−2) fails the final wording because of a four-way contact at the origin.
- Grades 4–5 Problem 3: D's full triangle has vertices (−7/4,1),(7/4,1),(0,−5/2). The segment claim is certified by intersection of closed half-planes, not by samples.
- Grades 4–5 Problem 6: two new sites (0,2),(0,−2) produce B's square [−1,1]². One added half-plane leaves a vertical tail of the old strip, proving minimality.
- Grades 4–5 Problem 7: reflected sites (0,−2),(24/13,16/13),(−24/13,16/13) produce the exact target triangle. Reflection equations and vertices are checked separately.
- Grades 4–5 Problem 8: R cannot be removed while P,Q remain, by convexity including ties. B=(0,−5/2) removes S strictly and leaves P,Q,R strictly with A; the new boundary is y=−1/4.

## Rendering and source checks

The PDF was compiled twice with LaTeX/TikZ and rendered at 100 dpi. Every final guide page was inspected individually. No clipping, overlaps, blank spill pages, broken glyphs, unreadable labels or TeX overfull warnings remain. A first-draft two-line spill and escaped apostrophe captions were repaired before the final render. Text checks confirm two complete solution blocks on each solution page and draft/unpiloted labeling throughout.

References consulted: final student sources and PDFs; the Week 15 outline and adversarial review; project design guidance; David M. Mount, CMSC 754 Lecture 10, *Voronoi Diagrams and Fortune's Algorithm*, Fall 2021, pp. 1–3, https://www.cs.umd.edu/class/fall2021/cmsc754/Lects/lect10-vor.pdf; Natasha Rozhkovskaya, *Math Circles for Elementary School Students*, “Introduction: Berkeley 2009,” local EPUB section. Source conventions and pedagogical limits are explicit on guide page 2.

The schedule, pacing and hints are proposals. No pilot, actual attendance, supply inventory or printing calibration has been claimed.
