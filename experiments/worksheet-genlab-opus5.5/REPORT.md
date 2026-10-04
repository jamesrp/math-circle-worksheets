# Worksheet generation workflows: findings (genlab-opus5.5)

October 1, 2026. Ten generation approaches, two activity outlines, 31 evaluated packets, 176 subagents, all Opus. The lab notebook is NOTES.md; the frozen eval is eval/EVAL-v1.md; raw numbers are in analysis/.

## Summary

1. **A written house standard in the writer prompt is the biggest lever by far.** Going from your naive prompt to any instructed prompt raised the AI judge's quality index from about 3.6 to 4.2–4.5 (out of 5). It cut the judge's estimate of your editing time from about 165 minutes to 25–70, and removed nearly all surface slop. A one-paragraph do-not list alone (A1) already took surface tells to zero.
2. **The best single prompt combined the positive standard, the do-not list, and seven human-written example problems (A3).** The pairwise judge preferred it to the other instructed prompts in 8 of 8 judgments, mostly for its K–1 pages. On the quality index, the three instructed prompts are within noise of each other.
3. **One review-then-revise pass reliably helps.** In all 14 cases where a review pass was added to a draft, the judge preferred the revised packet in both presentation orders (28/28). The gain is modest ("nearly identical, slightly better") but real. It roughly halves the remaining edit time, and the reviewers caught consequential problems: the 2×/3× blocks trivializing every "fewest pieces" problem, an impossible flip task, and a K–1 game whose answer was backwards.
4. **The plainest pipeline won.** Your suggested "do a thorough adversarial review → revise to address the review" (B1) beat a three-critic pipeline (adversarial + simulated classroom + math verifier, with a conservative reviser) in 4 of 4 head-to-heads. A checklist critic, a classroom simulator, and a math verifier each helped individually, but no more than the generic reviewer did. Plan-first (a designer agent, then a writer) did not help.
5. **Your K–1 complaints are fixable by prompt.** Once the standard said K–1 gets real mathematics and as much to do as the other bands, K–1 packets included impossibility tasks, "find all the ways", fewest-pieces, and a strategy game. The judge's estimate of K–1 work for a quick child rose from 19 minutes (your Week 1) and 30 (naive) to 40–50 with A1 and A3. The positive standard alone (A2) reached only 30–35, so the do-not list and the examples matter for K–1.
6. **Your blind ranking confirms the main result and exposes one judge bias.** You ranked the instructed AI packets (A3 and A3 + review) above your own edited Week 1 in every band, and the naive packet last. The judge agreed on 12 of 15 comparisons. Its only misses were naive vs your Week 1: it scored the sloppy-but-rich naive packet higher, and you did the opposite. The judge's voice score alone matched your full ranking. So for you, slop costs more than the judge assumed; a future eval should weight voice more heavily (details below).
7. **The review pass is invisible in a skim.** You found A3 and A3 + review "very similar", which matches the judge's "slightly better". Its value is specific in-class fixes, for example adding "Use only the small blocks" while 2×/3× blocks are on the table, rather than a better overall impression.

## What was tested

**Inputs.**
- Outline A: Week 1 tiling, with two kernels: the up/down coloring obstruction and hexagon rhombus tilings with flips and ribbons.
- Outline B: Week 7 take-away games, with backward induction, periodicity, and Sprague–Grundy.
- Each outline gives the kernels, the materials, and one line of suggested emphasis per band, but no problem lists.
- Each run produced three student PDFs (K–1, 2–3, 4–5) and no facilitator guide.
- Writers never saw the existing worksheets. They worked only in their own run folder in the cloud workspace.

**Approaches** (prompts in prompts/blocks and prompts/stages; exact assembled prompts are saved in each run folder):

| ID | Workflow | Agents per outline |
|---|---|---|
| A0 | Your naive prompt, plus the outline and session context | 1 |
| A1 | A0 plus a do-not list (titles, encouragement, meta-talk, cute framing, "not X but Y", hints, automatic follow-ups, sub-steps, a thin K–1, vague tasks) | 1 |
| A2 | Positive house standard (who reads the page, what a page contains, substantial problems, method left to the child, enough work for 40 minutes, K–1 gets real mathematics, concreteness, plain language), written in plain prose with reasons | 1 |
| A3 | A2 + do-not list + 7 human example problems (year-1 handouts, Rozhkovskaya, Math Circle by the Bay, family math puzzles; unrelated topics) | 1 |
| B1 | A3 draft → "do a thorough, adversarial review" → "revise the packet to address the review" | 3 |
| B2 | A3 draft → 7-point checklist critic (evidence + smallest fix, "no change needed" allowed) → minimal-edit reviser | 3 |
| B3 | A3 draft → simulated classroom (your actual ten children cast realistically, parent reading K–1 aloud, running clock) → minimal-edit reviser | 3 |
| B4 | A3 draft → independent math verifier (re-solves everything with code) → minimal-edit reviser | 3 |
| B5 | Plan-first: mathematician designer (exact instances, verified answers, time budget) → writer with the A3 prompt | 2 |
| C1 | A3 draft → three critics (B1 + B3 + B4 critics) → one minimal-edit reviser that adjudicates | 5 |

