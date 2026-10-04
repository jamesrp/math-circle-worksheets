# Week 17 independent mathematical review

Reviewed `draft/return-visit.pdf`, all three actual rendered pages, against current AGENTS.md and the generated PROMPT.md/CRITIC-MATH.md. The outline's explicit shared-collection layout governs the harness's generic three-packet filenames. Draft SHA-256: `cc320125ba330bbf76b29a2b45bb1580e3016eb3ad7774c4db8fa8fb03840d6f`.

**No located mathematical errors; no mathematical corrections required.** Each page's stated band checks out completely for correctness. This review does not establish classroom readiness or physical material fit.

## Grades K–1 and up — page 1, Problem 1

The task asks for a smallest deterministic R/B machine that remembers whether adjacent RR has occurred anywhere, with YES persisting after further input. The answer is exactly **three states**. A valid construction has states `0` (no trailing R, NO), `1` (one trailing R and no RR yet, NO), `2` (RR has occurred, YES), with R transitions `0→1, 1→2, 2→2` and B transitions `0→0, 1→0, 2→2`. The empty row outputs NO. The histories empty, R, and RR must occupy different states: append R to distinguish the first two, and stop to distinguish RR from either. These are valid common-continuation witnesses under the printed rules.

The printed test rows give `RRBB→YES`, `RBR→NO`, `BRRB→YES`; all match the goal, including occurrence before the last card. The separate last-blue convention example has one R and one B transition from each state, START at X/NO, R loops at X, B goes X→Y, R goes Y→X, and B loops at Y. Its printed RBB trace is exactly `X→X→Y→Y`, output YES. The empty row outputs NO in this demonstration. All arrows and labels were inspected in the actual PDF.

Independent checks: all 8,191 R/B words of lengths 0–12 match their direct predicates for the reconstructed example and three-state RR construction. A product-state breadth-first equivalence search, without a word-length cutoff, rejects every complete one-state (2) and two-state (64) labeled machine with designated start state 0. A different start label is covered by relabeling.

## Grades 2–3 and up — page 2, Problem 2

The task asks for the fewest states recognizing even red count AND even blue count, explicitly including zero. The answer is exactly **four states**, one per parity pair. R toggles red parity, B toggles blue parity; only even/even says YES. The printed rows give: `No cards→YES`, `R→NO`, `RB→NO`, `RRBB→YES`, `BBR→NO`, `BRBR→YES`. None of the supplied rows is inconsistent with the rule.

Necessity: the histories empty, R, B, RB realize four distinct parity pairs. For any two, append the R and/or B needed to bring the first to even/even; the second retains a different parity pair. The six pairwise common endings were independently computed and checked, including empty endings. Exhaustive product-state equivalence searches reject all complete one-, two-, and three-state labeled machines (2, 64, and 5,832 respectively), without a word-length cutoff. The four-state construction also agrees with direct counts for all 8,191 words of lengths 0–12.

## Grades 4–5 — page 3, Problem 3

The task asks children to propose an equal-count machine, challenge it with rows, and decide whether any fixed finite number of states works for every length. The universal answer is **no**. The printed examples have equal counts for RRBB and RBRB (YES) and unequal counts for BRR (NO). No fixed successful finite construction is assumed by the final question; unsuccessful proposed machines are the objects to challenge.

For any deterministic machine with m states, the m+1 histories `R^0, R^1, …, R^m` include `R^i` and `R^j` at the same state with `i<j`. Append the same `B^i` to both. The final state and output must agree, while `R^i B^i` has equal counts and `R^j B^i` does not. The argument covers i=0: the common ending is empty, and stopping adds no state or memory under the printed rules. It covers arbitrary lengths and does not rely on finite experimentation establishing the theorem.

An independent executable collision checker generated an actual false answer for every complete one-, two-, and three-state labeled machine (2, 64, 5,832). The longest constructed counterexamples in those searches had lengths 1, 3, and 5. This finite audit supports the implementation of the common-ending argument; the preceding all-m argument supplies the unbounded conclusion.

## Actual PDF diagram and geometry audit

All three pages were separately rendered at 1.5× and inspected at full-page readable size. The PDF is three US Letter pages (612×792 points). Blank working rectangles measure, allowing PDF rounding, 6.90008×2.50003 inches (page 1), 6.90008×3.50004 inches (page 2), and 6.90008×3.20004 inches (page 3). The worked example's two state circles measure 0.63001 inches across, with equal horizontal/vertical scaling. They are convention graphics, not supplied 4 cm working discs. Page 2 has six correctly separated example rows; page 3 has three blank recording rows. Text spans are within the page and the rendered state/arrow/card labels are legible. No claimed regular polygon appears in this packet.

## Reproducible evidence

`math-review-check.py` is independently written and does not import or rely on the writer's verifier. Run from the repository root:

```sh
tmp/example-edit-env/bin/python tmp/worksheet-runs/encore-week-17-20261004-v1/math-review-check.py
```

It writes `math-review-evidence.json`: exact printed-row outputs, the RBB trace, all small-machine exhaustive counts, pairwise continuation witnesses, the equal-count collision audit, actual PDF dimensions, and the reviewed PDF hash. Separate reviewed renders are in `math-review-render/page-01.png` through `page-03.png`. The draft and its sources were not changed.
