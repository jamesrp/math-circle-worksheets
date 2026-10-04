# Research notes: AI worksheet-generation workflows (genlab-opus5.5)

Chronological lab notebook. Newest entries at the bottom. Facts about runs are recorded as observed; interpretations are labeled.

## 2026-09-30 — Setup

### Question
Which generation workflows (DAG of agents + prompts) produce the best student worksheet packets, judged before any human editing? Secondary: which eval signals track James's judgment.

### What I looked at before designing (orchestrator only; generator agents never see these)
- AGENTS.md (James's house standard), plans/week-01-classroom-review.md, plans/week-01-tiling-redesign.md, the current Week 1 PDFs (gold), Week 1 archive-v1 (pre-edit AI), Week 7 current packet, year-1 handouts (human).
- Did NOT read James's parallel experiment in experiments/worksheet-genlab/ (kept independent).
- research/R1-sources.md: math-circle books and collections (Rozhkovskaya, Math Circle by the Bay, Math for Love, JRMF, EFM, year-1 handouts). Key: statements 15–60 words; one explicit ask that names the output; plan more than fits; K–1 is capable when posed with objects and few words, read aloud; trick questions and long reading fail.
- research/R2-web.md: slop taxonomies (Antislop, LAMP, Wikipedia signs), LLM-as-judge methodology, workflow evidence. Key: LLM judges are weak at noticing slop and prefer familiar (low-perplexity) text; "don't do X" partially works and can prime; self-critique helps only with specific, correct feedback; critics nitpick; revisions homogenize; checklist/defect-counting judges are more reliable than holistic Likert; pairwise is discriminative but gameable; plant known-good/known-bad anchors.

### Design choices (and why)
1. Two outlines (A tiling, B games). Outlines give the mathematical kernels + materials + a one-line suggested emphasis per band — the level of the upstream ideation James says already works. They deliberately do not give per-band problem lists, so the experiment tests the worksheet-writing step where the slop appears.
2. All agents Opus. Fable was rate-limited on probe. Consequence: judge and generator share a model family, so self-preference is uncontrolled by panel diversity; mitigations are anchors (human-edited gold, seeded-defect variants), a deterministic lint layer, and James's blind ranking at the end.
3. Generators work only in their own run directory in the cloud container and are told not to read anything else; gold PDFs exist elsewhere on the machine, so isolation is by instruction (post-hoc check: look for gold-specific artifacts).
4. Prompts are delivered as a file (PROMPT.md) in the run directory; the Agent call just says "read and follow". Same mechanism for every arm, keeps exact prompts on disk for provenance (sha recorded in PROMPT.md.meta.json).
5. Prompt blocks: naive-ask (James's naive prompt, verbatim apart from naming the three levels), spec (positive house standard with reasons, written in plain prose to match the target register), neg (category-level do-not list, with a few quoted examples as James would write them), exemplars (7 human problems from R1 sources + James's year-1 handouts, topics unrelated to either outline).
6. Common harness for all writers: file locations, toolchain, render-and-look QA, isolation. No style content.

### Eval design (EVAL-v1, to be frozen after the pilot)
- Layer A (deterministic, tools/lint.py): pages, words, problems, surface tells (exclamations, em dashes, emoji, encouragement/meta/label lexicons, not-X-but-Y regexes, bold/large lines of 3+ words). Descriptive only.
- Layer B (primary): AUDIT judge = the organizer's strict editor. Reads every page image + text, works every problem, logs every edit with category and minutes (1/3/10/30), estimates minutes of work for quick/typical child, scores 0–5 on 8 dimensions. Two independent audit runs per packet. PRIMARY METRIC = estimated organizer edit minutes (summed over bands, mean of the two audits; recomputed from the edit list, not the judge's arithmetic). Secondary: readiness (0–5), minutes of work per band.
- Layer D: PAIR judge, whole packet vs a fixed anchor per outline (GOLD-A for A, ASTRA-B for B), both orders, per-band + overall verdicts. Inconsistent order pairs count as ties.
- Judge standard = James's own AGENTS.md text, condensed, plus his three stated complaints — deliberately not my generator "spec" wording, so spec-following arms are not graded against their own prompt.
- Validation before freeze: GOLD-A must beat seeded variants VAR-SLOP-A (14 injected slop/scaffolding items, recall measured against anchors/VAR-SLOP-A.key.json) and VAR-THIN-A (K–1 cut to 2 trivial tasks, 2–3 and 4–5 truncated) in both orders, and audits must log the injected defects.

