# Week 53 fresh adversarial critic review

**Stage:** independent critic only, October 4, 2026. No worksheet, source, guide, workflow block, existing week or index was edited. No subagents were used.

**Disposition:** targeted revision required before release. The paid-once minimum-cost connecting-network investigation is sound and worth preserving. Clarify Problem 8's final question (F1). The other findings are smaller convention/documentation improvements or explicitly untested classroom hypotheses; they do not justify removing the upper mathematics or manufacturing a separate K–1 packet.

## Evidence and scope

Read `AGENTS.md`, repository `README.md`, `plans/new-themes-52-63/STAGE-ROUTING.md`, root `REPUBLISHING.md`, the complete run `PROMPT.md` and `CRITIC.md`, Week 53 research/outline, and all relevant files under `draft/src/`. Direct routing supersedes the generic separate-band filenames and page quotas.

Reviewed the **actual combined `draft/students.pdf`, all nine Letter pages**, SHA-256 `f12a42477b64ba4957740c7c4ef32eaa534081a9fc2c7acb429ee1e6331f5130`. Fresh 108-dpi page renders, extraction and selected higher-resolution clips are in `critic-qa/`. Every page was visually inspected, including every grade header, graph, price, thick purchased link, small record and workspace. All pages have the intended header/footer and consecutive Problems 1–9; there is no visible clipping, overlapping text, extra title, Name/Date field or teacher commentary.

The writer's actual-PDF vector checker was rerun: `critic-qa/vector-output-checks.json`. It reconstructs and verifies all printed links, purchased links, numerals/dots and vertex coordinates. The critic also independently enumerated connected subsets without importing the writer's verifier: `critic-qa/spot-math-checks.json`. A fresh standalone source copy was built under `critic-qa/standalone-src/`; `standalone-rebuild-checks.json` confirms extracted text, Letter dimensions and all nine 144-dpi pixel arrays match the reviewed draft. This critic did **not** separately re-extract the ZIP; the writer's extracted-ZIP QA remains writer evidence. The independent math critic still follows and must review arbitrary-map proofs and all tasks independently. These checks establish neither physical handling nor classroom suitability.

Directly read local CS Unplugged Activity 9, printed pp. 76–80 / PDF pp. 1–5, and *Math Circle by the Bay*, “How we teach,” printed p. ix / PDF p. 10. The latter supports manipulatives, independent solving, comprehensible and unambiguous statements, and explanation; it does not validate this adaptation. CS Unplugged explicitly states ages **9 and up** and approximately 40 counters per child. Neither source establishes our supported K–1 access, 30-counter kits, staffing, preparation time or proposed map sizes as tested. The source/provenance notes correctly distinguish these design inferences from source evidence.

## Findings for the reviser

### F1 — Required: define the obstruction in Problem 8's general question

**Location:** PDF p. 8, final sentence: “Can a connected purchase with no loop get stuck above the least cost?”

“Get stuck” has no explicit mathematical meaning on the page. Two reasonable readings produce opposite answers:

- A loop-free connected purchase can cost more than the minimum: **yes**. The lower printed tree itself costs 14, whereas the top tree costs 8.
- A loop-free connected purchase can cost more than the minimum **while having no cheaper legal one-link swap**: **no**, the intended exchange-certificate theorem.

The preceding concrete swap question suggests the second reading, but leaves the defining condition to inference. This is especially consequential because the lower diagram is an immediate witness for the first reading. Source `MATH-NOTES.md` clearly intends the second.

**Repair:** explicitly retain the “no cheaper one-link swap” condition in the final question. For example, ask whether a connected purchase with no loop can cost more than the cheapest one even though no one-link swap makes it cheaper. Keep the question open; do not print the path-max certificate, algorithm or answer. Preserve both concrete purchases and the separate positive-cost loop question. This is a precision repair, not a recommendation to remove the arbitrary-map continuation.

### F2 — Minor: make the allowed price set explicit in Problem 7

**Location:** PDF p. 7, “Put prices from 1 to 4 on each map.”

The intended inverse problem uses six independently chosen **whole-number** prices in `{1,2,3,4}`, with repetition permitted. “From 1 to 4” is natural elementary phrasing, but mathematically can include fractions, which would conflict with the equal-value-counter implementation and the checked domain. There are six links, so the intended use of repeated labels should be immediately clear.

