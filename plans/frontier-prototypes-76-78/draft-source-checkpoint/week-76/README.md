# Week 76: Substitution strips

One shared four-page Grades 3–5 student prototype. Packet ID: F76-35-v1.

## Prerequisites and materials

Children need to read short A/B strings, preserve left-to-right order and work with a partner. The late questions ask for impossibility explanations; the infinite-tail question needs readiness for abstract reasoning and may need an adult. Grade labels are approximate. There is no K–1 or separate Grades 2–3 edition.

For each pair, provide 32 reusable A/B counters or cards and two separate table rows, plus four divider markers and pencils. Distinguish tiles by letters as well as any color. Separately handled counters should be at least 15 mm wide. The printed 7–10 mm cells are pencil diagrams, not counter-fitting mats. Long physical strips extend onto the table. Reuse the older row's counters only after the new row has been checked. No cutting or exact-fit pieces are required.

## Build

Requires Python 3 (standard library only) and a normal TeX Live installation with pdfLaTeX, TikZ/PGF, geometry, fancyhdr and Latin Modern fonts.

From this directory:

    python3 check_math.py
    python3 build.py --out /path/to/output

The builder creates students.pdf in the requested directory, checks the finite examples and rejects overfull TeX boxes. It creates and removes temporary build files inside the output directory. On failure it leaves build-error.log. The source folder is portable and contains no external images, borrowed text, workflow prompts or downloaded resources.

## Checks and limits

check_math.py verifies every fixed diagram string, whole-row histories, crop examples and both genuinely possible alignments of the short ambiguous crop. Its exact factor-language computation checks all three- and five-letter factors and the two finite witnesses against the repeating strips. Passing these checks is not a proof of infinite nonperiodicity.

Print single-sided on US Letter at 100%. Page diagrams and typography are subject to digital rendering review. Physical handling, timing, adult support needs and classroom use remain untested. The abstract final question is an optional stopping point by readiness, not an expectation that every child complete an infinite proof.
