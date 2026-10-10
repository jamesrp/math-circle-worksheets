# Editable worksheet sources

LaTeX/TikZ, geometry generators, build scripts, mathematical checks, packet notes, and review records live here. For printable PDFs, use the [year-2 print index](../README.md).

The additional [octagon investigations, Weeks 64–65](../WEEKS-64-65-DRAFT.md), contain restored portable sources and separate regenerated student/adult PDFs. The organizer authorized main-branch integration on October 6; both activities remain unpiloted and physically untested.

Each `week-NN/` source folder corresponds to the PDF folder `../week-NN/`. The `fall-weeks-02-10/` builder assembles the nine weeks into `../combined/`. Supporting plans and mathematical data stay in the project's top-level `plans/`; build and rendering files go in top-level `tmp/`.

**October 3, 2026 concrete revision.** Weeks 3–10 and the new [Week 1 encore](week-01-encore/README.md) each have `src/` (student pages), `guide-src/` (adult guide and answer checks) and a `build.sh` that builds in `tmp/pdfs/week-NN-build/` and writes four PDFs to `../week-NN/`. Run, for example, `sh lowell-math-circle-year-2/source/week-07/build.sh`. Each week's previous sources are in `week-NN/archive/`, whose patched `build.sh` writes only to `../week-NN/archive/`. The combined Weeks 2–10 sets were not rebuilt; the September sets are in `combined/archive-before-concrete-2026-10-03/`.

Run these commands from the project root:

```sh
# Week 1 core worksheets
sh lowell-math-circle-year-2/source/week-01/build.sh

# Week 1 optional extensions
sh lowell-math-circle-year-2/source/week-01/build-extensions.sh

# Week 2 shared collection and unified adult guide
sh lowell-math-circle-year-2/source/week-02/build.sh

# One other week (change the number as needed)
sh lowell-math-circle-year-2/source/week-05/build.sh

# Weeks 2–10, their mathematical checks, and all five combined packets
sh lowell-math-circle-year-2/source/fall-weeks-02-10/build.sh
```

Builds require Python 3 and pdfLaTeX with the packages listed in each week's README. Combined packets additionally use `pypdf`, `pdfplumber`, and `reportlab`; the builder selects the bundled Python when available. Rendering for visual review uses Poppler. Give pages a fresh visual check after editing their content or layout.

The [generated activity library, Weeks 11–51](../WEEKS-11-51.md), uses separate portable packages in `week-NN/`: each has a current source ZIP, a complete `editable/` copy, dependencies and build instructions. Copy the entire editable package into the project's `tmp/` folder before rebuilding. The current reference PDFs match the weekly print copies. The October 4 [targeted worked-example report](../../plans/targeted-worked-examples-2026-10-04/REPORT.md) records the revised releases and verification. The subsequent [approved fresh-review revision](../../plans/fresh-review-revision-2026-10-04/REPORT.md) synchronizes six revised student PDFs and 39 refined guides with current editable packages, references and portable ZIPs. Prior affected base releases are separately archived; `verify_revision.py` checks the current packages and records specific pre-existing unchanged-font alternatives. These activities have no current combined weekly book.

[Week 3](week-03/README.md) uses the September 30 concise v4 investigations; `archive-before-concise-2026-09-30/` preserves v3. Weeks 4–10 retain v3 task sequences and the adopted student-page format. Week 2 now uses F02-S-v1: one 42-page shared collection with 50 problems and a unified adult guide. Extras may span multiple pages. Their `archive-before-classroom-guidance-2026-09/` folders retain the prior v2 sources and separate archive-only builds. The [revision review](../../plans/fall-weeks-02-10-classroom-guidance-review.md) documents the rationale and validation.

The older Week 1 design is in [week-01/archive-v1](week-01/archive-v1/README.md). Its separate build script writes only to `lowell-math-circle-year-2/week-01/archive-v1/`, with separate temporary build files.

The separate [atlas builders](atlas/README.md) turn reviewed data in `plans/atlas/` into two facilitator planning books in `combined/`. They do not modify the weekly packets.

The [random-ten worksheet builder](atlas-random-ten/README.md) makes a separate student book and facilitator key for ten randomly selected atlas entries, with its own designs, mathematical checks and page-review records.

The [Week 2 shared collection](week-02/README.md) uses ReportLab for exploration, drawing, and network pages, LaTeX/TikZ for ring investigations, and a unified adult guide. Run `week-02/build.sh` for the current outputs; the earlier grade packets and auxiliary are preserved under `archive-before-shared-collection-2026-09-28/` in the source and PDF folders. The combined builder includes the identical shared Week 2 library in all four student sets and the unified guide in the facilitator set. Their grade labels apply only to Weeks 3–10; print Week 2 once.

To refresh only a changed week in the existing combined sets, use `fall-weeks-02-10/refresh-week.py --week 3` (with the bundled Python, changing the week number as needed). This preserves all other embedded pages and regenerates contents/bookmarks; the current combined PDFs and build manifest are required.

## Geometric group theory prototypes 66–75

The [review index](../WEEKS-66-75-PROTOTYPES.md) links each student packet, theorem-first adult guide, source README and portable ZIP. Each package rebuilds both PDFs independently and includes the mathematical checkers. These focused prototypes remain unpiloted.

## Frontier prototypes 76–78

The [three-topic review index](../WEEKS-76-78-PROTOTYPES.md) links the substitution, persistence and tropical-geometry student/adult pairs and portable ZIPs. Every package reconstructs both PDFs independently and includes its mathematical verifiers and source lineage. These are unpiloted prototypes with explicit prerequisites and material-rehearsal limits.

## Infinity, ordinal, surreal and knowledge drafts 79–84

Each package in `week-79/` through `week-84/` builds one selected-band student/material PDF and a separate facilitator PDF using Python 3 and pdfLaTeX, with standard-library mathematical checks. Its adjacent portable ZIP contains the same six owned source files. The [mobile index](../WEEKS-79-84-DRAFT.md) and [release evidence](../../plans/infinity-prototypes-79-84/README.md) give exact coverage and byte-identical extracted-ZIP reconstruction results. No reference books or workflow style excerpts are packaged.
