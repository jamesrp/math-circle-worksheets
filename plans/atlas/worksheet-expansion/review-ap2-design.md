# AP2 independent mathematical and design review

Reviewer: expand_ad1. Date: 2026-09-25. **Closed: no remaining design findings. Approved for production, subject to independent PDF review.** No AP2 author files were edited by this reviewer.

I read the eight families' student prompts before comparing their solutions, independently derived all 48 prompts and eight extensions, then read every key, hint, prerequisite, source field, figure specification and the author's checker. All numerical results and general proof arguments agree. I reopened all eight primary sources at the relevant passages, rather than relying only on the atlas or author note.

The independent `review-ap2-checks.py` and `review-ap2-checks-results.json` pass. They provide exact finite/identity corroboration, including a density-matrix calculation independent of the author's probability-tree implementation, polynomial transfer matrices independent of the Ising link-encoding proof, and enumeration of all equally likely sampler ticket proposals. Neither author's nor reviewer's finite tests are substitutes for the general proofs summarized below.

## Findings and closure

Three narrow repairs were requested and independently reread after the owner applied them:

1. **AP-16 facilitator launch:** replaced “54-ticket bag” with “large weighted ticket bag.” This prevents the spoken launch from disclosing the total weight asked later. Closed.
2. **AP-17 prompt 1:** “nonzero turn point” now explicitly means `T=(t,d) with d≠0`. A nonzero event alone did not imply a spatial excursion. The later symmetric-route question still deliberately allows d=0 and treats its endpoint value. Closed.
3. **AP-13 prompt 4 key:** the complete dimming set now includes every translate by 2πk, k∈Z, as required by the real-phase domain. The displayed representative interval was already correct. Closed.

No erroneous mathematical constants, unsupported physical laws, missing general proofs or source-locator corrections remain. Rendering must preserve the explicit model changes, gates and unknown answer counts.

## Independent derivations, scope and usability

### AP-11 — flow maps

Prompts 1–2: the inlet rate is 6·2=12. The sole conserving narrow mean is 4; any different proposed w changes the intervening inventory at 12−3w. The two-patch family is u+2v=12, with nonnegative interval 0≤v≤6. Speeds (2,5) have weighted mean 4 but ordinary average 7/2. This is a conservation check on section data, not a solution of viscous fluid equations.

Prompts 3–4: separate outlets satisfy 2u+v=12, 0≤u≤6. Choices (2,8) and (5,2) give opposite speed rankings; the endpoints yield max u=6 and max v=12. Observing u=4 gives v=4 and rates 8,4, but the ledger contains no pressure variable or constitutive law.

Prompts 5–6: tank volume 8+3t reaches capacity 20 at t=4; level rises at 3/4. Overflow starts after capacity is reached. This supplies a storage alternative to inferring a leak from two unequal rates. For the gas, mass balance is 12=9ρ, so ρ=4/3. The uniform section densities and changed compressibility assumption are explicit.

Extension: integrating the continuity equation gives dM/dt=−∮ρu·n. For constant density and u=(ax,by), divergence is a+b and net rectangle flux is 2(a+b). Thus precisely b=−a passes. The rectangle is a permeable control region, not implicitly a solid-walled tube.

The exact tube, patches, branch and tank data suffice for custom diagrams. Units and mean normal velocity are genuine prerequisites. The new destination is complete nonuniqueness and model discrimination; graph traversal is correctly recorded as a different prior activity. Preparation is modest and the vector-calculus continuation is honestly separated.

### AP-12 — fastest crossing

Prompts 1–2: direct AB meets the boundary at x=4. Its lengths are 4√2 and 3√2, time 25√2/12 and total distance 7√2. At x=3, both lengths are five, time 35/12 and distance ten. Since 1225<1250, the longer spatial route is faster. Differentiating T(x)=√(x²+16)/3+√((7−x)²+9)/4 gives T′(3)=0.

Prompt 3: T″=16/[3(x²+16)^(3/2)]+9/[4((7−x)²+9)^(3/2)] is strictly positive on the whole real line. Therefore the stationary point is the unique global minimizer, including all outside crossings. As an independent alternative certificate, Cauchy gives L1≥(3x+16)/5 and L2≥(4(7−x)+9)/5; after dividing by 3 and 4 the x terms cancel and give T≥35/12, with equality only at x=3. Angles from the vertical normal have sines 3/5 and 4/5; their speed-divided values agree at 1/5.

Prompts 4–6: T increases throughout gate [4,6], so its boundary winner is x=4 with positive derivative 1/(12√2). For target 0<s<7, solving stationarity gives w=3(7−s)√(s²+16)/(s√((7−s)²+9)). It is finite/positive and the same convexity proof certifies its unique optimum. In particular s=3 gives w=4 and s=4 gives w=3. The derivative signs at 0 and 7 exclude those endpoints for finite positive w. Increasing w raises the derivative at the old root, so the new root moves left.

