# GA2 design handoff

2026-09-25. Eight families: GA-09, GA-10, GA-12–17. The complete data contain **25 staged student pages, 50 keyed prompts and eight solved guide extensions**. Every page has an explicit prerequisite line, full prompt solutions and hints; every family has an index gate, exact figure data, materials, timing suggestions, sources and a candid assessment. These are unpiloted designs. The originals and accepted ten trials remain unchanged. Independent design review is now closed in `review-ga2-design.md`; production evidence is recorded separately in `ga2-maker-qa.md`.

The work follows AUTHOR-BRIEF.md, NEXT-BATCH-NOTES.md, the root README, the trial design brief/review/assessment and the source-supported teaching notes. I reread *Math Circle by the Bay*, printed preface pp. viii–x: the source supports deep themes, manipulatives, independent attempts, practicing explanations and flexible pace. The concrete investigations, staging, timings and print choices below are editorial designs, not lessons claimed to appear in that book. The Rozhkovskaya notes also motivate keeping copying and arithmetic purposeful. Graph play does not remove calculus or algebra gates.

## GA-09 — choose a shape, then choose its future

The original traveling/fading comparison becomes a design and discrimination problem. Learners choose speeds and damping rates, then classify them by actual partial derivatives. Moving to fixed endpoints exposes why the traveling profile fails a different boundary problem. The family W_b=sin x(cos t+b sin t) lets learners create different wave futures sharing one initial shape. They then match the heat solution's initial velocity too and still exhibit different futures: the evolution law is essential. The last page derives the k² heat rate and k wave frequency, then proves a two-mode heat profile cannot remain a scalar multiple of its initial shape.

**Calculus is the core.** A graph transparency is a representation, not a replacement for partial differentiation. The energy extension uses integrals and integration by parts. Hunter's heat/wave equations, two initial conditions and fixed-end energy context were reopened; every selected formula is directly verified here. No general PDE completeness or uniqueness theorem is inferred from a few modes. The independent reviewer requested that Q6 attach zero initial velocity specifically to the wave, and the text now does so explicitly.

Advanced/specialist, with a worthwhile stop after designing and separating the fixed-end futures. Every boundary restriction remains explicit. The renderer must keep the whole-line and fixed-interval axes distinct and leave later profiles for the learner to draw.

## GA-10 — program the folded interval

This uses the actual slope-two tent map, with current-state labels L on [0,1/2) and R on [1/2,1]. The learner chooses a four-letter word before receiving the inverse cards. Backward affine composition constructs its candidate, and forward checking tests the labels and return. LRRL gives the new exact cycle 4/15,8/15,14/15,2/15; LRLR and LLLL reveal why word length is not necessarily least period.

A complete four-cycle inventory follows: three cycles, with representatives of denominators 17,15,17. This is justified rather than merely enumerated. Every inverse composition is an affine self-map with slope ±2^(−n), hence has one fixed point in [0,1]. Cancelling inverse branches proves the return, and the chain 1/2→1→0 excludes all periodic boundary ambiguity. Unique half itineraries distinguish the 2^n points. Repetition of a shorter inverse word proves that least word and orbit periods agree. The extension derives the divisor recurrence, giving 54 points in nine least-period-six cycles.

Fractions and affine composition are real gates. Teschl's equation (11.13), printed p.297, was reopened. The nearby symbolic-conjugacy theorem concerns μ>2; the data explicitly do not apply that theorem to μ=2. Our exact periodic-word argument covers the needed slope-two statement independently. No visual irregularity is called a proof of chaos.

Promising for an algebra-ready group. The four pages can span more than one meeting. Cycle workspace must be open rather than preallocating exactly three answer diagrams. Worked cycles in figure data are guide-only.

## GA-12 — can tiny payments break a budget?

Learners choose two target budgets and discover the different obligations of proving a finite success and proving a permanent upper bound. The geometric formula uses the number of payments n consistently: G_n=2−2^(1−n), with eight payments first bringing the gap below 1/100. Ungrouped harmonic cards invite the grouping rather than displaying it. The H_16 argument is strictly greater than 3, not only greater than or equal to it.

