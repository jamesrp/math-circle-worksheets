# Week 2: one shared collection

The current **42-page student library has 50 problems** with one numbering system, no grade labels, and five bookmarked groups of activities. Everyone begins with a legal pair move on page 1. Then adults offer pages by interest and readiness. The page order is a filing order, not a required sequence.

- [Shared student collection](../../week-02/week-02-shared.pdf), **F02-S-v1**.
- [Compact puzzle catalog](../../week-02/week-02-shared-catalog.pdf), **4 pages, F02-S-CAT-v2**: unnumbered opening guidance and ten consecutively numbered problems with small start-to-target diagrams. Original target-image sizes are retained. Most captions simply say “Make each target picture”; the visit-every-lamp, island, bridge, and partner-puzzle tasks keep their specific instructions. This is a separate September 30 version of the opening lamp puzzles.
- [Upper puzzle catalog](../../week-02/week-02-shared-catalog-upper.pdf), **6 pages, F02-S-CAT-UP-v1**: six substantial investigations, renumbered 1–6, with 26 start-to-target puzzles and a hardest-target design challenge. Short prompts replace the detailed presentation of original Problems 15–32 and 43–50. Covers reachability, components, complementary cycle solutions, lower bounds, and tree uniqueness. [Facilitator notes, solutions, and design record](../../../plans/week-02-catalog-upper.md). Prepared September 30; unpiloted.
- [Shared adult guide](../../week-02/week-02-shared-facilitator.pdf), **16 pages, F02-S-FAC-v1**: launch, exact page finder, print recipe, parent scripts, solutions, proof conversations, and observation prompts.
- [Fast Finisher / Bonus Challenges](../../week-02/week-02-bonus-challenges.pdf), **4 pages, F02-BONUS-v1**, with a separate [2-page facilitator key](../../week-02/week-02-bonus-facilitator.pdf): do-nothing moves, bridge predictions, one solo switch, and unequal press prices. [Prerequisites, exact instances, source notes and checks](../../../plans/week-02-bonus.md). Prepared September 30; unpiloted reserve.
- [Session plan and design rationale](../../../plans/week-02-shared-collection.md).

Prepared September 28, 2026; **unpiloted**. This implements the organizer's decision to use a shared collection after reviewing the visual revisions. Earlier versions are preserved in `archive-before-shared-collection-2026-09-28/` under source, weekly output, and combined output folders.

## Find a page

| Student pages | Problems | What children do | Entry needs |
|---|---|---|---|
| 1–8 | 1–14 | Match pictures, undo partner moves, move one light, explore larger graphs, invent puzzles | Follow a demonstrated pair move; pointing and adult reading suffice |
| 9–16 | 15–22 | Record moves, compare targets, collect all four-lamp patterns | Replay a move list with help; count up to four |
| 17–28 | 23–32 | Make targets in different ways, cancel repeats, compare complementary sets, find shortest lists | Track several moves; count up to six; adult can record |
| 29–34 | 33–42 | Draw shapes, divide houses, count rooms, mark neighboring rooms | Drawing and small counts; an independent change of activity |
| 35–42 | 43–50 | Explore disconnected islands, add a bridge, overlap paths, solve trees with cuts | Match labeled lamps, track components, compare odd/even counts |

Problems 26 and 28 each use two pages. All other page/problem mappings are in the adult guide. The first four-lamp boards use the same diamond orientation as later numbered boards. Working boards remain blank; target pictures show the desired ON lamps. Dots and dark counters both mean ON.

## Manage the hour

Current roster: **10 children, KK1 / 3333 / 445; three adults, two mathematicians and one parent**. Keep three stable tables with one adult each; the initial seating can remain familiar. Pages can cross those groups. A child who demonstrates the rule can jump to collecting, shortest-solution work, or a larger graph without completing earlier pages. A child may choose drawing at any point. Adults may read or scribe; handwriting speed is not an entry test.

