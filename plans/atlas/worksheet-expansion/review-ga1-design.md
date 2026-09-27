# Independent design review: GA1

Reviewer: AP1 author. Reviewed the eight families in `ga1-data.json`, all 55 student prompts, all 13 guide extensions, figures, source records, `ga1-design.md`, and the full author check program. I first read the student tasks without their solutions and solved the instances, then compared the keys. `review-ga1-checks.py` supplies separately written calculations, without importing the author checker; its eight-family result file passes. Finite tests support instances; the arguments below establish the universal claims.

This is design review, not PDF or classroom review. Exact display, usable workspace and staging must be checked again in the actual printed pages.

## Findings requiring closure

1. **GA-04 page 1 intro:** define “legal root” before asking the learner to find one: doubling its angle must give the target angle modulo a full turn. The existing task mentions testing by doubling, but does not explicitly state that this is the legal-move rule.
2. **GA-06 first guide extension:** replace “supplied definition” with “supplied necessary condition” for a smooth complex curve having a disc neighborhood. The topological property is necessary and supports this obstruction; by itself it does not define complex smoothness. The actual punctured-neighborhood proof is correct.

No numerical or universal-proof errors found. These two small wording fixes are sufficient at design stage; closure is recorded below after rereading the owner's edits.

## GA-01 — orientation, not one marker

Checked tasks 1–7 and the commuting-power extension. Direct coordinate turns give XY: red −z, blue −y; YX: red +y, blue +x. Following YXY⁻ returns blue while sending red to +y. An independent search of all words of lengths 1, 2 and 3 finds no earlier winner and eight length-three winners. The key's case split is stronger than a search: same-axis inverse pairs are identity, same-sign pairs reverse blue, and mixed-axis pairs leave blue horizontal. Two nonparallel directions determine a proper rotation; merely tracking blue does not.

For flat half-turns at 0 and 2, the two orders send 0 to +4 and −4. Same-center planar turns commute because signed angles add. Among the 16 pairs of powers, the commuting pairs are exactly those with either exponent zero plus (2,2), eight distinct pairs. The author's matrices agree with the explicit room-axis cycles.

The supplied direction cycles, reset and room-fixed axes are adequate. The renderer must make those fixed axes unmistakable; a cube-attached axis diagram would change the problem. The shortest hidden twist is a substantial new payoff beyond Week 3 composition. This is a strong first-pilot candidate after a physical rehearsal.

## GA-02 — the exchange earns the match

Checked tasks 1–7 and bisection extension. Direct interpolation of the specified height cycle 0,5,1,4,2,3 gives first-half difference values −4,3,−2,4. Its three affine roots are x=4/7,8/5,7/3 with common heights 20/7,13/5,2. Nonzero slopes and strictly interior roots make the list exhaustive. Opposite post checks alone miss all three.

The general proof tracks a continuous difference that changes sign after a half-turn, because the markers exchange starting heights. The half-open jump example gives unequal antipodal values at every point, including both seam locations. The straight-trail example has constant difference 1/2 and lacks the exchange. After k exact-sign bisections, bracket width is 1/(6·2^k) turn and midpoint error at most half that width. No uniqueness of a zero is assumed in the general bracket statement.

The repeated profile, labeled spacings and exact three-spacing marker span are sufficient. The drawing must include the seam ramp and continuation. Continuity is an actual reasoning gate; fractional interpolation is optional. The attempted fence design gives meaningful learner agency, and no early equality points are printed. Strong first-pilot candidate.

## GA-03 — dense points, arbitrarily cheap covers

Checked tasks 1–7 and both extensions. Five widths 1/1000 cost 1/200. The infinite rule w_n=1/(100·2^(n+1)) for n≥1 sums to 1/200; after N terms its tail is 1/(200·2^N). For a budget B, widths B/2^(n+1) total B/2. Positive width covers the center regardless of overlap or ordering. Equal positive widths cost Nw after N requests and cannot meet a finite assigned-cost budget forever. This is correctly distinguished from union length.

