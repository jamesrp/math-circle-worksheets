> Archived October 3, 2026. This version was replaced by the [concrete revision](../README.md); its PDFs are in `lowell-math-circle-year-2/week-03/archive/`, and `sh lowell-math-circle-year-2/source/week-03/archive/build.sh` rebuilds it there.

# Week 3: Code machines and return times

Revised September 30, 2026, using the **current top-level Week 2 catalogs** and the substantial-problem guidance in AGENTS.md. **v4 is unpiloted.** Four student packets now contain **17 substantial problems instead of 35 small tasks**. Shared rules appear once; children choose how to investigate and record. Optional tracing, loop diagrams, classification methods, hints, and complete proofs are in the adult guide.

## Current print files

| Packet | Pages / problems | Main investigations |
|---|---|---|
| [K–1](../../../week-03/archive/week-03-k-1.pdf), F03-K-v4 | 3 / 5 | Send and recover shape messages; compare whole-message returns; invent recoverable keys; find every input for an ambiguous output. |
| [Grades 2–3](../../../week-03/archive/week-03-grades-2-3.pdf), F03-M-v4 | 3 / 5 | Hidden keys with zero, one, or two solutions; partial-message returns; all four-letter return times; a six-turn five-letter machine. |
| [Grades 4–5](../../../week-03/archive/week-03-grades-4-5.pdf), F03-U-v4 | 3 / 4 | Contrast four machines; classify all possible five-letter returns; test key order, including overlapping keys that commute; undo a combined machine. |
| [Optional extra, roughly grades 6–7](../../../week-03/archive/week-03-extra-grades-6-7.pdf), F03-X-v4 | 3 / 3 | Construct specified returns; prove the eight- and nine-letter records; settle whether another letter always improves the record. |
| [Facilitator](../../../week-03/archive/week-03-facilitator.pdf), F03-FAC-v4 | 6 | Common launch, prerequisites, realistic preparation, timing, hints, full solutions and proofs, source findings, and observation prompts. |

The grade labels are approximate entry points. Read aloud and scribe freely. The youngest tasks need shape matching, then counting to three; middle tasks use A–D as labels and small counts. Upper tasks require completeness reasoning; extras use common multiples through 20. Formal algebra is not required. See guide page 1 for the complete readiness map.

## Prepare an hour

Current roster: **10 children, KK1 / 3333 / 445; three adults**. Print three K first pages, four middle first pages, and three upper first pages: **ten starting sheets**. Keep one adult at each familiar table; pages can travel by interest and readiness. Bring selected continuation masters and blank paper or whiteboards. A printer in the room is not assumed. Twelve student master pages plus six adult pages do not constitute an assignment to finish.

Let children handle materials for about four minutes, then give a brief whole-group demonstration of one substitution turn and its record. Allow two long work periods with a movement break and time to share. Stop after a satisfying investigation or continue it; no page is an access test for the next one.

Paper, pencil/eraser, and existing whiteboards or counters suffice. Optional hand-drawn cards: two sets of three shapes per youngest child; A–D for each middle child; A–E for each upper child, with F–I in reserve. Repeated symbols can be drawn. Keep an input visible while making its output. Print US Letter, single-sided, Actual Size.

[Plan and design record](../../../../plans/week-03-redesign.md) · [Review](REVIEW.md) · [Checked mathematical data](../../../../plans/week-03-checks.json)

## Build and verify

From the repository root:

```sh
sh lowell-math-circle-year-2/source/week-03/build.sh
```

The existing multi-file LaTeX build runs `verify.py`, compiles the five PDFs twice, and writes them to `lowell-math-circle-year-2/week-03/`. Build files stay in `tmp/pdfs/week-03-build/`. Python 3, pdfLaTeX, TikZ, and Source Sans Pro are already available. No new installation is needed.

The verifier exhausts all permutations of sizes 1–9 and checks every printed clue, explicit key, first return, composition, inverse, and largest-loop bound. Its report lives in `plans/week-03-checks.json`. Proofs remain in the facilitator guide.

To update only Week 3 in the existing combined sets, run `lowell-math-circle-year-2/source/fall-weeks-02-10/refresh-week.py --week 3` with the bundled Python (or another Python with pypdf, pdfplumber, and ReportLab). It requires the existing combined PDFs and `tmp/pdfs/fall-weeks-02-10/manifest.json`, regenerates contents/bookmarks, and preserves every other week's pages. It does not restore or rebuild archived Week 2 material.

The preceding v3 sources and PDFs are preserved separately in `archive-before-concise-2026-09-30/`. Its adjusted build script writes only to that archive. The previous plan is under `plans/archive-before-concise-2026-09-30/`. Record only material actually encountered in the [use log](../../../../plans/fall-k-5-year-a-use-log.md), using v4 IDs and exact keys/messages.
