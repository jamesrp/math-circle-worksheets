# Week 97 independent mathematical answers

Scope: the actual six-page Grades 3–5 `draft/students.pdf` and its `draft/src/students.tex`. No younger packets exist in this accepted scope. Checked the extracted PDF, all six rendered pages, dot-array code, and every numeric support card. The separate standard-library checker independently constructs square counts by repeated addition and remainders by complete-bundle subtraction, then cross-checks division. It imports no writer code. Its finite tests support data accuracy; the arguments below establish the universal statements.

## Convention needed throughout

Remove bundles **until fewer than one bundle's worth remain**. For a positive bundle size m, this uniquely produces one output in 0,...,m−1. The input is the side length of the square, not its area. An input of zero is allowed and produces zero. All finite input ranges below are inclusive. The count of possible inputs for one output is different from the count of different outputs across the whole range.

The opening has nine dots in a 3-by-3 square, the same nine dots partitioned into two four-dot bundles and one leftover, and a one-dot output. The arithmetic 9=4+4+1 is exact. The Problem 1 input panels show respectively 0,1,4,9,16 counters in square arrays. All 51 printed support-card occurrences have the correct product. Larger task arrays are represented by number facts, so a supply of 64 counters is not a claim that every later square can be built simultaneously.

## Complete inventories

Each entry reads `output: all possible inputs`. The inputs in the column for m are exactly 0 through m−1. An omitted output from 0 through m−1 is impossible in that column.

| Bundle size m | Complete output-to-input inventory | Different outputs |
|---|---|---:|
| 3 | 0: {0}; 1: {1,2} | 2 |
| 5 | 0: {0}; 1: {1,4}; 4: {2,3} | 3 |
| 7 | 0: {0}; 1: {1,6}; 2: {3,4}; 4: {2,5} | 4 |
| 8 | 0: {0,4}; 1: {1,3,5,7}; 4: {2,6} | 3 |
| 9 | 0: {0,3,6}; 1: {1,8}; 4: {2,7}; 7: {4,5} | 4 |
| 11 | 0: {0}; 1: {1,10}; 3: {5,6}; 4: {2,9}; 5: {4,7}; 9: {3,8} | 6 |
| 15 | 0: {0}; 1: {1,4,11,14}; 4: {2,7,8,13}; 6: {6,9}; 9: {3,12}; 10: {5,10} | 6 |

## Page 1, Problem 1

Task: find every pair of distinct inputs 0–4 with equal square output for bundles of 5, and impossible outputs.

Exactly two unordered pairs: {1,4}, producing 1; and {2,3}, producing 4. Input 0 has no different partner. Outputs 2 and 3 cannot occur. Reversing the order of a pair does not give a different mathematical pair; either recording convention is fine if the full collection is clear. Exhaustive verification requires only the five allowed inputs. There is no claim yet about inputs greater than 4.

## Page 2, Problem 2

Task: reverse the square-output operation for bundles of 7, with secret input in 0–6, then compare the possible-input counts of occurring outputs.

Output 0 forces input 0. Output 1 allows 1 or 6; output 2 allows 3 or 4; output 4 allows 2 or 5. The outputs with the most possibilities are 1,2,4, each hiding two inputs. The fewest is 0, hiding one. Outputs 3,5,6 are excluded by “among outputs that occur,” so their zero possible-input counts do not answer the minimum question. The partner cannot determine a unique input from a nonzero output; the task correctly requests every possibility. Operationally the maker should hide the square as well as the chosen input, otherwise the square's side length discloses the secret.

## Page 3, Problem 3

Task: compare largest equal-output collections for bundles of 7,8,9 over their stated full input ranges.

- Bundles of 7: outputs 1,2,4 tie at two inputs each.
- Bundles of 8: output 1 alone has the largest collection, {1,3,5,7}, of size four.
- Bundles of 9: output 0 alone has the largest collection, {0,3,6}, of size three.

Thus bundles of 8 allow the largest ambiguity in these specified ranges. Zero can hide several inputs: two for 8 and three for 9. The zero input remains a participant. The question is an existential comparison of these examples, not a universal claim that any composite modulus has multiple zero roots; for example 15 has only zero itself as a zero root.

## Page 4, Problem 4

Task: reverse output 1 for bundles of 15 over inputs 0–14, then ask whether any output hides more inputs.

The four inputs are 1,4,11,14. Their squares are 1,16,121,196, each one above a multiple of 15. No output hides more than four inputs. Output 4 ties, with inputs 2,7,8,13. The complete inventory above establishes the negative answer, rather than checking only output 1. The phrase “between 0 and 14” has no answer-changing endpoint ambiguity here: 0 is not a root of 1, whereas excluding 14 would incorrectly lose a root. The shared input-range convention should be inclusive, as elsewhere in the packet. Ordinary school usage normally is inclusive; explicit 0–14 notation would also remove this minor interpretive possibility.

