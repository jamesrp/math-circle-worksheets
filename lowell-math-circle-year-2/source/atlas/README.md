# Build the mathematics atlas

These two builders print the reviewed facilitator plans and research map. Editable mathematical content and review records live in [plans/atlas](../../../plans/atlas/README.md). They do not create student worksheets or change the existing weekly packets.

From the project root:

```sh
sh lowell-math-circle-year-2/source/atlas/build.sh
```

The script selects the bundled Python when available; otherwise supply a Python installation with `reportlab`, `pypdf`, `pdfplumber` and Pillow using the `ATLAS_PYTHON` environment variable. The builders use installed Arial, Arial Unicode and Apple Symbols fonts on macOS. Consult their font setup before building on another platform. Rendering requires Poppler's `pdftoppm`.

- `build_plans.py` reads the three family JSON files and writes `combined/math-atlas-investigation-plans.pdf`.
- `build_research_map.py` reads the surveys and map/frontier files and writes `combined/math-atlas-research-map.pdf`.
- Builder intermediates and page maps belong in `tmp/pdfs/atlas/`, relative to the repository root.
- `verify_print.py` independently checks all-page character bounds and family-source text/URL preservation. Its report retains unmatched fields for review; extraction alone does not establish visual correctness.

The default build renders both books at 90 dpi and makes contact sheets: investigation plans under `tmp/pdfs/atlas/plans/contacts/`, research map under `tmp/pdfs/atlas/map/contact-sheets/`. Full-page PNGs are in each volume's `pages/` directory. The initial edition has 188 plan pages (two pages per family after eight introductory pages) and 82 research-map pages.

Run the atlas index and seed builders after changing their data; `build.sh` does this before making PDFs and performs the structural release check afterward. Mathematical checks and review records remain in `plans/atlas/reviews/`. A successful build does not replace mathematical review or visual inspection. Render all pages after a layout change, inspect every contact sheet, and inspect full-size pages containing dense text or difficult notation. The independent PDF review reports document the first edition's actual scope.

The output books are US Letter facilitator references with internal navigation and clickable sources. Print only the relevant pages. They contain answers and should not be handed to participants as student packets.
