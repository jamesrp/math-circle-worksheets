# Week 93: scope, source evidence, and readiness

Status: new unpiloted investigation. Allocated by the batch coordinator after current-main inventory; reserved Weeks 85-91 untouched.

The kernel is a nonlinear area-preserving rectangle iteration. The arithmetic mean of the two sides becomes one new side; area conservation determines the other. The sides trap the unknown equal-area square side, and an exact gap identity proves improvement. This is an elementary square-root specialization of Newton iteration, presented through area and enclosure rather than tangents or long arithmetic.

## Corpus and overlap boundaries

Weeks 20 and its bonus already cover harmonic averaging, cycles, self-averaging convergence, and energy minimization. None is repeated. Week 48's inside/outside area covers and Week 51's guaranteed ranges supply meaningful connections: an exact range is now improved by a geometric transformation. Atlas GA-28/AP-06 use bisection and Newton's tangent iteration/cubic cycle; this packet does not repeat either method or example. The arithmetic/harmonic side update and missing-square area identity were not found in the inspected family indexes or source search. This is not a claim that the general root-finding field is new to the library.

## Primary mathematical context and independent derivation

Tobin A. Driscoll and Richard J. Braun, *Fundamentals of Numerical Computation*, §4.3, Newton's method, equations (4.3.2) and (4.3.7), Definition 4.3.2 and its assumptions:
https://fncbook.com/newton/

The authored online chapter was inspected October 17, 2026. It supplies the general Newton update and quadratic-convergence context. The specific rectangle construction, missing-square identity, nested side brackets, global convergence for positive starting sides, and printed rational instances are independently derived here. We do not attribute these classroom diagrams to the source or make historical claims about Babylonian knowledge. The algebraic specialization is x_next=(x+A/x)/2.

For positive a<=b, set m=(a+b)/2 and h=ab/m. Then h*m=ab, a<=h<=m<=b, and m-h=(b-a)^2/[2(a+b)]. For a<b the new gap is less than half the old gap. The common limiting side is sqrt(ab). The missing square in the m-by-m comparison has side (b-a)/2 and area m^2-ab. Exact rational computation can certify bounds; arbitrary rounded decimals cannot silently be treated as exact.

## Pedagogy and practical limits

*Math Circle by the Bay*, Preface printed viii-x (PDF9-11), was consulted through the manifest-verified authorized local original. Its support for deep connected themes, manipulatives, independent work, and flexible duration informs the design. The choice to allow an honest grades3-5 gate, rather than manufacture a K-1 version, is our readiness judgment. The book itself does not prescribe this activity.

The main route needs rectangular area, halves, division and interpreting supplied fractions. A grades2-3 child who understands area can do a concrete entry, but the adult must not perform every mathematical choice. Exact prepared side cards and an optional calculator keep transcription from dominating. Drawings with rational sides are conceptual unless explicitly calibrated for cutting. Children must first know why the rectangle is being changed: find a closer square shape of the same area and narrow a guaranteed side range. The later identity/proof is a return-visit route, not a requirement for every child in one hour. Material fit and classroom piloting are untested.