Extension: positive heights and speeds make T″>0 generally, with T′(0)<0<T′(d). The constrained optimum is the unrestricted root clipped to [L,U], including a singleton gate. These statements cover the exact one-crossing, two-straight-segment route class; they do not claim every optical stationary path is a minimum.

The coordinate/scaled diagrams, unfilled crossing marker and generic normal-angle figure are sufficient. Calculus is the core rather than an optional afterthought. The inverse speed design is substantive and distinct from prior equal-speed reflection work.

### AP-13 — coherent phase retrieval

Prompts 1–2: the two initial sums are 3 sin t and sin t, with brightness 9 and 1 compared with 4 for A alone. B=−2 sin t cancels pointwise; for positive amplitude it is the only cancellation up to phase periods. A one-detector scalar model does not imply disappearance of energy everywhere.

Prompts 3–4: P=2+cosφ and Q=sinφ, so the supplied orthogonal period averages yield I=P²+Q²=5+4cosφ. Cosine's complete range proves every I∈[1,9] is attained. Each interior value has two representatives in [0,2π); the cosine is recovered but the sine sign is generally lost. Dimming requires cosφ<−1/4, giving the stated open interval and, after the repair, all 2π translates.

Prompts 5–6: I=5 means E=2 sin t±cos t. Adding cos t gives brightness 8 or 4, while adding sin t gives 10 in both cases. Generally J−I=1+2sinφ, so cosine=(I−5)/4 and sine=(J−I−1)/2. The supplied observations decode to (3/5,4/5). A pair is compatible exactly when these coordinates lie on the unit circle; (5,6) would give (0,0), hence fails. The reconstruction is unique modulo a period.

Extension: direct double-angle integration gives averages 1/2,1/2,0. Uniform phase across stable full-period blocks averages 5+4cosφ to 5. This is a different stipulated observation regime, not a value assigned to every coherent phase.

Common waveform scales, signed amplitudes, stable frequency/polarization and unchanged reference normalization must remain visible. The proposed coefficient plane and blank wave sum are sufficient. Trigonometry is an honest core gate, with integration separate. Prior aliasing/signal-basis work is distinguished from the new controlled-reference inverse problem.

### AP-14 — heat engines and entropy

Prompts 1–2: energy balance alone allows every nonnegative split of 12. Entropy requires Qc≥6; the advertised (8,4) gives −1/150. Maximum permitted work is six. In general W≤Qh(1−Tc/Th), and equal positive reservoir temperatures force W=0 under the stipulated nonnegative-output convention. The second law is explicitly supplied; an energy ledger does not derive it.

Prompts 3–4: reversible middle choices 400 and 450 give (Qm,W1,W2)=(8,4,2) and (9,3,3), both ending with Qc=6. Products of consecutive temperature ratios telescope for any finite descending sequence; work differences telescope independently. Middle-reservoir transfers cancel, so added ideal stages cannot beat the external bound.

Prompts 5–6: the changed first stage has W1=3 and Sgen=1/400. The second gives Qc=27/4 and W2=9/4, total W=21/4 and lost work 3/4. Direct subtraction yields Wrev−W=Tc Sgen for fixed external data. Nonnegative stage entropy productions cannot be canceled by a reversible stage.

Extension: refrigerator signs give Qh=Qc+Win and Qh/Th−Qc/Tc≥0, hence Win≥Qc(Th−Tc)/Tc and COP≤Tc/(Th−Tc). The numerical case has Win≥6 and COP≤1. The heating/cooling/work arrows reverse appropriately.

Reservoir cards and arrow ledgers provide adequate exact data. Kelvin temperatures, cyclic return, heat directions and absence of net middle storage are explicit. The algebraic core is valid with a supplied physical law; it is not a claim to have constructed an engine. Preparation does not require heat or machinery.

### AP-15 — measurement order and an optimal intervening basis

Prompts 1–2: X→Z has four joint branches of probability 1/4, making its recorded Z=e1 probability 1/2. Z→X records Z=e1 with probability zero. Every live outgoing branch sums to one. After the X=+ branch the proper conditional probability of Z=e1 is 1/2; reusing e0 wrongly makes it zero. The different recorded statistics are correctly distinguished from the equal final unreported mixed states for these two particular orders.

Prompts 3–4: Z→Z is certain; Z→X→Z changes the final answer with probability 1/2 even if the middle label is erased. The projector products are [[1/2,1/2],[0,0]] and [[1/2,0],[1/2,0]]. Applied to e0 their squared norms are 1/4 and 1/2, matching X=+ then Z=e0 and the reverse order. Rightmost-first action and zero-probability branches are handled.

