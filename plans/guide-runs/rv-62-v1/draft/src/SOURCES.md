# Source and adaptation record

## Consulted directly

- Final return-visit student PDFs, identifiers W62-RV-K-v1, W62-RV-M-v1,
  W62-RV-U-v1: 6, 10, 10 pages. All 26 pages rendered and visually inspected.
  Associated `src/` includes final instances, diagram geometry and generated TeX;
  independently transcribed instances and a new solver are in `check_guide.py`.
- `worksheet-workflow/outlines/week-62-return-visit.md`, all three kernels;
  `plans/return-visit-drafts/week-62/review.md` and `review-math.md` describe an
  earlier draft. In particular middle P4 changed, and upper P5–11 moved/expanded.
  The final PDF map, not the older key's numbering, governs this guide.
- Base Week 62 guide W62-FAC-v3, pp.1–3 for model/preparation/launch, remaining
  pages for first-visit boundaries; materials W62-M-v1, its single page, inspected
  visually. It prints three kits of eight letter cards and four headers.
- Week 8 return-visit guide RV8-FAC-v3, all five pages as a structural model;
  Week 98 facilitator guide source and solution text as a tone/density model.
- Igor Pak, MIT 18.315 Spring 2005 course, notes by Amanda Redlich,
  [Lecture 4](https://ocw.mit.edu/courses/18-315-combinatorial-theory-introduction-to-graph-theory-extremal-and-enumerative-combinatorics-spring-2005/1a85b3cef5c53f1dbab7dd5d18b54035_lec04.pdf),
  both scanned pages inspected. The opening theorem/proof on p.1 establishes
  recoloring connectivity for at least maximum degree plus two colors. The guide
  specializes that result to rings; it does not use the other handwritten claims.
- E. Lehman, F. T. Leighton, A. R. Meyer,
  [Mathematics for Computer Science](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf),
  revised June 6, 2018, section 10.5.2, printed pp.435–438 / PDF pp.443–446.
  Theorem 10.5.8 and Corollary 10.5.9 are the earliest-scheduling/critical-path
  references. The unit-duration, unlimited-parallel-capacity assumptions matter.
- Publisher abstract and bibliography (not full proof) for L. Cereceda,
  J. van den Heuvel, M. Johnson,
  [Finding paths between 3-colorings](https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.20514),
  *Journal of Graph Theory* 67(1) (2011), 69–82; DOI 10.1002/jgt.20514.
  This confirmed the subject and bibliographic details, not a precise theorem
  attribution for the cycle up-count. The invariant is proved independently here.

## Outline bibliography, not independently consulted as proof sources

The outline candidly gives some details from memory. Preserve that boundary:

- P. Erdős, A. L. Rubin, H. Taylor, *Choosability in graphs*, Congressus
  Numerantium 26, 125–157, proceedings of the 1979 West Coast conference.
  The linked Erdos archive uses a 1980 filename, and catalog records differ in
  year conventions. A direct full-text retrieval failed; no specific theorem/page
  from this paper is asserted. The guide gives elementary proofs for its graphs.
- V. G. Vizing (1976): the outline supplies no title or page range. Not checked;
  not treated as a precise citation for any guide proof.
- R. Diestel, *Graph Theory*, chapter 5, list-coloring section: the outline gives
  no edition; exact section/page unverified. Not used as a checked locator.
- L. Cereceda, J. van den Heuvel, M. Johnson, *Connectedness of the graph of
  vertex-colourings*, *Discrete Mathematics* 308 (2008), 913–919. Bibliographic
  details also appear in the consulted 2011 publisher reference list; full text
  not consulted.
- J. van den Heuvel, *The complexity of change*, *Surveys in Combinatorics 2013*,
  LMS Lecture Note Series 409. Outline reference; chapter pages not checked.
- L. Mirsky, *A dual of Dilworth's decomposition theorem*, *American Mathematical
  Monthly* 78 (1971), 876–877. Outline reference; full text not consulted. The
  elementary scheduling proof is given in the guide and verified against MIT.
- Gallai (1968) and Roy (1967), via D. B. West, *Introduction to Graph Theory*,
  2nd edition, section 5.1. Outline references, not directly checked. The guide
  proves the circle-free orientation/coloring connection it uses; it does not
  invoke the stronger unrestricted-orientation theorem as an unexplained fact.
- R. P. Stanley, *Acyclic orientations of graphs*, *Discrete Mathematics* 5
  (1973), 171–178. Outline context only. Negative chromatic-polynomial evaluations
  and the outline's Stanley counts are not part of this guide's tasks or answers.

## Pedagogy and scope

The optional MSRI books are absent in this checkout. The base Week 62 guide
reports Math Circle by the Bay preface pp.viii–x (PDF 9–11) on manipulatives,
continuing depth and variable pace, and Rozhkovskaya Lessons 7–8 on missed legal
moves and transcription. Those are second-hand reports from the base guide,
not freshly inspected originals or evidence of this activity working.

The new guide proposes visible key counters, partner endpoint checks, one move
word, staged introductions and readiness-dependent later routes. These are
inferences/proposals, not classroom observations. All exposition, worked guide
examples, solution organization and checker code are newly authored. No source
PDF, scan, book figure, old solver, generated prompt, or external source text is
included in this portable source folder. Student pages were left untouched.
