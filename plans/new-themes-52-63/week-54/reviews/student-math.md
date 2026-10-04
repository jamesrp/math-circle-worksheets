# Week 54 independent mathematical review

Reviewed the actual nine-page `draft/students.pdf`, every rendered page, every concrete source diagram, and all nine problems. Direct combined-packet routing applies: pages 1–5 are Grades 2–5 and pages 6–9 are Grades 4–5; no independent K–1 packet is claimed.

## Located issue

**Grades 4–5 / page 6 / Problem 6 — specify that joining routes run to termination.**

Exact text: “Start with four 3-unit strips and six 1-unit strips. Try different legal joining routes. Can the routes end with different collections? Decide whether this can happen from any all-odd collection.”

The intended answer is no when each route continues until all strip sizes are different. Exhaustive independent enumeration finds 70 maximal legal size-choice routes from the supplied 18-unit collection; every one ends at `(12,4,2)`.

The printed text does not require reaching that stopping state. Under its literal finite-route reading, two legal one-join routes end differently: joining two 3-unit strips yields `(6,3,3,1,1,1,1,1,1)`, while joining two 1-unit strips yields `(3,3,3,3,2,1,1,1,1)`. Both are legal routes whose endpoints remain joinable. This makes “Can the routes end with different collections?” have a different correct answer.

Smallest fix: change “Try different legal joining routes.” to **“Try different legal joining routes until all sizes are different.”** The same condition then carries into the general question.

## Coverage

The Grades 2–5 material on pages 1–5 checks out completely for mathematical correctness. Grades 4–5 pages 7–9 also check out. All illustrated input/intermediate/output unit counts, complete odd/distinct catalogs and matches, conjugation examples, and restricted-catalog counts are correct. No other located mathematical issue was found.

The independent solved audit and reproducible checks are in `independent-math/math-audit.md`, `independent-math/check_math.py` and `independent-math/verified-data.json`. They cover all 7,338 partitions of totals 0–24, every legal join/split terminal outcome, complete requested answer lists, universal arguments and their limits, and actual source-coordinate/PDF unit-square matching. Neither the writer verifier nor earlier critic reports were used.

Physical handling and classroom piloting were not performed.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
