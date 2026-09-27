# Independent review of the three systems investigations

September 25, 2026. Reviewer: the decision/probability worksheet author, independently reviewing the other author's GA-11, AP-26 and AP-07. Read-only review of `systems-design.md`, every student page and keyed solution in `systems-data.json`, and `systems-checks.py`. All 32 student prompts and the facilitator extensions were checked. No classroom or PDF-layout result is implied by this mathematical/design review.

**Verdict:** mathematical content passes. These investigations preserve real reasoning at appropriately different prerequisite gates. One answer-discovery issue was sent to the author for repair: AP-07 C11's explicit “five or fewer” reveals the six-update minimum on the same page as the discovery question C10. Ask instead for exclusion of all schedules with fewer updates than the learner's proposed minimum; retain the five-factor specialization in the optional hint and solution. This is a pedagogical repair, not a false mathematical claim.

## Independent calculations and prompt coverage

### GA-11: G1–G8, all three student pages

- **G1:** additivity forces zero, negatives and integer values before the fraction calculation. The four verdicts are impossible, forced, impossible, forced. Three copies of the forged `21/10` output give `63/10`, contradicting the forced output 6 at input 2. Six copies of `5/6` force `15/6=5/2`. The two-route game supports a certificate instead of a guessed pattern.
- **G2–G3:** for arbitrary signed integer `m` and positive `n`, `n f(m/n)=3m`; the required zero/negative cases are included. The supplied false `−5` output at `−7/4` fails because four copies give `−20`, while additivity forces `−21`.
- **G4–G5:** the rational proof genuinely stops when no integer multiple of the input is an integer. Failure of that proof alone is correctly distinguished from construction of a counterexample. The enlarged domain is explicitly `Q+Q√2`, with unique coordinate pairs. The concrete pair sum is `(-2,5/2)`.
- **G6–G7:** I independently verified `f_A(a+b√2)=3a` and `f_B(a+b√2)=3a+5b` by expanding the sum of two arbitrary pairs. Both give `3r` for every rational `r` and differ at `√2`. Uniqueness of the representation follows from irrationality and is necessary for well-definedness. The output construction is not silently extended to all real inputs.
- **G8:** the numerical gap is `5−3(1.4142)=0.7574`, but one close pair does not prove discontinuity. A rational sequence approaching `√2` has outputs approaching `3√2`, different from 5. The key explicitly supplies the missing infinite limiting argument and specifies continuity in the stated domain.

The general classification `f_c(a+b√2)=3a+cb` also follows from rational homogeneity. The worksheets' symbolic/irrational-number gate is honest; this should not be sold as an elementary hands-on success merely because early fractions are accessible. No material answer leak: machine formulas remain withheld until invention, and the expanded domain and supplied uniqueness premise are clear.

### AP-26: D1–D12, all four student pages

- **D1–D3:** the delayed rule gives current positions `1,0,−1,−1,0,1,1,…`. Zero is a false finish. Current-state feedback instead reaches zero and stays there. For a delayed starting pair `(a,b)`, next current is zero exactly when `a=b`, but the following current is `−b`; only `(0,0)` is permanently parked.
- **D4–D6:** the two supplied current-equal states produce next currents 0 and 2. The complete six-pair orbit is `(1,1),(1,0),(0,−1),(−1,−1),(−1,0),(0,1)`. A repeated whole state implies repeated future because the rule is deterministic. Solving `T(a,b)=(c,d)` gives `(a,b)=(c−d,c)`, so distinct histories cannot merge.
- **D7–D8:** direct composition gives `T²(a,b)=(b−a,−a)` and `T³(a,b)=(-a,-b)`, hence `T⁶=I`. A nonzero real pair cannot have period 1, 2 or 3. The supplied divisibility argument properly rules out apparent shorter periods 4 or 5: every first-return period must divide 6. The zero pair is correctly exceptional.
- **D9:** with embedding `E(a,b)=(a−b/2, √3 b/2)`, the images of the independent unit directions under `T` are precisely their clockwise 60-degree rotations. Thus all nonzero orbits are regular hexagons in this embedding. The warning that a standard Cartesian pair plot need not be regular is important and correct. The `(1,2)` orbit and invariant `a²−ab+b²` check out.
- **D10–D11:** independent algebra for `H(a,b)=(b,b−a/2)` gives `H²=(b−a/2,(b−a)/2)`, `H³=((b−a)/2,−a/4)`, and `H⁴=(-a/4,-b/4)`. The printed exact fractions for `(1,1)` agree. Scaling each residue class modulo 4 proves convergence of all coordinates, not merely a sampled subsequence.
- **D12:** for `(1,1)`, every coordinate in the first four pair states has magnitude at most 1. At tick `4k+r`, the magnitude is therefore at most `4^(-k)`; `k=4` gives `1/256<1/100`. Every tick from 16 onward is covered. The answer is explicitly sufficient rather than earliest, as requested.

