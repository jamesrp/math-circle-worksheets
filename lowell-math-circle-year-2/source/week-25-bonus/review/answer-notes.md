# Week 25 revised answers and assumptions

Three investigations: extra diagonal shadows (P1), cell-query information with adaptive/fixed continuation (P2–P3), and equal-total legal shadows that cannot fit (P4). One shared Grades K–5 companion. Younger supported entry is concrete counter placement and game play; optimal-query explanations belong to readiness-dependent older work. These are not three redundant age variants. Everything is unpiloted. Cover-card procedure and physical counter/printed-cell fit have not been rehearsed.

The source uses 22 mm working cells on P1, P3 and P4. The six candidate diagrams on P2 are compact records; the hidden game uses the separate large 3×3 table grid, with one opaque cover per cell. Candidate pictures remain visible. Adults may read/record; children choose pictures and queries. The first non-task worked picture is 110/001/100, and its full northwest-to-southeast diagonal counts are (1,0,1,2,0), in bottom-left-singleton to top-right-singleton order. The dashed lines are the intermediate membership step.

## Problem 1

There are six pictures with one occupied cell in each row/column. The P2 catalog happens to give all six, but P1 is encountered first and does not prescribe this catalog as the method. In catalog order (occupied columns for A,B,C):

1. (1,2,3): diagonal counts (0,0,3,0,0).
2. (1,3,2): (0,1,1,1,0).
3. (2,1,3): (0,1,1,1,0).
4. (2,3,1): (1,0,0,2,0).
5. (3,1,2): (0,2,0,0,1).
6. (3,2,1): (1,0,1,0,1).

Only pictures 2 and 3 share the diagonal counts. They are 100/001/010 and 010/100/001. Equal extra shadows therefore still do not establish uniqueness. A complete six-picture check supplies an explanation; young children can simply exhibit the pair.

## Problem 2

Worst-case adaptive minimum is three cell questions. Two binary replies give at most four distinct histories and cannot identify six pictures. Three suffice: ask A1. If occupied, ask B2, which distinguishes catalog pictures 1 and 2. If A1 empty, ask A2. If A2 occupied, candidates 3/4 remain; B1 distinguishes them. If A2 empty, candidates 5/6 remain; B1 distinguishes them. Thus some histories need two questions and others three; determined-picture naming is free. Candidate visibility externalizes bookkeeping. Short play supplies experiments; the decision tree and history count establish the bound.

## Problem 3

Four questions chosen before any answers are necessary and sufficient. Ask A1,A2,B1,B2. The occupancy answers determine the first two rows' occupied columns, hence the third.

Every three-cell query set fails. Classify the numbers of queried cells by row, allowing row/column relabeling:

- (3,0,0): an unqueried 2×2 rectangle lies in the other two rows.
- (2,1,0): choose the latter two rows and the two columns avoiding the single queried cell in the middle row; again an unqueried 2×2 rectangle.
- (1,1,1) with two queried cells in the same column: those two rows and the other two columns give an unqueried rectangle.
- (1,1,1) with three different queried columns: relabel so the asked cells are A1,B2,C3. The two 3-cycle pictures 010/001/100 and 001/100/010 both answer empty to every query.

An unqueried rectangle supports two distinct permutation pictures with occupied opposite corners and the same remaining occupied cell outside the rectangle; they give the same replies. Therefore none of the cases separates all six pictures. This corrects the outline's claim that EVERY three-query set misses a rectangle: the three-diagonal-cell query set does not miss a rectangle, but the 3-cycle collision supplies the necessary obstruction. No lower-bound proof is printed on the student pages. Exhaustive checks over 84 three-cell query sets in `src/check.py` confirm zero separators; the independent reviewer must check the correction.

## Problem 4

- Top left rows (3,3,0), columns (3,3,0): impossible. Two full rows need six counters, while those rows can take at most min(2,3)+min(2,3)+min(2,0)=4 from the columns. Even one full row contradicts the zero column.
- Top right rows (3,2,1), columns (2,2,2): possible. Exactly three labeled pictures: 111/110/001; 111/101/010; 111/011/100.
- Bottom left rows (2,2,2), columns (3,3,0): unique 110/110/110.
- Bottom right rows (3,3,1), columns (3,3,1): impossible with all positive counts. The two full rows need six counters; columns can supply at most 2+2+1=5 to those rows. Equivalently they would force two counters into the column whose shadow says one.

All local counts lie 0–3 and total sums match; these conditions are insufficient. The general chosen-k-row capacity inequality is requirement ≤ sum min(k,column count). The student task asks for concrete obstructions, not Gale–Ryser sufficiency.

## QA and sources

`src/check.py` verifies all represented candidate shadows, adaptive depth, all fixed query subsets up to four, and all 512 binary pictures against the four count cases. Results in `writer-checks.json`; this is writer validation, not independent math review. Standalone portable build accepts optional output directory; dependencies are standard LaTeX packages and pdflatex/PDFLATEX. Every draft page was rendered and inspected. Background source Ryser (1957), §3 concerns base switch connectivity, not these new queries or diagonal conclusions. Existing Week 6 whole-word score games are related but different.

## Revision representation checks

The same complete d1-d5 convention is now anchored at both Problem 1 working-board borders, with faint membership lines. d1=C1; d2=B1,C2; d3=A1,B2,C3; d4=A2,B3; d5=A3. No target counters or matching-pair answer was added.
