# Eleven week-tied guides: writer handoff

**writers done; critic next (Claude)** — October 31, 2026.

This is the writer-only handoff for [the brief](../briefs/week-guides.md): four return-visit guides and seven K–1 guide sections, **60 pages total**. Each was written in a fresh Codex session from the final student PDFs. All remain **unpiloted and physically unrehearsed**. No guide critic or reviser stage has run; no critic findings are claimed fixed.

**Review branch only. Do not merge this folder into `main`.** The draft PR is for Claude's review and the next workflow stage, not a release or approval of these guides. The brief requires `plans/guide-runs/` to stay on `codex/week-guides` until the critic/reviser stages are complete, then be removed during packaging. Student pages, existing guides, draft catalog records, and published print files are unchanged.

## Drafts

| Run | Topic | Guide | Report | Portable source |
|---|---|---|---|---|
| rv-53 | Connecting networks | [8 pages](rv-53-v1/draft/facilitator.pdf) | [Writer report](rv-53-v1/writer-report.md) | [Source](rv-53-v1/draft/src/) |
| rv-58 | Fair division | [8 pages](rv-58-v1/draft/facilitator.pdf) | [Writer report](rv-58-v1/writer-report.md) | [Source](rv-58-v1/draft/src/) |
| rv-62 | Conflict networks | [8 pages](rv-62-v1/draft/facilitator.pdf) | [Writer report](rv-62-v1/writer-report.md) | [Source](rv-62-v1/draft/src/) |
| rv-63 | Cards away from home | [8 pages](rv-63-v1/draft/facilitator.pdf) | [Writer report](rv-63-v1/writer-report.md) | [Source](rv-63-v1/draft/src/) |
| k1-57 | Area from dots | [4 pages](k1-57-v1/draft/k1-guide.pdf) | [Writer report](k1-57-v1/writer-report.md) | [Source](k1-57-v1/draft/src/) |
| k1-66 | Lamplighter streets | [4 pages](k1-66-v1/draft/k1-guide.pdf) | [Writer report](k1-66-v1/writer-report.md) | [Source](k1-66-v1/draft/src/) |
| k1-81 | Buckets of Fish | [4 pages](k1-81-v1/draft/k1-guide.pdf) | [Writer report](k1-81-v1/writer-report.md) | [Source](k1-81-v1/draft/src/) |
| k1-87 | Voting and agendas | [4 pages](k1-87-v1/draft/k1-guide.pdf) | [Writer report](k1-87-v1/writer-report.md) | [Source](k1-87-v1/draft/src/) |
| k1-91 | Rotor-router machines | [4 pages](k1-91-v1/draft/k1-guide.pdf) | [Writer report](k1-91-v1/writer-report.md) | [Source](k1-91-v1/draft/src/) |
| k1-97 | Square remainders | [4 pages](k1-97-v1/draft/k1-guide.pdf) | [Writer report](k1-97-v1/writer-report.md) | [Source](k1-97-v1/draft/src/) |
| k1-98 | Growing from a few seeds | [4 pages](k1-98-v1/draft/k1-guide.pdf) | [Writer report](k1-98-v1/writer-report.md) | [Source](k1-98-v1/draft/src/) |

## Checks completed

- Every writer recomputed the printed answers independently, with exhaustive finite enumeration where appropriate, and inspected every served student page and every resulting guide page: **19 student PDFs / 144 pages; 11 guides / 60 pages**. The reports distinguish finite checks from general proofs and record final-PDF numbering rather than relying on outdated student reviews.
- Every guide compiles without errors or overfull boxes. Each portable source includes its own checker and a `build.sh` that compiles the PDF into its parent directory and runs the checker.
- The coordinator repeated all eleven builds in the integration checkout and again from separate clean copies outside the repository, with only each guide's source and its unchanged student PDFs alongside it. All checkers passed; **all eleven rebuilt PDFs and their extracted text were identical**.
- Student PDF hashes are unchanged. Catalog build and path checks pass without generated-file changes. Source paths, font embedding, US Letter size, page bounds, recurring identifiers and Git whitespace checks pass. Sources contain no host-specific setup paths; TeX intermediates and generated stage prompts are excluded.
- [verification.json](verification.json) records page counts, guide and student hashes, and the integration verification results. Per-guide reports give mathematical coverage, exact replacement sections, visual checks, source access limits and operational risks. These writer checks are not Claude's independent critique or classroom validation.

## Findings for Claude to examine

These are writer findings, not a critic verdict; the student pages have not been changed.

- **Return visit 58:** upper Problem 6's arbitrary-value wording follows a fixed target of 4. The guide uses each person's original total divided by 3 when totals change, and gives a counterexample to retaining 4. Middle games also need a second-round mark at 112.5 mm, not only half-panel reasoning.
- **Return visit 53:** price-invention domains and the strict/tied reading need an adult convention. One squared-price road costs 36, exceeding the 30-counter kit; the guide uses written totals for oversized purchases.
- **Return visit 62:** nearby allowed-slot labels may visually run together; the arrow rule needs the caveat that an indirect directed path also prevents shared slots.
- **K–1 87:** movable D/E/F launch labels are not in the base kit; the guide identifies temporary adult-made labels. Return visit 63 also explicitly calls for loose small counters rather than treating them as printables.
- **K–1 91 and 98:** later integration must synchronize stale companion wording/page references. The Week 91 overview still says there is no independent K–1 packet; Week 98's existing older-band key has page references shifted by its extra-workspace page. Exact locations are in the reports; those existing guides were left untouched.

All reports retain kit, reading/recording, reset, staffing and pacing limits. Finishing a packet in one hour is not required; deeper material and return routes remain available.

## Next stage

In a checkout of this branch, regenerate the machine-local stage prompts:

```sh
python3 worksheet-workflow/guide/make_week_runs.py --dir plans/guide-runs
```

This fills `WRITER.md`, `CRITIC.md` and `REVISE.md` in each run; **do not commit those generated absolute-path prompts**. Claude now runs each `CRITIC.md` in a separate fresh session and commits that run's `review-guide.md`, then sets the work-board line to `critics done; reviser next (Codex)`. Codex's reviser and packaging phases remain pending. Follow the brief for final destinations, README/catalog updates and removal of these run folders before eventual main integration.

To repeat a draft build in this checkout (normal Python 3/PyMuPDF, Poppler and pdfLaTeX dependencies; see each source README):

```sh
for run in plans/guide-runs/*-v1; do
    bash "$run/draft/src/build.sh" || exit 1
done
python3 catalog/build.py
python3 catalog/check_path.py
```

For a detached clean build, copy a run's `draft/src/` to a new folder and place that draft's final student PDF(s) beside `src/`; run `bash src/build.sh`. This does not require rebuilding or changing the students.
