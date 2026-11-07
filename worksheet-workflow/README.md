# Worksheet workflow

How agents draft a week's student worksheets (K–1, grades 2–3, grades 4–5). This is the workflow that did best in the October 2026 experiment, [experiments/worksheet-genlab-opus5.5/REPORT.md](../experiments/worksheet-genlab-opus5.5/REPORT.md). In a blind review, the organizer preferred its Week 1 tiling packets to his own hand-edited Week 1, and ranked the naive single-prompt version last.

## The stages

Each stage runs in a fresh agent with only its stage file as instructions. The reviewer must not be the agent that wrote the draft.

1. **Writer** (`PROMPT.md`). It gets the outline, the session context, the organizer's standard for student pages (`blocks/spec.md`), a do-not list (`blocks/neg.md`), seven human-written example problems (`blocks/exemplars.md`), and technical notes. It writes `draft/k-1.pdf`, `draft/grades-2-3.pdf` and `draft/grades-4-5.pdf`, with sources in `draft/src/`.
2. **Reviewer** (`CRITIC.md`). Its instruction is one sentence: "Do a thorough, adversarial review of the packet." It reads the brief and the draft and writes `review.md`. In the experiment this plain reviewer did as well as or better than a checklist reviewer, a simulated-classroom reviewer, and a combination of three reviewers.
   - Optional **math check** (`CRITIC-MATH.md`). It re-solves every problem with code and writes `review-math.md`. Worth running for weeks whose answers come from enumeration (games, tilings, counting). In the experiment it caught a K–1 game whose answer was backwards.
3. **Kid-fit review** (`CRITIC-KIDS.md`, added November 5, 2026 and not yet part of a full tested run). A fresh agent asks whether children at these tables will enjoy the packet and manage it themselves. It does not read `review.md`, and does not look for other reviews of the week. It checks for the five patterns that [plans/review/KID-FIT-REVIEW.md](../plans/review/KID-FIT-REVIEW.md) found behind most weak weeks:
   - a hands-on start that turns into record-keeping;
   - precision children don't have;
   - a procedure instead of choices;
   - a surprise that is told, not felt;
   - an adult who runs it.

   It rates each band's activity and page separately (strong, workable, weak or skip), and holds K–1 to its own bar. It writes `review-kids.md`, starting with a summary table, and marks fixes that need a new activity "outline: for the organizer" instead of inventing one. Like any cold review, it is a filter, not a pilot. In that review, chip firing's pages were rated weak, but it was a hit when run as play, and the lamp puzzles were rated workable but flopped on paper.
3b. **Adult cold read** (`CRITIC-ADULT.md`, added November 7, 2026 and not yet part of a full run). A fresh agent reads only the band PDFs, as a parent volunteer handed them ten minutes before the session, and says whether an adult can tell from page 1 what the children are trying to do, what each word means and what goes in each space. It writes `review-adult.md`, starting with a summary table, and lists located page fixes; gaps that belong with the adults are marked "for the adult card". It may run alongside the other reviewers. Run it once more, in a fresh agent, after the reviser: it then reads `final/` and writes `review-adult-final.md`, and any blocking gap is fixed before the packet is presented. It came from the [adult cold-read pilot](../plans/review/ADULT-READ-PILOT.md), where the organizer could not follow Weeks 24 and 34 at a glance and nothing in the workflow read the pages as an adult.
4. **Reviser** (`REVISE.md`). It is told to "revise the packet to address the review." It copies `draft/src/` to `final/src/` and builds `final/*.pdf`. Where `review-kids.md` rates an activity above its page, it changes the page and keeps the activity. It leaves fixes marked for the organizer undone and names them.

The review pass gives a small improvement that is hard to see when skimming. Its value is specific fixes, such as "use only the small blocks" when 2× and 3× blocks are on the table, or an impossible flip task. It costs about 1.8 times as much as the writer alone.

## Running it

1. Write the outline: copy `outlines/TEMPLATE.md` to `outlines/week-NN-<topic>.md`. Give the mathematical kernels, a one-line emphasis per band, and the materials, with their physical constraints. Do not list problems; choosing them is the writer's job. `outlines/week-01-tiling.md` and `outlines/week-07-games.md` are the two outlines that were tested.
2. Check that `context.md` matches the current group (roster, adults, shape of the hour).
3. Generate the stage files:
   `python3 worksheet-workflow/make_prompts.py --outline worksheet-workflow/outlines/week-NN-<topic>.md --run tmp/worksheet-runs/week-NN-v1`
   To write fewer packets, such as K–1 pages for a week whose other bands already exist, add `--bands k-1` (any comma-separated subset of `k-1`, `grades-2-3`, `grades-4-5`).
4. Run each stage file in a fresh agent, in order: `PROMPT.md`, then `CRITIC.md` (and `CRITIC-MATH.md` if wanted), then `CRITIC-KIDS.md` and `CRITIC-ADULT.md`, then `REVISE.md`, then `CRITIC-ADULT.md` again on `final/`. The kid-fit and adult reviewers may run alongside `CRITIC.md`, since they don't read `review.md`.
   - Claude Code: start one subagent per stage, with the prompt "Your instructions are in <run>/<STAGE>.md. Read it and follow it exactly."
   - Codex: one `codex exec` call per stage with the same one-line prompt, or a new session per stage.
