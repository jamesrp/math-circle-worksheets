# Week 28 facilitator guide source

Draft, unpiloted, unscheduled library slot. No physical paper models were tested in this work. Adult hands-on pretesting remains required.

## Rebuild

From this directory, run:

    python3 check_math.py
    python3 build_guide.py

The builder writes `../facilitator-guide.pdf` and regenerates `independent-checks.json`. It never imports, executes or overwrites the student-page builder. Keep this directory beside the output PDF when moving it. All content and diagrams are in `build_guide.py`; there are no external image assets or font binaries in this source package.

Requirements: Python 3, ReportLab (tested 4.4.9), and the DejaVu Sans regular, bold and oblique system fonts. The builder looks in ordinary Linux font directories and `~/.fonts`; adjust `fontdirs` for another operating system. All visible PDF text uses embedded DejaVu Sans fonts. A standard Helvetica resource is present but no visible text uses it.

For visual checking, use Poppler:

    mkdir -p ../facilitator-render
    pdftoppm -r 100 -png ../facilitator-guide.pdf ../facilitator-render/page

Optional structural QA needs PyMuPDF and runs with `python3 validate_pdf.py`. Rendering is a separate visual gate; structural validation alone does not establish page quality.

## Contents and checks

- `build_guide.py`: complete editable prose, tables, model and solution diagrams; 16 US Letter pages.
- `check_math.py`: independent standard-library finite enumeration. It exhausts all 24 sector-stack permutations without assuming the 3-to-1 answer, revisits revised K–1 tab stocks and routes, checks wedge subsets, ray additions, upper angle orders and the unequal D layer witness.
- `independent-checks.json`: current mathematical results. Physical testing is explicitly false.
- `validate_pdf.py`: page count, text bounds, visible fonts, required sections and student reference hashes.
- `qa.json`: recorded final structural and visual QA, with PDF hash.

The guide contains the continuous uniqueness argument for the added ray, because testing integer degrees alone cannot prove uniqueness between ticks. Its right-angle necessity proof is an exhaustive noncrossing-layer argument; its sufficiency proof gives the two-book-fold construction. General Kawasaki–Justin sufficiency is identified as source-backed context, not inferred from the necessary-condition proof. D has a separate explicit reflected-sector/layer certificate and a concrete counterexample to unrestricted use of the 3-to-1 rule.

## Inputs and source fidelity

Read-only inputs were the parent run's PROMPT.md, review.md, review-math.md, final v2 packet sources and final PDFs. The guide answers all 18 final problems; it does not use the draft's obsolete K–1 Problems 4 and 6 or upper Problem 5 as the final tasks.

Source links, pinpoint sections and pedagogy limits are on PDF page 16. Source PDFs were checked on 2026-10-03. The Rozhkovskaya reference was read from the local EPUB, Introduction Berkeley 2009 and Lesson 6, Problems 6.6–6.8 and At the lesson. No claim is made that the proposed Week 28 teaching sequence was piloted.

Final PDF pages 1–16 were individually rendered and visually reviewed at 100 dpi; revised diagrams and page 4 were rerendered and reviewed. The original 17-page layout was corrected to remove a sparse overflow page. All internal page references were rechecked against the final 16-page layout. Student PDFs were not edited.