**Repair:** state that every link gets a price of 1, 2, 3 or 4. Do not require all four values, introduce a price-sorting method, or constrain the child's designs. The unique-versus-multiple objective is a substantial and open inverse investigation and should remain.

### F3 — Minor operational ambiguity: one swap changes the result, not the fixed reference

**Location:** PDF p. 5: “returning one bought link and buying one unused link. All four places must stay connected.”

The small worked visual buys first and returns second, correctly preserving connection during physical execution. The sentence lists returning first; literal continuous “must stay connected” would make the first step impossible on either printed tree. More importantly, “find every” requires all rows to refer to the **same printed input**, not a chain of successively cheaper trees. The existing “From each thick purchase” largely communicates that reference, and the source notes correctly state it. This is an unpiloted comprehension risk rather than a demonstrated failure.

**Repair if wording is touched:** make final-result connectivity explicit and retain the unchanged pictured purchase as the reference for each alternative. Do not turn the task into a prescribed search order. Keep the buy-then-return worked visual and the contrasting input with no improving swap.

**Guide/material handoff:** preprinted thick input links cannot literally be erased. The later guide should explain that input pictures remain references while removable markers or a separate trace/copy represent each proposed result. The return/buy table already gives a light, recoverable record. A child should not be required to operate a constantly changing reference while simultaneously listing all swaps.

### F4 — Low: correct two physical-spacing claims in source notes

**Location:** `draft/src/DESIGN-NOTES.md`, map-size paragraph.

It claims nearest-place spacing on pages 1–6 and 9 is at least 52 mm and page 8 has about 39 mm. The actual vector geometry gives **51.0 mm on p. 6** and **37.5 mm on p. 8**. Page 7 is 40.25 mm as approximately reported. This does not establish a fit defect; it is a source-documentation discrepancy. Correct the figures so the later guide and physical pretest use the actual printed geometry.

## Page-by-page audit

| PDF page / problem | Concrete mathematical work and review result |
|---|---|
| 1 / 1, Grades 2–5 | Shared rules state whole printed links, thick purchase records, one payment, refunds and turns only at circled places. The X/Y/Z available → bought/payment → kept record visual appears before the task, with meaningful `2+4=6` intermediate payment and a deliberately nonoptimal purchase. Numerals and dots are bridged explicitly. The two large triangle tasks have cost 3; the left has one optimum, the right two. Children choose links and can trace reachability; adults can read/pay without making the choices. This is a short introductory younger entry, potentially below five minutes for confident third graders; see pacing note below. |
| 2 / 2, Grades 2–5 | Genuine minimum-cost enumeration: cost 4, three optima, CD plus any two of the three price-1 triangle links. D must remain connected; three small copies support pen records. Prices and link ownership are legible. Recording all three is a small, checkable collection rather than an unweighted tree catalog. |
| 3 / 3, Grades 2–5 | Cost 7, unique AB/BC/CD. Buying the three cheapest links AB/BC/AC costs 6 and isolates D, so this is a real greedy trap. The task gives the objective and leaves the method to the child. The explanation request is the core optimality question, not a gratuitous follow-up. The main map and two record copies leave ample space. |
| 4 / 4, Grades 2–5 | Cost 6, three optima, CD/DE plus any two price-1 triangle links. The eight-link map adds a second local triangle and costly alternatives; the same tied triangle is revisited in a larger global connection problem. The first four cheapest links can omit E. Three records are sufficient. It is closely related to Problem 2, but cost/connectivity choices still matter; no forced page-count objection. |
| 5 / 5, Grades 4–5 | The non-task buy/return visual shows input, paid intermediate and final cost 6 → 9 → 5. Two fixed inputs contrast three improving swaps with none. From the left cost-10 input: AD→CD gives 9, AC→BC gives 7, AC→CD gives 8. The right cost-6 input has no cheaper legal swap. The rejected AD→BC swap would disconnect D even though its arithmetic is cheaper. All choices must be checked against the input, not only price. Tables fit the entire result list. See F3 for wording/physical handling. |
| 6 / 6, Grades 4–5 | A substantive forced/forbidden classification with reasons, not a printed cut algorithm. Cost 8, unique AB/BC/CD/DE/EF; AC/DF/BD/CE are excluded. Repeated prices coexist with a unique optimum. All nine links and their prices are distinguishable, with substantial argument space. Source notes supply actual cuts/cycles for later adults; full proof verification remains for the math critic. |
| 7 / 7, Grades 4–5 | Two six-link K4 maps offer genuine inverse design and checking; the child selects prices and explains uniqueness/nonuniqueness. Six writable price fields on each map are positioned near the correct links. Both goals have valid witnesses in the source. Large blank space permits alternative purchase drawings and arguments. See F2. |
| 8 / 8, Grades 4–5 | Two six-place fixed purchases are connected, acyclic five-link inputs at costs 8 and 14. The upper has no improving swap; the lower does (e.g. BD=5→CD=2, cost 11). Strict positivity is stated for the loop-removal claim. Concrete exchange work precedes a deep generalization; no theorem is handed to students. Space remains for recorded swaps and reasoning. F1 is required because the final generalization's intended condition is implicit. |
| 9 / 9, Grades 4–5 | Cost 6, unique AB/BC/CD on the printed map; the general distinct-price uniqueness question is a substantial readiness-dependent continuation. The six prices are distinct and attached to the correct links. The square has equal horizontal and vertical scaling. The crossing is unmarked and the shared circled-place rule prohibits changing links there; labels 5 and 6 are separated from the crossing. There is room for a purchased-network trace and argument. |

