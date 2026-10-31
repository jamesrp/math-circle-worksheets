# Week 53 return visit writer report

## Deliverable and scope

Completed the **writer stage only**: `draft/facilitator.pdf`, **8 US Letter pages**, and portable `draft/src/` containing `facilitator.tex`, `build.sh`, independent `check_guide.py`, and `README.md`. No student page, base-week file, index or catalog was edited. No commit, push, critic review or revision stage was performed. The next stage is the independent Claude critic.

The guide opens with the actual minimax-path theorem and converse; threshold-group counts and the common MST price list/cost formula; the difference between repricing networks and trips; and optional-place limits, local traps and the at-most-r-minus-two branching-square bound. Each band has final-PDF problem/page references, complete answers for find-all tasks, discretionary question hints, concrete reasoning, prerequisite-dependent continuations and a manageable one-hour route. The non-task launch has an input, one purchase and completed network visual.

## Inputs inspected

- Rendered and personally read **every final student page**: K–1 7 pages / 8 problems; grades 2–3 6 pages / 8 problems; grades 4–5 10 pages / 12 problems.
- Read final editable graph/TeX/build sources, outline, both prior page reviews, return-visit README, base guide and relevant base research notes; read/rendered the Week 8 return-visit and Week 98 models. The final problem numbers differ from the earlier reviews; the guide does not recycle their old numbering.
- The original external references are not present in this checkout and were not represented as newly consulted. The guide distinguishes outline/base-note source citations from directly consulted originals.

## Mathematical verification

The checker imports no student builder, map module or previous reviewer code. Its graph data were independently transcribed against the final page renders. It enumerates all link subsets for all 12 fixed map types, altered-price variants and required-place choices; enumerates all simple trips; verifies threshold groups; and checks the minimax equivalence, price-list formula and order-preserving repricing on every spanning tree of the printed no-square maps.

Key independently recomputed results include:

- K–1: 3 optima at cost 4; 2 at cost 9; group thresholds 1/2/3 with first A–F connection at 3; optional-star comparisons 8/6, 8/9, 8/8; diamond 12/8; two-square unique cost 6.
- Middle/upper strip map: 6 optima at cost 9, all prices 1,1,1,2,4; first connection thresholds 2,2,4,4. Upper five-place map: 3 optima at cost 6.
- All original/+2/doubled/squared six-place cheapest-trip sets and costs, with full shortest-distance labels for a completeness certificate.
- Optional 2,2,4 star: exactly 6 cheapest purchases; two-terminal grid: exactly 2. The single-change barrier from the outer pair is 10, with a checked 8→10→8→6 witness.
- Both inverse-price formulas were compared to brute force for every positive triple from 1 through 8 (512 triples each). The general formulas are explained in the guide rather than claimed from those bounded tests.
- Input SHA-256 and problem-to-page maps are checked, as are all eight final guide pages and recurring header/footer.

`build.sh` and standalone `check_guide.py` passed. A retained compile audit reports **no errors or overfull boxes**.

## Student-page and operational findings

No new wrong fixed-map answer was found. The revised diagrams, no-square qualifiers, extra contrasting map, numbering and recorded network links match the final PDFs. The guide explicitly handles these remaining risks without changing the pages:

1. **Price invention has implicit conventions.** K–1 P8 and middle P6 do not explicitly restrict invented prices to positive whole numbers. The guide makes that session convention explicit. K–1 P8's valid family is unbounded, not just the old checker's prices 1–6.
2. **Middle P6 has a strict-versus-tied reading.** The intended strict switch gives `AC = AB + BC + 1`; allowing tied cheapest trips also admits the two equality boundaries. Both readings are acknowledged, with an adult question rather than automatic rejection.
3. **The kit does not cover all trial purchases.** The 18/15 and 16/16 comparisons exceed 30 counters together. Moreover, upper P8's squared-price map contains a single price-36 road. The guide says to record and reuse counters for the paired totals and use written arithmetic for oversized trial purchases; it does not claim every legal purchase is physically payable with one kit.
4. **Optional places change earlier theorems.** Middle P7 applies to the no-square maps used so far; P8 introduces a new rule. The guide distinguishes this explicitly and does not transfer the all-place theorem to the optional maps.
5. Spare record maps are workspace, not target answer counts. Using a square need not mean buying every spoke; that matters especially for the 2,2,4 comparison and inverse problem.

No missing cuttable object or mat template was found. Base Week 53 has no separate materials PDF: counters, removable tape, pawn/finger, tray and sleeves are supplied objects, and the new pages contain their maps. Add the requested scrap-paper second payment area. No base student print is needed for the proposed routes; optional familiar-map prints are identified by exact file/page.

## Visual QA and clean rebuild

All **8 final guide pages** were rendered at 120 dpi and personally inspected, with no clipping, overlaps, broken tables, missing glyphs or orphan overflow pages. All **23 student pages** were separately rendered and read. The latest wording adjustment affected only overview page 1; that page was re-inspected after the final build. Headers, footer IDs, page references and diagrams were checked.

A fresh copy of `src/` outside the repository, with only the three student PDFs beside it, rebuilt successfully with the checker passing there. Both extracted text **and PDF bytes** matched the delivered artifact:

- PDF SHA-256: `c016af17334b328b62cd7d2547676ed138bc7a31a7ce07b4f72408d651785962`
- `pdftotext -layout` SHA-256: `a1e602d04cd45bd9f52720b0213f0229e9d9c5b03f079710e3bae61a7b00d58d`

The local TeX installation needed the coordinator's external isolated environment setup; no machine-specific setup path was embedded in the portable sources. The checker first finds student PDFs beside `src/`, then derives the repository fallback by walking ancestors. QA images, text, logs and generated absolute-path stage prompts are **not deliverables** and must not be committed.

## Not established

The guide and activities are **unpiloted and physically unrehearsed**. Tape placement, pawn clearance, payment handling, invented-price demands, adult staffing feasibility and preparation/session timings remain untested with children. This report is not an independent critic verdict and claims no physical rehearsal or source-original access that did not occur.
