# Week 38 Seams and cuts editable source

Prepared October 3, 2026. Unpiloted. This is one topic with three entry-level adaptations and a separate adult guide. Week 38 is a library identifier, not a meeting date.

## Rebuild from any folder

Unzip the whole folder, including fonts and reference-pdfs. Install Python 3 and the packages in requirements.txt, plus a normal TeX Live distribution providing pdfLaTeX, TikZ, geometry, Helvetica and standard PDF font maps, and Poppler's pdftoppm. Run:

    python3 -m pip install -r requirements.txt
    python3 build.py
    python3 verify.py
    python3 verify_math.py

Commands can be run after changing into this folder; build.py and verify.py also work when invoked by their full path. Paths with spaces are supported. No project checkout, network access, custom cached TeX format, or original workspace path is needed. DejaVu fonts are bundled with their license. Platform packages remain prerequisites rather than included executables.

## What to edit

Student layouts and prompts are in src/ (the Python generator and generated TeX files); the TeX files are generated snapshots. Adult content is in facilitator-src/guide.json, content.json or guide.md, with its renderer in that directory. Rebuild after edits and inspect every page. Running verify.py after an intentional change should fail until you deliberately replace the approved reference PDFs. PDF timestamps can differ; this check compares every page's text, dimensions and rendered pixels instead of claiming byte-identical builds.

reference-pdfs contains the exact approved student and guide PDFs for comparison. These are duplicates for verification, not extra printing. The guide contains precise mathematical overview, later proofs and solutions, source references, prerequisites, launch and preparation. verify_math.py checks finite cases; it does not establish classroom effectiveness or replace the written proofs.

AGENTS.md and worksheet-workflow contain the exact organizer-approved project guidance. Their historical links to the full corpus remain unchanged; rebuilds do not depend on those linked files. The two approved page examples are included in approved-examples. The selected source outline is in worksheet-workflow/outlines. No private assistant notes or production conversations are included.

## Use and rights

Choose pages by prerequisites; grade labels are approximate. Print student pages single-sided on US Letter at actual size. Mandatory exact-material tests remain unperformed: trace boundaries, make complete center cuts, check piece/edge counts, and test continuous arrow transport. Keep loops on the table and away from bodies. Physical demonstrations and classroom timing have not been tested. Preserve source attribution. Referenced third-party books and articles retain their rights; they are not redistributed by this package. The original worksheet prose, diagrams and build sources are provided for the organizer's use and adaptation. No broader third-party license is implied.

## Targeted worked examples, 4 October 2026

All three packets add the neutral flat-washer edge-membership example on page 2, before Problem 3 on its own page 3. Three labeled dots become two grouping ovals. Each packet now has 6 pages. Seam recipes, four-dot targets, cutting questions and task dimensions are preserved.

The example drawing lives in `src/examples.py`; the normal builder imports it and regenerates the TeX. `python3 src/check_examples.py` independently checks the example geometry or conversion without importing the packet generator or answer data. All pages were rendered and inspected; original task text/order and working-diagram dimensions were checked. References and the portable source ZIP describe this current revision. Earlier source releases are archived separately. These revisions remain unpiloted.