Independent row enumeration gives indices 8,32,5188 for 2/3,4/7,37/101. The general index formula follows by summing row lengths 2 through q, then adding p+1. Every rational therefore occurs at a finite position, including unreduced repetitions. The supplied interval-cover theorem rules out covering all of [0,1] below total length 1; every omitted point inside [0,1] must be irrational. The density proof uses q(b−a)>1 and p=floor(qa)+1, with strict inequalities at both ends.

The second extension correctly invokes the separately proved GA-29 Cantor construction to show uncountable zero-measure sets exist. The present worksheet does not claim its countable-set argument proves that result.

Figures are appropriate schematic records; tiny widths must be explicitly not to scale. Infinite series and universal nth-point reasoning are real core gates. The supplied cover lower bound is clearly labeled rather than disguised as an experiment. Rich but advanced relative to ordinary elementary fraction work.

## GA-04 — a root cannot switch invisibly

Checked tasks 1–6 and principal-angle extension. At target θ, the two roots are θ/2 and θ/2+180°. A chosen continuous running angle ending at 360° ends its starting root at 180°, irrespective of reversals. The key's quotient proof is sound: two legal choices have continuous quotient in {+1,−1}, hence constant on the route interval. It also handles the alternative initial choice. A global continuous single-valued root contradicts the end reversal at the same target point.

Net k turns yield root angle 180°k, restoring it exactly for even k, including negative and zero k. Triple roots of target 120° are 40°,160°,280°, and three target circuits first restore the chosen root. For mth roots, return is equivalent to m dividing k. The principal-angle rule is single-valued everywhere but discontinuous at its cut, and is continuous after deleting that target point.

The mathematical rule should be stated explicitly in the launch (finding 1). The paired blank dials and running-angle strip support actual choices without supplying the answer. Continuity and angle arithmetic are the honest gate; complex notation is only a compact proof language. No arbitrary-loop lifting theorem is smuggled in because routes are supplied by running angles.

## GA-05 — maximum propagation beyond the path

Checked tasks 1–7 and both extensions. Path values are 3,6,9. In the shortcut graph, b=(a+c)/2; symmetry or equation subtraction gives a+c=12, then a=9/2 and c=15/2. Raising the right boundary to 16 gives 6,8,10 and changes 3/2,2,5/2. Direct substitution verifies each average against the actual five-edge graph.

A maximum above all boundary values forces every neighbor of its interior maximizer to share that maximum. A path to a boundary square supplies the contradiction. Finiteness and one boundary node in every component are essential and explicitly present. Negating values supplies the lower bound. Two unconstrained connected circles may both carry 100, showing why the boundary condition matters.

The difference of two assignments obeys the same averaging rule with zero boundary, proving at most one solution. Boundary differences in [0,4] give the perturbation bound by the same argument. The text does not infer existence from uniqueness. The strict-increase extension correctly includes the fixed-square separation example: an intervening fixed boundary can prevent influence even in a connected whole graph.

The path overlaps accepted AP-01 and is honestly labeled a reset. The new network-design challenge, component condition, uniqueness and sensitivity proof supply substantial new work. Diagram coordinates create no ambiguous crossing; fixed squares versus empty averaging circles must remain visible. Strong first-pilot candidate for average-ready learners, with simultaneous consistency rehearsed first.

## GA-06 — two complex coordinates and two branches

Checked tasks 1–6 and both extensions. For z=1+i, w=−1+i or 1−i; for z=2−i, w=1+2i or −1−2i. Factorization into (w−iz)(w+iz) and absence of zero divisors give both complete branches, meeting only at the origin. All-real coordinates give only the origin; real z with complex w gives the two real-parameter slices.

Away from the origin z is nonzero, so the continuous ratio w/z belongs to {+i,−i}; it cannot change along a path. The supplied two-piece route through the origin has matching endpoints and satisfies the equation on both halves.

The invertible coordinates give uv=z²+w², w=(u+v)/2, z=(v−u)/(2i). For level 1, u≠0 and v=1/u give the complete set. The u=2 example is (3i/4,5/4); u=i gives (−1,0). On u=e^(iθ), 0≤θ≤π, the inverse gives (z,w)=(−sinθ,cosθ), correctly joining (0,1) to (0,−1). For nonzero constant c the same inverse with v=c/u gives genuine holomorphic charts.

The punctured-neighborhood obstruction is correct: every relative neighborhood of the origin meets both branches, and removing the origin separates them, unlike a punctured disc. Its disc property should be labeled necessary rather than a full definition (finding 2).

