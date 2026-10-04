# Week 29 revised answers and assumptions

Three investigations: ordered rod words (P1–P2), finite-stock complements (P3–P4), third-generator redundancy and minimum-piece continuation (P5–P6). Extra targets are not counted as separate investigations. One shared Grades K–5 companion; adult can record words/split totals while children choose and arrange rods. Recurrence/general explanations require readiness. Everything is unpiloted; rod dimensions, finite-kit procedure and physical unit fit have not been rehearsed. All compact diagrams are records; physical construction occurs beside the page with a separate ruler/two lanes. No ruler or cutout template is supplied.

## Problems 1 and 2

Whole 3/4 rods, fixed left endpoint, identical same-length pieces. Swapping unlike rods creates a new word. Non-task visual is actual row 4,3,4 read left-to-right and output word 4,3,4, total11. The pictured divisions correspond to rod lengths but scale is compact, not physical1cm.

- Length7: (3,4), (4,3), count2.
- Length10: (3,3,4), (3,4,3), (4,3,3), count3.
- Length14: (3,3,4,4), (3,4,3,4), (3,4,4,3), (4,3,3,4), (4,3,4,3), (4,4,3,3), count6.
- Length18: one word with six3s; ten words with two3s and three4s: 33444,34344,34434,34443,43344,43434,43443,44334,44343,44433. Count11. Compact strings here abbreviate comma-separated rod-length words, not decimal integers.

Let f(n) count words. f(0)=1 for the empty row; f(n)=0 for n<0. Ending in3 gives one word for each prefix reaching n−3; ending in4 gives one for each prefix reaching n−4. Every nonempty word falls into exactly one last-rod case, so for positive n, f(n)=f(n−3)+f(n−4). The value f(0)=1 is a separate starting condition, not an instance of that recurrence. Alternatively, with x three-rods and y four-rods, choose the x positions among x+y: binomial(x+y,x), summed over 3x+4y=n. A concrete complete list or last-rod grouping is a child's explanation. The P1 table has extra blank slots for smaller targets and does not imply they all need filling. The P2 twelve spaces likewise do not claim twelve answers.

## Problems 3 and 4

Sealed box contains exactly four3s and three4s, total24; no borrowing. Finite kit must be distinct from the unlimited table kit. The non-task split uses three3s and one4 (13); unused one3 and two4 (11). Two visible lanes externalize one split record. P3 cases:

- 6: used3+3; unused3+3+4+4+4=18.
- 9: used3+3+3; unused3+4+4+4=15.
- 10: used3+3+4; unused3+3+4+4=14.
- 19: impossible. Its complement5 would have to be a subset of3/4 rods, which is impossible. Direct combinations with at most three4s require nonintegral or too many3s.
- 22: impossible, because complementary length2 is impossible.

General complement: with stock4 three-rods/3 four-rods, subset(x,y) makes n=3x+4y and its unused complement(4−x,3−y) makes24−n. Thus n is possible iff24−n is possible, including0/24. Reachable targets are0,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24; gaps1,2,5,19,22,23. This full catalog is adult data, not a repeated printed gap-catalog task.

Equal rows have length12. Only the finite subset combinations for12 are four3s or three4s, so split all four3s into one row and all three4s into the other. This is possible even though the numbers of rods differ. Finite complement symmetry is valid for any finite stock with totalT; unlimited eventual coverage is inapplicable above24.

## Problems 5 and 6

Unlimited copies of each stated length, separate from finite box. Three independent toolkits are tested; no cumulative addition ambiguity. Original3/5 reachable set has gaps1,2,4,7, and every target≥8 is reachable (8=3+5,9=3+3+3,10=5+5; add3 to continue). This supports the new-generator conclusions, not a separate base gap task.

- Added8: no new target, because every8 can be replaced by3+5, independently for every occurrence.
- Added7: only target7 is new. It itself fills a gap; 1,2,4 remain impossible, and all other targets were already reachable.
- Added4: new targets4 and7. Original gaps1,2 still fail; 4 is now a single rod and7=3+4. All others were already reachable.

General theorem: adding lengthc to unlimited a/b rods changes no reachable targets iff c was already reachable with a/b. If c=ax+by, replace everyc by that construction. If not, c itself is a new target. This replacement argument assumes unlimited copies and need not work in the sealed box.

Minimum rods:

| Target | 3 and5 | 3,5,8 |
|---|---|---|
|16|4 rods:3+3+5+5|2 rods:8+8|
|24|6 rods:3+3+3+5+5+5|3 rods:8+8+8|

For16 without8, at leastceil(16/5)=4 rods, attained; with8 at least2, attained. For24 without8, five rods can sum at most25 but their sums have form15+2y, always odd, so cannot equal24; four or fewer sum at most20. Six attain24. With8, at least3, attained. Thus8 changes optimal piece count although it adds no reachable targets. P6 is this new optimization distinction, not unordered-build enumeration.

## QA and sources

`src/check.py` gives complete ordered words, enumerates all20 finite-stock combinations, tests complementary targets, checks added-length reachability through100, and computes exact minimum-piece counts. The finite range100 is supporting experiment; replacement/gap certificates above establish the infinite claims. Writer checks are not independent review. `writer-checks.json` stores results. Portable build accepts output directory, uses pdflatex/PDFLATEX and standard packages only. Every page rendered/inspected. Chapel Hill Math Circle's Frobenius activity is the base source precedent; no claim it supplies these new recurrence, complement or generator tasks.

## Revision scope

Problem 3 now asks for the unused length only for each successful build. No split should be entered for the impossible targets 19 or 22; those rows support an impossibility record. All targets, rod diagrams and mathematical models were preserved.
