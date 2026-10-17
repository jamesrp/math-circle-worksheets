# Independent mathematical verification — Week 87 draft

Fresh reviewer; no writer code imported or executed. Reviewed PROMPT.md, then all 14 actual rendered draft pages and the source geometry; read the adversarial review for its located concerns. This record supplies positive verification and explanations; review-math.md lists the located defects. Source/PDFs were not edited.

## Reproduction and evidence

- `python3 independent_check.py` runs the independent finite checks using only the standard library and writes `results.json`.
- `python check_pdf_geometry.py` needs PyMuPDF; it reads the actual draft PDFs and writes `geometry.json`, including all four SHA256 hashes.
- All 14 pages were independently rendered at 1.2 pixels per PDF point and visually inspected: shared 1–3, line 1–4, upper 1–2, materials 1–5. Render PNGs remain temporary, not required as published provenance.
- All PDFs are US Letter, 612 × 792 points. Printed profile orders, voter identities, favorite positions, and conversion diagrams agree with the checked inputs below.

## Shared Grades 2–5

**Page 1 convention.** Fixed DFE/EFD/FED cards give D/E votes D,E,E, hence E wins 2–1. V3 does not vote for unavailable F. Page 2 retains that profile; E/F votes F,E,F, so F wins the final 2–1. These are complete valid operations.

**Problem 1, page 1.** The request is a letter beating both others. ABC/BCA/CAB gives A over B, B over C, C over A, each 2–1. There is no such letter.

**Problem 2, page 2.** Any desired candidate wins by waiting: wait A, first B/C gives B then A beats B; wait B, first A/C gives C then B beats C; wait C, first A/B gives A then C beats A. The order within the first pair is immaterial. No card changes between rounds.

**Problem 3, page 3.** Both requested designs exist with three different cards. ABC/ACB/BAC gives A over B 2–1 and A over C 3–0, so A wins all agendas. ABC/BCA/CAB supplies the changing-winner design. Independently enumerating all 20 unordered sets of three distinct rankings finds 18 with a universal winner and 2 with a cycle. Enumeration of all 216 labelled profiles also confirms that a universal pairwise winner exists exactly when all agendas have the same winner. These counts are adult verification, not a required student enumeration.

## Line Grades 3–5

**Page 1 convention.** Favorite 2 with X=0,Y=5 gives distances 2,3 and X; favorite 3 with X=1,Y=5 gives 2,2 and Tie. Each example is arithmetically correct. Neither shows the full multiple-voter operation; that located design issue is already in review.md. The critic's suggested unchanged input 0,1,5,8,10 with X=2,Y=8 has votes X,X,Tie,Y,Y and a 2–2 tied contest.

**Problem 1, page 1.** For 0,2,4,7,10, the unique universal winner is 4. Against 0 or 10 it gets 3 votes, the opponent 1, and 1 tie. Against each other tick it wins 3–2. All ten checks appear in results.json.

**Problem 2, page 2.** In displayed order the winners are 0,4,6 for favorite multisets (0,0,0,8,10), (1,4,4,4,9), (0,1,6,9,10). Repeated favorites retain separate votes; zero retains its voter. Each wins every other tick, checked exhaustively.

**Problem 3, page 3.** Let the five favorite locations in nondecreasing order be p1,...,p5 and m=p3. Against q<m, voters at p3,p4,p5 strictly prefer m because each is at or to its right: |p−q|=|p−m|+(m−q)>|p−m|. Against q>m, voters at p1,p2,p3 strictly prefer m by the reflected argument. Therefore m receives at least three strict votes, even if the remaining voters tie or share favorite locations. The result holds on the real line whenever m is offered, not only on this finite board. The independent finite check covers all 3,003 multisets of five ticks, each against ten other ticks (30,030 comparisons). This corroborates rather than substitutes for the argument.

**Problem 4, page 4.** For 1,3,7,9 the nonlosing ticks are exactly 3,4,5,6,7; no tick strictly beats every other one. Proof on the real line: if x is in [3,7], any challenger y<x is opposed by the voters at 7 and 9, who strictly prefer x; any challenger y>x is opposed by those at 1 and 3. Thus x cannot lose (at most two votes for y). If x<3, proposal 3 wins the voters at 3,7,9, so x loses. If x>7, proposal 7 wins the voters at 1,3,7. Two distinct proposals in [3,7] split 2–2; hence no strict universal winner exists. For the printed tick domain take the integer points of this interval. The independent checker additionally verifies the median interval for all 1,001 four-voter tick multisets. Do not describe every even electorate as having no strict winner: coincident middle favorites can make the median interval a singleton. The printed four distinct favorites do have no strict winner.

## Upper Grades 4–5

**Problem 1, page 1.** Top profile ABC/ACB/BAC has A beating B 2–1 and C 3–0; A survives or awaits any first round and beats its opponent, so the agenda cannot change its victory. Bottom ACB/CBA/BAC has B over A, A over C, C over B, all 2–1. As in a three-cycle, each waiting candidate wins. Each displayed card is included in the independent checker.

**Problem 2, page 2.** Worked conversion: favorite 1, D=0,E=4,F=9 gives distances 1,3,8 and strict DEF. Correct unchanged input.

The target ABC/BCA/CAB cannot arise from three distinct candidate locations on any common real line with nearer preferred. Let the left, middle, right candidate positions be a<b<c. For any favorite p≤b, |p−c|>|p−b|, so c is farther than b. For any p≥b, |p−a|>|p−b|, so a is farther than b. Thus the middle candidate is never strictly last. But each of A,B,C is last on one of the required cards. Whichever candidate occupies the middle contradicts that card. This covers all real positions, including favorites outside the candidates, and all six candidate orders. Tied distances do not rescue a strictly ranked target. `results.json` lists the six order/obstructed-voter certificates. The additional 1,428 integer-distance checks are only supporting experiments, not the impossibility proof.

## Actual printed materials geometry

PDF vector measurements (rounding tolerance 0.01 mm) confirm: three 45×80 mm fixed cards, six 28 mm square option tiles, five 18 mm circular vote tokens, six 45×80 mm blank cards, thirty-six 21 mm square letter slips, three 54 mm square tally wells with eighteen 17 mm target circles, a 175×100 mm knockout mat, five 13 mm favorite circles, X a 13 mm square, and Y a rotated square with 18 mm diagonals. All polygons have the expected four sides; all board axes have equal intended physical scale.

Ranking rows are (80−10)/3=23.33 mm tall, allowing 21 mm slips with vertical clearance. Knockout first/final-pair wells are 61×39 mm, allowing two 28 mm tiles beside each other with 5 mm total horizontal spare room. Single 29 mm wells have 1 mm total spare width; the Out well is 29×85 mm and can hold two losers vertically. These nominal fits need real cutting/handling rehearsal.

Five favorite lanes have 19 mm pitch over a 160 mm span; numbered ticks have 16 mm pitch. Coincident favorites occupy independent lanes with 6 mm edge separation for 13 mm circles. Adjacent X/Y proposal markers have a minimum 0.5 mm horizontal edge gap if centered on adjacent ticks. The printed model distinguishes votes, which move, from favorite positions, which remain fixed.

Two geometry/state issues remain exactly as located in review.md: the tally targets are smaller than the actual vote tokens and their placement gives zero nominal token/boundary clearance; and line proposal markers do not have duplicate X/Y tally labels. These are material-operation defects, not counterexamples to the mathematics. No physical rehearsal or classroom trial was performed.