The central payoff is a rule defeating every finite harmonic budget. Tail blocks N+1 through 2N show that ignoring an arbitrary finite prefix cannot save a budget, whereas retaining only powers-of-two indices can. That distinction makes the infinite reasoning concrete without requiring huge fraction sums. The guide extension carefully distinguishes ordinary partial sums of 1−1+… from their convergent averages.

The real gate is fractions, doubling and quantified unboundedness. Lebl's geometric remainder and harmonic proof in §2.5 were reopened; the target, tail and deletion arguments are fully supplied. GA-03's cover budgets and GA-29's Cantor lengths are cross-linked, rather than repeated as the same geometric exercise.

First-pilot candidate for fraction-ready learners. Provide loose cards and open grouping space; do not prearrange the dyadic proof groups. Physical strip resolution is not treated as a limit on the mathematical sequence.

## GA-13 — how narrow can the error band be?

A learner places any affine line and a challenger chooses any position to inspect. Endpoint interpolation is a legitimate early trial that loses at the center. Only later do the three-point residual inequalities remove the slope and force E≥1/2. The constant 1/2 attains the bound on the entire interval. Equality forces both intercept and slope, so uniqueness is established separately from attainment.

The last page lets learners move and stretch the interval to [h−r,h+r], r>0. Subtracting its affine part and rescaling transfers both optimality and uniqueness, yielding p=2hx−h²+r²/2 and E=r²/2. The [1,3] check gives 4x−7/2. Comparing the endpoint secant shows exactly why centering its residual range halves the worst error. The polygonal guide extension solves a different best-constant problem and does not claim a best tilted line.

No calculus is needed; inequalities and affine algebra are genuine gates. NIST DLMF §3.11(i) provides the minimax/alternation context, but the chosen proof is elementary and does not invoke the general theorem. Vertical error, total band thickness and average error remain distinct.

Promising with algebra. A supplied parabola and blank candidate-line workspace support search, while the initial graph must not reveal the optimal horizontal line or its alternating extrema.

## GA-14 — choose a photograph that reveals the motion

Two rotating arrows with frequencies 1 and 5 give identical full positions and heights at every quarter-second sample. The learner chooses an additional height observation. The key gives both a success (1/8) and a tempting interior failure (1/12), where different arrow positions have equal heights. Expanding the candidate class exposes the limit of that success: all k≡1 mod 4 match the original record, and all k≡1 mod 8 survive the extra one-eighth-second height.

Changing the schedule to half-seconds makes the lost information even clearer: every nonnegative integer frequency has the same zero-height record, but only odd frequencies match the full-arrow record. Finally a polynomial perturbation constructs a different continuous signal matching any finite observation list. The optional irrational-time full-arrow test identifies frequency 1 only within the stated integer-frequency class and exact ideal model.

Turns and fractions support entry; modular periodicity and algebra support the complete conclusions. Stroock's §1 periodic exponentials were reopened as source context; no general sampling theorem is borrowed or asserted. Candidate classes are stated before every claim. The irrational-time result is explicitly not a finite-precision promise.

Promising with specific gates. The renderer supplies blank dials and records rather than drawing the coinciding arrows or choosing the successful extra time for the learner.

## GA-15 — decode a picture from four sign patterns

The actual four Walsh characters become 2-by-2 sign cards with a fixed coordinate order. Learners choose hidden weights, build a picture and challenge a partner to decode it. The new supplied target (5,0,1,2) requires weights (2,1/2,1,3/2), making the real-coefficient convention consequential. Detector invention grows into orthogonality, the division by four, explicit reconstruction for every array and uniqueness.

The final page predicts row/column swaps by acting on the cards, then asks what is lost when only two detectors are retained. All nonnegative arrays with total 8 and row contrast 2 are classified as (p,5−p,q,3−q), with 0≤p≤5 and 0≤q≤3. This is an actual two-parameter ambiguity rather than one pair of anecdotes. The extension constructs eight binary-character patterns and proves their /8 normalization by pairing cancellations.