B1–B4 and C1 were applied to the same A3 draft per outline, so their differences come only from the added stages. A3 was then run a second time (r2), and B1 and C1 were repeated on the new drafts.

**Evaluation** (frozen before any wave-1 packet was judged; see eval/EVAL-v1.md):
- Judges see rendered page images and extracted text, under random packet IDs.
- Judges score against your AGENTS.md student-page and design guidance, condensed, plus your three complaints. They were never shown my generator prompt wording.
- The audit judge plays your strict editor. It logs every edit with a category and minutes, estimates the minutes of work for a quick child, and scores eight 0–5 dimensions per band. Each packet got two independent audits.
- Primary metric: the quality index (AQI), the mean of those 0–5 scores.
- The pairwise judge picks which packet you should take to class, per band and overall. Each comparison is judged in both orders.
- Validation: the judge caught 14 of 14 slop items seeded into your Week 1 (both audits). It ranked your Week 1 above its slop-seeded and thinned variants on every band, in both orders. AQI test–retest reliability was 0.975, and 32 of 34 pairwise comparisons gave the same winner in both orders.
- I had planned edit minutes as the primary metric and demoted it during validation, before seeing any arm results. It was too noisy, and it priced each slop line at one minute.

## Results

Quality index (AQI, 0–5; mean of two audits), human voice score, and the judge's estimate of your edit minutes:

| Packet | AQI tiling | AQI games | Voice (A / B) | Edit min (A / B) |
|---|---|---|---|---|
| A0 naive | 3.60 | 3.65 | 2.3 / 2.3 | 164 / 169 |
| A1 + do-not list | 4.35 | 4.31 | 4.5 / 4.5 | 66 / 52 |
| A2 positive standard | 4.23 | 4.46 | 4.3 / 4.8 | 72 / 23 |
| A3 standard + do-not + examples (r1 / r2) | 4.42 / 4.58 | 4.31 / 4.52 | 5.0 / 4.2–4.7 | 35 / 31 |
| B1 + generic review/revise (r1 / r2) | 4.60 / 4.40 | 4.56 / 4.65 | 4.3–5.0 | 12 / 27 |
| B2 + checklist review | 4.52 | 4.52 | 4.8 / 5.0 | 21 / 24 |
| B3 + simulated classroom | 4.54 | 4.67 | 4.8 / 5.0 | 18 / 14 |
| B4 + math verifier | 4.38 | 4.50 | 4.8 / 4.2 | 33 / 22 |
| B5 plan-first | 4.31 | 4.48 | 4.3 / 4.7 | 35 / 23 |
| C1 three critics (r1 / r2) | 4.56 / 4.56 | 4.44 / 4.67 | 4.3–5.0 | 16 / 25 |
| Your Week 1 (GOLD-A) | 3.40 | — | 3.5 | 181 |
| Astra Week 1 v1, pre-edit | 1.88 | — | 1.0 | 312 |
| Astra Week 7 current | — | 3.10 | 3.0 | 234 |

Head-to-head (both orders):
- A3 beat A1 and A2 on both outlines (8/8 judgments).
- Every review-pass packet beat its own base draft (28/28 judgments).
- B1 beat C1 on both outlines, for both drafts (8/8).
- A3 and C1 each beat your Week 1 and Astra's Week 7 with strength 2–3 of 3.

**Noise.** Running the identical A3 prompt twice changed AQI by 0.16–0.21. That is as large as the differences among the instructed prompts and among the review pipelines. Only the large effects stand out from it: the naive prompt versus any instructed prompt, and a paired review pass versus none. The ranking within those groups (A1/A2/A3; B1/B2/B3/B4) would need more replicates to settle on AQI.

**Leftover issues after a review pass.** Per packet, the judge still logs about 6 minutes of clarity edits, 4 of layout, 4 of format, and 2 of slop. Part of the format time is because my standard leaves the "/ <id>" off the footer. The slop that survives is a recognizable kind: prose that narrates the diagram or announces the obvious. Examples: "Here are seven rules." and "The blank small drawings of boards are for recording."

