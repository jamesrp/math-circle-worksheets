# Week 97 fresh final student–guide review

## Scope and verdict

Independent final-pair reviewer; no publication or source edits. Read AGENTS.md, the current group context, the final student and guide sources, actual PDFs, package documentation and earlier critic/math/revision reports. Rendered and personally inspected every page of both PDFs at 1.5× (918×1188 pixels per US Letter page), including page edges and footers. This is one six-page Grades 3–5 packet and one six-page facilitator guide, with no claimed K–1 packet.

**PASS: mathematics, final page layout, readiness and student–guide agreement. No remaining required correction.** The coordinator added the requested concrete divisor definition on guide page 5 and updated the page 6 review-status sentence. I re-rendered and inspected both changed pages, confirmed that guide pages 1–4 are pixel-identical to their previously inspected versions, and independently rebuilt the final pair again. Both final PDFs match their rebuilds byte-for-byte.

## Every-page visual coverage

| File/page | Actual inspection |
|---|---|
| Student 1 | Same fixed input 3 throughout: nine dots, two four-dot bundles plus one, one-dot output. Non-task bundle-4 collection has clear input/output labels and distinguishes possible inputs from different outputs. Revised stopping condition is explicit. Input arrays 0–4 have correct counts and equal scaling. Problem and wide working box fit. |
| Student 2 | Partner inverse task, square facts through 6², and large work area are legible. Header/footer and page number intact. |
| Student 3 | Three bounded input domains and comparisons are unambiguous; facts through 8² and working box fit. |
| Student 4 | Inclusive 0–14 domain, 15 correct square facts, and work area fit cleanly. |
| Student 5 | Universal-input problem is visibly distinct from testing examples; square facts through 15² and ample workspace fit. |
| Student 6 | Count includes zero; odd-prime conjecture and composite checks are clear. Eleven product cards and workspace fit. |
| Guide 1 | Theorem-first overview precedes solutions. Assumptions, zero conventions, finite versus universal claims, composite limitations, optional product classification and readiness map are legible. |
| Guide 2 | Full preparation/launch/first-route text fits. Same nine counters remain the reference in the launch; collection-reading demonstration and partner secrecy agree with students. |
| Guide 3 | Complete size-5/7/8/9 tables fit without clipping. All solution text, hints and footer are clear. |
| Guide 4 | Size-15 inventory, size-7 large-input sequence, area proof and diagram fit. The shortened vertical “3×7=21” label lies wholly inside its rectangle, with no overlap. Area regions have the correct 7:3 and 7:3 proportions. |
| Guide 5 | Prime inventories, factorization, exact-pair proof, prime-divides-product proof and composite limitations fit. The added divisor definition is concrete and fits cleanly; re-rendered and re-inspected after correction. |
| Guide 6 | Optional product-class table, complete operation example, general proof, connections and provenance fit. No missing glyphs or collisions. Final completed-review status sentence was re-rendered and re-inspected after correction. |

No clipping, overlap, accidental blank page, broken symbol, incorrect dot count, distorted square, header/footer mismatch or insufficient line spacing was found. Student problems are consecutive 1–6. No extra student headings, Name/Date fields or adult commentary were introduced.

## Independent mathematics and completeness

I recomputed the finite inventories independently of the package checker using a fresh Python dictionary indexed by x² modulo m. These match every guide entry:

| m | Output: input collection |
|---|---|
| 3 | 0: {0}; 1: {1,2} |
| 4 | 0: {0,2}; 1: {1,3} (worked convention only) |
| 5 | 0: {0}; 1: {1,4}; 4: {2,3} |
| 7 | 0: {0}; 1: {1,6}; 2: {3,4}; 4: {2,5} |
| 8 | 0: {0,4}; 1: {1,3,5,7}; 4: {2,6} |
| 9 | 0: {0,3,6}; 1: {1,8}; 4: {2,7}; 7: {4,5} |
| 11 | 0: {0}; 1: {1,10}; 3: {5,6}; 4: {2,9}; 5: {4,7}; 9: {3,8} |
| 15 | 0: {0}; 1: {1,4,11,14}; 4: {2,7,8,13}; 6: {6,9}; 9: {3,12}; 10: {5,10} |

Problem 1 has exactly the two printed different-input pairs and missing outputs 2,3. Problem 2's occurring-output restriction correctly makes output 0 the minimum, and 1,2,4 the tied maxima. Problem 3's maxima have sizes 2,4,3 for bundle sizes 7,8,9, respectively; zero has multiple inputs for 8 and 9. Problem 4 has exactly four inputs for output 1, and output 4 ties rather than exceeds it. Every finite table covers each allowed input exactly once. Problem 5's inputs 7–15 give 0,1,4,2,2,4,1,0,1. Problem 6 counts are 2,3,4,6; composite counts are 3,4,6 for 8,9,15.

