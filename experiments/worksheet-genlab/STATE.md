# Worksheet-generation experiment — state and resume instructions

Last updated: 2026-09-29 (session 1). Workspace: `/home/claude/genlab` in the cloud sandbox; mirrored to `~/math-circle/experiments/worksheet-genlab/` on the organizer's Mac by `tools/checkpoint.sh` + device_commit_files.

## How to resume in a fresh session
1. Stage `checkpoint-latest.tar.gz` from `~/math-circle/experiments/worksheet-genlab/` and extract it to `/home/claude/genlab` (`mkdir -p /home/claude/genlab && tar -xzf ... -C /home/claude/genlab`).
2. Re-stage the reference material into `/home/claude/genlab/ref/` only if needed (Week 1 PDFs/sources under `lowell-math-circle-year-2/`, book extracts under `tmp/genlab-extract/`); calibration packets are already inside the tarball under `eval/calibration/`.
3. Read this file's "Progress" section and continue from the first unfinished step. Every run directory records its own progress (`pipeline.json`, `DONE-<stage>.md` markers, `snapshots/`).
4. Rendering for evaluation: `bash tools/render.sh <packet_dir>`; lint: `python3 tools/lint.py <packet_dir>`.

## Fixed design (do not change mid-experiment)
- Outlines: `spec/outlines/{T-tilings,P-pegs,B-bulgarian}.md`
- Task brief `spec/task-brief.md` (tb-v1); guidance `spec/antislop-v1.md`; template `spec/genlab-common.tex`; workflows `spec/workflows.md` (W01–W10) with prompts in `spec/prompts/`; run prep `tools/prep_run.py <W> <T|P|B> <seed>`.
- Evaluation: `spec/eval/judge-absolute.md`, `spec/eval/judge-pairwise.md` (rendered with `tools/prep_judge.py`); fact sheets `notes/facts-*.md`; deterministic lint `tools/lint.py`. FROZEN after calibration passes.
- Model: Fable for all generator roles and the primary judge.

## Progress
- [x] Research memos: `notes/research-orchestration-and-judging.md`, `notes/research-math-circle-books.md`
- [x] Fact sheets: `notes/facts-T-tilings.md`, `notes/facts-P-pegs.md`, `notes/facts-B-bulgarian.md`
- [x] Spec: outlines, task brief, guidance v1, template, workflows W01–W10, prompts, tools
- [x] Calibration packets built: `eval/calibration/{CAL-Ap-recompiled (pre-feedback Week 1), CAL-Bp-recompiled (post-feedback), CAL-C-chrome, CAL-D-truncated, CAL-E-matherror}`
- [x] Calibration judge runs (5 absolute + 8 pairwise) → `eval/calibration/results/`; PASSED; decision recorded in `notes/eval-calibration.md`; EVAL FROZEN
- [x] Vertical slice: W01 on T/P/B end to end incl. absolute judge (q889=T, q359=B judged; q409=P collected, not yet judged)
- [ ] Generation runs: all W × {T,P,B}; noise-floor seeds for W01, W02 → `runs/`
- [ ] Evaluation: collect anonymized packets into `eval/packets/`, absolute + pairwise judging → `eval/results/`
- [ ] Analysis + research notes + findings report + human blind-ranking bundle

## Ledger of runs (workflow, outline, seed → status) — as of 2026-10-02
- W01 s1: T, P, B DONE. W02 s1: T, P, B DONE (shared base; branched into W03/W04/W07/W09/W10 and W08/cand1).
- W05 s1: B DONE (4/4); T and P at 3/4 (rewriter re-run pending; pre-rewrite sources restored from before-rewrite/, partial archived in partial-rewriter-ratelimit-4/).
- W06 s1: T, B DONE (4/4); P at 2/4 (formatter + copyeditor pending; partial archived).
- W03/W04/W10: writer stage done (base), 1 stage (W10) or 2 stages (W03, W04) pending per outline.
- W07: base done; simulators + rewriter pending. W08: cand1 done; cand2/cand3 + selector pending. W09: base done; rounds pending.
- Judged: abs q889 (T/W01), abs q359 (B/W01); q409 (P/W01) collected, judge cut.
- PAUSED 2026-10-02 pending the organizer's decision on the trimmed scope (see notes/research-log.md).

## Rate-limit notes
Fable has a per-window limit (~10–12 heavy agent runs per 5-hour window observed). Batches are kept to ≤6 heavy runs; partial outputs of cut agents are archived as `*-partial-ratelimit-N`, except complete artifacts (dossier/bank) accepted with a note in DONE-*.md.