Prompts 5–6: the rational basis gives 2(9/25)(16/25)=288/625<1/2. The general target is 2sin²θcos²θ=1/2−2(sin²θ−1/2)², so the sharp single-question bound is 1/2, attained only at θ=π/4 in the given range. The model forbids postselection, feedback and extra evolution in this claim.

Extension: two angles π/6 then π/3 yield intermediate plus probability (3/4)²+(1/4)²=5/8; summing all final branches gives (5/8)(3/4)+(3/8)(1/4)=9/16. This exceeds a bound expressly restricted to one intermediate question. My independent density-matrix channel tests corroborate the rational-basis and X/Z statements without reusing the author's tree function.

The state cards, blank trees, supplied Born/update rules and later matrix gate are adequate. Outcome sign conventions do not affect the squared probabilities. This is an honestly advanced vector/probability task; a classical conditional-evidence puzzle is not substituted for it.

### AP-16 — a finite Ising sampler

Prompts 1–3: ++−− and +−+− have the same plus count but weights four and one. Open-row agreement multiplicities are 2·C(3,a), yielding [2,6,6,2], class weights [2,12,24,16], total 54 and alignment probability 8/27, compared with 1/8 under uniform spins. The first-spin/link encoding has both an inverse and exhaustive image, so it is a proof rather than a guessed catalog.

Prompt 4: neighboring records need probability ratio two, requiring p/(1−p)=2, hence p=2/3. A fair first spin and fresh replacement draws yield row probability 2^a/54. The three tickets are an exact implementation, not an approximate simulation.

Prompts 5–6: closure requires an even number of D symbols; sufficiency follows by reconstruction. The four-link ring has counts [2,0,12,0,2], total weight 82 and alignment probability 16/41. There are 162 equally likely first-spin/four-ticket elementary proposals, of which 82 close. Each accepted spin configuration has exactly 2^a elementary preimages, proving conditional probability 2^a/82 and acceptance 41/81. Independent retries terminate almost surely. My transfer-polynomial computation and elementary proposal enumeration verify these results independently.

Extension: E=−J(2a−L) gives b=exp(2βJ) after canceling a common factor. The open sum is 2(1+b)^(n−1); the ring parity sum is (b+1)^n+(b−1)^n. Ferromagnetic positive βJ means b>1, while the abstract formulas remain valid for every b>0. Finite positive analytic sums do not establish a phase-transition singularity.

Counters and clearly drawn physical links suffice. Site labels intentionally distinguish rotations. The repaired spoken launch no longer leaks 54; production must likewise leave ring parity/counts unknown. Counting/weighted fractions support a real early payoff, with conditional probability as a later gate.

### AP-17 — clocks along spacetime routes

Prompts 1–2: legal T=(t,d) satisfy 0<t<10 and |d|<min(t,10−t); the repaired chosen excursion has d≠0. (5,3) is legal, (2,3) exceeds light speed outward, and (5,5) is lightlike and excluded. The stationary clock gives ten; each traveler leg gives √(25−9)=4, total eight. Euclidean drawn length uses the wrong sign and is not clock time.

Prompts 3–4: symmetric duration is 2√(25−d²). A six-unit reading needs d=±4. All positive durations up to ten are attained when d=0 is permitted; zero is an excluded limiting value. Every permitted finite route satisfies τ=Σ√(Δt²−Δx²)≤ΣΔt=10, with equality exactly when each displacement is zero. This covers arbitrary finite turns and unequal timings.

Prompts 5–6: the boost sends T to (4,0) and R to (25/2,−15/2). A's squared duration remains 100; B's two squared durations remain 16 and 16. Expanding the metric yields exact invariance and future time stays positive. A has velocity −3/5 throughout the primed frame; B changes from 0 to −15/17. T′ is not on A's worldline, and one boost covers the entire history. Turnaround, not a naive exchange of velocity descriptions, distinguishes the paths.

Extension: at fixed d=3 the legal time interval is (3,7), with symmetric strictly concave proper-time sum. Its sole maximum is eight at t=5; both endpoint limits are √40 and are not attained. Thus no legal least value exists.

Figures explicitly distinguish coordinate order (t,x) from drawing axes (horizontal x, vertical t), and provide enough primed range for the actual reunion. The metric and instantaneous-turn idealization are supplied; calculus is only the fixed-distance extension. The learner can choose and prove within the actual relativistic model without a misleading ruler analogy.

### AP-18 — orbital inverse data

Prompts 1–2: circular balance gives M=rv² in G=1 units; all three cards yield 36. At r=16 the speed is 3/2. The (4,4) card yields 64 and fails; treating diameter as radius doubles inferred mass. Cancellation of the positive test mass follows directly from force balance.

