# Three worksheet designs: rules, memory, and approximation

September 25, 2026. Fixed random sample IDs: **GA-11, AP-26, AP-07**. These designs preserve the atlas originals. They are unpiloted proposals, with explicit solutions and exact checks, awaiting independent design and PDF reviews.

The full student wording, page boundaries, prompt IDs, staged hints, answers to every prompt, source locators, and figure specifications are in [systems-data.json](systems-data.json). [systems-checks.py](systems-checks.py) verifies the main identities and all 32 prompts' solution/hint coverage; [check results](systems-checks-results.json) report seven passing groups. These checks supplement the general mathematical arguments, rather than substituting for them.

## Candid assessment

| Family | Worksheet verdict | What makes it more than a calculation page | Honest prerequisite gate |
|---|---|---|---|
| **AP-26 — The parking robot remembers yesterday** | Strongest immediate candidate of these three. | Play a delayed controller; find a false finish; discover that one reading is not a state; construct a pair-state cycle; prove an all-start six-cycle; optionally turn the state map into a literal rotation or weaken correction to prove convergence. | Signed subtraction and careful two-card updates for the concrete core. Variables for the universal theorem. Fractions and algebra for the optional convergence page. |
| **GA-11 — The addition machine has a secret** | Conditional strong for a symbolic/logical group. The elementary fraction portion alone is too slight. | Two routes expose a forged output; one proof forces every rational input; students invent two legal machines on a specified irrational domain that agree on every rational yet disagree at √2. | Signed fractions, algebra, rational versus irrational, and willingness to prove a rule for arbitrary inputs. Continuity is a separate extension. |
| **AP-07 — Can you trust the cooling simulator?** | Strong after substantial redesign, at a calculus gate. A recurrence-only elementary sheet would be unsatisfactory. | Derive tangent stepping, compare at equal elapsed time, produce a stable-but-inaccurate counterexample, optimize the placement of two updates, then prove the exact minimum budget for a 10% target. | Derivatives as slopes, exponential decay, algebra. A supplied or proved product inequality for the global update-budget bound. |

The Week 1 benchmark is a sequence from meaningful action to a new representation and a proof, not a requirement that every sheet use swaps or state graphs. AP-26 uses a graph because discovering the correct state is the mathematical issue. AP-07 instead uses a design/optimality challenge, and GA-11 uses adversarial certificates followed by construction of counterexamples.

## Student pages and intended delivery

**GA-11: three pages.** Page 1 is a partner certificate game, page 2 proves the rational theorem and introduces a larger input domain, and page 3 asks students to invent and verify two different additive machines. Do not give the formula for the machines on page 2. The premise that every `a+b√2` has a unique rational pair is supplied; its proof is in the guide. The close decimal comparison does not by itself prove discontinuity; the final question explicitly demands arbitrarily close rational inputs for that conclusion.

**AP-26: four pages, the fourth optional.** Pages 1–2 give the playable rule and discovery of pair-state memory. The graph area is blank: do not print a six-node ring before students discover the cycle. Page 3 provides the universal algebra route and an optional triangular-grid geometric route. Page 4 changes the feedback gain to one-half and asks for a proof of convergence and a certified tolerance time. An hour can stop after page 2 with substantial mathematics; the full four pages need not be compressed into one session.

**AP-07: four pages, the fourth an advanced continuation.** Page 1 begins with the differential model and tangent construction. Page 2 separates positive decay, alternating decay, bounded nondecay, growth, and accuracy. Page 3 is the central two-update optimization; this is the strongest self-contained endpoint. Page 4 permits unequal step schedules and asks students to attain 10% accuracy with the fewest updates, then prove a matching lower bound. Print its title as **An accuracy budget**, not “A six-update challenge”: the latter leaks the result. The final backward-Euler question demonstrates that a qualitatively better method can still miss the accuracy goal.

## Mathematical results to guard during editing

- **GA-11:** Additivity and `f(1)=3` force `f(m/n)=3m/n` on the rationals. On `D={a+b√2 : a,b rational}`, every `f_c(a+b√2)=3a+cb` is additive and well-defined. Choosing `c=0` and `c=5` gives the intended pair. This is not an explicit pathological construction on all real numbers. A single close input pair with separated outputs is not a discontinuity proof.
- **AP-26:** `T(a,b)=(b,b−a)` satisfies `T³=−I` and `T⁶=I`; every nonzero real pair has exact period six and `(0,0)` is fixed. The inverse is `T⁻¹(c,d)=(c−d,c)`. The regular hexagon appears in the embedding `(a−b/2,√3 b/2)`, not necessarily on a Cartesian old/current plot. Half-gain `H(a,b)=(b,b−a/2)` satisfies `H⁴=−I/4`. For start `(1,1)`, tick 16 is a sufficient, deliberately nonminimal, certificate that both coordinates stay within `1/100` thereafter.
- **AP-07:** Euler's multiplier is `1−h`. Settling to zero requires `0<h<2`; boundedness includes `h=2`, which does not settle. For two positive durations summing to 1 the estimate is `8h(1−h)≤2`, uniquely optimized by equal half-steps. This remains below the exact `8/e`. Any schedule of at most five positive durations summing to 1 can be padded by zero placeholders and bounded by `8(4/5)^5=2.62144`, below the allowed lower target `7.2/e≈2.648731976`. Six equal steps attain `8(5/6)^6≈2.679183813`, relative error about 8.9653%. The check uses rigorous rational bounds on `e` so the threshold is not a rounding accident.

## Source and pedagogy distinctions

Re-read *Math Circle by the Bay*, preface printed viii–x (PDF 9–11). Its actual teaching guidance includes deep connected themes, manipulatives, varied pace, playful dialogue, independent attempts, and returning to explanations. The authors explicitly avoid universal timing predictions. The page sequence, gates, partner games, and approximate hour plans here are our design inferences, not claims that those authors tested these activities.

The original atlas's source trail was rechecked: Reem's Cauchy-equation paper for functional equations and regularity; Åström–Murray's chapter summary for state feedback; Driscoll–Braun §11.3 for the Euler multiplier. Exact URLs and boundaries are in the data. The delayed six-cycle problem, the two-machine worksheet construction, the two-step optimization, and the six-update accuracy budget are independently developed here. Do not attribute those exact worksheet problems to those books.

No activity use is entered into the use log. These drafts are not evidence that any of the three will succeed with a particular group; the prerequisite gates and candid rankings should survive into the facilitator guide.
