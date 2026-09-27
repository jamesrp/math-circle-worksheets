# GA2 independent design and mathematics review

Reviewer: root/editor (not the author). Status: closed and approved for PDF production. All eight families, 50 student prompts and eight guide extensions checked.

The reviewer solved the student tasks before comparing every answer and extension. Independent exact arithmetic support is in `review-ga2-checks.py` and its results. The script is not a proof of continuum or infinite statements.

## Findings so far

- GA-09 prompt 6: clarify that zero initial velocity applies to the wave evolution only. Sent to author; closure pending final wording.
- Source locator refinements were shared before handoff: Boyd convolution is slides 3-29/3-30; Dandavati orthogonality is Theorem 3.3 and the basis theorem is 3.8. Author confirmed both from source. Final text will be checked.

## Independent mathematical checks

### GA-09: all six prompts and energy extension

Differentiating U_c gives U_tt=-c²U_c and U_xx=-U_c, so exactly c=±1 obey wave. The heat identity fails at (0,0) if c≠0 and at (π/2,0) if c=0. For V_a, V_t=-aV_a and V_tt=a²V_a, so heat requires a=1 and wave is impossible for real a. These checks account for every allowed parameter, not a numerical selection.

For W_b=sin(x)(cos(t)+b sin(t)), both second derivatives are -W_b and its initial time derivative is b sin(x). Fixed endpoints hold. Thus b=-1 matches the heat initial derivative but at x=t=π/2 the wave is -1 and the heat is positive. The traveling wave fails the fixed boundary. Mode k requires heat rate k² and wave angular frequency k. The two-mode heat solution cannot be a scalar multiple of its initial shape for t>0: x=π/2 fixes the scalar e^-t, and x=π/4 forces e^-4t=e^-t, impossible for t>0. The energy identity gives π(1+b²)/4; the heat square norm is πe^-2t/2. Integration-by-parts boundary terms vanish because the boundary is fixed for all times.

The stated calculus gate is necessary and honest. Graph movement is only an entry representation. Selected functions and boundary conditions are sufficient; the source is not used to claim arbitrary PDE uniqueness.

### GA-10: all eight prompts and period-six extension

Independently composed every L/R inverse word of lengths 1 through 8 (510 words), solved its affine fixed-point equation with rational arithmetic, checked every forward half-label and return, and compared the least orbit period with the least word period. In particular the three four-cycles are the disjoint orbits of 2/17, 2/15 and 6/17 listed in the key; LRRL starts at 4/15, LRLR at 2/5, LLLL at zero.

For the general argument, B_w is an affine self-map with slope ±2^-n. Its endpoint inequalities give a unique fixed point in [0,1]. Cancelling T with each inverse yields an n-step return and the required closed-half memberships. A periodic orbit cannot hit 1/2 or 1 because these reach zero and cannot return; hence each periodic state has an unambiguous label. That proves injectivity of the word encoding. A shorter repeated block has the same inverse fixed point; conversely a smaller orbit return repeats the labels. Division with remainder shows a least period divides any return time. Thus least word and orbit periods coincide. P_n=2^n-sum(P_d over proper divisors d) gives P_6=54 and nine cycles.

Four student pages are justified: experimentation, inverse design, inventory, and the completeness proof are distinct stages. The cycle inventory is withheld until after learner search. Fractions/algebra and the general proof gate are explicit. The source's slope-greater-than-two coding theorem is correctly distinguished from the independently proved slope-two periodic statement.

### GA-12: all six prompts and partial-sum-average extension

With n payments the geometric sum is 2-2^(1-n), so strict error <1/100 first occurs at n=8. The harmonic blocks ending at powers of two contribute at least 1/2, and the block containing 1/3 makes H_16>3 strict. For any budget B choose integer k>2(B-1); H_(2^k)≥1+k/2>B. At B=10, 2^19 is a sufficient index, explicitly not the first crossing.

Starting after any N, the blocks (N,2N], (2N,4N], etc. each contribute at least 1/2. This proves unbounded tails independently of a statement about the original full sum. The geometric tail has total 2^(1-N). Keeping harmonic indices 1,2,4,... instead yields total 2 by deleting infinitely many terms. Alternating ±1 payments have oscillating partial sums; their averages tend to 1/2 with exact odd/even formulas. Every infinite claim has a quantified finite construction or explicit remainder argument. The fraction gate and need for infinite quantifiers are stated; physical cards are labeled amounts rather than misleading reciprocal-length objects.

### GA-13: all six prompts and best-constant extension

At x=-1,0,1 the residual inequalities force |b|≤E and |1-b|≤E, so E≥1/2. The constant 1/2 attains the bound everywhere; equality forces b=1/2 and then a=0. On [h-r,h+r], subtract the already affine term and rescale z=(x-h)/r. This bijection of competitors yields the unique p=2hx-h²+r²/2 and E=r²/2. The secant lies r²/2 higher and has worst error r². Independently checked the alternating residual certificates on 45 integer-endpoint intervals using exact fractions. The polygonal target has extrema -2,4, so the unique best constant is 1 with error 3; the same extremal inequalities prove the general midpoint formula, including the constant-target case.

The objects specify vertical rather than perpendicular error and whole-interval rather than sampled accuracy. No calculus is needed for the complete proof. Student choice precedes the supplied three-point proof prompt. NIST's minimax/alternation discussion supplies context; the exact proof is independent.

## Primary-source audit in progress