Prompts 3–4: monotonicity of rv² sends the speed intervals to [841/25,961/25] and [3249/100,3969/100]. Their intersection is [33.64,38.44], and choosing √(M/r) for every M in it proves sufficiency. At radius 16 the rival speeds are 3/2 and 2. Closed error intervals are disjoint exactly for 0≤ε<1/4; at the threshold they share 7/4. The guide correctly distinguishes a supremum threshold from a largest permitted error.

Prompts 5–6: the projected products reveal q²M=36, so all compatible pairs are M≥36 and q=6/√M. Distinct pairs (36,1) and (144,1/2) certify nonidentifiability; there is no finite upper mass bound. An independent period gives v=2πr/T, then M=4π²r³/T² and q=wT/(2πr). The supplied period yields v=6,M=144,q=1/2 and passes the allowed-q check.

Extension: differentiating the circular trajectory gives inward acceleration magnitude rω²=v²/r. Restoring G produces M=rv²/G=4π²r³/(GT²), both with mass units. If G is also unknown, only GM is identified by the dynamics; q can still be separately inferred from true period and measured speed.

The true-radius circles, tangent arrows, distinct error-interval page and separately stipulated common projection law are sufficient. The model is explicitly circular Newtonian motion about one dominant center; nothing silently treats projected radii as true. Algebra and units form an honest entry with calculus separate.

## Independent source checks

These primary passages were reopened and read on the review date; the new task instances and proofs above were derived independently. No source PDF screenshot inspection is claimed.

- [Tong, Fluid Mechanics](https://davidtong.org/pdfs/teaching/fluid-mechanics/fluids1.pdf), §1.1.3 pp.9–10 and narrowing-pipe relation p.20: local/integral mass continuity, constant-density specialization and area-speed balance. No pressure law is inferred from the ledger.
- [MIT, Essentials of Geophysics chapter 4](https://ocw.mit.edu/courses/12-201-essentials-of-geophysics-fall-2004/b78f19037066b01c0977aa9dda43b225_ch4.pdf), §4.14 pp.163–164, equations 4.91–4.94: stationary travel time and angles from the normal. The source expressly distinguishes stationarity from minimum time; the worksheet supplies its own strict global proof.
- [Tong, Electrodynamics](https://davidtong.org/pdfs/teaching/electromagnetism/electro3.pdf), §4.3.1–2 and §4.4 pp.93–94: phase/polarization, linear combinations and real-field quadratic period averages. Scalar normalized brightness is explicitly defined by the worksheet.
- [Tong, Classical Thermodynamics](https://davidtong.org/teaching/statistical-physics/statmechhtml/S4), §4.3.2 equation 4.162 and §4.3.3: Carnot efficiency, heat signs and irreversible-cycle inequality. Reservoir entropy and loss examples are correctly specialized.
- [Tong, Quantum Formalism](https://www.davidtong.org/teaching/quantum-mechanics/qmhtml/S3), §3.3 equations 3.71–3.72 and intervening measurement discussion: normalized squared amplitudes, state update and immediate repetition. The real two-component specialization is honest.
- [Tong, Phase Transitions](https://davidtong.org/teaching/statistical-physics/statmechhtml/S5), §5.2 equations 5.192–5.193 and §5.3.1: nearest-neighbor energy, ferromagnetic sign, canonical weights and periodic chain. The finite sampler is independently developed.
- [Tong, Dynamics and Relativity](https://davidtong.org/pdfs/teaching/dynamics-and-relativity/dynrel.pdf), §7.1 pp.109–110, §7.2.3 pp.120–121 and §7.4.1 pp.133–134: Lorentz transforms, turnaround asymmetry and proper time. The worksheet's boost and complete trip were separately recalculated.
- [OpenStax, Satellites and Kepler's Laws](https://openstax.org/books/college-physics-ap-courses-2e/pages/6-6-satellites-and-keplers-laws-an-argument-for-simplicity), §6.6 equations 6.60–6.67: small-test-mass circular balance, cancellation and period relation. The common projection and guaranteed-error models are additions explicitly stipulated in the worksheet.

All design repairs are closed. Production should now build actual student objects and generous workspaces, keep answers off earlier sheets, then receive the independent all-student-page and guide-contact/dense-page PDF pass. These activities remain unpiloted; no classroom-pilot approval gate is imposed.

Additional root precision repair reread after closure: AP-13 prompt 5 now explicitly distinguishes the compatible phases modulo 2π. This matches the periodic signal model and the existing key; it creates no new task or solution change. Approved.

Post-production supplied-object clarity closure (2026-09-26): AP-14 prompt 1 now asks learners to label the three energy transfers, matching the already drawn arrows. AP-15 explicitly supplies e1=(0,1) in the first introduction; its materials refer to the printed unit-state definitions rather than nonexistent cutout cards. Reread these current data fields: the mathematical tasks and solutions are unchanged, and these clarity repairs are approved. Root separately closed the fresh v3 PDF review.
