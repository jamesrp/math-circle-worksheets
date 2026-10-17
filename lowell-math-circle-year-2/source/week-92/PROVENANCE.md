# Week 92 production provenance

Unpiloted; physical rehearsal untested. Prepared 2026-10-17 under the existing user authorization for additional analysis activities.

The coordinator researched actual corpus PDFs and primary sources, wrote the outline, and generated the unmodified shared workflow prompt set with `make_prompts.py`. Run-specific instructions allowed one consolidated student packet with honest prerequisite-based bands and no forced K–1 variant. They did not change shared templates.

Fresh, isolated agents completed the stages in order: `writer92`, `critic92`, `math92`, and `reviser92`. The writer and reviser were different agents; the coordinator did not author or revise student pages. Each stage used its own checkout and received only its stage-file pointer plus runtime/output instructions. Reviews and the revision response are preserved in `reviews/`. Portable historical copies of the four generated stage files are in the repository plan folder, with local run paths normalized.

The facilitator guide was separately authored by the coordinator after the student draft. It includes theorem-first facts, assumptions and limits, complete answers, proofs, readiness routes, optional later visits, and source attribution. Guide writing is an additional unpiloted step, not an outcome validated by the student workflow.

`check_math.py` was independently authored from the mathematical definitions, without using the writer's code. Finite exact checks support printed examples; the guide supplies general proofs. A separate fresh mathematical reviewer also checked every student problem and edge cases. Final pair verification and portability evidence are recorded in `QA.md`.

Only owned source and output artifacts are included. Consulted books remain outside this package. The cited primary sources supply mathematical context; diagrams and activity sequences were independently authored.

During the writer stage an erroneous outline suggestion that whole interval width might shrink was caught and removed from all active instructions. The corrected guide states and proves that width never decreases; distinct points may nevertheless merge. This correction is retained explicitly to prevent reintroduction. Week 92 is a new uncertainty investigation within the existing atlas GA-10 tent-map theme, not a claim of a wholly new theme.
