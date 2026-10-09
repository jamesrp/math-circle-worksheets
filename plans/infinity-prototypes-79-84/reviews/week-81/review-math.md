# Week 81 independent mathematical review

Reviewed 9 October 2026. I read the writer brief with its selected-band override, independently rendered `draft/students.pdf`, and inspected all six pages. I also read the separate `infinity-drafts/lowell-math-circle-year-2/source/week-81/guide/facilitator.tex`. No draft, guide, index, branch, or published file was edited.

## Located corrections

**M1 — Facilitator page 4, Take-3 encore: explicitly lift the warm-up refill cap.** The guide says: “Encore: allow removing 1, 2 or 3 from the chosen bucket, retaining finite leftward refills. Investigate multiples of four as the new losing target.” The following sentence repairs earlier buckets by adding “at most three.” This is correct with unrestricted finite refills, but the guide should say that rule explicitly, because Problems 1–3 use the 0/1 cap. If that earlier cap is inherited, the asserted classification fails: `(1,1)` is a second-player win although neither count is a multiple of four. Its only successors are `(0,1)`, `(1,0)`, `(2,0)`, and each is a first-player win when taking 1–3 is allowed. Smallest fix: begin “For this encore, use unrestricted finite refills, then allow removing 1, 2 or 3 …”. Alternatively a new 0–3 refill cap suffices, but must be stated as a separate variant. The independent script checks both the counterexample and the 0–3 variant. This is a rule-interpretation correction; it does not invalidate the stated uncapped theorem.

**M2 — Facilitator page 4, provenance: source date.** The guide gives “March 3, 2017.” Hamkins's [primary post](https://jdh.hamkins.org/buckets-of-fish/) is dated **March 4, 2017**. Change the date or omit it. The game, finite termination proof, all-even strategy, capped variant, and Take-3 discussion are correctly attributed.

The style critic's quantity-card/bucket width mismatch remains a separate material-fit correction; I did not alter or duplicate that review. Digital mathematical checking does not establish physical fit.

## Student packet: all problems check out

Grades 2–5 pages 1–4, including the capped rules, all starts, and all sixteen sorting cards, are mathematically correct. Grades 4–5 pages 5–6, including the explicit rule change to arbitrary **finite** refills, are mathematically correct. No K–1 edition was requested by the scope override.

The reusable board and the cutout quantity cards carry no mathematical conclusion for children. Their numerical labels, bucket order and number-card conversion match the tasks. The first visual is the legal move `(1,1,2) → (1,1,1) → (2,2,1)`; the first arrow removes exactly one from bucket 3, and the second adds one to each earlier bucket. The page 5 visual has twelve counters, card 12, then card 11 after one removal. The empty sorting card `(0,0)` belongs in the second-player group because the first player has no move under the printed rule.

Exact answer keys for the separate facilitator guide:

| Problem | Start, read left to right | Player with a winning strategy | One winning successor under the capped rule |
|---|---|---|---|
| 1 | `(0,0,1)` | first | `(0,0,0)` |
| 1 | `(1,1,0)` | first | `(2,0,0)` |
| 1 | `(2,1,1)` | first | `(2,2,0)` |
| 1 | `(2,2,2)` | second | no winning opening |
| 2 | `(0,0)`, `(2,0)`, `(0,2)`, `(2,2)` | second | no winning opening |
| 2 | the other twelve printed cards | first | see exact successors in the JSON |
| 3 | `(2,2,2)` | second | no winning opening |
| 3 | `(1,2,2)` | first | `(0,2,2)` |
| 3 | `(2,1,2)` | first | `(2,0,2)` |
| 3 | `(2,2,1)` | first | `(2,2,0)` |
| 3 | `(0,2,0)` | second | no winning opening |
| 3 | `(3,3,1)` | first | `(4,4,0)` |