The facilitator-only general-gain root analysis is also correct, including endpoints and the double root at `k=1/4`. Signed arithmetic supports the concrete core, variables support the all-start proof, and fractions/algebra support the optional contraction page. The blank state graph preserves discovery; the triangular grid is a meaningful optional new representation.

### AP-07: C1–C12, all four student pages

- **C1–C3:** derivative and initial value verify `8e^(-t)`. A tangent step gives `(1−h)y`; the listed endpoints `(1/2,4),(3/2,−4),(3,−16)` are correct. The distinction between temperature relative to room and absolute temperature is explicit.
- **C4–C6:** for multiplier `1−h`, the five cases partition all `h>0`, with zero at `h=1` and bounded nondecaying alternation at `h=2` handled separately. Taking `h=1` gives a 100% relative error at the same elapsed time `t=1` despite settling. Replacing the rate by 2 moves the settling threshold to `h<1` and strict positivity to `h<1/2`.
- **C7–C8:** at elapsed time 1, the two-step value is `8h(1−h)=2−8(h−1/2)^2`. The maximum 2 is uniquely reached at equal halves and lies below `8/e`; that last comparison is what turns maximizing the estimate into minimizing error. The relative error is `1−e/4`, about 32.043%.
- **C9:** splitting `H=u+v` changes the multiplier from `1−H` to `1−H+uv`. Positivity and the exact exponential upper bound are needed for the accuracy conclusion, and both are supplied. This is appropriately restricted to the scalar equation and the stated interval.
- **C10–C11:** independently, any schedule with at most five positive durations summing to 1 can be padded to five factors `1−h_i` by zero-duration placeholders. The factors are nonnegative with sum 4, so the supplied product theorem gives `Y≤8(4/5)^5=2.62144`. The permitted lower endpoint is `7.2/e≈2.64873`, so no such schedule succeeds. Six equal durations give `8(5/6)^6≈2.67918` and about 8.9653% error. The mathematical lower bound handles *unequal* schedules and fewer than five steps, rather than only checking a table of equal steps. I also inspected the script's rational exponential-tail bounds; they genuinely certify the strict threshold rather than assuming rounded decimal comparisons.
- **C12:** backward Euler gives multiplier `1/(1+h)`, positive and decaying for every fixed `h>0`. Its one-step value 4 at `t=1` nevertheless has relative error `e/2−1≈35.914%`, so qualitative improvement does not meet the numerical accuracy goal.

The product-maximization proof in the guide correctly handles zero-factor boundary points via the positive all-equal competitor. The general-rate extension needs the stated nonnegative-factor restriction and includes it. Calculus and exponential functions are proper prerequisites for the full worksheet. The low-gate recurrence-only activity has not been misleadingly promoted as equivalent.

## Layout and trial cautions for the later PDF review

- AP-26 pages 3–4 and AP-07 pages 3–4 carry substantial proofs. Retain the optional/later-session labels and actual reasoning space; do not compress them into small-font answer boxes.
- GA-11's argument is excellent for a symbolic group but conditional as a general elementary-circle worksheet. Keep that assessment in the delivered guide.
- For the triangular grid, preserve the nonorthogonal axis directions precisely. For cooling, label actual elapsed time and preserve the large negative vertical range needed by the `h=3` tangent.
- The design provides a source-specific connection and does not claim exact problems copied from sources. The review checked the internally supplied mathematics, not a fresh full read of each external source or proof of classroom engagement.

## Closure

The systems author changed C11 to ask for exclusion of schedules with fewer updates than the learner's proposed minimum. The five-factor specialization remains only in staged hints and facilitator solutions. I checked the updated wording; the answer-leak finding is closed. All mathematical/design findings are now closed; PDF rendering still needs its own review.
