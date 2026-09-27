# First-edition review and release record

Prepared 25 September 2026. This is an AI-assisted mathematical and editorial review record, not certification by a human educator or evidence of classroom success.

## Mathematical and pedagogical review

Three authors surveyed distinct territories and drafted their families. Each then reviewed a different author's complete volume, following the [review protocol](review_protocol.md): solve the stated learner problem before reading the supplied answer, check boundaries and hypotheses, assess whether the student question preserves its claimed mathematical mechanism, and inspect prerequisites, learner choices, practical setup and recorded prior use.

- [AD-01 through AD-24](reviews/algebra-discrete-review.md): all 24 core instances, solutions and boundaries reviewed; [independent checker](reviews/ad-independent-checks.py) and [results](reviews/ad-independent-checks-results.json).
- [GA-01 through GA-36](reviews/geometry-analysis-review.md): all 36 reviewed; [independent checker](reviews/ga-independent-checks.py) and [results](reviews/ga-independent-checks-results.json), with analytic proofs recorded in the report.
- [AP-01 through AP-30](reviews/applied-probability-review.md): all 30 reviewed; [independent checker](reviews/applied-probability-checks.py), with exact and analytic checks recorded in the report.
- Root-editor [spot checks](reviews/editor-spot-checks.md), [initial exact checks](reviews/check_initial_examples.py), and [coverage audit](reviews/coverage-audit.md) provide additional evidence.

The independent checks included finite exhaustive enumerations where feasible, exact rational computations, algebraic proofs and explicit counterexamples. They check the recorded examples and stated arguments; they do not establish every theorem in the research continuations. All material findings reported in the three independent plan reviews were repaired and reread before the print edition.

Representative repairs:

- GA-10: corrected an itinerary extension that had named a different periodic orbit.
- GA-22: completed the four-point convex-hull proof's collinear and boundary cases.
- GA-36: used a centered contraction that actually preserves the specified closed interval.
- AD-06 and AD-18: made reflexive lattice comparisons and linearity explicit in the learner rules.
- AP-29: distinguished immediate prefix-tree decoding from the broader notion of unique decodability.
- AP-05: replaced a source whose interpretation did not support the card's careful frequentist coverage distinction; the finite five-error example is independently proved.
- Multiple cards: clarified exact materials, synchronous updates, with-replacement draws, graph conventions, temperature units, quantum measurement claims and shared instances.

Source portions were inspected during authorship; the independent reviewers reopened a documented sample and checked its hypotheses. Some survey sources were inspected only for scope or contents, and some advanced continuations remain explicit source gaps. Each source's `checked` field and the review reports retain those limits. A source entry is provenance, not a quality score. This release does not claim that all linked documents or all general theorems received complete independent audits.

## Breadth and returning participants

All 63 top-level fields have dossiers. The 90 families give primary coverage to all 60 substantive fields; 00, 01 and 97 support the project. The 231 seeds are a research queue, not 231 developed activities. Every lower-level taxonomy entry remains unvisited in the coverage accounting. A representative family never marks its whole field complete.

The [prior-use map](prior-use-map.md) compares the organizer's available year-1 materials and current Weeks 1-10. The [connections register](connections.md) flags repeated objects and mechanisms, including exact reused examples across volumes. Actual teaching history can only be established by the organizer and the use log. No classroom pilots are recorded for the new atlas designs.

## Print review

Both books were built and all 270 pages rendered. Independent PDF reviewers inspected every contact sheet and selected full-size pages, including every reasoning page in the GA-13 through AP-30 assignment. Their reports distinguish actual image inspection from automated checks:

- [Investigation book, pages 1-80](reviews/main-pdf-review-ad-ga.md).
- [Investigation book, pages 81-188](reviews/main-pdf-review-ga-ap.md).
- [Research map, all 82 pages](reviews/research-map-pdf-review.md).
- [Additional editor checks](reviews/editor-pdf-spot-checks.md).
- [Consolidated final fix and recheck](reviews/pdf-final-fix-review.md), with [final artifact checks and hashes](reviews/pdf-release.json).

One material PDF-only error was found: a formatter lowered only the first letter of two-letter PDE derivative indices. The final fix round repaired all three affected occurrences on research-map page 38, added the missing reciprocal companion-book link on investigation page 1, and made the map renderer remove its own stale page images before rebuilding. No mathematical source content changed in that round.

The complete build and checks then passed again. Exactly two page images changed; the other 268 were byte-for-byte and pixel-identical to the reviewed renderings. The repair agent and root editor separately inspected the changed pages. The repair agent also checked an unchanged exponent-formatting control page. No reported material finding remains open.

The final books have **188 investigation-plan pages** and **82 research-map pages**. Source-preservation checks cover all 3,108 family text/URL entries, all 231 seed anchors and the remaining survey text. Bookmarks, contents destinations and source annotations were checked structurally; this does not certify current network availability of every external source. The books preserve source caveats and are facilitator references. Later student packets still need their own diagram and classroom review.

## Known limits and next decisions

The one-hour menus and preparation times are estimates. Readiness gates are descriptive, not measured grade thresholds. An oral or manipulative entry does not make an advanced continuation suitable for a young child. The remaining work is to deepen the [research frontier](FRONTIER.md), select specific investigations for pilot use, record observed needs, and only then create detailed student packets and a coherent returning-child schedule.

The machine-readable [release checks](release-check.json) record the exact final family-source hashes and structural counts. PDF hashes and page-inspection scope are recorded after final production. Re-run the relevant mathematical checks and render any changed pages before replacing this reviewed edition.
