# Editable worksheet sources

LaTeX/TikZ, geometry generators, build scripts, mathematical checks, packet notes, and review records live here. For printable PDFs, use the [year-2 print index](../README.md).

Each `week-NN/` source folder corresponds to the PDF folder `../week-NN/`. The `fall-weeks-02-10/` builder assembles the nine weeks into `../combined/`. Supporting plans and mathematical data stay in the project's top-level `plans/`; build and rendering files go in top-level `tmp/`.

Run these commands from the project root:

```sh
# Week 1 core worksheets
sh lowell-math-circle-year-2/source/week-01/build.sh

# Week 1 optional extensions
sh lowell-math-circle-year-2/source/week-01/build-extensions.sh

# One week (change the number as needed)
sh lowell-math-circle-year-2/source/week-05/build.sh

# Weeks 2–10, their mathematical checks, and all five combined packets
sh lowell-math-circle-year-2/source/fall-weeks-02-10/build.sh
```

Builds require Python 3 and pdfLaTeX with the packages listed in each week's README. Combined packets additionally use `pypdf`, `pdfplumber`, and `reportlab`; the builder selects the bundled Python when available. Rendering for visual review uses Poppler. Give pages a fresh visual check after editing their content or layout.

The older Week 1 design is in [week-01/archive-v1](week-01/archive-v1/README.md). Its separate build script writes only to `lowell-math-circle-year-2/week-01/archive-v1/`, with separate temporary build files.

The separate [atlas builders](atlas/README.md) turn reviewed data in `plans/atlas/` into two facilitator planning books in `combined/`. They do not modify the weekly packets.

The [random-ten worksheet builder](atlas-random-ten/README.md) makes a separate student book and facilitator key for ten randomly selected atlas entries, with its own designs, mathematical checks and page-review records.
