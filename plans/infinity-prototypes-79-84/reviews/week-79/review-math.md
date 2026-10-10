# Independent CRITIC-MATH: Week 79

Reviewed 9 October 2026. Selected-band override applied: `draft/students.pdf`, five pages; no K–1 packet is requested. Read `PROMPT.md` and `CRITIC-MATH.md`; reviewed every rendered student/material page and the separate four-page facilitator source. No author checker was imported or used. Reviewed content hashes are in `math-check-results.json`.

**Student verdict:** Grades 2–5 Problems 1–3 (pages 1–2), Grades 4–5 Problem 4 (page 3), and shared materials (pages 4–5) check out mathematically. The first visual is empty bowls → add 1,2 in A → A={2}, B={1}; it matches the legal action. The cutouts contain 1–24 exactly once, on equal-scale 30 mm squares. Each A/B mat is 180 by 96 mm, digitally sufficient for twelve 30 mm cards without overlap. Physical fit remains untested.

## Located corrections

### 1. Facilitator, page 3, proposed finite day: day 0 is an exception to the stated witness

**Exact text:** “For any proposed finite day $N$, label $N+1$ is still in A at that day.”

**Evidence:** Day 0 starts with both bowls empty. Label 1 has not yet entered, so it is not in A. The witness works exactly for positive finite N: $N+1\leq 2N$ and $N+1\in A_N$. Day 0 still cannot contain the complete limiting configuration, because B is empty rather than all positive labels.

**Smallest fix:** “For any proposed positive finite day $N$, label $N+1$ is still in A. On day 0, neither bowl has any labels.” The conclusion that no finite day contains the complete limiting configuration remains valid.

### 2. Facilitator, page 4, indicator supremum: day 0 must be excluded

**Exact text:** “Convergence is not uniform: $\sup_k a_n(k)=1$ for every $n$.”

**Evidence:** $A_0=\varnothing$, so $a_0(k)=0$ for every positive label k and the supremum is 0. For every $n\geq1$, $A_n$ is nonempty and the supremum is 1. Omitting one initial term does not affect the failure of uniform convergence.

**Smallest fix:** Replace “for every $n$” with “for every $n\geq1$”.

## Verification boundary

The independent checker `check_math_independent.py` replays 500 days under each rule, verifies every finite set and count formula including day 0, checks introduction days for labels 1–1000, checks move days and subsequent membership for labels 1–500, and verifies all printed examples. It records Problems 1–4's outcomes in `math-check-results.json`.

The infinite statements are supported by the actual proof, not a long replay: from empty day 0, adding $2n+1,2n+2$ to $\{n+1,\ldots,2n\}$ and moving $n+1$ gives $\{n+2,\ldots,2n+2\}$. Hence label k is introduced at $\lceil k/2\rceil$, moves exactly on day k, and remains in B for every later day. This proves $\forall k\ \exists N\ \forall n\geq N$ eventual membership; it does not prove $\exists N\ \forall k$. The finite-day obstruction uses $N+1$ for $N\geq1$, with day 0 handled separately.

Under the changed rule, $2n$ moves immediately on day n; $2n-1$ stays in A permanently. Every fixed finite label window therefore stabilizes, but all labels cannot already have been introduced on a finite day. Both rules have exactly n cards in each bowl after completed day n. Their count histories coincide while their eventual-membership limits differ. The guide's failure-of-sum-interchange calculation is correct: $\sum_k\lim_n a_n(k)=0$ while $\lim_n\sum_k a_n(k)=+\infty$. The positive-day supremum witness proves nonuniform convergence. No claim of a physically forced endpoint follows.

All numbered student prompts admit their intended actions and outcomes. Predicting label 20's move day does not require physically running twenty days with only 24 supplied cards. No mathematical revisions to the student PDF are required by this review. The requested shorter first route (six enacted days, twelve available) is a pacing decision for the separate critic/revision stage; it does not change these calculations.
