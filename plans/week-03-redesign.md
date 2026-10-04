# Week 3: reversible code machines, concise investigations

Prepared September 30, 2026. **Unpiloted v4.** The [current print packets and build instructions](../lowell-math-circle-year-2/source/week-03/README.md) replace v3 in the main Week 3 output folder. Each student packet has three pages; the adult guide has six. Previous files are separated in `archive-before-concise-2026-09-30/` under the source and output folders; the previous plan is [here](archive-before-concise-2026-09-30/week-03-redesign.md).

## Reference and design decision

The actual models reviewed were the current, top-level [Week 2 compact catalog](../lowell-math-circle-year-2/week-02/week-02-shared-catalog.pdf) and [upper catalog](../lowell-math-circle-year-2/week-02/week-02-shared-catalog-upper.pdf), plus the [upper catalog's adult notes](week-02-catalog-upper.md). Their key principle is a clear goal that supports substantial independent work, with contrasting examples and little prescribed method. The response here is not to make all mathematics diagram-based: key tables specify the mapping, message pairs supply clues, and blank areas leave the record to the child.

The earlier Week 3 edition had 35 numbered tasks, often telling children to trace, draw loops, mark multiples, or enumerate prescribed partitions. This edition has 17 problems: K 5, middle 5, upper 4, extra 3. Shared rules are stated once, while optional scaffolding moves to the facilitator guide. Central completeness, impossibility, and optimality questions remain explicit. The guide includes all required prerequisites, materials/preparation, timing, launch, exploration prompts, hints, extensions, and checked solutions.

The three approximate entry levels and the extra packet are retained. The user asked to transfer the Week 2 principles, not to replace all weeks with a shared-book format. Adults can offer any page by readiness; reading or handwriting does not determine mathematical access.

## Problems and mathematical purpose

| Packet / page | Problems | Concrete work and depth |
|---|---|---|
| K / 1 | 1–2 | Six forward/backward shape-message examples, including repeated shapes; partner message invention. |
| K / 2 | 3 | Two keys and three starting messages: the whole message can return later than one fixed symbol. |
| K / 3 | 4–5 | Invent keys whose messages can always be recovered; find all four inputs that produce two squares under a non-injective key. |
| Middle / 1 | 1 | Six hidden-key clues: two, one, zero, zero, two, one solutions. Distinguish inconsistent repeated inputs from merged distinct inputs. |
| Middle / 2 | 2–3 | Nine return experiments using three keys and three messages; two keys can agree on ABBA but have different whole-key return times. |
| Middle / 3 | 4–5 | Construct all four-letter return times, then achieve six with five letters and explain the four-letter obstruction. |
| Upper / 1 | 1 | Four five-letter keys return in 5,6,4,2 turns. The longest single loop need not produce the longest return. |
| Upper / 2 | 2 | Construct and justify all possible five-letter first return times, including the maximum six. No classification algorithm is supplied. |
| Upper / 3 | 3–4 | Overlapping swaps fail to commute, disjoint swaps commute, and inverse three-cycles overlap but commute. Repeat and undo a combined machine. |
| Extra / 1 | 1 | Build eight-letter keys with returns 4,6,8,12,15, without supplied loop sizes. |
| Extra / 2 | 2 | Construct and prove the records for eight and nine letters: 15 and 20. |
| Extra / 3 | 3 | Find the record for sizes 1–9, disprove strict growth using five/six letters, and prove adding a letter can never lower the record. |

## Preparation, prerequisites, and the hour

Use the current **ten-child roster, KK1 / 3333 / 445, with three adults**, replacing the obsolete seven-child example. Parent anchors the youngest table; the other mathematician the four third graders; organizer the three oldest. Start with ten first sheets: 3 K, 4 middle, 3 upper. Keep selected continuation masters, blank paper/whiteboards, and adult notes. No room printer is assumed. Cards are optional hand-drawn scraps: two sets of three shapes per K child; A–D per middle child; A–E per upper child; F–I in reserve.

K starts with shape matching and adult reading, then counting to three. Middle uses letters as labels, small counts to six, and a one-to-one rule. Upper coordinates several return times and justifies completeness. Extra uses common multiples through 20 and a bound covering every case. Children can act, point, dictate, or use their own records. Formal group theory, factorials, and written proof are not entry requirements.

Proposed hour: 0–4 handle materials; 4–8 common demonstration; 8–28 sustained investigation; 28–33 movement/reset; 33–50 continue or choose another question; 50–55 share; 55–60 tidy. Show one turn without changing a newly written output again in that same turn. Demonstrate an empty input before an arrow and a letter-key column. Do not show a solving algorithm. Ordinary problems may occupy 8–15 minutes, bounds 15–30 or longer; these are planning allowances, not classroom evidence.

A recovered message, a useful impossible clue, or the five-versus-six return comparison can be a complete session. The facilitator may introduce arrow loops only after children have followed repeated substitutions and need a useful record. Largest-loop case organization and common-multiple markings are optional hints, not required intermediate work.

## Mathematical checks and complete arguments

The six middle clue solution sets, as output rows for inputs ABCD, are: `{CDAB,CDBA}`, `{BCDA}`, empty, empty, `{ABCD,ABDC}`, `{DBAC}`. Identical inputs have identical outputs for any function; distinct inputs have distinct outputs for a reversible key. Equality patterns are therefore preserved exactly.

Under middle P/Q/R, starting messages D, ABBA, ABCD have return rows `[1,2,4]`, `[3,2,4]`, `[3,2,4]`. The keys BCAD and BCDA both encode ABBA as BCCB, while their whole-key orders are three and four. The message does not test all key entries.

Following a finite reversible key gives disjoint loops: a first repeat other than the start would give one symbol two distinct predecessors. Remove each loop and continue. A loop returns at multiples of its length; all letters return together at the least common multiple. Four-letter partitions give orders 1,2,3,4; five-letter partitions give 1,2,3,4,5,6. The guide supplies every partition and explains completeness. A 3+2 key attains six and requires five letters.

For composition, P/Q yield CABDE versus BCADE, P/L yield BACED in either order, and V/W yield ABCDE in either order. Disjoint moved sets suffice for commuting, but overlap alone decides nothing. The exact test checks both routes on every input. The P-then-Q machine has order three; Q-then-P undoes it, since both component swaps are self-inverse.

Eight-letter constructions with loop sizes 4+4,6+2,8,4+3+1,5+3 give 4,6,8,12,15. The eight-letter largest-loop bounds for 8,7,6,5,4,at most 3 are 8,7,6,15,12,6. Nine-letter bounds for 9,8,7,6,5,4,at most 3 are 9,8,14,6,20,12,6. The guide expands the leftover partitions and justifies the bounds.

Maxima for sizes 1–9 are **1,2,3,4,6,6,12,15,20**. Five and six give a plateau; adding a fixed new letter proves that the maximum never decreases at any size. The optional g(7)=12 is justified by all largest-loop cases as well as construction 4+3.

[verify.py](../lowell-math-circle-year-2/source/week-03/verify.py) exhausts every permutation for sizes 1–9, checks every stated clue/witness/return/composition, and verifies the exact largest-loop bounds. [Results](week-03-checks.json) are mathematical data, not evidence of teaching. Computation supplements the guide's proofs.

## Source findings and our adaptations

Locally reviewed during this revision:

- **Rozhkovskaya, Math Circles for Elementary School Students**, Lesson 2, Problems 2.2–2.8 and “At the lesson” (`OEBPS/part0012.xhtml`): coded messages, repeated-letter clues, and successful reasoning by children not yet fluent readers. Hidden short-alphabet keys and arbitrary permutations are our adaptation; the source mainly uses shifts.
- **Lesson 3**, “At the lesson,” item 1 (`part0013.xhtml`): children attempted and explained before a table was supplied; reserve problems accommodated different experience. **Lesson 8**, item 2 (`part0018.xhtml`): copying and coloring speed divided the group. Moving procedural tables into adult support is our response, not a source prescription.
- **Math Circle by the Bay**, preface printed viii–x (PDF 9–11): substantial themes, manipulatives, independent work, clear statements, varied pace/depth, and reserve questions. These findings support our approach; they do not establish the exact prompts or their duration.
- **Lowell year 1, Handout 8, Problem 8.1**: apples shared evenly for possible guest counts, providing a prior common-multiple connection. A saved handout does not establish which children encountered it.

Existing mathematical lineage remains: Judson, *Abstract Algebra: Theory and Applications*, Chapter 5 §5.1, on permutations and cycle decomposition; Deléglise, Nicolas, Zimmermann, *Landau's function for one million billions* (2008), §1.1–1.3, for the maximal-permutation-order question. This revision relies on self-contained finite proofs and makes no claim about current research status. Week 4 deliberately narrows arbitrary reversible keys to fixed circular shifts.

## Review and future evidence

[REVIEW.md](../lowell-math-circle-year-2/source/week-03/REVIEW.md) records mathematical, visual, and combined-packet checks. Previous combined print sets are preserved in `combined/archive-before-week-03-concise-2026-09-30/`. Only Week 3 and the contents/bookmarks are refreshed in the combined files; their already embedded Week 2 collection is preserved.

Record F03-K/M/U/X-v4 only for actual use, with problem numbers, keys, starting messages, children's records, adult rescue, and requests to continue. Distinguish observed behavior from proposed explanations, and tried/conjectured/checked/proved/supplied claims. Future returns can change the alphabet, composition question, or extremal size rather than repeat the same examples. This revision has not been classroom-tested.