Reopened all eight cited primary sources on 2026-09-25. Inspected NIST §3.11(i); Dandavati Theorems 3.3 and 3.8; Boyd printed slides 3-29/3-30; O'Neil Theorem 3, printed p.54; Lebl harmonic Example 2.5.11 and grouping pp.90-91. Also inspected Hunter §5.1, p.127, and §7.1, pp.211–212 (both initial conditions, fixed boundaries, energy integration); Teschl equation (11.13), p.297, and §§11.3–11.4, pp.298–301 (slope-two map versus greater-than-two symbolic coding); Stroock §1, p.2, periodic exponentials. Stroock supplies the Fourier framework, not the worksheet's alias classification or a sampling theorem proof.

### GA-14: all six prompts and irrational-time extension

Independently compared phases: at t=n/4, frequencies 1 and 5 differ by n whole turns. At t=1/8 their heights are opposite; t=1/12 gives equal heights but different arrows. For a nonnegative integer k, the n=1 quarter-time height requires k≡1 (mod 4), which also suffices at every scheduled time. Adding the eighth-time height retains exactly k≡1 (mod 8). At half-time sampling all integer frequencies have zero height; full arrows retain exactly odd frequencies. Thus the change of sensor gives a strictly stronger but still ambiguous record.

For any finite set of distinct measured times, the nonzero polynomial perturbation εΠ(t-t_j) vanishes precisely there. Adding it to any continuous signal gives another continuous signal agreeing at all measurements. For the explicitly narrower integer-frequency family, a full-arrow observation at √2 would require (k-1)√2 to be an integer, forcing k=1. The two results concern different candidate classes; no finite-precision claim is made. The proposed dials and timing strips are appropriate and the exact trigonometric gate is honest.

### GA-15: all six prompts and eight-pattern extension

Independently calculated the target's detector outputs 8,2,4,6 and weights 2,1/2,1,3/2; direct reconstruction gives 5,0,1,2. Every pair of distinct sign cards has dot product zero and every self dot product is 4. The key establishes spanning by direct symbolic reconstruction rather than merely counting cards; detector application establishes uniqueness. Column swaps negate S,D and row swaps negate R,D. The incomplete record fixes row totals 5 and 3, giving exactly (p,5-p,q,3-q) for p∈[0,5],q∈[0,3]. Two missing card readings always determine the picture; the key correctly allows exceptional boundary cases where one further reading already suffices.

For the three-bit extension, pair coordinates differing in a bit where the two characters differ; cross-products cancel and self-products sum to 8. The dual cancellation identity proves reconstruction with scale 1/8. The independent checker reconstructed 625 signed integer patterns and verified all four translations for each. Signed counters, fractional weights, explicit order and nonphysical negative corrections prevent the common modeling errors.

### GA-16: all six prompts and third-window extension

The 3-by-2 overlap is zero outside [0,5], equals t on [0,2], 2 on [2,3], and 5-t on [3,5]. The general expression max(0,min(a,b,t,a+b-t)) is symmetric. A requested support width S and height H can occur exactly when S≥2H>0, with ordered widths (H,S-H) and the reverse, coincident when S=2H. For S=7,H=2 these are (2,5),(5,2).

Solving 0≤t-x≤b gives the correct reflected/shifted interval [t-b,t]. Using [t,t+b] instead gives h(t+b), a left shift; endpoint inclusion changes measure-zero sets only. The two triangles and rectangle give area b²+b(a-b)=ab. The third unit convolution has pieces t²/2, -t²+3t-3/2, and (3-t)²/2, with zero outside [0,3]. Values and first derivatives agree at 0,1,2,3; second derivatives do not. Exact checks integrated 36 rational-width pairs and recovered the widths from support and peak. The full graph is proved, not inferred from samples. The core's supplied indicator-integral fact and the calculus extension are separated appropriately.

### GA-17: all six prompts and weighted-kernel extension

Independent integration gives (1-λ)m=F. For λ≠1 the only possible u=f+λF/(1-λ) has exactly the claimed mean, so the condition is sufficient and the solution unique. At λ=1, F≠0 is impossible; F=0 yields exactly all u=f+C. This checks all six displayed forcing/dial choices. The x² adjustment must be a=1/3. A nonzero change then destroys compatibility at exactly λ=1; at λ=1-δ the forcing shift ε instead gives the constant solution difference ε/δ. Hence maximum error ≤η is equivalent to |ε|≤δη, with the stated test errors 1/10 and 1.

For the xt kernel, the weighted moment satisfies (1-λ/3)m=M. The singular value is 3, not 1. When M=0 the complete solution family is f+Cx; otherwise there is no solution at 3. Away from 3 the candidate and weighted mean verify each other directly. The f=x and f=x-2/3 examples have the required incompatible/compatible moments. Functions are explicitly continuous and the integral gate is substantive. The general compact-operator theorem remains source context, while both particular kernels receive complete direct proofs.

## Design conclusion pending author-check handoff

All eight families, 50 student prompts, eight facilitator extensions and their full solutions have now been independently read and checked. Diagrams/workspace specifications provide the necessary objects and preserve learner choices. The new instances are distinct from the original ten; prior-use notes identify related mechanisms without presenting renamed copies as new activities. No open mathematical or pedagogical blocker was found. GA-09 prompt 6's zero-velocity ambiguity is repaired; the final source locator text for GA-15 and GA-16 is correct. Remaining review step: read/run the author's final check program and read the finished design note before closing this review and authorizing rendering.

## Final closure

Read the completed `ga2-design.md` and every branch of `ga2-checks.py`; ran the author checker successfully and the independently written `review-ga2-checks.py` also passes. The design note matches the final data, exact figure specifications and source-scope statements. All findings are closed. Approved for custom PDF production and the separate maker/independent rendered-page reviews.