The paired Argand grids are adequate and carefully avoid portraying all of C² as one planar X. Complex arithmetic and factorization remain hard prerequisites. This is a specialist investigation, but its representational surprise and exact parameterization are substantial; no inappropriate elementary proxy is substituted.

## GA-07 — chosen tests, deceptive fit, identity

Checked tasks 1–6 and both extensions. For the odd cubic, 0°/180° supply a+b=1, 60°/120° supply a+4b=−8, and 90° supplies no constraint. Thus exactly a pair from the two informative classes determines a=4,b=−3. A finite test can reject a candidate but cannot by itself justify all inputs.

The supplied symmetric cosine identity yields the recurrence and its induction. The rival added polynomial vanishes at all five printed inputs 0,±1,±1/2, but at √2/2 contributes −√2/16. Both composition orders expand to 32x⁶−48x⁴+18x²−1. The general multiplication-of-angles argument proves T_m∘T_n=T_(mn) on [−1,1]; the supplied polynomial root bound extends the identity to every real (indeed complex) input. It also covers m=0 or n=0. Independent rational evaluations outside and inside the cosine interval corroborate the displayed expansion.

The cubic zeros are 0,±√3/2. The comparison with cos(3x) fails already at x=0, clearly distinguishing coordinate from angle. Figures supply genuinely useful unit-circle rays but must not preprint T3. Trigonometry and polynomial algebra are genuine gates. Test selection and a false fit add a useful proof payoff beyond formula derivation.

## GA-08 — full forward classification, with calculus retained

Checked tasks 1–9 and both extensions. Substituting at² yields a=√a, hence a=0 or 1. A positive a in at⁴ would require a fixed t=1/(2√a) at every positive time, impossible. These give the distinct solutions zero and t². A delayed square is correct on each open piece; its join quotients are 0 from the left and h from the right, so it is differentiable at c with derivative zero. The unpatched square (t−c)² both violates y(0)=0 and has a negative derivative before c despite positive required rate.

For every nonnegative solution, y′≥0 gives monotonicity. Its zero set is all time or [0,c]; continuity supplies the endpoint. On the positive tail, v=√y has derivative 1, and continuity at c gives v=t−c. This proves the entire claimed classification; no division at zero occurs. The forever-zero case and immediate departure c=0 are included. Every classified candidate was already verified at its join.

For y′=y, the integrating factor has zero derivative and initial value zero, proving uniqueness directly. The square-root Lipschitz quotient 2/√h is unbounded. This does not logically imply nonuniqueness: the negative-sign equation is nonincreasing, and nonnegativity from zero forces the sole forward solution zero. The restriction to a half-line and forward time is explicit. The source's open-domain theorem is not applied without its hypotheses.

The power extension has exponent β=1/(1−α)>1 and coefficient (1−α)^β; both differential equation and zero join derivative check. The blow-up extension distinguishes local uniqueness from global existence with 1/(1−t) on the maximal forward interval from zero, [0,1).

Every page prominently requires calculus. Blank axes and join quotient workspaces support choosing c and explaining the critical point; the satisfying stop genuinely verifies a differential equation. This is the user-requested hard gate, not a slopes-only activity. The full classification is an excellent advanced continuation.

## Source and production scope

All eight records include actual source locators and identify which results are borrowed versus independently proved. The source connection is appropriately narrower than the activity in GA-05 (continuous theorem versus finite graph analogue) and GA-08 (local theorem versus direct half-line calculation). I checked the finite instances and universal arguments themselves; I did not repeat every source's external page retrieval. The author's recorded source inspection remains source-provenance evidence.

The data anticipates correct diagrams, delayed answers and sufficient reasoning space. Actual fit and physical usability cannot be certified until rendering. Staged pages should not be forced into one hour or shrunk to achieve their proposed count.

## Closure

Both findings are closed. I reread the updated GA-04 launch: legality is now explicitly doubling modulo a full turn. I reread the GA-06 family extension gate and first extension prompt/gate: all call the disc-neighborhood property a supplied necessary condition. The mathematical keys remain correct. GA1 is clear to proceed to rendering; PDF review remains required.