## What I would use now

1. **Writer:** the A3 prompt, which is prompts/blocks/spec.md + neg.md + exemplars.md, assembled by tools/make_prompt.py. Add the footer id to spec.md. Consider one more do-not item aimed at the leftover slop: "no sentences that describe the diagram or say what the blanks are for."
2. **One review pass:** a fresh agent with the brief, the PDFs, the sources, and code tools gets "Do a thorough, adversarial review" (prompts/stages/critic-generic.md). A reviser then gets "Revise the packet to address the review" (reviser-generic.md). This costs about 1.8× a single writer.
3. **For problems whose answers depend on enumeration** (games, tilings, counts): optionally add the math-verifier critic. Its most important catch, a K–1 game whose answer was backwards under the page's own rule, was only partly flagged by the generic critic (as a missing rule).
4. Watch length when the reviser is generic: on one draft it added two pages to grades 4–5.

Skip plan-first, simulated-classroom-only, and conservative minimal-edit revisers on this evidence. None beat the plain pipeline.

## Caveats

- **Single judge family.** Fable hit its usage limit on the first probe, so every writer, critic, and judge was Opus. LLM judges are known to favor text that resembles their own, and nothing here controls for that. The seeded-defect check shows the judge sees slop; it does not show the judge weighs slop the way you do. Its stated rule of thumb was that clutter can be deleted in minutes while missing content cannot be added in fifteen.
- **Two outlines, one or two drafts each.** The findings that hold across both outlines and both drafts are the instruction effect and the review-pass effect. Treat everything finer as a hypothesis.
- **Not classroom-tested.** All of these AI packets are unpiloted. The judge's "minutes of work" are estimates.
- **The judge standard and the B2 checklist come from the same AGENTS.md text.** B2 is partly optimized toward the judge. B1 and B3 use different signals and did as well.

## Your blind ranking (October 1)

Key: W = your edited Week 1, X = A3 (best single prompt), Y = A3 + generic review/revise (B1), Z = naive prompt (A0). Your order in every band: X = Y > W > Z, and you would take X or Y to a session over W.

The judge's pre-registered order was Y > X > Z > W (K–1 and 2–3) and Y > X > W = Z (4–5). Agreement on the 15 comparisons you didn't call ties:

| Metric | Agrees with you |
|---|---|
| Quality index (AQI, the pre-registered primary) | 12/15 (misses: naive vs your Week 1, in 2 bands, tie in the third) |
| Voice score alone | 15/15, and it ties X and Y as you did |
| Count of slop edits | 15/15 |
| Judge's edit minutes | 13/15 |
| Pairwise judge (pairs actually judged) | A3 beat your Week 1 in every band (agrees); naive beat your Week 1 in K–1 and 4–5 (disagrees) |

Interpretation:
- The judge's taste matches yours except on how much slop costs. My judge prompts told it so, in effect: the pairwise prompt assumed fifteen minutes of editing per band, and the audit priced each deleted line at one minute. Both made clutter look cheap.
- The voice score reproducing your ranking is suggestive only: four packets, one rater, chosen after the fact.
- For a next eval version: report voice as a co-primary or use it as a gate (rank by AQI only among packets with voice ≥ 4.5), and drop the "fifteen minutes" framing. Under the experiment's rules this would be EVAL-v2, with everything re-judged, rather than a patch to v1.
- Nothing in your ranking changes the recommendations above. It strengthens the first one: the instructed prompt is what turned Z into X.

## Cost

176 subagents. 8.7M output tokens; 56M cache-write and 1.24B cache-read input tokens. Judging was about 60% of the total. A leaner eval for future rounds: one audit per packet plus paired comparisons only for the questions being asked. AQI is reliable enough (0.975) that a second audit adds little.

## Files

- NOTES.md: lab notebook (design decisions, every wave's results, interpretations)
- STATE.md: checkpoint and resume pointer
- eval/EVAL-v1.md: frozen eval, validation, metric pre-registration; eval/prompts/ for judge prompts
- prompts/: writer blocks and stage prompts; inputs/: the outlines, context, harness
- runs/<ARM>-<A|B>-r<k>/: each run's prompt, reviews, revision notes, sources, final/ PDFs
- analysis/results.json, analysis/packets.csv: all metrics and pairwise results
- research/R1-sources.md (math-circle books), research/R2-web.md (slop, LLM judges, workflows)
- human-review/: blind booklets and FORM.md; analysis/human-review.json: your ranking and the agreement scores
