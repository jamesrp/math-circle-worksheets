# Week 32 independent facilitator mathematics audit

**Pass after final-source verification.** Independently read all 4 mathematical-overview paragraphs, all 12 solution paragraphs, and every extension in actual `guide.json`; cross-checked the actual five-page `bonus-facilitator.pdf` text and actual final student PDF. Mathematical statements, assumptions, witnesses, solutions, bounds, counts, and task mapping are valid. No mathematical issue remains.

Actual investigation ranges: **1-2, 3, 4**. Actual final student problem numbers: **[1, 2, 3, 4]**. Every student example and diagram was independently checked in the run's `final-audit.md` and executable `independent-check.py`; this guide audit separately checks the added adult claims rather than assuming student checks cover them.

Exact minima and every specified witness agree with the final student boards. The added 4×3 lower bound is valid: the only three-square area candidate is three side-2 squares, whose disjoint horizontal projections would need width 6. All restricted-size boundary/projection arguments and the height-5 packing extension are sound. The reverse reconstruction formula (q s+t,s), each supplied recipe's reduced dimensions, scale ambiguity, and last-square-size scale recovery are correct. All 255 positive recipes with lengths 1–4, entries 1–4 and last entry ≥2 were independently reconstructed and checked forward at three scales; algebra explains the general statement.

One edge-case explanation was corrected before this signoff. On guide PDF page 4, the original sentence “the preceding distinct square size is a strictly larger positive integer multiple of the last” did not cover a one-group nonsquare recipe such as [2] for a 2×1 rectangle. The current text separates one-group integer aspect ratio ≥2 from the multi-group previous-size/last-size argument. The theorem was valid throughout; the revised proof now covers both cases.

`guide-checks.json` records independently computed extra cases, scope, source/PDF hashes, exact final task mapping, and any resolved finding. General theorems were read and checked algebraically; finite enumerations support their supplied instances and do not substitute for general proofs.

Guide JSON SHA-256: `eca51bed4928ad18ad2fc15607112689d2e17970389083afc9557861fb7f5609`. Guide PDF SHA-256: `d1fd28800dde5b87fd4fccdb166edac5023e9b1c819ecde00d6545d4f966579f`. Final student source SHA-256: `533b945f671e8759c7986a3e4ce9123f706c2e139c1a64d32f7d43f0519c8ef6`.

Readiness, staffing, preparation and timing are stated as unpiloted proposals; no physical fit/procedure or classroom pilot is inferred from this mathematical pass. Source-attribution prose is not an assertion that these encore tasks were classroom-tested in those sources.