### Arms planned (wave 1, single agent)
- A0 NAIVE: James's naive prompt + outline + context + harness.
- A1 NAIVE+NEG: A0 + do-not list (James's "anti-slop instructions" suggestion).
- A2 SPEC: positive house standard (reasons, volume, K–1, concreteness), no do-not list, no examples.
- A3 FULL: SPEC + NEG + EXEMPLARS.
Wave 2 (orchestration) will be built on the drafts of the best wave-1 arm so that post-processing stages are compared on identical drafts (paired design).

## 2026-09-30 evening — Vertical slice, judge validation, eval frozen

- Fable probe failed (usage limit) -> all agents Opus.
- Installed texlive-fonts-extra in the container so the gold sources compile (sourcesanspro) and seeded variants match gold typography exactly.
- A0-A (naive, tiling) ran end to end: 254k subagent tokens, 24 min, 15 pages. Output is polished and colorful with the classic tells: activity titles on every page ("How many greens?", "Ribbons: a secret code"), "Talk about it." boxes, "Your turn!", "Coming up. … find a secret code hiding inside every tiling", "Tips. … Stuck? Look for…", Name fields, exclamation marks. Mathematically strong (L-score parity proof for flips, 20-tiling big hexagon, 3D cube view).
- Pilot audit (80 dpi) worked but the judge spent many turns cropping/zooming diagrams -> bundles moved to 110 dpi and a line added telling judges the images are legible. Then the eval was validated (see eval/EVAL-v1.md) and FROZEN before any wave-1 packet was judged.
- Wave 1 generation finished (8 runs, ~15–25 min each, 157k–255k subagent tokens each).
- Lint on wave 1 (before any judging): any style instruction kills surface tells. Tells/100 words: A0 naive 2.0 (A) and 4.5 (B: 69 bold headings, 20 exclamations); A1 (do-not list only) 0.0 / 0.08; A2 (positive spec) 0.09 / 0.3; A3 (spec+neg+examples) 0.26 / 0.43; GOLD-A 0.0; ASTRA-A 3.7; ASTRA-B 0.08.
  Interpretation: surface slop is the easy part; a short list or a positive standard removes it. Remaining differences will be in substance, volume, concreteness, level, and subtler voice.
- Metric choice (pre-registered from validation only): AQI primary; edit minutes demoted (noisy). Pairwise design changed from "every arm vs one anchor" to: wave-1 round robin within each outline (both orders); wave-2 each pipeline vs its own input draft (paired A/B); finalists vs anchors at the end. Reason: A0 already beats GOLD-A, so "vs GOLD" would saturate.

## 2026-09-30 night — Wave 1 results (single-agent prompt variants)

AQI (primary, mean of 2 audits; 0–5) and pairwise round robin among the instructed arms (both orders):

| Packet | AQI A (tiling) | AQI B (games) | mean AQI | voice | SLOP edits/packet (A, B) | edit min (A, B) |
|---|---|---|---|---|---|---|
| A0 naive | 3.60 | 3.65 | 3.63 | 2.33 / 2.33 | 15.5, 25.5 | 164, 169 |
| A1 naive + do-not list | 4.35 | 4.31 | 4.33 | 4.50 / 4.50 | 3.5, 3.0 | 66, 52 |
| A2 positive standard | 4.23 | 4.46 | 4.35 | 4.33 / 4.83 | 2.5, 2.0 | 72, 23 |
| A3 standard + do-not + examples | 4.42 | 4.31 | 4.37 | 5.00 / 4.17 | 0.0, 5.5 | 35, 31 |
| GOLD-A (human-edited Week 1) | 3.40 | — | | 3.50 | 8.5 | 181 |
| ASTRA-A (Week 1 v1, pre-edit) | 1.88 | — | | 1.00 | 37 | 312 |
| ASTRA-B (Week 7 current) | — | 3.10 | | 3.00 | 8.5 | 234 |

Pairwise (wave-1 round robin, instructed arms): A3 beat A1 and A2 in both outlines, in both orders (8/8 judgments). A1 beat A2 in A (2/2); A1 vs A2 in B split by order (tie). Order consistency 5/6 pairs.

Findings:
1. Any style instruction is the single biggest lever. Naive -> instructed raises AQI by ~0.7 and cuts judge-estimated edit time by 60–85%. A one-paragraph do-not list (A1) already captures most of it; surface tells drop to ~0.
2. Among instructed prompts, differences in AQI are within audit noise (replicate spread up to 0.46), but the pairwise judge consistently prefers A3 (standard + do-not + human exemplars). Its K–1 pages are the reason most often cited (a strategy game, "find all the ways", real impossibility tasks, ~40+ min of work).
3. The AI judge rates every instructed packet well above the human-edited GOLD-A (4.2–4.5 vs 3.40). Main cited GOLD weaknesses: K–1 is thin (~19 min for a quick child), 2–3 Problem 1's impossible boards have odd area so the coloring idea isn't needed, 4–5 page 2 prints all six tilings right after asking children to find them. This is the most important thing for James's blind ranking to check.
4. Residual defects in A3 drafts (from the audit edit lists): small clarity issues (ambiguous cross-references such as "the hexagon board" when two hexagon boards exist), recording space too small for children's drawing, a subtle math edge case (a 4-flip round trip is impossible from the two extreme tilings), a few narration sentences, and a footer id (my generator spec omitted the "/ <id>" that James's standard includes — a systematic 1-minute FORMAT edit on every spec arm; noted, not fixed, so arms stay comparable).
5. Generator prompts in wave 1 used a relative run path ("runs/A3-A-r1"); agents resolved it correctly. Stage prompts from wave 2 on use absolute paths.