Print US Letter, single-sided, Actual Size. Start with **ten copies of page 1**, a shared master library, and the small table stacks specified in guide page 1. Keep one adult guide per adult, or print the guide's designated relevant pages. Give one student sheet at a time. Later masters can be shown while children work on blank paper or whiteboard tablets; no classroom printer is assumed. Paper, pencils, erasers, whiteboards/markers, and optionally existing two-sided counters are enough. No new construction accessories are needed.

## Build and verify

From the repository root:

```sh
sh lowell-math-circle-year-2/source/week-02/build.sh
```

The script checks the finite mathematics, builds the exploration/drawing pages with ReportLab, compiles the three visual TeX sections, assembles the student library, and builds the unified adult guide and compact puzzle catalog. Current outputs are the three shared PDFs. Compilation/render files go in `tmp/pdfs/week-02-shared/`; catalog review renders go in `tmp/pdfs/week-02-catalog/`.

To rebuild only the catalog, run `build-shared-catalog.py` with the bundled Python (or a Python environment with ReportLab) from any directory. It reuses the graph data and vector drawing routine from `build-shared-explore.py`; it does not require LaTeX. Print at Actual Size to preserve the original small-target scale. Catalog pages cover Problems 1–3, 4–5, 6–7, and 8–10 respectively. For comparison with the full collection and adult guide, catalog Problems 1–10 correspond to original Problems 2, 5, 6, 7, 8, 9, 10, 11, 12, and 13. The catalog omits the one-lamp-ON constraint and redundant descriptions of starting states. The wider island diagrams use a downward start-to-target arrow. This version is unpiloted and is not substituted into the combined Weeks 2–10 packets.

Editable current sources:

- `build-shared-explore.py`: shared pages 1–8 and 29–34.
- `build-shared-catalog.py`: separate four-page start-to-target puzzle catalog.
- `build-shared-catalog-upper.py`: separate six-page upper catalog. Rebuild independently with Python and ReportLab; verify with `plans/verify-week-02-catalog-upper.py` from the repository root. Data and checked edge sets live in `plans/week-02-catalog-upper-data.json` and `plans/week-02-catalog-upper-checks.json`. Review renders go in `tmp/pdfs/week-02-catalog-upper/`. This optional catalog is not included in the main build or combined packets.
- `build-bonus.py`: separate four-page bonus packet and two-page adult key. Verify with `plans/verify-week-02-bonus.py`, then run this builder with Python and ReportLab. Instance data and checked results live in `plans/week-02-bonus-*.json`; renders go in `tmp/pdfs/week-02-bonus/`. Not included in the main build or combined packets.
- `shared-collect.tex`: pages 9–16.
- `shared-shortest.tex`: pages 17–28.
- `shared-networks.tex`: pages 35–42.
- `build-shared-guide.py`: adult guide.
- `assemble-shared.py`: PDF assembly, bookmarks and structural checks.
- `common.tex`: existing TeX styling used by the three shared components.

Mathematical data and section order live in `plans/week-02-shared-data.json` and `plans/week-02-shared-manifest.json`. `plans/verify-week-02-shared.py` applies the independent graph/room verifier to the shared data; `verify.py` exhaustively checks the ring, component and tree instances. Checked results stay in `plans/`.

Requires Python with ReportLab, pypdf and pdfplumber, and the existing pdfLaTeX/TikZ installation. The build selects the bundled Python when available; set `SHARED_PYTHON` to another suitable Python if needed. The existing multi-file TeX workflow is retained. No plugin or extra installation is needed on this machine.

The five combined Weeks 2–10 files now all embed this same Week 2 material: the shared student book in each student set and the shared guide in the facilitator set. Their grade labels distinguish only Weeks 3–10. Rebuild them with the bundled Python and `source/fall-weeks-02-10/assemble.py`; selected sets can still use `--level`.

[REVIEW.md](REVIEW.md) records the final checks. Record only material actually encountered in the [use log](../../../plans/fall-k-5-year-a-use-log.md); a printed reserve is not a taught session.
