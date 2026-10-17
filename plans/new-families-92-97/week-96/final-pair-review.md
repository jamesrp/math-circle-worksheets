# Week 96 independent final-pair review

Date: 2026-10-17. Scope: the two student PDFs and six-page facilitator PDF in `published-pdfs/`, paired against `package/` sources and mathematical checks. Read-only review; no worksheet/source edits by this reviewer. The coordinator supplied a corrected facilitator page 6 during review; that latest page was re-rendered and re-read.

## Verdict

**PASS for the current 15-page PDF set. No remaining mathematical, student/guide alignment, or rendered-layout blocker found.** The existing unpiloted and unrehearsed status is appropriate and must remain. This is a digital review, not classroom evidence or a physical rehearsal.

One located issue was corrected before this verdict: facilitator page 6's gcd return-visit prompt originally said the largest bag selectable from “either” original bag. That could invite a union reading with answer 36. The latest PDF says “both of them,” which unambiguously asks for the common sub-bag with value 12. I visually inspected the corrected page 6 and verified its new final paragraph preserves the digital/physical distinction.

Release-assembly follow-through, outside the PDF verdict: this review snapshot's `package/README.md` refers to `QA.md` and `reference-pdfs/`, neither yet present in the snapshot. Its stage-level `final-sources.zip` contains only the student-stage `src/` files, not the final paired package. The coordinator subsequently reported that the final number-family release package includes QA.md/reference-pdfs and that its extracted archive rebuild matches all three PDFs byte-for-byte, with release-check.json recorded. I did not independently inspect that separate assembled archive; this is no remaining PDF blocker. The `package/` build I inspected works and produces all three current PDFs exactly.

## Page-by-page coverage

Every page below was extracted, read in full, independently rendered at 108 dpi, and visually opened. All have legible text, intact diagrams/tables, appropriate margins, and consistent headers/footers; no clipping or overlaps found.

| Packet / page | Content checked against guide and mathematics | Result |
|---|---|---|
| Grades 2–3 / 1 | Shared multiplicative split rules; 20 → 4×5 → {2,2,5} worked visual; two routes each for 12,18,24,36; four working areas. Guide p3 routes all preserve product and terminate in the correct prime bag. | Pass |
| Grades 2–3 / 2 | Same-input {2,2,5} → shaded {2,5} → value 10 visual, quotient 2; empty selection=1; full inventories for 12 and18, each six values. Guide p3 matches. | Pass |
| Grades 2–3 / 3 | Four-token 24 versus three-token30; each has eight selected values. Guide p3 lists exactly the eight for each. Large collection workspaces. | Pass |
| Grades 2–3 / 4 | Four/six/eight-choice design using primes2,3,5; minima6,12,24. Guide pp3,5 covers construction, completeness and optional minimality. | Pass |
| Grades 4–5 / 1 | Shared 20 worked visual; splitting routes36,48,60; unique final multisets. Guide pp3–4 covers all starts and legitimate alternative routes. | Pass |
| Grades 4–5 / 2 | Same-input selection visual; 24/30 divisor catalogs and exactness question. Guide p4 supplies both directions and uniqueness, not merely a list. | Pass |
| Grades 4–5 / 3 | P3 counts for36,60,72 are9,12,12; P4 seven2s/four3s gives40. Guide p4 matches both questions and makes full-number arithmetic unnecessary. | Pass |
| Grades 4–5 / 4 | P5 complete unordered multiplicity patterns for6,8,9,10,12; explicit label-independent example; all patterns can use at most three prime labels. Guide p5 conventions/table are consistent. | Pass |
| Grades 4–5 / 5 | P6 least positive numbers for4,6,8,9,10,12 divisors, allowing any primes; guide p5 proves why omitted larger primes cannot improve minima. | Pass |
| Facilitator / 1 | Theorem-first overview precedes solutions; n>1 factorization, positive divisors, distinct primes/positive exponents, repeated-token convention, n=1 empty bag, divisor formula and minimum principle. Experiments, conjecture and proof distinguished; band/prerequisite map explicit. | Pass |
| Facilitator / 2 | Staffing, materials, brief shared launch, supported reading/multiplication, retained same20 bag for the selection bridge, first-route pages, stopping points and return visits. Timings total about49–59 minutes before discretionary transition slack; the text explicitly treats durations as choices. | Pass as an unpiloted plan |
| Facilitator / 3 | Every lower-band answer and route; catalogs12,18,24,30; lower-band minima; references to proof pages5–6. | Pass |
| Facilitator / 4 | Every upper P1–4 answer; route intermediates48/60, complete catalogs36/60/72, count formula and40-divisor bag. Crossrefs to guide p3/p6 correct. | Pass |
| Facilitator / 5 | Every pattern and least representative for all six divisor counts; proof by complete multiplicative partitions, smallest primes, exponent-swap inequality; grade2–3 crosslink and upper P5/P6 distinctions. | Pass |
| Facilitator / 6 | Termination, prime-divides-product proof via Euclidean-algorithm/Bézout consequence, cancellation uniqueness, two directions of divisor bijection; corrected common-sub-bag gcd12/lcm72 extension; sources, review evidence, limits. | Pass on latest rendered bytes |