Problem 4: from `(0,1)`, take from the right and add respectively 9, 29 or 99 to the left to obtain exactly 10, 30 or 100 moves. For any finite requested length `L≥1`, refill with `L−1`; refilling with `L` instead gives `L+1` and beats the requested length strictly. There is no upper bound covering all such choices. Under the earlier 0/1 cap this same initial state permits at most **two** moves, so the page's explicit rule change is essential and correctly placed.

Problem 5: no legal infinite play starts at `(1,1,1)`, or any other finite tuple. This remains true however large the finite refills are. Infinite initial contents, infinitely many initial buckets, creating buckets, or refilling the chosen/later bucket are outside the rules and outside the proof.

## Independent general arguments

**Termination.** Fix any hypothetical infinite legal play on a fixed finite number of buckets. Some bucket is used infinitely often; choose the rightmost such bucket `j`. All buckets to its right are used only finitely often. Therefore bucket `j` can be refilled only finitely often, and each refill is finite. Its initial contents plus all receipts are consequently finite, so it cannot be used infinitely often. Contradiction. This proof does not presume a known uniform time for the final rightmost action. It also establishes the capped game's termination.

**All-even criterion.** A move out of an all-even tuple leaves its selected bucket odd, because same-bucket refill is forbidden. Thus no move can go from all-even to all-even. For a tuple with at least one odd count, choose the rightmost odd bucket, remove one, and add one to every earlier odd bucket and zero to every earlier even bucket. Later buckets were already even and are unchanged. This is legal under either 0/1 capped refills or unrestricted finite refills and reaches all-even. The empty state is all-even; termination then turns the two-direction criterion into the claimed normal-play winning strategy. The argument says nothing about a shortest or longest winning play.

**Unbounded finite duration.** From `(0,1)`, the first move may produce `(M,0)` for any chosen finite `M`. The only possible later action removes one from the left, so total play length is exactly `M+1`. An unbounded family of finite plays supplies no infinite legal play.

**Take-3 encore.** With unrestricted finite refills, all multiples of four form the losing target. A removal of 1, 2 or 3 changes a selected multiple to a nonmultiple. From any nontarget tuple, remove the remainder 1, 2 or 3 from its rightmost nonmultiple and add 0–3 to earlier buckets to restore multiples of four. Termination supplies the conclusion. A 0–3 refill cap admits the same repair; a 0/1 cap does not.

**Ordinal description.** The guide's adult-only potential `ω^(m−1)a_(m−1)+…+ωa_1+a_0`, for left-to-right counts `(a_0,…,a_(m−1))`, decreases on every legal move: the highest changed coefficient decreases and all higher coefficients are fixed. Each lower coefficient remains finite. This uses ordinary ordinal order; it is correctly distinguished from surreal arithmetic and is not required of children.

## Reproducible evidence and review limits

Run `python3 verify_math.py` from any directory while this workflow run and its referenced guide remain in their reviewed locations. The script imports only Python's standard library and no author code. It extracts printed tuples directly from the student TeX, checks them against the visibly inspected starts, generates legal moves independently, and recursively determines winning outcomes without assuming the parity theorem.

Execution passed **340 capped seed tuples** with one through four buckets and each initial count 0–3, every one of the **26 printed start occurrences**, all legal descendants encountered, the worked move, the four large finite-duration witnesses, and **84 Take-3 seeds** under a 0–3 refill cap. The JSON records 3,672 cached states across these checks, exact winner/successor/duration data, and SHA-256 snapshots of the reviewed PDF, student source and guide source. These finite checks support the review; the written arguments above establish the unrestricted and arbitrary finite-bucket claims.

For the capped game, the independent checker also verifies shortest duration `sum(a_i)` and longest duration `sum(2^i a_i)` on the finite seed set. Every capped move lowers that latter integer by at least one, and adding one to all earlier buckets makes the decrement exactly one. These are checking tools, not added student tasks or claims about optimal winning duration.

All six rendered pages were inspected individually. Their dots, quantity numbers, bucket labels, card order and task starts match the source mathematics. This report is for the **draft snapshot**, not a claim that an unseen revision has been verified. Classroom use, actual-size printing, counter fit and procedural rehearsal remain untested.
