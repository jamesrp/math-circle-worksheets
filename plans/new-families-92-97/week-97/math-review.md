# Week 97 independent mathematics review

Scope: the one accepted Grades 3–5 packet, `draft/students.pdf`, all six pages and all six problems. There are no K–1 or separate 2–3/4–5 packets in this run. Read the writer brief first, checked the actual PDF and source, rendered every page, independently enumerated all finite answers, checked every printed square-product card, and proved the two universal statements. The standalone checker and complete answer/proof inventory are `independent-check_math.py`, `independent-check-results.json`, and `math-answers.md` in this run.

## Located issue requiring revision

**Grades 3–5, page 1, shared rules before Problem 1 (affects Problems 1–6).** Exact text: “Remove complete bundles of the given size. The number left is the output; it can be 0.”

The operation does not explicitly say to continue until another complete bundle cannot be removed. For example, with the pictured input 3 and bundles of 4, removing just one complete bundle leaves 5 rather than the pictured output 1. Both moves satisfy the literal instruction, but produce different outputs. For Problem 1, an input of 4 has 16 counters; removing one complete bundle of 5 leaves 11, outside the intended output range 0–4. All enumerated answers and the prime theorem require the unique remainder.

Smallest fix: “Remove complete bundles of the given size until fewer than one bundle's worth remain.” Keep the existing worked visual, which correctly uses the same fixed input through all panels.

## Remaining mathematics

The Grades 3–5 packet checks out mathematically after that shared-rule clarification. No incorrect product card, array count, finite answer, collision claim, impossible task or false generalization was found. The complete inventories distinguish zero roots, maximum possible-input counts, and the number of different outputs correctly. All composite counterexamples are valid. Problems 5 and 6 explicitly request explanations beyond finite testing; their intended universal results have proofs in `math-answers.md`. The optional nonzero square/non-square product classification requested for the future guide is also independently verified and proved there.

This report concerns draft mathematics only. Introduction-reading conventions and operational age fit belong to the separate adversarial review; final rendered output and ZIP-release verification remain subsequent stages.