The inputs, intermediate actions and outputs in both shared worked visuals match. No student packet claims K–1 coverage. Student problems remain consecutive within each packet (1–4 and1–6). Adult hints stay in the guide. No student page needs an additional procedural example to understand an unfamiliar code: the only new count-pattern convention has an explicit contrasting-bag example in P5.

## Independent mathematical verification

Ran `python3 package/check_math.py`: PASS. Read the checker as well as its output. It enumerates legal factor routes, physical subsets versus indistinguishable sub-bags, divisor inventories, unordered factor patterns and all smaller integers for each minimum. Its three exponent slots are justified for these targets because four distinct primes imply at least16 divisors.

Independently used a divisor sieve through10368, incrementing every multiple of each positive integer (not the package's prime-factor/subset method). It gives:

- τ(12),τ(18),τ(24),τ(30),τ(36),τ(60),τ(72),τ(10368) = 6,6,8,8,9,12,12,40.
- First integers with divisor counts4,6,8,9,10,12 are6,12,24,36,48,60.

Manually checked all printed route arrows and the guide's complete pattern rows. The factor partitions are respectively {4,2·2}, {6,3·2}, {8,4·2,2·2·2}, {9,3·3}, {10,5·2}, and {12,6·2,4·3,3·2·2}; subtracting1 yields exactly the printed multiplicities. The least representatives in every row are numerically correct, including2^11=2048. The exponent exchange and replacement by a smaller unused prime prove global minimality after pattern exhaustion. They are not inferred merely from finite tests.

The uniqueness argument correctly relies on Euclid's lemma; it does not assume factorization uniqueness while trying to prove it. Bézout's identity from the Euclidean algorithm is an explicitly identified adult-level dependency. The sub-bag argument covers the empty selection and complementary quotient; repeated physical copies do not introduce extra distinct values. Optional gcd/lcm values12/72 satisfy12·72=24·36.

## Sources and practical limits

Checked Conrad's linked primary PDF, Theorems1.1/2.1/2.3 and Lemma2.2 on PDF pp1–3; the stated attribution is accurate: https://kconrad.math.uconn.edu/blurbs/ugradnumthy/uniquefactnZF%5BT%5D.pdf . The packet clearly labels its divisor-count and minimum derivations as independently written consequences.

Read the authorized retained *Math Circle by the Bay* preface, printed viii–x/PDF9–11. SHA-256 matches the repository manifest and SOURCES.md: `84e0277cd94b1e501d153834b7123a72958f8c01b806e7bdfcca012a3191e427`. The attributed deep themes/connections, independent work, manipulatives and long-theme pacing are supported. Exact tasks and timing are correctly labeled design choices.

Checked the actual Fall2025 Handouts8/9 originals: Problems8.1 and9.1 match the apples/possible guest counts and door-toggle claims. Checked current Week9 guide p9 (lcm corner meeting), Week29 guide pp1–4 (additive rod construction), Week31 guide pp1–4 (gcd visibility) and bonus pp1–2 (prime-power double-visibility distinction). Checked the older divisors-of12 seed and current AD-06 student pp20–22/adult pp29–33; the stated prior-use boundary is accurate.

The 36-counter kit suffices for the concrete lower-band starts and20 launch; upper starts use factor cards and supported multiplication, as the guide states. Extra repeated prime tokens may be drawn; the eight supplied2s do not illegally limit the11-token pattern. Reading aloud/recording help is separated from adults choosing mathematical routes. The proposed pace and three-adult table arrangement are plausible, but classroom independence and 10–15-minute preparation are untested estimates, not verified observations. No redesign is required on these hypotheses alone.

## Rebuild evidence and identity

Ran `python3 package/build.py --out pair-review-rebuild --work pair-review-build` successfully, including the portable checker and both TeX passes per PDF; repeated after the coordinator's page6 correction. The builder rejects overfull content. All three freshly rebuilt PDFs byte-match the current published PDFs:

| File | SHA-256 |
|---|---|
| week-96-grades-2-3.pdf | `8f9b7638b5dfb887eb722fbc13dc5ebabe3290b3899d885e02cec84d76095097` |
| week-96-grades-4-5.pdf | `505193d7a1ab4c8e4d7bac78eafe2c21d539f25577c4eb574c1f6dd947b83024` |
| week-96-facilitator.pdf | `1b2931f795e4d1c8bc4796fba7150d9ec01760ebc1459dfbea10922a603721ba` |

No optional content change is needed for this digital approval. The coordinator separately reports completion of the final archive-assembly check; preserve its evidence and the unpiloted status.