## Mathematical identity, prerequisites and pacing

This is **global purchased-network cost**, not shortest A-to-B routes, tree walks, traversal words, or number-of-links minimization. Every numbered concrete task keeps all pictured places in play. The pawn is only a connectivity check, and no step ledger is required. Costs are the sum of bought-link labels, paid once. Even the tied catalogs optimize prices and supply examples for exchange/uniqueness; they are not a replacement unweighted-tree enumeration packet. I read the supplied novelty comparison against Week 13, Weeks 21/50 and atlas AD-05; I did not independently repeat a whole-corpus novelty sweep in this stage.

The pages leave selection, organization, pricing and explanations with the children. No Kruskal prescription, cut-search recipe, intended proof sequence, or completed target enumeration is printed. Problem 3 contains a purposeful cheapest-links trap. Problems 5/8 require checking connection after an exchange, so merely comparing two prices is insufficient. Problem 6 distinguishes repeated prices from forced multiplicity, and Problem 7 lets children create their own evidence. These are the packet's strengths and should survive revision.

The approximate bands are honest. Pages 1–4 require label recognition, dot counting initially and numerals 1–6 later, with optional adult arithmetic/recording. Actual optimum totals are 3, 4, 7 and 6; the task demand is relational connection and comparison rather than advanced arithmetic. Pages 5–9 require following paths, keeping a fixed bought set, interpreting every/some/none, comparing totals, and explaining alternatives. Integer arithmetic itself is modest; the universal exchange and uniqueness arguments have much greater abstraction demands than the grade header alone signals. The source notes explicitly treat those as readiness-dependent continuations and multiple visits, which is appropriate.

Problem 1's two triangles may be quick for confident third graders after the shared demo. That is an **unpiloted pacing hypothesis**, not grounds to manufacture harder K–1 pages or split bands. It provides an accessible supported entry. Problems 2–4 give those children substantial work immediately afterward; Problems 5–9 provide ample upper depth. The future guide should offer few pages at a time and preserve flexible stopping points. It should not claim each numbered problem has been timed or that finishing nine pages is an hour's goal.

## Materials and release limits

The fixed maps have at most nine links and available-price sum at most 26. The inverse maps have six links priced at most 4, total at most 24. Thus 30 counters and ten markers per pair/trio allow even buying every link before returning any. The shared example costs 6 and all its links cost 9, within the 15-counter launch stock. Payment counters are kept off-map; bought-link membership is externalized separately. The five-kit allocation matches the supplied eleven-child fixed-table context.

The working circles are approximately 10.4 mm; compact record/example circles are approximately 5.6 mm. The small records are suited to pen traces, not pawn play. Maps give workable digital spacing and visible prices; this reviewer has not physically checked 12–15 mm counters, pawns or markers, dry-erase clutter, refunds, or the parent volunteer supporting two young pairs. Source notes correctly mark these and preparation estimates untested. Preserve those limits in the separately authored guide, and pretest the actual materials before describing them as ready.

The author has supplied original LaTeX/TikZ, editable graph data, builders/verifiers and concise source notes. The clean source copy has no repository dependency. The expected guide is absent because this is the student stage; its absence is not a critic blocker. Before release, finish F1 and relevant minor corrections, then independent math review, fresh revision with final-page inspection, and separate theorem-first guide authoring/review. No public or remote copy is asserted current.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