## Page 5, Problem 5

Task: decide whether an arbitrarily large whole-number input can give a new output modulo 7, with an explanation for all inputs.

No. For any nonnegative integer n, divide n into complete sevens and a remainder: n=7q+r with 0≤r<7. Then

n²−r² = (7q+r)²−r² = 7q(7q+2r),

which is a multiple of 7. The two squares leave the same output. The only outputs are therefore 0,1,2,4, already reached by the inputs 0–6. Checking many large examples alone is not proof.

A picture can establish the same fact. From an n-by-n square remove a rectangle of width 7q and height n, then from the remaining r-by-n rectangle remove a rectangle of height 7q and width r. Both removed areas divide into bundles of 7; an r-by-r square remains. For n=10, this removes 70 and then 21 counters, leaving 9; 100 and 9 both leave output 2. Do not assume that removing seven rows removes only seven counters: each full row has its own width. The argument works for every positive bundle size m with n=mq+r, not just 7.

Printed P5 facts give outputs for inputs 7–15 respectively 0,1,4,2,2,4,1,0,1. They contain no new output. The checker tests the exact algebraic identity and outputs through input 700; the displayed identity covers all whole-number inputs.

## Page 6, Problem 6

Task: count outputs for 3,5,7,11, discover the odd-prime rule, explain it universally, and test composites 8,9,15.

The counts including zero are 2,3,4,6. The intended rule is (p+1)/2 for every odd prime p, or “one for zero, and one for each pair of nonzero opposite inputs.”

For inputs x,y in 0,...,p−1, equal square outputs are equivalent to p dividing x²−y²=(x−y)(x+y). A prime dividing a product divides at least one factor. Therefore x=y, or x+y is a multiple of p. For distinct inputs the latter sum is positive and less than 2p, so x+y=p. Conversely, equal inputs or a pair summing to p always produce equal outputs. Zero is alone: p divides x² only when p divides x, and in this range only x=0 qualifies. The nonzero inputs form (p−1)/2 disjoint pairs {x,p−x}; no nonzero input pairs with itself because 2x=p has no integer solution for odd p. Different pairs cannot share an output, by the same collision criterion. Adding zero gives (p+1)/2 outputs.

A self-contained justification of the prime-product fact: if prime p does not divide a, consider the least positive integer d of the form ua+vp with integer u,v. Division with remainder shows d divides both a and p: otherwise the remainder of either on division by d is a smaller positive integer of the same form. Since p is prime and does not divide a, d=1. Multiply ua+vp=1 by b. If p divides ab, both uab and vpb are divisible by p, so b is divisible by p. This proof is adult background; pupils can use a facilitated picture/number argument and revisit generality later.

The rule does not extend to the three listed composites: actual counts for 8,9,15 are 3,4,6; the expression (m+1)/2 would give 4.5,5,8. The comparison at 8 is intentionally outside the odd hypothesis as well as the prime hypothesis. Stronger counterexamples to the pairing claim are 1²=3² modulo 8 (1+3≠8), 0²=3² modulo 9 (0+3≠9), and 1²=4² modulo 15 (1+4≠15). The prime-product fact fails there: 8 divides (3−1)(3+1)=8 but divides neither factor, for example. Do not call all composites exceptions to every prime-pattern statement; only these concrete counterexamples and the stated restricted theorem have been established.

## Optional adult return visit: multiplying output classes

This is not an additional student problem. For odd prime p, let Q be the nonzero square remainders and N the other nonzero remainders. Exclude zero throughout. Then Q×Q lands in Q, Q×N and N×Q land in N, and N×N lands in Q. Modulo 7, Q={1,2,4} and N={3,5,6}. This describes classes of outputs, not the original square-map inputs.

Proof: nonzero multiplication modulo p is cancellable by the prime-product fact, and hence permutes the finite nonzero remainders. In particular every nonzero a has an inverse. Products and inverses of squares are squares. For a fixed nonsquare a, the set aQ has the same size as Q and is disjoint from Q: if aq were a square, multiplying by the square inverse of q would make a a square. The prime output-count theorem gives |Q|=|N|=(p−1)/2, so aQ=N. Any other nonsquare b has the form aq with q in Q; therefore ab=a²q lies in Q. This also proves square times nonsquare is nonsquare and covers every product class.

The independent checker verifies these product classes, all nonzero multiplication permutations, and the exact square-collision criterion for every odd prime through 97. Those finite checks are distinct from the proof. The classification is not asserted for composite moduli, and zero cannot be silently included in Q or N.

## Result and limits

All intended numerical answers, diagrams, support products and theorem claims are correct under complete removal. One mathematically relevant wording fix is required in the opening; it is located in `review-math.md`. The source proof claims in this report are independent derivations, not paraphrases of the writer's verification. This is a mathematical review of the draft, not a final-PDF release check, physical rehearsal, classroom pilot, or age-fit validation.