All 51 printed square-product card occurrences check arithmetically. The newly added bundle-4 convention is correct, with exactly two different outputs and output 1 hiding two inputs. Zero is consistently an allowed input/output; it is excluded only from the optional nonzero product classification.

Universal statements were checked as proofs, not certified by finite tests:

- Writing n=mq+s, removing mq columns and then mq rows from the remaining rectangle removes multiples of m and leaves s². The area identity n²−s²=mq(mq+2s) covers q=0, s=0 and any positive m. The 10×10 diagram removes 70+21 and leaves 9, with both 100 and 9 having remainder 2 modulo 7.
- Equal squares modulo odd prime p imply p divides (x−y)(x+y). The supplied least-positive-linear-combination argument establishes the prime-divides-product lemma without depending on Week 96. Within 0,…,p−1 this gives equal inputs or distinct inputs summing to p. Zero is alone; the nonzero opposite pairs are distinct and no different pairs share outputs. Thus the count (p+1)/2 including zero is proved. The composite counterexamples identify the exact failed inference; size 8 is explicitly outside oddness as well.
- Nonzero multiplication modulo prime p is injective by cancellation and hence permutes the finite nonzero labels, giving inverses. Nonzero square labels are closed under products and inverses. Multiplication of all squares by a fixed nonsquare a gives distinct nonsquares, and equal cardinalities make this every nonsquare. Writing another nonsquare b=aq yields ab=a²q square. This establishes Q×Q→Q, Q×N→N, N×N→Q with zero excluded. No composite assertion is made. The concrete 3×5=15→1 example properly changes to a rectangle, which the text explains.

As an extra sanity check, my separate code tested exact opposite-pair equivalence and every nonzero product-class combination for all odd primes below 200, plus the area identity for m=1,…,50 and n=0,…,999. These experiments support the transcription checks, not the universal proofs.

## Readiness, materials, provenance and limits

The guide's group counts and rotating roles agree with current context (four third graders and a three-child upper table). Sixty-four counters per pair cover the concrete first three tasks, one square at a time; larger squares use supplied facts and drawings. A separate familiar activity for K–1 is explicitly required. The launch demonstrates the full action before tasks and explains the new collection-reading convention. Reading/recording support is separated from adults managing the mathematics. Problems 1–2 form a credible first route, with comparisons and proofs reserved for readiness-dependent return visits; no promise says all six pages fit one hour.

The inference connection is precise: an exact output can lose input information without random sampling or measurement noise. Prime-factor and finite-field activities are treated as connections, not required prior lessons. The optional multiplication continuation changes the question substantively.

I reopened both primary Conrad references. Modular Arithmetic §3, PDF pp. 3–4, contains representative-independent multiplication and the composite square-root counterexample; Quadratic Residue Patterns Modulo a Prime uses the nonzero convention. Guide and SOURCES.md agree on their citations and distinguish zero-inclusive student counts. Prior-corpus and Math Circle by the Bay provenance is carried in the coordinator's documented source audit; I did not re-audit that whole corpus for this final-pair stage. No borrowed whole paper/book is present in the inspected source package.

Unpiloted operational concern remains: the size-15 remainders may require an adult-supported multiples strip even with square facts supplied. The guide already handles this without prescribing the child's mathematical organization. Actual printing, materials, timing and classroom use remain untested.

## Build and version evidence

Ran the supplied build.py in this isolated checkout into pair-build/ with a separate pair-work/. Its independent check_math.py passed; both pdfLaTeX builds passed without overfull boxes. Rebuilt PDFs are byte-for-byte identical to inspected publication PDFs:

- Student: 129835 bytes; SHA-256 0300f0ba01ce6d27df59ffd80603c6ee876ffe99215dbcd9c9a59b3421f8aa22.
- Final guide after readiness/status update: 200317 bytes; SHA-256 55459ecc27c955b12cd7cceef6d7da9eaa093eec0c86162f1c1064c03ba84b09.

Rendering evidence: tmp/worksheet-runs/week-97-v1/pair-render/{students,facilitator}-1.png through -6.png; matching extracted text was also saved. The editable sources and inspected PDFs agree. Portable ZIP assembly/reference copies/QA.md were not yet present in this review snapshot; final archive contents, clean extracted rebuild and remote integration remain coordinator checks and are not claimed here.
