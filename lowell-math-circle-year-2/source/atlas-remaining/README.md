# Builders for the remaining eighty investigations

These sources produce three student books and three matching facilitator guides from the [worksheet expansion](../../../plans/atlas/worksheet-expansion/README.md). The original ten-trial books and weekly packets use their own builders.

From the project root:

```sh
sh lowell-math-circle-year-2/source/atlas-remaining/build.sh
```

To build one subject, use `--group algebra-discrete`, `--group geometry-analysis` or `--group applied-probability`. Full outputs go to `lowell-math-circle-year-2/combined/`; the final six filenames begin `atlas-algebra-discrete-`, `atlas-geometry-analysis-` and `atlas-probability-applications-`.

For an isolated development preview:

```sh
sh lowell-math-circle-year-2/source/atlas-remaining/build.sh \
  --batch ad1 --output-dir tmp/pdfs/atlas-remaining/ad1-preview
```

This writes a student and guide PDF to that directory, plus `qa/student/` and `qa/facilitator/` containing extracted text, page PNGs, contact sheets and build reports. `--only AD-03` selects an individual family. Use a fresh output directory after repairs when visually rechecking a page; the viewer can cache an older same-path image. `--qa-dir`, `--dpi` and `--no-render` are also available.

## Data and rendering

Each eight-family module (`ad1.py`, etc.) owns its custom student diagrams and layouts. Editable prompts, exact solutions, prerequisites, sources, extensions and mathematical data are in `plans/atlas/worksheet-expansion/<batch>-data.json`. `common.py` prints the student prompts and records their IDs; it generates the complete facilitator key. A module may also provide worked guide figures. `sheet.py` supplies Letter-page typography and vector drawing helpers, derived from the reviewed random-ten builder.

The builder verifies the assigned family set, unique prompt IDs within each family, complete solutions, exactly-once printed prompt coverage, planned page counts and stable contents pagination. It extracts and renders every page, detecting blank pages, out-of-page text and suspect glyphs. These checks do not replace independent proof review or inspection of the actual diagrams and workspaces. Review records and the final page index live with the plans.

## Runtime

The shell wrapper uses the bundled Python when available; set `ATLAS_PYTHON` to override it. Required packages are ReportLab, pypdf, pdfplumber and Pillow; page rendering uses Poppler `pdftoppm`. Fonts are the macOS Arial Unicode, Arial Bold, Arial Italic and Apple Symbols files configured in `sheet.py`, embedded in the output PDFs. Supply equivalent fonts and update `register_fonts()` on another platform.

Each batch has a mathematical check program in the plans directory. Run the relevant program after changing an instance or argument, then rebuild, inspect the changed pages and renew independent review for substantive mathematical or teaching changes. The checks support the written proofs; an exhaustive finite computation must not be cited as a general theorem.

## Assemble the reviewed release

After every batch's mathematical and PDF findings are closed, register the accepted preview and input hashes in `plans/atlas/worksheet-expansion/reviewed-previews.json`, then run the full build above. Inspect the new contents pages in all six books. The page bodies are compared with their independently reviewed previews by the release audit.

Generate the page finder and release manifest with a Python environment containing the listed packages. On this workspace, the bundled runtime is:

```sh
ATLAS_PYTHON=/Users/jamespfeiffer/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3
"$ATLAS_PYTHON" plans/atlas/worksheet-expansion/build_index.py
"$ATLAS_PYTHON" plans/atlas/worksheet-expansion/audit_release.py
```

The audit requires all six books, all eighty assigned families, complete prompt coverage, preserved original inputs and ten-trial outputs, closed reviews, correct contents destinations, rendered pages and matching body text/geometry. It also reruns the mathematical check programs. It writes `release-manifest.json` only after all checks pass. Font subset identifiers may change during assembly; the comparison retains the actual typeface and geometry. Source changes after review require renewed review and registration, not simply replacing the saved hashes.