Wave-1 winner for building wave 2: A3 (best by pairwise 8/8, and highest mean AQI across outlines, 4.37 vs 4.35/4.33). Pre-registered rule satisfied by both metrics.

## Wave 2 design (orchestration on top of A3)

Post-processing arms all start from the SAME A3 draft per outline (paired design: any difference is caused by the added stages). Critique source varies; the reviser is held fixed (minimal-edit policy) except in B1, which tests James's proposed naive pipeline end to end.
- B1 GENERIC: critic "do a thorough, adversarial review" -> reviser "revise the packet to address the review".
- B2 CHECKLIST: critic with a 7-point checklist (math, clarity, workspace, level/amount, giving away thinking, words that do no work, format), evidence + smallest fix required, MUST/SHOULD, "no change needed" explicitly allowed -> minimal-edit reviser (verify each issue, smallest change, no new text unless required, re-solve, notes of fixed/skipped).
- B3 SIM-CLASSROOM: critic simulates the actual ten children (cast from the roster; parent reads K–1 aloud verbatim; children read literally, can't draw small figures, get bored by copying) with a running clock -> minimal-edit reviser.
- B4 MATH-VERIFIER: independent mathematician re-solves everything with code, checks diagrams vs text and edge cases -> minimal-edit reviser.
- B5 PLAN-FIRST: mathematician designer writes design.md (exact instances, verified answers, per-problem time budget >=40 min quick child per band, K–1 real math) -> writer with the A3 prompt + "write from this design".
Caveat recorded in advance: B2's checklist and the eval audit both derive from James's standard, so B2 is partly "optimizing toward the judge". B3/B4 use different signal sources, and James's blind ranking is the external check.
Eval for wave 2: 2 audits per packet + pairwise vs the A3 base draft (both orders).

## 2026-10-01 early — Wave 2 results (orchestration on the A3 drafts)

All post-processing arms start from the identical A3-r1 draft per outline. Pairwise = arm vs its own A3 base, both orders (1 = arm wins both).

| Arm | pairwise vs base A / B | AQI A (Δ) | AQI B (Δ) | edit min A / B (base 35 / 31) | words Δ A / B |
|---|---|---|---|---|---|
| B1 generic review -> generic revise | 1.0 / 1.0 | 4.60 (+0.18) | 4.56 (+0.25) | 12.5 / 27 | +35 / +32 |
| B2 checklist review -> minimal revise | 1.0 / 1.0 | 4.52 (+0.10) | 4.52 (+0.21) | 20.5 / 23.5 | +29 / +3 |
| B3 simulated classroom -> minimal revise | 1.0 / 1.0 | 4.54 (+0.12) | 4.67 (+0.36) | 18 / 13.5 | -37 / +84 |
| B4 math verifier -> minimal revise | 1.0 / 1.0 | 4.38 (-0.04) | 4.50 (+0.19) | 32.5 / 21.5 | 0 / +30 |
| B5 plan-first (designer -> writer), fresh draft | 0.5 / 1.0 | 4.31 (-0.11) | 4.48 (+0.17) | 35 / 23 | +226 / -95 |

Observations:
1. One critique -> revise pass reliably helps: B1–B4 won all 16 of 16 paired judgments against their own base drafts, in both orders. The effect is modest ("nearly identical, X slightly better"; strength 1 in most, 2 in a few) but consistent, and it roughly halves the judge-estimated remaining edit time.
2. No verbosity creep: revisions changed the word count by -37 to +84 words on ~1,100–1,500-word packets. The minimal-edit policy and the generic reviser behaved similarly here; Opus's generic reviser did not over-edit.
3. The generic "do a thorough adversarial review" critic was excellent (2,400–2,900-word reviews with code-verified answers). It found the most consequential issue in A: the outline's 2x/3x Upscale blocks would trivialize every "fewest pieces" problem, and no page said "small blocks only". It also found the impossible 4-flip round trip from the two extreme tilings. James's suggested "just do a review" baseline is strong when the reviewer is a frontier model with tools.
4. Which critic is best is not resolvable at n=1 per outline: AQI differences among B1–B3 (0.02–0.15) are within audit noise. B3 (simulated classroom) had the largest gain on games (+0.36) and the lowest remaining edit time there; B1 led on tiling.
5. The math verifier (B4) found few issues because the A3 writers had already verified their answers with code; its main catch on A duplicated B1's. Its value is insurance, not average quality.
6. Plan-first (B5) did not beat the single-agent A3 writer: tied on A (its 30-page tiling packet ran long; K–1 Problem 3 misworded), better on B. The designer+writer split produced more pages, not better ones. Not worth the extra cost on this evidence.
7. Cost (subagent tokens, final context per agent): critics 120–180k, revisers 110–165k, designer 195–295k, design-writers 170–300k, single-prompt writers 155–255k.

## Wave 3 design (final approach C1 + replication)

- C1 TRIPLE-CRITIC: adversarial review + simulated classroom + math verifier (three independent critics) -> one minimal-edit reviser that adjudicates overlapping/conflicting reports. On r1 drafts it reuses the existing B1/B3/B4 reviews (so C1-r1 differs from B1/B3/B4 only in having all three reports).
- Replication: fresh A3 drafts (A3-A-r2, A3-B-r2, identical prompt sha). On r2, run C1 (three new critics) and B1 (generic reviser reading the same new generic review). This measures draft-to-draft variance and whether the pipeline gain holds on a new draft, and gives a direct C1 vs B1 comparison on r2.
- Anchor checks: A3-r1 and C1-r1 vs GOLD-A (tiling) and vs ASTRA-B (games), both orders.

## 2026-10-01 — Wave 3 results (C1 triple-critic, replication, anchors)

Paired comparisons (both orders; 1.00 = first-named packet won both judgments):

| Comparison | tiling (A) | games (B) |
|---|---|---|
| C1-r1 (triple critic -> minimal reviser) vs its A3-r1 base | 1.00 | 1.00 |
| C1-r2 vs its A3-r2 base | 1.00 | 1.00 |
| B1-r2 (generic review -> generic revise) vs its A3-r2 base | 1.00 | 1.00 |
| B1 vs C1, r1 drafts | 1.00 (B1) | 1.00 (B1) |
| B1 vs C1, r2 drafts | 1.00 (B1) | 1.00 (B1) |
| A3-r1 vs anchor (GOLD-A / ASTRA-B) | 1.00 (A3 beats GOLD, strength 2–3) | 1.00 (A3 beats ASTRA-B, strength 3) |
| C1-r1 vs anchor | 1.00 (strength 2–3) | 1.00 (strength 2–3) |

AQI: A3 r1 -> r2 replicate moved 4.42 -> 4.58 (A) and 4.31 -> 4.52 (B). C1-r2 4.56 (A), 4.67 (B); B1-r2 4.40 (A), 4.65 (B).

Observations:
1. Review -> revise is robust: across all 14 post-processing comparisons with their own base drafts (B1–B4, C1 on r1; B1, C1 on r2), the revised packet won both orders every time (28/28 judgments).
2. More critique is not better. The plain generic pipeline (B1) beat the triple-critic pipeline (C1) in all four head-to-heads (8/8 judgments, all "slight"). C1's minimal-edit reviser skipped 8–12 of 23–27 reported issues ("would make the page worse", duplicates) and never added content; B1's generic reviser addressed nearly everything and sometimes added problems or recording pages. With a strong model, "address the review" outperformed a conservative edit policy. On r2 the generic reviser did grow the tiling packet (2–3: 8 -> 9 pages, 4–5: 8 -> 10), so length should be watched.
3. Draft-to-draft variance is as large as most arm differences. The same A3 prompt run twice differed by 0.16–0.21 AQI, the same size as the A1/A2/A3 spread and the post-processing gains measured by AQI. Paired pairwise comparisons on the same draft are the only signal here that is clearly above noise.
4. The verifier critic earned its keep on r2: it found that the K–1 hexagon game in A3-A-r2 has the opposite answer under the page's own placement rule — a real error that would have reached children. Generic critics flagged the same rule gap.
5. Residual defects after a review pass are small and mostly clarity/layout: about 6 min CLARITY, 4 LAYOUT, 4 FORMAT (my spec omits the footer id), 2 SLOP per audit. The remaining slop is a recognizable kind: prose that narrates the diagram or restates the obvious ("Here are seven rules.", "The blank small drawings of boards are for recording.").
6. Reliability over the whole experiment: AQI ICC 0.975 (31 packets x 2 audits); pairwise overall winner identical in both orders for 32/34 pairs.
7. Cost: 176 subagents in total; 8.7M output tokens, 56M cache-write and 1.24B cache-read input tokens. Judges (131 calls) were ~60% of the total. Per outline, a single writer is ~116k output tokens; adding one critic + one reviser is ~1.8x the writer's cost; three critics ~2.9x; plan-first ~2.4x.

## Human blind review prepared
human-review/: blind-k-1.pdf, blind-grades-2-3.pdf, blind-grades-4-5.pdf, FORM.md. Four Week 1 tiling packets labeled W/X/Y/Z: GOLD-A, A0-A-r1 (naive), A3-A-r1 (best single prompt), B1-A-r1 (single prompt + generic review/revise). The letter key and the AI judge's pre-registered rankings of these four are in eval/private/human-review-key.json, held back from the device sync until James has ranked.

## 2026-10-01 — James's blind ranking (Week 1 tiling, four packets)

Key: W = GOLD-A (his edited Week 1), X = A3-A-r1 (best single prompt), Y = B1-A-r1 (A3 + generic review/revise), Z = A0-A-r1 (naive).

James, verbatim: "K-1: Z felt too sloppy, X and Y are very similar to each other and good, and W I think is probably the input and I thought fine (I agree X/Y are better). 2-3: Similar to above: Z sloppy, X/Y similar and good, W was input. I think W is pretty good here but think X/Y are improved and keep what's good from W. 4-5: Same as above. The formatting is much better in X/Y than in W. I would bring X or Y (I find them very similar) to a session over W."

His order in every band: X = Y > W > Z. The judge's pre-registered AQI order: Y > X > Z > W (K–1, 2–3), Y > X > W = Z (4–5).

Agreement on the 15 untied human comparisons (5 pairs x 3 bands):
- AQI: 12/15 concordant, 2 discordant, 1 tie. Every miss is W vs Z.
- human_voice: 15/15, and it scores X = Y = 5.0, matching his "very similar".
- SLOP edit count: 15/15. Edit minutes: 13/15. Substance index: 12/15. Readiness: 12/15 (1 discordant, 2 ties).
- Pairwise judge (pairs actually judged): A3 beat GOLD in all bands (agrees); A0 vs GOLD the judge preferred the naive packet in K–1 and 4–5 (disagrees).

What this says:
1. The headline findings survive the human check. Instructed single-prompt output beats naive output, and James would take the AI packets (X, Y) to class over his own edited Week 1.
2. The judge's one systematic error is weighting slop too lightly: it ranked the sloppy-but-rich naive packet above his clean Week 1, and he ranks them the other way. The PAIR prompt's framing ("he will have only about fifteen minutes per band to edit") and the audit's 1-minute price for deleting a line both told the judge clutter is cheap. For James it is not.
3. The review pass is not visible in a skim: he found X and Y "very similar", matching the judge's "slight" verdicts. Its value is in specific in-class fixes (for example Y adds "Use only the small blocks", which X lacks while 2x/3x blocks are on the table), not overall impression.
4. Post hoc, the voice score alone reproduced his full ordering. With four packets and one rater this is suggestive, not established; a v2 eval should report voice as a co-primary (or gate on it) and drop the "fifteen minutes of editing" framing. Per the experiment's rules this is a recommendation for a new eval version, not a change to EVAL-v1.
