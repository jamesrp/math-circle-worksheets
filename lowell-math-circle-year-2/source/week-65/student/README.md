# Week 65: Hyperbolic octagon streets, student version 2

Original student text and vector diagrams. One shared Grades 3-5 packet:
six US Letter pages, five consecutively numbered problems, plus a loose
recording sheet. Digitally reviewed; not physically rehearsed or classroom piloted.

## Portable build

Requires Python 3 and a standard TeX installation with pdfLaTeX, TikZ, and
amssymb. No network, external art, nonstandard Python modules, or fixed
machine paths are needed. From any directory:

    python3 /path/to/src/build.py
    python3 /path/to/src/independent_check.py

The first command writes `../students.pdf`, regenerates `students.tex`, and
writes `checks.json`. Use `--output PATH` to choose another PDF location.
`--verify-only` generates the TeX/checks without compiling. Generated TeX can
also be compiled directly with ordinary `pdflatex` (two runs). `build.log` is
a disposable compilation log. The separate mathematical audit writes
`independent-checks.json` and imports no code from the builder. Its Lorentzian
reconstruction and enumeration were authored by the independent mathematical
reviewer; the reviser adapted its input/output paths and label-spacing datum
for this v2 source package.

## Page and problem map

1. Problem 1: finite square-grid full-state returns of 4, 6, and 8 moves.
2. Problem 2: curved-edge heading/arrival/turn visual, then all-left and
   all-right walks on one right-angle octagon. Four moves reach E; the first
   full-state return is eight moves.
3. Problem 3: the outside boundary of two side-sharing octagons, compared
   with two side-sharing ordinary squares. Only local turns are counted by
   the child. Both starts are top shared endpoints, where final arrival
   continues straight into the starting heading.
4. Problem 4: drawn complete streets through P, and a comparison explicitly
   involving ordinary lines extending forever in both directions.
5. Problem 5: two- and four-door routes among four rooms in another view of
   the same geometry. The coin board retains its original scale.
6. Extra workspace for Problem 5. Keep this loose sheet beside page 5.
   Three short-route rows and ten long-route rows provide surplus space,
   rather than preprinting the number of solutions. Long-route rows are
   6.9 inches wide and 0.55 inches apart.

## Construction and checks

The regular {8,4} seed has vertices

    v_k = sqrt(sqrt(2)-1) exp(i(pi/8 + k*pi/4)).

Geodesics are circles orthogonal to the unit boundary, or diameters. The
circle routine explicitly handles the diameter case. Reflected rooms are
hyperbolically congruent; they are not Euclidean translated copies.

For the two-room board set m = 2^(1/4) - sqrt(sqrt(2)-1), and apply

    T(z) = (z-m)/(1-m*z).
    left_k = T(v_k); right_k = -conjugate(left_k).

The common side is a vertical diameter segment. Its midpoint is not a
junction and has no dot. The outside cycle is left_0 through left_7,
then right_6 through right_1, back to left_0. The supporting geodesics
continue into all drawn crossing stubs. Equal x/y scale is 3.6 inches per
disk unit. The unextended pair is 6.26990 by 3.51844 inches; all stubs fit
within a 6.65789 by 3.91996 inch envelope.

Checked results:

- One octagon: eight 90-degree corners, four-move position E, eight-move
  full-state return in either direction. The central board retains scale
  3.23 inches/unit; shortest dot-to-dot distance is 40.41272 mm.
- Two octagons: 14 boundary edges, 12 local left quarter-turns, and two
  straight junctions. The square comparison has six edges, four left
  quarter-turns, and two straight junctions.
- Pair-board minimum separation among *all pairs* of distinct junctions is
  17.85020 mm, not the shortest curved-edge length of 18.94836 mm. The clear
  footprint gap is 7.85020 mm for two 10 mm disks, or 2.85020 mm for 15 mm
  disks. Prefer slim 10 mm arrows; print at actual size (100%).
- Central octagon label centers are 11.61639 mm from their vertex dots.
  The nearest rendered label glyph bounding box is 8.83603 mm from its
  vertex, clear of a 10 mm counter footprint. The square-grid start label
  was also moved away from its dot.
- The curved visual's headings are 157.5 degrees on departure, 112.5 degrees
  on arrival, and 202.5 degrees after the local left turn.
- The entire defining circles of both selected streets miss R, with positive
  separation gaps 0.91017972 and 1.09122572. This is a complete-line claim,
  not an inference from a cropped drawing.
- The four-room graph is Home-A-star-B-Home. There are two two-crossing
  routes and eight four-crossing routes; all are recorded in both checks.
- Independent finite directed-grid enumeration gives 2, 6, and 54 full-state
  returns at lengths 4, 6, and 8. The child only needs examples.
- All 57 independently reconstructed radius-two tiles have right-angle
  corners and equal hyperbolic edge lengths. Layers 1, 8, 48 and multiplicities
  40 once plus 8 twice are verification data, not student census work.
- The independent audit reads all 105 actual drawn TikZ arc specifications.
  Maximum boundary-orthogonality error is below 1.4e-9 in disk coordinates.

## Verification limits

Every final page must be rendered and inspected after changing it. A clean
source-only rebuild verifies portability; equality of rendered pages verifies
that no hidden local artifact supplied an input. Digital spacing and geometry
checks do not replace a 100%-print rehearsal with the actual counters. The
packet and its revised timing/age-fit assumptions remain unpiloted.

Mathematical reference: David E. Joyce, *Hyperbolic Tessellations*, Clark
University, https://mathcs.clarku.edu/~djoyce/poincare/poincare.html
(inspected 2026-10-05). This packet uses {8,4}; it does not reproduce the
{8,8} genus-two edge-identification construction. No workflow exemplar text
or third-party artwork is included.
