# Worksheet workflow

How agents draft a week's student worksheets (K–1, grades 2–3, grades 4–5). This is the workflow that did best in the October 2026 experiment, [experiments/worksheet-genlab-opus5.5/REPORT.md](../experiments/worksheet-genlab-opus5.5/REPORT.md). In a blind review, the organizer preferred its Week 1 tiling packets to his own hand-edited Week 1, and ranked the naive single-prompt version last.

## The three stages

Each stage runs in a fresh agent with only its stage file as instructions. The reviewer must not be the agent that wrote the draft.

1. **Writer** (`PROMPT.md`). It gets the outline, the session context, the organizer's standard for student pages (`blocks/spec.md`), a do-not list (`blocks/neg.md`), seven human-written example problems (`blocks/exemplars.md`), and technical notes. It writes `draft/k-1.pdf`, `draft/grades-2-3.pdf` and `draft/grades-4-5.pdf`, with sources in `draft/src/`.
2. **Reviewer** (`CRITIC.md`). Its instruction is one sentence: "Do a thorough, adversarial review of the packet." It reads the brief and the draft and writes `review.md`. In the experiment this plain reviewer did as well as or better than a checklist reviewer, a simulated-classroom reviewer, and a combination of three reviewers.
   - Optional **math check** (`CRITIC-MATH.md`). It re-solves every problem with code and writes `review-math.md`. Worth running for weeks whose answers come from enumeration (games, tilings, counting). In the experiment it caught a K–1 game whose answer was backwards.
3. **Reviser** (`REVISE.md`). It is told to "revise the packet to address the review." It copies `draft/src/` to `final/src/` and builds `final/*.pdf`.

The review pass gives a small improvement that is hard to see when skimming. Its value is specific fixes, such as "use only the small blocks" when 2× and 3× blocks are on the table, or an impossible flip task. It costs about 1.8 times as much as the writer alone.

## Running it

1. Write the outline: copy `outlines/TEMPLATE.md` to `outlines/week-NN-<topic>.md`. Give the mathematical kernels, a one-line emphasis per band, and the materials, with their physical constraints. Do not list problems; choosing them is the writer's job. `outlines/week-01-tiling.md` and `outlines/week-07-games.md` are the two outlines that were tested.
2. Check that `context.md` matches the current group (roster, adults, shape of the hour).
3. Generate the stage files:
   `python3 worksheet-workflow/make_prompts.py --outline worksheet-workflow/outlines/week-NN-<topic>.md --run tmp/worksheet-runs/week-NN-v1`
4. Run each stage file in a fresh agent, in order: `PROMPT.md`, then `CRITIC.md` (and `CRITIC-MATH.md` if wanted), then `REVISE.md`.
   - Claude Code: start one subagent per stage, with the prompt "Your instructions are in <run>/<STAGE>.md. Read it and follow it exactly."
   - Codex: one `codex exec` call per stage with the same one-line prompt, or a new session per stage.
5. Look at `final/*.pdf`. When it is approved, move the PDFs and sources into `lowell-math-circle-year-2/` following AGENTS.md, and record the packet as unpiloted.

## Notes

- **Keep the files as a set.** The prompts were tested together, and they are written in plain prose on purpose: a prompt's style carries into the pages it produces. If you change one, note the change below.
- **`blocks/spec.md` is the writer-facing version of the student-page sections of AGENTS.md.** If one changes, change the other.
- **No facilitator guide.** The tested workflow produced student pages only. A facilitator guide (hints, solutions, proofs) is a separate step and has not been tested.
- **Outputs are unpiloted.** The AI reviewer and the experiment's judge are the same model family as the writer, and none of these packets has been used with children.

## Changes since the tested version

- 2026-10-01: footer now includes the packet id (`blocks/spec.md`), matching AGENTS.md.
- 2026-10-01: do-not list gained one item on sentences that narrate a diagram or say what the blanks are for. This was the main slop left after a review pass.
- 2026-10-01: paths and isolation notes generalized from the experiment's cloud setup. Each stage file now says which stage it is, so an agent that also reads AGENTS.md doesn't start the workflow again.
- 2026-10-03: `context.md` updated for the eleven children at fixed KK11 / 3333 / 445 tables, the five-minute run, and the lesson of Weeks 1–2 (rules enforced by materials or the other player; partner play; deeper questions late). Nine outlines added (`week-01e-pattern-blocks.md`, `week-03-shuffle-machines.md` … `week-10-bridges.md`) and run with writer, critic, math check and reviser; records in `tmp/worksheet-runs/*-v1/`. Added `guide/GUIDE-TEMPLATE.md`, the untested prompt used afterwards to write each week's adult guide from the final pages; it is not part of the tested set.
