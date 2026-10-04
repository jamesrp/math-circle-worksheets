# Week 41 Torus portals and lifts editable source

Prepared October 3, 2026. Unpiloted. This is one topic with three entry-level adaptations and a separate adult guide. Week 41 is a library identifier, not a meeting date.

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

Choose pages by prerequisites; grade labels are approximate. Print student pages single-sided on US Letter at actual size. Exact mats, copies, extensions and pawn/tracing handling remain untested. Check matching opposite-edge marks without reversal, add copies before reaching the edge, and test the two-pawn task. Trimming is adult-only. Physical demonstrations and classroom timing have not been tested. Preserve source attribution. Referenced third-party books and articles retain their rights; they are not redistributed by this package. The original worksheet prose, diagrams and build sources are provided for the organizer's use and adaptation. No broader third-party license is implied.