5. Look at `final/*.pdf`. When it is approved, move the PDFs and sources into `lowell-math-circle-year-2/` following AGENTS.md, and record the packet as unpiloted.

## Notes

- **Keep the files as a set.** The prompts were tested together, and they are written in plain prose on purpose: a prompt's style carries into the pages it produces. If you change one, note the change below.
- **`blocks/spec.md` is the writer-facing version of the student-page sections of AGENTS.md.** If one changes, change the other.
- **No facilitator guide.** The tested workflow produced student pages only. A facilitator guide (hints, solutions, proofs) is a separate step and has not been tested; the untested guide and materials prompts are in [guide/](guide/README.md).
- **Outputs are unpiloted.** The AI reviewer and the experiment's judge are the same model family as the writer, and none of these packets has been used with children.

## Changes since the tested version

- 2026-10-01: footer now includes the packet id (`blocks/spec.md`), matching AGENTS.md.
- 2026-10-01: do-not list gained one item on sentences that narrate a diagram or say what the blanks are for. This was the main slop left after a review pass.
- 2026-10-01: paths and isolation notes generalized from the experiment's cloud setup. Each stage file now says which stage it is, so an agent that also reads AGENTS.md doesn't start the workflow again.
- 2026-10-03: `context.md` updated for the eleven children at fixed KK11 / 3333 / 445 tables, the five-minute run, and the lesson of Weeks 1–2 (rules enforced by materials or the other player; partner play; deeper questions late). Nine outlines added (`week-01e-pattern-blocks.md`, `week-03-shuffle-machines.md` … `week-10-bridges.md`) and run with writer, critic, math check and reviser; records in `tmp/worksheet-runs/*-v1/`. Added `guide/GUIDE-TEMPLATE.md`, the untested prompt used afterwards to write each week's adult guide from the final pages; it is not part of the tested set.
- 2026-10-25: `make_prompts.py --bands` asks for a subset of the three packets, for K–1 pages to join weeks that have none (the six-year path's gap 1). It rewrites only the sentences that list the packets, in the generated stage files; the block and stage files are unchanged, and without `--bands` the generated text is identical to before (checked on `week-07-games.md`). Single-band runs are untested.
- 2026-10-25: added the untested guide and materials stages in `guide/` (`GUIDE-WRITER.md`, `GUIDE-CRITIC.md`, `MATERIALS.md`, `GUIDE-REVISE.md`, `GUIDE-REVISE-MATERIALS.md`, described in `guide/README.md`), used for the twelve new-theme drafts' facilitator guides and materials files. The tested stage files and blocks are unchanged.
- 2026-11-05: added the kid-fit review stage, `stages/critic-kids.md` (`CRITIC-KIDS.md`, writes `review-kids.md`), between the adversarial review and the reviser, on the organizer's agreement (November 5) to a proposal that followed the [kid-fit review of all 209 weeks](../plans/review/KID-FIT-REVIEW.md). `stages/reviser.md` gained two sentences: it reads `review-kids.md`, keeps an activity rated above its page, and leaves outline-level fixes for the organizer. `make_prompts.py` writes the new stage file. The writer, critic and math-check files are unchanged. The stage was tried on two existing packets, Week 10 and Week 77 (see the test note below). It has not been part of a full writer-to-reviser run.
  - Test note (November 5): each test was a fresh agent working on that week's current PDFs, with its outline as `PROMPT.md`. Week 10, bridges, was strong in every band in the sweep. The stage rated its activity strong in every band and its pages workable, and the K–1 bar was met. Week 77, persistent holes, was weak in the sweep, and only a grades 4–5 packet exists. The stage rated its activity workable and its page weak. So it told the two weeks apart, and it said what to fix on Week 10's pages without downgrading its activity. It rated Week 77's activity a notch higher than the sweep did. Both reviews are in [plans/review/kid-fit/stage-test/](../plans/review/kid-fit/stage-test/). Week 138, busy beaver, wasn't tested because it has no pages yet.
- 2026-10-30: added `guide/RV-GUIDE-WRITER.md`, `guide/K1-GUIDE-WRITER.md`, `guide/WEEK-GUIDE-CRITIC.md`, `guide/WEEK-GUIDE-REVISE.md` and `guide/make_week_runs.py`, the guide stage for drafts that belong to an existing week (return visits and K–1 pages), written October 25 and not yet run to the end.
- 2026-11-07: added the adult cold-read stage, `stages/critic-adult.md` (`CRITIC-ADULT.md`, writes `review-adult.md` on the draft and `review-adult-final.md` on `final/`), on the organizer's yes (November 7) to the [adult cold-read pilot](../plans/review/ADULT-READ-PILOT.md). `stages/reviser.md` gained one sentence: it reads `review-adult.md` and leaves "for the adult card" items to the guide. `make_prompts.py` writes the new stage file and narrows it with `--bands` (checked on `week-07-games.md`, all bands and `--bands k-1`). The writer, critic, math-check and kid-fit files are unchanged. Tried in the pilot as a plain brief on five existing weeks and on the revised Weeks 24 and 34; not yet part of a full writer-to-reviser run.
