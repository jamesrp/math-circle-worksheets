# Checked sources and attribution limits

Checked 2026-10-06. Page numbers below were verified in the actual PDF text, with printed numbering distinguished from the 1-based file-page count. Whole references and extracted pages are working inputs only, not deliverables. No copied source diagrams or substantial quotations are included.

## Core definitions and lineage, Weeks 66–69 and74

Cornelia Druţu and Michael Kapovich, *Geometric Group Theory*, author-hosted [PDF](https://www.math.ucdavis.edu/~kapovich/EPR/ggt.pdf).

- Week 66: Exercise 7.82, printed 233/PDF 253, supplies the wreath-product distance decomposition.
- Week 67: Definitions 6.1–6.3, printed 177/PDF 197; Examples6.19(1)–(5), printed 180/PDF 200, give intervals, medians, coordinate medians and trees.
- Week 68: §9.1, especially Definition 9.3 and Exercise 9.4, printed 287–289/PDF 307–309. The text distinguishes unbounded from bounded complementary components and warns about the infinite cardinality convention.
- Week 69: Definitions 11.1–11.2, printed 363/PDF 383, define thinness for chosen geodesic triangles and a uniform bound.
- Week 74: §8.9, Definition 8.94 and equation8.12, printed 285/PDF 305, define subgroup distortion; this page does not contain the elevator exercise.

These are checked expository sources, not claims of original historical priority. Specific small boards and numerical examples in the prototypes are authored specializations, independently proved in `review-math.md`.

## Week 66: a direct research source for lamplighter dead ends

Sean Cleary and Jennifer Taback, *Dead end words in lamplighter groups and other wreath products*, [author preprint](https://arxiv.org/pdf/math/0309344). Checked §3.1, printed/PDF 4–6, especially Definition 3.1 and Proposition 3.2; §4.1, Definition 4.1 and the family following it, printed/PDF 9. This directly supplies the state interpretation, exact word-metric mechanism, and dead-end lineage. The tiny target used here is an independently checked example, not presented as a copied worksheet problem.

## Week 70: finite blocking

Samuel Lelièvre, Thierry Monteil and Barak Weiss, *Everything is illuminated*, [preprint](https://arxiv.org/pdf/1407.2975). Checked the opening definition of a blocking set on printed/PDF 1 and Lemma 12(a)–(c), printed/PDF 12, with proof on13. Distinct torus points have blocking cardinality4; the midpoint preimages supply the blocking set. The side-4 coordinates and four-diagonal minimality argument in the prototype are an elementary specialization. Source and target are excluded from allowed shields.

## Week 71: inverse bounce information

Aaron Calderon, Solly Coles, Diana Davis, Justin Lanier and Andre Oliveira, *How to hear the shape of a billiard table*, June 25,2018 [author-hosted PDF](https://justinlanier.org/wp-content/uploads/2020/10/bounce.pdf). Checked introductory ABA comparison and Figure 2 on printed/PDF 4; §1.3 Proposition 1.6 and Corollary 1.7 on6; finite-information Theorem 6.3 as stated in the introduction on3. This directly supports the acute-rhombus/square distinction and the edge-parallel-stretch exception.

Moon Duchin, Viveka Erlandsson, Christopher J. Leininger and Chandrika Sadanand, *You can hear the shape of a billiard table: Symbolic dynamics and rigidity for flat surfaces*, October 17,2019 [preprint](https://arxiv.org/pdf/1804.05690). Checked the title/abstract and Bounce Theorem in §1, printed/PDF 2–3. It is broader rigidity context; the elementary worksheet should not imply that its finite experiments prove that theorem. Rectangles need corresponding labels, and corner trajectories are excluded.

## Week 72: Heisenberg area convention

Moon Duchin and Christopher Mooney, *Fine asymptotic geometry in the Heisenberg group*, [preprint](https://arxiv.org/pdf/1106.5276). Checked §1.1, representation and Lemma 1 on printed/PDF 3, and the exponential-coordinate group law on15. The source uses symmetric height; its matrix entry is height plus `xy/2`. The robot's integer memory is the matrix entry, so source height equals robot memory minus `xy/2`. Closed-loop areas agree. This convention conversion is required whenever the source is cited for the activity.

## Week 73: inspiration only

Moon Duchin, *Billiards and Geometric Topology*, [Reed colloquium abstract](https://people.reed.edu/~davidp/talks/talks05-06/talks/duchin.html), scheduled [November 3,2005](https://people.reed.edu/~davidp/talks/talks05-06/talks.html). The actual abstract was read: it discusses comparing metrics on surfaces and flat structures. It does not contain the side-preserving 4-by-1 to2-by-2 optimization. That elementary Lipschitz calculation is developed and proved independently here. Do not attribute the activity or its answer to the talk, or call it the Teichmüller metric.

## Week 74: Baumslag–Solitar connection

Nicholas Touikan, [*HNN extensions and dual tracks*, §3.2.3](https://ntouikan.ext.unb.ca/MATH6022/IntroCGGT/html_output/section-15.html). Checked the presentation `BS(1,2)=<a,t | t^-1 a t=a^2>` and discussion of the distorted cyclic subgroup. The nonnegative-level elevator is an independently defined shortcut model, not a depiction of the full Cayley graph. The numerical optimality proofs are independent.

## Week 75: correction to the scope of the citation

Diana Davis, *Billiards, Surfaces, and Geometry*, [author-hosted book PDF](https://dianadavis.github.io/billiards-book.pdf). Checked Chapter 4, “Twisted cylinders,” printed 110–113/PDF 128–131, especially Problem 111 and Figure 83, printed 111/PDF 129. Problem 111 is **torus shear and reassembly respecting edge identifications**. It does not state the fixed-boundary annulus strand model or the formula `max(|a−b|−1,0)`. Credit it for related twist/shear and unfolded-cylinder inspiration only. The arc formula and fixed-endpoint hypotheses are an independently derived extension proved in `review-math.md`.

## Reproducibility and access notes

Web retrieval initially failed for the large Davis PDF and Reed abstract. Direct HTTPS retrieval succeeded; the exact cited pages and abstract were then read locally. The research PDFs were not copied into a source package. `source-fingerprints.json` records the actual retrieved bytes' hashes for precise version identification. The thinness, median, ends and related page references were checked against the author-hosted book version, not inferred from a table of contents.
