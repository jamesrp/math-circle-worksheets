# Ten random atlas investigations

This builder makes the student worksheets and separate facilitator guide for the [random worksheet trial](../../../plans/atlas/worksheet-trial/README.md). It is separate from both the atlas planning books and the ten weekly packets.

From the project root:

```sh
sh lowell-math-circle-year-2/source/atlas-random-ten/build.sh
```

The script uses the bundled Python runtime when available, otherwise `python3`. Set `ATLAS_PYTHON` to choose another interpreter. Dependencies are ReportLab, Pillow, pypdf, pdfplumber and Poppler's `pdftoppm`. The current font configuration in `sheet.py` uses macOS Arial Unicode, Arial Bold, Arial Italic and Apple Symbols, and embeds the required glyphs in the PDFs. To build on another platform, supply equivalent font files and update `register_fonts()`.

The two final PDFs go to `lowell-math-circle-year-2/combined/`. Every page is rendered at 100 dpi, checked for missing glyphs and page-boundary violations, and included in contact sheets in `tmp/pdfs/atlas-random-ten/`. These mechanical checks supplement actual visual review; they do not certify legible knot crossings, clear instructions or usable writing space.

For a development preview:

```sh
sh lowell-math-circle-year-2/source/atlas-random-ten/build.sh \
  --only GA-25 --output-dir tmp/pdfs/atlas-random-ten/ga25-preview
```

Preview renderings and QA reports go under that output directory's `qa/` folder, so independent authors can build disjoint groups concurrently. `--qa-dir`, `--dpi` and `--no-render` are also available. The final build uses the unchanged draw order from `sample.json`; it does not sort by perceived worksheet quality.

## Editing

- `geometry.py`: knot coloring, Cantor addresses, and roads/trees/dual courtyards.
- `systems.py`: additive machines, delayed feedback, and the calculus cooling simulator.
- `decisions.py`: congestion, battery scheduling, absorbing walks, and prefix codes.
- `sheet.py`: shared page, typography, diagram and guide-pagination helpers.
- `build.py`: contents links, assembly, extraction, rendering and mechanical inspection.

Mathematical content, prerequisite gates, prompt IDs, sources, solutions and diagram data are in the corresponding `*-data.json` files in `plans/atlas/worksheet-trial/`. Some condensed student wording and diagram labels are in the renderer modules; edit and review both when changing a prompt. The guide must continue to answer every printed task. Design drafts describe intent and may include more generous initial workspace estimates than the final layouts.

Run the three author checkers and the independent geometry checker after changing mathematics:

```sh
python3 plans/atlas/worksheet-trial/geometry-checks.py
python3 plans/atlas/worksheet-trial/systems-checks.py
python3 plans/atlas/worksheet-trial/decisions-checks.py
python3 plans/atlas/worksheet-trial/systems-review-geometry-checks.py
```

The [review record](../../../plans/atlas/worksheet-trial/REVIEW.md) distinguishes finite checks, general proof arguments, page review and untested classroom performance. Source files use reproducible PDF metadata; repeat builds of unchanged inputs should have identical PDF hashes.