Signed arithmetic, halves and weighted sums are core; the general basis interpretation needs linear algebra reasoning. Dandavati's Definition 3.1, Theorems 3.3 and 3.8 on printed pp.5–7 were reopened. Our unnormalized dot-product convention and reconstruction scaling are derived directly; the paper's general reconstruction display is not copied as a normalization authority.

First-pilot candidate for a signed-number group. Negative contributions are corrections, not negative physical illumination. Sign cards need symbols as well as colors, and the real-valued family must not be made into a finite answer-slot inventory.

## GA-16 — predict what the sliding window draws

The windows are now length 3 and 2, with the right endpoint of the moving interval labeled t. Learners choose positions and predict the entire graph before deriving it from endpoint intersections. General widths reveal commutativity geometrically, and the inverse-design problem asks which chosen support width S and peak H can occur. The full answer S≥2H>0, widths H and S−H in either order, includes the triangular equality case and precisely describes what the graph cannot distinguish.

Only after the geometry does the page identify the overlap as ∫f(x)g(t−x)dx. Shifting the opposite window endpoint while retaining the old parameter is explicitly diagnosed as a translated graph. Open versus closed indicator endpoints are distinguished from their equal integrals. Graph area gives ab directly. The third-unit-window extension derives all quadratic pieces and proves the new graph is C¹ but not C².

The geometric core uses lengths and piecewise reasoning; the indicator-integral interpretation is honestly supplied. Calculus is required for the third convolution. Boyd's convolution material is on slides **3–29 and 3–30**, correcting the broader original locator. The causal functions are extended by zero to make the real-line formula precise.

First-pilot candidate for the core. Print two usable strips at a common scale and leave the graph empty. Avoid premarking the four true breakpoints before prediction.

## GA-17 — a graph feeds back its own mean

Learners choose both a forcing graph and a feedback dial. The two supplied forcings x² and 2x−1 produce unique, absent and nonunique cases. Introducing the unknown integral reduces the whole equation to (1−λ)m=F. The guide proves necessity, reconstructs each candidate to prove sufficiency, and proves uniqueness for λ≠1. The critical value **λ=1** is retained in the original normalization, with the full one-parameter family when F=0.

A constant adjustment x²−a lets the learner repair compatibility at λ=1. Nearby λ=1−δ exposes a different phenomenon: a forcing perturbation ε changes the entire solution by ε/δ. This supplies an exact error-tolerance design rather than conflating large sensitivity with nonexistence. The xt-kernel extension derives a new moment equation and critical λ=3, including both critical forcing outcomes and all solutions.

Definite integrals are a core prerequisite, not an optional interpretation of a finite averaging game. O'Neil's Fredholm alternative, printed p.54/PDF p.55, was reopened; it gives context only. Both rank-one kernels are completely solved directly for continuous real forcings.

Advanced/specialist, with a satisfying scalar reduction and compatibility classification. The renderer should give forcing graphs and empty shifted-graph space at the launch, without displaying the final three-case classification prematurely.

## Verification and handoff

`ga2-checks.py` passes. It checks formal sine/cosine and exponential derivative identities; all 2,046 inverse words of lengths 1–10 with exact rational forward itineraries and least periods; strict harmonic blocks and finite geometric gaps; exact extrema for 25 moved/scaled minimax intervals and 625 competitors; 513 integer-frequency alias tests plus polynomial record perturbation; 625 Walsh arrays and their translations plus the eight-character Gram matrix; 64 window pairs over exact displacement grids and the complete third-window join calculations; and polynomial coefficient identities for 42 forcing/dial pairs plus 80 sensitivity cases. Schema and selected printed-key regressions also pass.

Each result states its proof scope. Finite audits support, but do not replace, the general all-word, all-budget, all-line, all-frequency, all-array, all-width and all-continuous-forcing arguments written in the keys. This note records the design-stage reasoning. Independent design review subsequently closed; the separate maker record documents the generated previews and visual coverage. Independent PDF review remains a separate release gate. No additional artifact marker was run.
