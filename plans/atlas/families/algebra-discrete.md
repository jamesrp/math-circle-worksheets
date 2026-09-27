# Algebra Discrete - investigation families

Facilitator planning cards. These are proposed investigations, not classroom-piloted student packets. The JSON alongside this file is the editable source; this Markdown is generated.

<a id="ad-01"></a>
## AD-01 - Build a world that defeats a rule

Primary field: 03. Related: 06. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How do models distinguish a valid inference from a statement that happens to hold in a few examples?

**Anchor.** For predicates R and S on a specified finite universe, 'every R is S' means no object satisfies R and not S. Its converse is a different sentence. A countermodel satisfies every premise while falsifying the conclusion.

**Bridge (exact-special-case).** A tray is a finite domain; color and shape are unary predicates. Building or altering a tray is constructing a model, and checking each object is evaluating the quantified sentence. Limits: These finite unary examples do not establish completeness, compactness, or a decision procedure for general first-order logic.

**Prerequisite gates.**

- **Entry:** O: distinguish two colors and two shapes, or equivalent tactile labels; spoken rules suffice.
- **Explore:** C: compare several objects while holding one rule fixed.
- **Explain:** P: identify the exact premise and conclusion and point to a witness.
- **Prove:** P: reason over the four possible combinations of two predicates, including an empty predicate class.
- **Reading:** None with adult reading; rule cards can use pictures.
- **Arithmetic:** Only small counts, if any.
- **Reasoning:** Language and quantifier scope are the real demands; avoid adding memory pressure through hidden objects.
- **Hard Stop:** Stop at explicit finite models before discussing arbitrary structures or metatheorems.

**Materials and preparation (10 minutes).** A tray and twelve red/blue circle/square cards, with spare duplicates. Draw a persistent four-cell property table. Prepare three rule cards, not a long worksheet.

**Launch.** Put any cards in your world. Every red object must be round. Can you make that rule true while 'every round object is red' is false? Keep both rules visible. Empty trays are allowed later, but begin with at least one object.

**Learner choices.** Choose the world's inhabitants, remove unnecessary objects, and invent a new proposed inference for another group to challenge.

**Hour menu.** 0-10 freely sort and invent descriptions; 10-15 test one sample world together; 15-35 build smallest counterworlds; 35-40 move to room corners representing four property types; 40-55 compare converses and empty classes; 55-60 display one world with an explanation. The first countermodel is a complete stopping point.

**Explore.**

- Which single object would break the first rule?
- Can your world contain a blue circle?
- Does adding a red square change truth or merely make the world larger?
- What happens if there are no red objects?

**Hint ladder.**

1. Mark forbidden card types rather than guessing entire worlds.
2. To defeat 'every round object is red', look for a round object that is not red.

**Checked instance.** Make every red object round, but make not every round object red. Then test whether every round object being blue follows.

**Reasoning.** A world containing one blue circle satisfies the first sentence because it has no red counterexample, and falsifies the converse. If a red object is required, use one red circle plus one blue circle. This second world also falsifies 'every round object is blue'. A red square is forbidden by the premise; blue squares are irrelevant to either implication.

**Boundary.** An empty tray satisfies both universal sentences, so it cannot defeat the converse. This is not the same as saying a red object exists. Explicitly separate universal and existence claims.

**Extensions.**

- Introduce an arrow relation 'visits'. Compare 'everyone visits someone' with 'someone is visited by everyone'; two vertices with only self-arrows separate them.
- Ask which two-predicate inferences are valid by considering all four object types; general finite-model theory is a later continuation, not established here.

**Satisfying stop.** A learner builds a smallest counterworld and explains which object defeats the conclusion while the premise survives.

**Prior use.** Year-1 truth/logic material is related; exact prior instances require the use log. Week 5 tests consistency and uniqueness, whereas this activity makes learners construct countermodels to proposed implications.

**Sources.**

- [Open Logic Project, Sets, Logic, Computation](https://slc.openlogicproject.org/slc-screen.pdf), Chapter 7 semantics and satisfaction; chapter 12 completeness/compactness inspected in survey. Inspection: excerpt only; the finite countermodels below are established directly.

<a id="ad-02"></a>
## AD-02 - The list that cannot catch your pattern

Primary field: 03. Related: 05. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can diagonalization construct an object different from every member of a proposed list, and what changes when the list is infinite?

**Anchor.** For any n by n binary array, choose the ith bit of a new length-n word opposite the entry in row i, column i. The new word differs from each listed row. For an infinite sequence of infinite binary sequences, the same coordinate rule constructs a sequence absent from the enumeration.

**Bridge (exact-special-case).** Rows are binary words; changing diagonal entries gives the exact finite construction used by the infinite argument. Limits: The finite game proves a finite avoidance result. Uncountability requires explaining an arbitrary infinite list and a rule defined at every positive integer, not drawing many rows.

**Prerequisite gates.**

- **Entry:** O: match two colors and locate a marked square in each row.
- **Explore:** C: track row and column indices with fingers or paired labels.
- **Explain:** P: assign a guaranteed disagreement to each opponent row.
- **Prove:** P and X: for the infinite extension, understand functions on positive integers and universal quantification over possible enumerations.
- **Reading:** None for colored cards; a short symbolic rule for the infinite stage.
- **Arithmetic:** Counting to four or five; no calculation.
- **Reasoning:** Coordinating two indices is harder than the arithmetic. Use one row at a time and retain comparison markers.
- **Hard Stop:** A participant may finish with the finite guarantee. Do not infer understanding of infinity from success at four rows.

**Materials and preparation (5 minutes).** Two-color counters, a four-by-four grid, and a four-place answer strip. Label matching rows/columns with four pictures if numeral reading is a barrier.

**Launch.** Your partner lists four patterns, each four counters long. Build a pattern missing from their list. Then make a method that works against any list they choose. You may inspect the whole list; rearranging their patterns is not required.

**Learner choices.** The list maker chooses patterns, including duplicates. The challenger chooses an initial strategy and later decides which coordinate will guarantee disagreement with each row.

**Hour menu.** 0-10 make and compare patterns; 10-15 play one challenge without prescribing a method; 15-35 trade adversarial lists and look for a guarantee; 35-40 stand in four numbered places and change one gesture each; 40-55 explain certificates or discuss a precisely defined infinite list; 55-60 show one disagreement per row. Infinity is optional.

**Explore.**

- How can you certify four differences without comparing every square?
- Must your answer be the only missing pattern?
- Can five rows of four bits always be defeated by the same diagonal recipe?
- What statement would a truly complete infinite list make?

**Hint ladder.**

1. Reserve a different answer position for each opponent row.
2. At the reserved position, deliberately choose the other color.

**Checked instance.** Defeat rows 0000, 0110, 1011, 1101 with a guaranteed rule.

**Reasoning.** The diagonal is 0,1,1,1, so choose 1000. It differs from row 1 in position 1, row 2 in position 2, row 3 in position 3, and row 4 in position 4. These four witness positions prove absence from the list, regardless of other matches. Other missing words may also work.

**Boundary.** All sixteen four-bit words can be listed, leaving no missing word. Therefore the claim is not 'every finite list misses a finite word'; the relation between number of rows and available coordinates matters.

**Extensions.**

- Use three symbols: any fixed rule choosing a different symbol works, so binary is convenient rather than essential.
- For infinite binary sequences, define b(i)=1-a_i(i). Explain why no row index can equal the resulting sequence; avoid decimal expansions and their nonunique representations.

**Satisfying stop.** A four-counter pattern with four visible mismatch certificates and an explanation that the procedure survives any changed list.

**Prior use.** Week 6 concerns identifying hidden finite codes, not diagonal construction or uncountability. This is a distinct question even though it reuses binary counters.

**Sources.**

- [Open Logic Project, Sets, Logic, Computation](https://slc.openlogicproject.org/slc-screen.pdf), Chapter 4, printed pp. 58-60, binary-sequence diagonalization and Theorem 4.18. Inspection: full relevant text.

<a id="ad-03"></a>
## AD-03 - The largest collection with no nested sets

Primary field: 05. Related: 06. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How large can a family of subsets be when no member contains another, and how can a chain decomposition certify optimality?

**Anchor.** An antichain in the Boolean lattice of subsets of an n-element set has size at most choose(n,floor(n/2)). The exact four-element problem admits a six-chain partition certificate, with six two-element subsets attaining the bound.

**Bridge (faithful-representation).** A card displays a subset of four named objects; legal collections are precisely antichains under inclusion. Partitioning cards into nested chains proves an upper bound. Limits: The supplied four-object certificate proves only that case. It does not establish a chain decomposition or Sperner's theorem for every n.

**Prerequisite gates.**

- **Entry:** O: recognize which pictured objects belong to each card; no arithmetic beyond small counts.
- **Explore:** C: distinguish containment from overlap and organize all sixteen subsets.
- **Explain:** P: argue that a legal collection can take at most one card from each nested chain.
- **Prove:** P: construct or justify the six-chain partition; general n needs a separate inductive chain construction or counting proof.
- **Reading:** None with picture sets; names may be replaced by four symbols.
- **Arithmetic:** Count up to sixteen and compare collection sizes.
- **Reasoning:** Track a universal pairwise condition; overlapping cards are legal unless one contains the other.
- **Hard Stop:** Stop at the exact four-object optimum if the general combinatorial proof is not accessible.

**Materials and preparation (15 minutes).** Sixteen cards, one for every subset of four pictures; counters to mark selected cards. Prepare six blank chain strips and optionally the certificate on a facilitator sheet.

**Launch.** Choose as many cards as possible. You may not choose two when every picture on one is also on the other. Sharing some pictures is allowed. Build a large legal collection, then convince another team that a larger one cannot exist.

**Learner choices.** Choose a collection, exchange small sets for large ones, choose how to organize the complete deck, and invent a certificate rather than chase the adult's target arrangement.

**Hour menu.** 0-10 sort and compare set cards; 10-15 demonstrate containment and a legal overlapping pair; 15-35 compete cooperatively for large collections; 35-40 form nested groups of participants; 40-55 build chain certificates; 55-60 show a matching construction and bound. Finding six is a worthwhile early stop.

**Explore.**

- Do all chosen cards need the same number of pictures?
- Why is the empty card difficult to combine with others?
- Can one long chain help limit your selection?
- How many chains would prove six is best?

**Hint ladder.**

1. Arrange cards by number of pictures, then inspect all two-picture cards.
2. Group the entire deck into nested chains. One selected card per chain is the most possible.

**Checked instance.** Determine the maximum for subsets of {1,2,3,4}.

**Reasoning.** All six pairs form a legal collection. Partition the deck into chains: empty<1<12<123<1234; 2<23<234; 3<13<134; 4<14<124; 24; 34. Each of the sixteen subsets appears once and every chain is nested. A legal collection uses at most one member of each of six chains, proving the maximum is six.

**Boundary.** For three objects the three singleton cards and the three pair cards each give a maximum, but choosing both full layers is illegal: for example {1} is contained in {1,2}. Equal layer sizes do not permit merging layers.

**Extensions.**

- Find the exact answer for five objects; the middle layer has ten sets, and a ten-chain certificate is a concrete next proof challenge.
- Investigate antichains in a divisibility poset. The largest same-size layer need not solve arbitrary partially ordered sets; the Boolean-lattice hypothesis matters.

**Satisfying stop.** A six-card construction together with a complete six-chain certificate that explains optimality.

**Prior use.** No matching current Week 1-10 mechanism. Week 5 also distinguishes a good construction from a proof of optimality, but its clue constraints and reasoning are different.

**Sources.**

- [Richard P. Stanley, Topics in Algebraic Combinatorics, 2013 author draft](https://math.mit.edu/~rstan/algcomb/algcomb.pdf), Chapter 4, Sperner property and Corollary 4.8; chain discussion. Inspection: full relevant theorem discussion; the particular six-chain certificate is original and checked below.

<a id="ad-04"></a>
## AD-04 - Send a whole tree in two numbers

Primary field: 05. Related: 68. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why do labeled trees on n vertices correspond exactly to words of length n-2 on those labels?

**Anchor.** Prüfer encoding repeatedly removes the smallest labeled leaf and records its neighbor until two vertices remain. For labels 1 through n, n≥2, this gives a bijection with length-(n-2) words, proving Cayley's count n^(n-2).

**Bridge (exact-special-case).** Labeled dots and string edges are actual trees; deleting leaves and reconstructing them are the encoding and inverse algorithm. Limits: The count is for labeled simple trees. Rotating a drawing does not produce a new tree, but changing which named vertices connect can.

**Prerequisite gates.**

- **Entry:** O and C: connect four labeled vertices, recognize a leaf as a vertex with one incident edge.
- **Explore:** C: follow the smallest-label tie-breaking rule and keep track of deleted vertices.
- **Explain:** P: explain why decoding is unique rather than merely successful in a few trials.
- **Prove:** P: induct on successive leaf deletions, using the relation between remaining code occurrences and degrees.
- **Reading:** Short algorithm cards; partner can read and record.
- **Arithmetic:** Order four small integers; count occurrences; powers only in the later counting interpretation.
- **Reasoning:** Dynamic state tracking is substantial; physically remove edges and retain a vertex ledger.
- **Hard Stop:** Complete the four-vertex correspondence before general coding proofs; avoid treating a large unverified catalog as proof.

**Materials and preparation (8 minutes).** Four numbered cards and reusable strings, with a two-place message slip. A second color can mark removed vertices; prepare a visible algorithm card.

**Launch.** Build a connected network on 1,2,3,4 with no loops around a cycle. Remove the smallest leaf and write its neighbor. Repeat once. Can your partner reconstruct exactly your edges using only the two-number message? Labels stay attached to their vertices.

**Learner choices.** Invent the tree, choose challenging messages, look for ambiguity, and decide how to prove the decoder cannot choose differently.

**Hour menu.** 0-10 build connected networks and remove redundant edges; 10-15 demonstrate one deletion; 15-35 exchange messages and debug decoding; 35-40 enact leaves leaving a human network; 40-55 organize all sixteen messages and argue uniqueness; 55-60 explain why two numbers suffice. General n is optional.

**Explore.**

- Which label cannot yet be removed if it still appears in the message?
- What does a repeated number tell you about the tree?
- Why must the same smallest-leaf rule be used every time?
- Can any two-number message fail?

**Hint ladder.**

1. At decoding, choose the smallest surviving label absent from the remaining message.
2. Join that label to the first message entry, remove the label and entry, then connect the last two survivors.

**Checked instance.** Decode message (2,4), then check by encoding. Count all trees on four labeled vertices.

**Reasoning.** Initially labels 1 and 3 are absent, so remove the smaller 1 and add edge 1-2. With message (4), surviving label 2 is smallest absent; add 2-4 and remove 2. Join survivors 3 and 4. The edges are {12,24,34}; encoding removes leaf 1 then leaf 2, recovering (2,4). Every two-entry word from four labels decodes by the same rule, and the inverse recovers it, giving 4×4=16 trees.

**Boundary.** If labels are ignored, there are only two shapes on four vertices: a path and a three-leaf star. The sixteen count must not be reported as sixteen unlabeled shapes.

**Extensions.**

- For five labels, choose a three-entry code first and predict which vertices will be leaves; degree equals one plus its number of code occurrences.
- Compare Prüfer's bijection with determinant-based spanning-tree counting in AD-05; the latter handles restricted edge sets but is less direct as a communication code.

**Satisfying stop.** Two partners exchange one tree with a message and explain why the reconstruction is forced.

**Prior use.** Week 10 uses routes in networks, not labeled-tree encoding. Network materials can be reused without treating the old route puzzle as this new investigation.

**Sources.**

- [Richard P. Stanley, Topics in Algebraic Combinatorics](https://math.mit.edu/~rstan/algcomb/algcomb.pdf), Chapter 9 appendix, three combinatorial proofs; Prüfer proof and Cayley count. Inspection: relevant text inspected; exact n=4 encoding and decoding proved below.

<a id="ad-05"></a>
## AD-05 - How many minimal networks survive?

Primary field: 05. Related: 15, 90. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can a determinant count spanning trees of a graph, and what combinatorial structure explains the answer?

**Anchor.** For a finite connected loopless graph, any principal cofactor of its Laplacian D-A equals its number of spanning trees. The core is a four-cycle with one diagonal; direct classification proves eight trees without requiring determinants.

**Bridge (exact-special-case).** Choosing edge subsets that connect every vertex without a cycle is exactly choosing spanning trees. The later Laplacian calculation describes this same graph. Limits: The direct eight-case count does not prove the general determinant formula. No claim is made that all networks or optimization problems reduce to this small example.

**Prerequisite gates.**

- **Entry:** O: join four places with removable strips and trace connections.
- **Explore:** C: distinguish connectedness, a cycle, and minimal connectedness; compare edge sets rather than drawing positions.
- **Explain:** P: split all possibilities by whether the diagonal is selected.
- **Prove:** L and P for the general Matrix-Tree Theorem: incidence matrices, determinants, and a determinant expansion such as Cauchy-Binet.
- **Reading:** None for the graph; symbolic matrix reading for the optional upper stage.
- **Arithmetic:** Count to eight; determinant stage uses signed products and sums.
- **Reasoning:** Completeness and duplicate control matter more than arithmetic. Give each edge a distinct label.
- **Hard Stop:** A correct combinatorial count is complete mathematics; stop there when determinant prerequisites are absent.

**Materials and preparation (10 minutes).** A square with vertices A,B,C,D in cyclic order, diagonal AC, and five removable edge strips. Eight small recording frames or photographs can replace repeated drawing.

**Launch.** Keep every place connected while using no unnecessary link: removing any chosen link must disconnect the network. Find every different network you can make using only these five available links. Two drawings count the same when they use the same links.

**Learner choices.** Choose which links survive, decide a recording scheme, invent an organizing question, and test another team's completeness argument.

**Hour menu.** 0-10 build and break networks; 10-15 agree on necessary links and duplicates; 15-35 enumerate minimal connected networks; 35-40 form a human cycle then remove one link; 40-55 prove the count or compute a cofactor; 55-60 compare the two descriptions. A classified eight-tree list is enough.

**Explore.**

- How many links must a minimal connected four-place network have?
- What changes when the diagonal is included?
- Can a three-link selection contain a cycle?
- Why should deleting a different matrix row and column give the same answer?

**Hint ladder.**

1. First handle networks without AC: delete exactly one edge of the square.
2. With AC present, choose one connection for B and one for D; explain why those choices suffice.

**Checked instance.** Count spanning trees of edges AB,BC,CD,DA,AC and verify one Laplacian cofactor.

**Reasoning.** Without AC, deleting one of the four cycle edges gives four trees. With AC, choose AB or BC for B and CD or DA for D, giving four more. Other diagonal-containing three-edge choices leave B or D isolated. Deleting D's row/column from the Laplacian gives [[3,-1,-1],[-1,2,-1],[-1,-1,3]], whose determinant is 15-4-3=8.

**Boundary.** A disconnected graph has no spanning tree on all its vertices. If a second diagonal is added, its crossing is not a vertex unless declared; declaring a junction changes the graph and the count.

**Extensions.**

- Add the second diagonal BD, treating its crossing as not a vertex. The graph becomes K4, which has sixteen spanning trees by AD-04.
- Assign positive edge weights: products of tree-edge weights sum to a weighted Laplacian cofactor. This continuation requires a separately checked weighted statement before use.

**Satisfying stop.** Eight drawings organized into two four-case groups, with a reason no other edge set works.

**Prior use.** Week 10 minimizes repeated travel, whereas this family counts minimal connecting subgraphs. AD-04 shares trees but studies an encoding of all labeled trees rather than restricted-edge counts.

**Sources.**

- [Richard P. Stanley, Topics in Algebraic Combinatorics](https://math.mit.edu/~rstan/algcomb/algcomb.pdf), Theorem 9.8 Matrix-Tree Theorem; chapter 9 incidence matrices. Inspection: full relevant theorem and proof discussion.

<a id="ad-06"></a>
## AD-06 - When the usual mixing rule breaks

Primary field: 06. Related: 08. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Which order structures admit greatest common lower bounds and least common upper bounds, and why can distributivity fail?

**Anchor.** A lattice is a partial order in which every pair has a meet and join. The five-element diamond M3 has bottom 0, top 1, and three pairwise incomparable middle elements a,b,c. It is a lattice but is not distributive.

**Bridge (faithful-representation).** Tiles are elements; upward arrows encode order, including transitive comparisons. Finding the lowest common ceiling and highest common floor is computing join and meet. Limits: The order diagram is not a road map: traversing downward then upward does not establish comparison. One counterexample distinguishes lattice from distributive lattice, not all varieties of lattices.

**Prerequisite gates.**

- **Entry:** O: follow upward comparisons and point to common places above two tiles.
- **Explore:** C: coordinate two partial-order searches and keep incomparability visible.
- **Explain:** P: evaluate two parenthesized expressions one operation at a time.
- **Prove:** P: check all pair types in M3 have a meet and join, then present one distributivity failure.
- **Reading:** Spoken operation names suffice; symbolic expression strips are optional.
- **Arithmetic:** None; 0 and 1 are names for bounds, not ordinary arithmetic values.
- **Reasoning:** Abstract comparison and nested operations are substantial. Use movable intermediate-result markers.
- **Hard Stop:** Do not introduce general representation or duality theorems without set-theoretic proof prerequisites.

**Materials and preparation (10 minutes).** Five labeled tiles, six arrows for 0<a,b,c<1, and a separate deck of the eight subsets of three pictures. Use 'floor' and 'ceiling' markers.

**Launch.** For two tiles, find the lowest tile at or above both (their join) and the highest tile at or below both (their meet). A tile counts as at or above/below itself. Start with picture-set cards ordered by containment, then try the five-tile diagram. For three chosen tiles a,b,c, compare a meet (b join c) with (a meet b) join (a meet c). Do these two recipes always agree?

**Learner choices.** Choose pairs, invent an order diagram, challenge whether a proposed common bound is the least or greatest one, and search for a shortcut failure.

**Hour menu.** 0-10 arrange picture sets by containment; 10-15 name common floor and ceiling; 15-35 investigate the diamond and compare operations; 35-40 participants stand at diagram vertices; 40-55 evaluate two competing expression routes; 55-60 show a counterexample. Do not require every participant to manipulate notation.

**Explore.**

- Are a and b comparable even though both sit above 0?
- Can there be several common upper bounds but only one least one?
- What is the ceiling of b and c?
- Do both expression routes finish at the same tile?

**Hint ladder.**

1. List all common upper bounds before choosing the least; do the dual search below.
2. For three distinct middle tiles, compute b join c first on one route, and a meet b plus a meet c first on the other.

**Checked instance.** Compare a meet (b join c) with (a meet b) join (a meet c) in M3.

**Reasoning.** Distinct middle elements have only 1 as a common upper bound and only 0 as a common lower bound. Thus b join c=1, so the first result is a meet 1=a. Each of a meet b and a meet c is 0, so the second result is 0. Since a differs from 0, distributivity fails. Equal middle elements and pairs involving 0 or 1 also have obvious unique bounds, verifying this is still a lattice.

**Boundary.** A poset with two incomparable upper bounds and no least common upper bound for some pair is not a lattice. 'There is something above both' is insufficient.

**Extensions.**

- For divisors of 12 ordered by divisibility, compute meet as gcd and join as lcm; compare the diagram with subsets.
- Investigate the lattice of subspaces of a two-dimensional vector space: distinct lines supply the same distributivity failure. This exact connection requires a real linear-algebra gate.

**Satisfying stop.** Two legal calculation routes end at different tiles, with each intermediate result justified from the diagram.

**Prior use.** No exact current-week match. Tiling flip orders may eventually produce lattices, but that additional structure must be proved separately rather than assumed from Week 1.

**Sources.**

- [Burris and Sankappanavar, A Course in Universal Algebra](https://math.hawaii.edu/~ralph/Classes/619/univ-algebra.pdf), Chapter I, §§1 and 3, lattice definitions and distributive/modular lattices. Inspection: relevant definitions and examples inspected; the M3 calculation is explicit below.

<a id="ad-07"></a>
## AD-07 - Everything your starting clues force

Primary field: 06. Related: 03, 08. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why do closure operations generate lattices of closed sets, and why does joining two closed sets sometimes create new consequences?

**Anchor.** On a finite set, repeatedly apply implications X implies y by adding y whenever every member of X is present. The least fixed point containing the starting set is extensive, monotone, and idempotent. Intersections of closed sets are closed; their join is the closure of their union.

**Bridge (exact-special-case).** Chosen token sets and forced additions are an actual finite closure operator. Order of processing eligible rules does not change the eventual closed set if all eligible rules are eventually applied. Limits: These are monotone addition-only implications, not arbitrary instructions with deletion or negation. The result does not promise order independence for every rule game.

**Prerequisite gates.**

- **Entry:** O: place named tokens and follow one visible if-then rule.
- **Explore:** C: track several rules without losing previously obtained tokens.
- **Explain:** P: distinguish a set already closed from a set still requiring additions.
- **Prove:** P: prove termination by finite growth and minimality by induction on additions.
- **Reading:** Three short rule cards, orally supported and drawn with arrows.
- **Arithmetic:** Count at most four tokens; no calculation.
- **Reasoning:** Conditional language and tracking prerequisites matter; put every rule and obtained token in view.
- **Hard Stop:** Keep rules positive and finite until the fixed-point argument is secure; arbitrary logical consequence is a separate advanced subject.

**Materials and preparation (8 minutes).** Tokens a,b,c,d and rule cards: a gives b; b together with c gives d; d gives c. Prepare a recording strip for each starting set and a closed/not-yet-closed marker.

**Launch.** Choose any starting tokens. You may add a token whenever a displayed rule allows it, and you never remove tokens. Keep going until no new token can be added. Can two different legal orders end with different collections? Which starting collections already need no changes?

**Learner choices.** Choose starting sets, choose which eligible rule fires first, challenge a claimed stopping point, and invent two closed collections whose union triggers something new.

**Hour menu.** 0-10 explore tokens and make informal recipes; 10-15 demonstrate one implication and one two-token prerequisite; 15-35 compare orders and catalog closed sets; 35-40 pass prerequisite cards around a circle; 40-55 investigate intersections and unions; 55-60 present one surprising forced addition. The full catalog is optional.

**Explore.**

- What does starting with only a force?
- Can a rule be used before all its inputs are available?
- Can an extra starting token ever make you lose an eventual token?
- Why can two individually finished collections have an unfinished union?

**Hint ladder.**

1. Underline prerequisites already present and mark each newly obtained token.
2. For a union surprise, try one closed set containing b and another containing c.

**Checked instance.** Find closures of {a}, {c}, and {a,c}; decide whether closed sets stay closed under union.

**Reasoning.** Starting at {a}, the first rule adds b and nothing else fires, so closure is {a,b}. Starting at {c} adds nothing. Their union {a,b,c} activates b-and-c, adding d, so its closure is {a,b,c,d}. Thus union need not be closed. Any closed set containing the starting set must contain each forced addition, by induction; hence every completed run produces the same least such set.

**Boundary.** If a rule deletes a prerequisite, order can matter: from {a}, 'replace a by b' and 'replace a by c' give different terminal sets. The addition-only hypothesis is essential.

**Extensions.**

- Enumerate all closed sets: empty, {b}, {c}, {c,d}, {a,b}, {b,c,d}, {a,b,c,d}. Verify intersections remain on the list.
- Connect to subalgebra generation or linear span only after defining their operations; they are further exact closure systems, not identical problem stories.

**Satisfying stop.** Two finished collections combine to force a new token, and the learner can explain why order does not change the final closure.

**Prior use.** Week 5 concerns clue uniqueness; this family studies closure under explicit implication rules. No exact reuse is claimed; actual prior encounter remains governed by the use log.

**Sources.**

- [Burris and Sankappanavar, A Course in Universal Algebra](https://math.hawaii.edu/~ralph/Classes/619/univ-algebra.pdf), Chapter I §5, closure operators and closed sets. Inspection: relevant definition inspected; finite rule-system claims proved by the explicit procedure.

<a id="ad-08"></a>
## AD-08 - Which numbers may share a name?

Primary field: 08. Related: 11, 20. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** When does identifying elements preserve an operation, so that a quotient algebra is well-defined?

**Anchor.** For addition modulo four, an equivalence relation is a congruence when equivalent inputs always have equivalent sums. Its congruences are equality, parity, and the indiscrete relation. The specific parity quotient has two classes with addition modulo two.

**Bridge (faithful-representation).** Colored bags are equivalence classes. Asking whether a bag-level sum depends on chosen representatives is exactly the congruence condition. Limits: The experiment concerns a specified operation. A partition valid for addition may fail for an additional operation; checking one algebraic structure does not check all signatures.

**Prerequisite gates.**

- **Entry:** O and C: use a supplied four-by-four addition table or move on a four-position ring.
- **Explore:** C: choose two representatives independently and compare result bags.
- **Explain:** P: exhibit a representative-dependent result as a counterexample, or check parity for all cases.
- **Prove:** P and M: propagate one identified pair by adding the same residue to both; use cyclic translation.
- **Reading:** Bag labels and a small table; oral instructions suffice.
- **Arithmetic:** Addition modulo four, supplied concretely; odd/even reasoning for explanation.
- **Reasoning:** Distinguish the object's name from the whole class and test all legal choices, not just one convenient representative.
- **Hard Stop:** Universal-algebra theorems about all algebras remain beyond this finite quotient investigation.

**Materials and preparation (8 minutes).** Cards 0,1,2,3, transparent colored bags or drawn class circles, and an addition table modulo four. Duplicate cards let pairs of inputs be shown simultaneously.

**Launch.** Rename some numbers so they share a bag. To add two bags, choose any number from each bag, add around the four-ring, and report the answer's bag. Your renaming is legal only if the answer bag never depends on the representatives chosen. Invent a legal renaming and an illegal one.

**Learner choices.** Choose partitions, choose adversarial representative pairs, and decide what extra identifications repair a failing renaming.

**Hour menu.** 0-10 play with ring addition; 10-15 demonstrate bag-level ambiguity without giving the valid partition; 15-35 test and repair partitions; 35-40 participants become bags and choose representatives; 40-55 classify all possible legal renamings; 55-60 show either a quotient table or a decisive failure witness.

**Explore.**

- What happens if only 0 and 1 share a bag?
- Does putting 0 with 2 force 1 to share with 3?
- Could every number share one name?
- Which information survives the parity renaming?

**Hint ladder.**

1. Hold one input fixed while changing the other representative.
2. If two numbers share a bag, adding 1 to both must give two numbers that also share a bag.

**Checked instance.** Test bags {0,2} and {1,3}; compare with bags {0,1},{2},{3}.

**Reasoning.** Even+even and odd+odd land in the even bag; even+odd lands in the odd bag, independently of representatives. The second partition fails: choosing 0+0 gives the first bag, while 1+1 gives {2}, even though both input bags were the same. For classification, any identified adjacent residues force all four together by translation. Identifying opposite residues forces exactly the parity partition unless further identifications are added. If no distinct residues are identified, equality remains.

**Boundary.** The singleton partition and the one-bag partition are both valid, although the latter discards all distinctions. Validity does not mean the quotient retains useful information.

**Extensions.**

- Repeat for addition modulo six and investigate partitions corresponding to remainders modulo two or three; require new witnesses and a proof before generalizing.
- Add the operation that maps 0 to 0, 1 to 0, 2 to 1, 3 to 1. The parity partition now fails because 0 and 2 have differently classified outputs.

**Satisfying stop.** A two-bag addition rule with a reason every representative choice agrees, plus a concrete failing partition.

**Prior use.** Week 4 uses cyclic arithmetic; the new central question is well-defined identification and information loss. The same ring alone is a representation reuse, not a new mechanism.

**Sources.**

- [Burris and Sankappanavar, A Course in Universal Algebra](https://math.hawaii.edu/~ralph/Classes/619/univ-algebra.pdf), Chapter II §5, congruences and quotient algebras. Inspection: relevant definition inspected; classification for the four-element example proved here.

<a id="ad-09"></a>
## AD-09 - Two clocks, one hidden position

Primary field: 11. Related: 08, 20. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** When can independent remainder reports be combined into one residue, and how does a common divisor obstruct compatibility?

**Anchor.** For positive coprime moduli m,n, every residue pair has a unique solution modulo mn. For general positive moduli, a pair is solvable exactly when the residues agree modulo gcd(m,n), and any solution is unique modulo lcm(m,n). The core proves the 3-and-4 case by a complete cycle.

**Bridge (exact-special-case).** Two counters recording one step at a time are the map from integer time to a pair of residues. Returning to both origins means a common multiple. Limits: A twelve-state picture proves its own case, not the theorem for arbitrary moduli. Independent clocks cannot produce every pair when their sizes share a factor.

**Prerequisite gates.**

- **Entry:** O and C: move two counters once for each shared step and recognize paired positions.
- **Explore:** C: record ordered pairs without swapping clock roles.
- **Explain:** M and P: reason about multiples, remainders, and the first joint return.
- **Prove:** M and P: use coprimality and a modular inverse or Bezout identity for the general theorem.
- **Reading:** Clock symbols suffice; an adult can read remainder clues.
- **Arithmetic:** Core uses counting to twelve; later stage needs multiplication, division, gcd and lcm.
- **Reasoning:** Track synchronized movement and distinguish uniqueness within one period from uniqueness among all integers.
- **Hard Stop:** Do not require a general Bezout proof for the complete small-cycle result; supply exact restrictions on the hidden time.

**Materials and preparation (10 minutes).** Clock faces labeled 0,1,2 and 0,1,2,3; two counters; a strip numbered 0 through 11. A second pair of four- and six-position clocks is optional.

**Launch.** A hidden time is one of 0 through 11. Both clocks start at 0 and move one position per step. The three-clock reports 2 and the four-clock reports 1. Find the time, then design a pair of reports that no one can solve—or explain why you cannot.

**Learner choices.** Choose clues, choose a search method, organize the full pair inventory, and choose changed clock sizes to challenge the conjecture.

**Hour menu.** 0-10 explore synchronized clocks; 10-15 solve one clue collaboratively; 15-35 invent reports and build a complete table; 35-40 walk two floor rings in synchrony; 40-55 try clocks with a shared factor and explain failures; 55-60 state exactly what can and cannot be guaranteed.

**Explore.**

- When do both counters first return to 0?
- Can a paired report repeat before then?
- Does the answer remain unique if time is unrestricted?
- What must a four-clock and six-clock agree about?

**Hint ladder.**

1. List the times matching just one report, then inspect the other clock.
2. For four and six positions, track whether both reported residues are odd or even.

**Checked instance.** Solve t=2 mod 3 and t=1 mod 4 for 0≤t<12; then test residues 1 mod 4 and 2 mod 6.

**Reasoning.** The times matching the first clue are 2,5,8,11; only 5 is 1 mod 4. Two times sharing both residues differ by a multiple of both 3 and 4, hence by 12, so the chosen interval gives uniqueness. For the changed clocks, t=1 mod 4 makes t odd, whereas t=2 mod 6 makes t even; no solution exists.

**Boundary.** Without a bounded interval or residue-class interpretation, 5,17,29 and infinitely many other times satisfy the first pair. State uniqueness modulo 12, not a unique integer.

**Extensions.**

- For moduli four and six, classify all twenty-four residue pairs: exactly twelve compatible same-parity pairs occur, with period twelve.
- For three pairwise coprime clocks, combine two first and then the third; prove the construction's uniqueness rather than assuming pairwise agreement is enough in unrelated constraint problems.

**Satisfying stop.** A hidden time with a uniqueness argument and one impossible pair explained by parity.

**Prior use.** Week 4 follows one modular orbit and Week 9 uses common multiples. This family combines simultaneous reports and exposes compatibility; prior ring movement can reduce setup time.

**Sources.**

- [Keith Conrad, The Chinese Remainder Theorem](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/crt.pdf), Theorem 1.1 and §2 existence/uniqueness proof. Inspection: full relevant coprime text; general compatibility is a separately explained continuation.

<a id="ad-10"></a>
## AD-10 - Square dots that also make a triangle

Primary field: 11. Related: 12. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can a geometric counting question become a Pell equation, and how does multiplication of quadratic expressions generate infinitely many solutions?

**Anchor.** For nonnegative integers m,n, m(m+1)/2=n^2 is equivalent to (2m+1)^2-2(2n)^2=1. Multiplication of x+y√2 by 3+2√2 preserves x^2-2y^2=1 and sends (x,y) to (3x+4y,2x+3y).

**Bridge (exact-special-case).** The same counter total admits triangular and square arrangements. The algebraic re-encoding and recurrence preserve exactly the required equality. Limits: Producing successive larger examples does not by itself prove that every triangular-square number has been found, or that no omitted one lies between generated examples.

**Prerequisite gates.**

- **Entry:** O and C: build rows of lengths 1,2,3,... and square arrays.
- **Explore:** M: compare triangular totals with square totals, using a supplied table if desired.
- **Explain:** A: expand squares and translate between m,n and x,y; a finite dot explanation remains possible earlier.
- **Prove:** A and P: verify a polynomial identity and show the recurrence preserves positivity and strictly increases size. Completeness needs a separate descent argument.
- **Reading:** Spoken launch; optional symbolic recurrence card.
- **Arithmetic:** Core uses thirty-six counters; extension uses multiplication of two-digit integers and polynomial expansion.
- **Reasoning:** Coordinate two different side-length parameters; label triangle height m and square side n separately.
- **Hard Stop:** Stop after a verified common arrangement when symbolic equations remove the learner's agency; the Pell proof is an explicit upper gate.

**Materials and preparation (10 minutes).** Thirty-six counters per pair, square grid and triangular-row mat, plus a calculator or prepared arithmetic strip for large extensions. Do not prepare 1,225 physical counters.

**Launch.** Use the same counters to make both a square and a triangle with one more counter in each successive row. One counter works. Find a larger collection that works both ways. Later, decide whether a proposed recipe makes a new example every time.

**Learner choices.** Choose which totals to test, invent a search table, explain failed candidates, and decide whether the recurrence should be trusted from examples or from an identity.

**Hour menu.** 0-10 freely arrange dots; 10-15 define the exact triangle convention; 15-35 search and verify thirty-six; 35-40 physically form increasing rows; 40-55 choose a drawing-based explanation or symbolic recipe; 55-60 distinguish a verified new example from a claimed complete list. The symbolic phase is optional.

**Explore.**

- Why does a triangle of eight rows use thirty-six counters?
- Can a formula replace moving thousands of counters?
- Which quantities must remain whole numbers?
- Does a recipe that works forever necessarily find every solution?

**Hint ladder.**

1. Compare a list of triangular totals with 1,4,9,16,25,36.
2. If m(m+1)=2n^2, multiply by four and add one to make (2m+1)^2.

**Checked instance.** Verify m=8,n=6 and use the recurrence to generate another triangular-square total.

**Reasoning.** Eight rows use 8×9/2=36=6^2. Set x=17,y=12; x^2-2y^2=289-288=1. The recurrence gives x'=99,y'=70, hence m'=49,n'=35. Indeed 49×50/2=1225=35^2. Algebraically (3x+4y)^2-2(2x+3y)^2=x^2-2y^2, so the equation is preserved. Odd x and even y remain odd/even, allowing the conversion back.

**Boundary.** The identity x^2-2y^2=1 also has negative solutions; blindly converting them may give negative row lengths. Restrict to positive x,y for the displayed growth recipe, and do not claim the generated next value is the next smallest without a completeness proof.

**Extensions.**

- In m,n coordinates the recipe is m'=3m+4n+1 and n'=2m+3n+1. Start at m=n=1 and verify that it reaches 8,6 then 49,35.
- An advanced continuation proves all positive solutions arise from powers of 3+2√2. Inspect and prove the descent/completeness argument separately before reporting an exhaustive classification.

**Satisfying stop.** Thirty-six dots visibly form both arrangements, with a count explaining why the match is exact.

**Prior use.** Year-1 material includes figurate numbers; whether this exact triangular-square investigation was used is unknown. Current Weeks 1-10 do not contain this Pell mechanism.

**Sources.**

- [Keith Conrad, Pell's Equation, I](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/pelleqn1.pdf), §3 Theorem 3.1, triangular-square numbers; §4 quadratic-unit multiplication. Inspection: full relevant text.

<a id="ad-11"></a>
## AD-11 - Four symbols where every nonzero number divides

Primary field: 12. Related: 13, 94. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can a field have four elements when arithmetic modulo four has zero divisors?

**Anchor.** The polynomial t^2+t+1 has no root over the two-element field and is irreducible. Its quotient F2[t]/(t^2+t+1) is a field with elements 0,1,t,1+t. Arithmetic uses 1+1=0 and t^2=t+1.

**Bridge (faithful-representation).** Two-bit cards represent polynomial coefficient pairs. XOR addition and the stated multiplication reduction are exactly finite-field operations, not numerals interpreted modulo four. Limits: Table play alone does not prove the existence or uniqueness of every prime-power field. The reason this quotient is a field depends on irreducibility.

**Prerequisite gates.**

- **Entry:** O and C: manipulate two-position cards and cancel matching pairs; read a supplied multiplication table.
- **Explore:** M or A: apply distributivity and reduce repeated terms with 1+1=0.
- **Explain:** P: identify an inverse for each of the three nonzero elements.
- **Prove:** A and P: justify arithmetic as a polynomial quotient, or verify all finite field axioms from tables without omitting associativity.
- **Reading:** Four symbol labels and short rules; adult can mediate table use.
- **Arithmetic:** Addition of bits; later polynomial multiplication and cancellation, with no fractions required.
- **Reasoning:** An unfamiliar operation is not ordinary integer arithmetic. Keep the two models, F4 and mod four, visually separate.
- **Hard Stop:** Do not call the system a field solely because a few products work; either supply quotient justification or explicitly keep the investigation at the inverse-table result.

**Materials and preparation (15 minutes).** Cards 00,10,01,11 labeled 0,1,t,u where u=1+t; two-color coefficient counters; multiplication workspace. Prepare a separate modulo-four table for comparison.

**Launch.** In this arithmetic, two copies of the same coefficient cancel, and t times t becomes 1+t. Find a partner for each nonzero symbol so their product is 1. Can ordinary arithmetic modulo four do the same? You may derive products with counters or consult a checked table.

**Learner choices.** Choose a product to derive, choose how to record inverses, test a proposed relabeling to modulo-four arithmetic, and challenge whether multiplication can lose information.

**Hour menu.** 0-10 explore two-bit addition; 10-15 demonstrate distributivity and the t-square rule; 15-35 complete nonzero products and inverse pairs; 35-40 walk the multiplication-by-t cycle; 40-55 compare with modulo four and discuss irreducibility; 55-60 show the precise difference between the systems. Quotient proof is optional.

**Explore.**

- What is t(1+t)?
- Can multiplying by a nonzero symbol send two different inputs to the same output?
- How many times must you multiply by t to return to 1?
- Why cannot simply renaming 0,1,2,3 repair modulo-four multiplication?

**Hint ladder.**

1. Expand first, then replace t^2 with t+1 and cancel duplicate terms.
2. Once t times u equals 1, use it to test whether either multiplication can collapse distinct inputs.

**Checked instance.** Find all nonzero products and inverses in {1,t,u}, u=1+t.

**Reasoning.** The identity leaves every symbol fixed. t^2=u. Also tu=t+t^2=t+(t+1)=1. Finally u^2=(1+t)^2=1+t^2=t because the two cross terms cancel. Thus 1 is self-inverse and t,u are mutual inverses; multiplication by t cycles 1,t,u. In contrast, modulo four, 2×2=0, so 2 has no multiplicative inverse.

**Boundary.** Using the reducible modulus t^2 instead would make nonzero t square to zero. The same four coefficient pairs would then form a ring but not a field.

**Extensions.**

- Prove the Frobenius map z↦z^2 fixes 0,1 and exchanges t,u; applying it twice restores every element.
- Construct a field of eight elements only after choosing and checking an irreducible cubic. Having eight labels by itself specifies neither the operations nor a field.

**Satisfying stop.** A complete nonzero multiplication triangle and a clear reason every nonzero symbol can be undone, unlike modulo four.

**Prior use.** Week 2 binary addition and Week 4 modular rings are preparatory representations. This family introduces irreducible-polynomial field arithmetic, a distinct mechanism.

**Sources.**

- [Keith Conrad, Finite Fields](https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf), Theorem 1.1 and warning on p.1 about Z/(p^n). Inspection: full relevant text; the specific four-element arithmetic is checked directly.

<a id="ad-12"></a>
## AD-12 - A cube that ruler and compass cannot double

Primary field: 12. Related: 51. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can algebra certify an impossible geometric construction even when approximation is easy?

**Anchor.** Starting from a unit segment with unmarked straightedge and compass, constructible coordinates lie in a tower of extensions of degree at most two over Q. Therefore any constructible real algebraic number has degree a power of two over Q. The irreducible cubic x^3-2 excludes the exact doubled-cube edge.

**Bridge (exact-special-case).** The permitted lines and circles are the classical construction operations; coordinate equations faithfully track the algebraic extensions they create. Limits: A rough physical drawing is an approximation. The impossibility concerns exact finite constructions with the specified tools, not marked rulers, origami, or numerical methods.

**Prerequisite gates.**

- **Entry:** V: use compass and unmarked straightedge to construct a square diagonal; participation need not begin with fields.
- **Explore:** A: solve linear and quadratic equations and distinguish exact expressions from decimals.
- **Explain:** A and P: show the doubled-volume edge must satisfy x^3=2; prove the cubic has no rational root.
- **Prove:** X and P: field extensions, minimal-polynomial degree, and the tower law are essential for the impossibility proof.
- **Reading:** A symbolic proof sheet, read together if necessary.
- **Arithmetic:** Squares, cubes, rational arithmetic, polynomial degree; calculator only for comparison with approximations.
- **Reasoning:** Distinguish failure to find a construction from a theorem ruling all legal constructions out.
- **Hard Stop:** The complete obstruction stays at the field-extension gate. Younger participants may finish with exact square-root constructions, without being told they have proved cube-duplication impossibility.

**Materials and preparation (10 minutes).** Compasses, unmarked straightedges, unit segment, graph paper, and one page showing equations of lines/circles. A prepared field-tower diagram reduces copying.

**Launch.** A unit cube has volume one. Construct a segment that would be the edge of a cube with volume two, using only unmarked straightedge and compass. First construct √2 exactly and compare that problem. If your best drawing is close, decide what would certify exactness or prove impossibility.

**Learner choices.** Choose constructions to attempt, choose coordinate descriptions, compare permitted-tool variations, and locate the precise step at which a proposed impossibility argument needs a theorem.

**Hour menu.** 0-10 construct and compare lengths; 10-15 fix exact rules and the volume target; 15-35 derive line/circle equations and square-root steps; 35-40 reset with a physical cube-volume comparison; 40-55 follow the field-degree obstruction at the appropriate gate; 55-60 state the conclusion with its tool hypotheses. Exact √2 is an earlier stop.

**Explore.**

- Does doubling the edge double the volume?
- What new equation appears when a line meets a circle?
- Why can two circle equations be reduced by subtraction?
- Could a degree-three number fit inside a tower whose total degree is a power of two?

**Hint ladder.**

1. Draw a unit square: its diagonal solves a quadratic equation.
2. For the obstruction, track coordinates after each operation, not the visual sophistication of the whole drawing.

**Checked instance.** Compare exact construction of √2 with exact construction of the positive root of x^3=2.

**Reasoning.** The unit-square diagonal has length √2 by Pythagoras. A doubled cube needs edge α=∛2. A rational root of x^3-2 would be an integer dividing 2, and none of ±1,±2 is a root; a cubic without rational roots is irreducible over Q, so α has degree three. Each permitted intersection adds at most a quadratic extension. By the tower law, the degree of any constructible coordinate divides a power of two, contradicting degree three.

**Boundary.** The power-of-two degree condition is necessary, not sufficient for an arbitrary algebraic number to be constructible. Also, using a marked ruler changes the permitted operations, so this theorem no longer settles the task.

**Extensions.**

- Construct √3 from a right triangle with legs √2 and 1, then describe its quadratic tower.
- Investigate trisection of a 60-degree angle through its cubic cosine equation, preserving the distinction between some trisectable angles and a universal trisection method.

**Satisfying stop.** Either an exact square-root construction with justification, or the complete degree-three contradiction with its tool restrictions stated.

**Prior use.** Week 1 shape manipulation is unrelated to field-degree obstructions. This deliberately keeps an advanced proof gate rather than presenting an elementary approximation exercise as field theory.

**Sources.**

- [Thomas Judson, Abstract Algebra: Theory and Applications](https://judsonbooks.org/aata-files/aata-html/fields-section-constructions.html), §21.3, Lemma 21.3.6, Theorem 21.3.7, doubling-the-cube subsection. Inspection: full relevant text; correct power-of-two statement includes degree one, unlike the page's k>0 wording.

<a id="ad-13"></a>
## AD-13 - The monomials that survive the forbidden corners

Primary field: 13. Related: 05, 15. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How does a monomial ideal turn algebraic quotient structure into a staircase of lattice points, and what does that staircase measure?

**Anchor.** In k[x,y]/(x^2,xy,y^3), for a field k, the residue classes of 1,x,y,y^2 form a basis. A monomial belongs to the ideal exactly when it is divisible by at least one displayed generator. Multiplication by x or y moves one step on the exponent grid, possibly to zero.

**Bridge (faithful-representation).** Grid point (i,j) represents x^i y^j. Forbidden northeast regions are exactly the multiples of ideal generators; surviving points encode a quotient basis. Limits: Grid play describes a monomial ideal, not arbitrary polynomial ideals. For relations involving sums, erasing every involved monomial would destroy the quotient's actual information.

**Prerequisite gates.**

- **Entry:** O and V: move right/up on a grid and recognize a forbidden region.
- **Explore:** C: classify all surviving positions and investigate how the boundary changes.
- **Explain:** P: prove every point outside the displayed survivors is forbidden, including points beyond the drawn window.
- **Prove:** A and L: understand polynomial linear combinations and basis independence for the formal quotient interpretation.
- **Reading:** Picture directions suffice initially; polynomial labels optional until the upper stage.
- **Arithmetic:** Small nonnegative coordinates; exponent addition for algebraic extension.
- **Reasoning:** Reason about an unbounded grid from a finite boundary; distinguish geometric squares from algebraic coefficient values.
- **Hard Stop:** The low entrance establishes an exact monomial-membership puzzle; abstract quotient dimension requires linear combinations and polynomial independence.

**Materials and preparation (10 minutes).** A grid showing coordinates 0 through 5 in each direction, movable markers at (2,0),(1,1),(0,3), transparent northeast shading, and four survivor tokens. Axes begin at zero.

**Launch.** A marked forbidden point spoils itself and every point reachable by moving right or up from it. Mark the forbidden starts (2,0),(1,1),(0,3). Which places survive? Convince a partner that drawing a larger grid will not uncover more survivors. Later, name a right step x and an up step y.

**Learner choices.** Choose how to shade, how to certify the infinite region, how to multiply survivor positions, and which generator to move for a new family member.

**Hour menu.** 0-10 explore right/up paths; 10-15 set the three forbidden starts; 15-35 find survivors and test multiplication moves; 35-40 enact coordinate steps; 40-55 compare changed corners or translate to polynomial quotients; 55-60 give a finite certificate for the whole infinite grid.

**Explore.**

- Can a point above a forbidden point ever recover?
- Which survivor dies when multiplied by x?
- Is any forbidden start redundant?
- How would the answer change if xy were allowed?

**Hint ladder.**

1. Separate the vertical axis, the column i=1, and all columns i≥2.
2. Any column i≥2 is killed by (2,0); in column i=1, every positive height is killed by (1,1).

**Checked instance.** Find the survivors and explain why they form a basis of the stated quotient.

**Reasoning.** At i=0, heights 0,1,2 survive; at i=1, only height 0 survives; i≥2 never survives. The monomials are 1,y,y^2,x. Every polynomial reduces to their linear combination by removing divisible terms. Every polynomial in the ideal contains only monomials divisible by x^2,xy,or y^3, so no nonzero linear combination of the four survivors belongs to the ideal. This proves spanning and independence, hence dimension four.

**Boundary.** If the sole relation is x-y=0, neither x nor y should be erased: their classes are equal, not zero. The forbidden-region rule applies specifically to monomial generators.

**Extensions.**

- Remove generator xy. The quotient k[x,y]/(x^2,y^3) has six survivor monomials in a two-by-three rectangle; compare the multiplication maps.
- Move the corners and count survivors by rows. Gröbner bases extend this normal-form approach to more general ideals, but require a separately defined term order and reduction theory.

**Satisfying stop.** Four surviving positions and a complete reason there are no hidden survivors beyond the paper.

**Prior use.** Week 1 also uses boards, but these positions encode monomial divisibility rather than tilings. The family adds commutative-algebra content rather than relabeling a packing puzzle.

**Sources.**

- [J. S. Milne, Algebraic Geometry](https://www.jmilne.org/math/CourseNotes/AG.pdf), Chapter 1 rings/ideals; chapter 2 Hilbert basis theorem and quotient-ring framework. Inspection: relevant framework inspected; this specific monomial basis has a self-contained proof below.

<a id="ad-14"></a>
## AD-14 - A nonzero symbol whose square vanishes

Primary field: 13. Related: 14, 26. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** What algebraic information is retained by nilpotents even when ordinary point sets look identical?

**Anchor.** The dual-number ring Q[ε]/(ε^2) consists uniquely of a+bε with rational a,b and product (a+bε)(c+dε)=ac+(ad+bc)ε. Its element ε is nonzero but ε^2=0; a+bε is invertible exactly when a is nonzero.

**Bridge (exact-special-case).** Two coefficient boxes encode an actual quotient ring. The ε^2 rule is an exact algebraic relation, not a numerical approximation. Limits: ε is not a tiny nonzero rational or real number. The activity does not establish schemes, tangent functors, or general infinitesimal geometry; those need additional definitions.

**Prerequisite gates.**

- **Entry:** A and F: distribute two linear expressions and add signed rational coefficients.
- **Explore:** A: reduce products using ε^2=0 and distinguish formal equality from substitution ε=0.
- **Explain:** P: show ε cannot vanish as a residue class and solve for an inverse.
- **Prove:** A and X: quotient rings and ideals; polynomial independence justifies the two-coordinate normal form.
- **Reading:** Symbolic rule card; paired oral explanation is useful.
- **Arithmetic:** Signed addition, multiplication, and rational reciprocals.
- **Reasoning:** Hold an unfamiliar but consistent algebra separate from ordinary real arithmetic; errors in ε^2 usually expose this conflation.
- **Hard Stop:** This is an algebra-gated investigation. Do not replace the relation with 'ε is almost zero' to lower the prerequisite.

**Materials and preparation (8 minutes).** Two-column coefficient mats labeled ordinary and ε, signed counters for integer trials, and paper for rational examples. Prepare comparison cards for Q[t]/(t) and Q[t]/(t^2).

**Launch.** Invent numbers a+bε under the exact rule ε^2=0. Addition works by columns; multiplication distributes before ε^2 terms disappear. Find nonzero numbers whose product is zero, and find surprising numbers that still have multiplicative inverses. You may choose your own coefficients.

**Learner choices.** Choose trial elements, design a failed cancellation argument, classify invertibility, and decide what is lost when every ε coefficient is discarded.

**Hour menu.** 0-10 explore two-column addition and products; 10-15 agree that ε is a formal basis symbol; 15-35 hunt zero divisors and inverse pairs; 35-40 reset with pairs of ordinary/ε roles; 40-55 derive a general inverse rule or polynomial first-order expansion; 55-60 present one statement distinguishing this ring from Q.

**Explore.**

- Why does ε^2=0 not force ε=0 here?
- Can 1+ε be invertible despite containing a nilpotent part?
- Which coefficient of a product decides whether it could equal 1?
- Do equations t=0 and t^2=0 have the same rational points but different quotient rings?

**Hint ladder.**

1. Compare ordinary coefficients before trying to solve the ε coefficient equation.
2. Multiply (a+bε)(c+dε) and set its two coefficients equal to those of 1.

**Checked instance.** Invert 2+3ε and compare its behavior with ε.

**Reasoning.** For an inverse c+dε, the equations are 2c=1 and 2d+3c=0. Thus c=1/2,d=-3/4, and direct multiplication gives 1. For a general nonzero a, the inverse is 1/a-(b/a^2)ε. If a=0, the ordinary coefficient of every product is zero, so no inverse exists. The element ε is nonzero because the polynomial t is not a multiple of t^2, although its square is in that ideal.

**Boundary.** Evaluating every dual number at ε=0 collapses ε to zero. That map preserves arithmetic but forgets information; it is not an injective identification of dual numbers with rational numbers.

**Extensions.**

- Expand (1+ε)^n. For nonnegative integer n all terms of degree two or higher vanish, leaving 1+nε; prove this by induction.
- For a polynomial f, expansion gives f(a+bε)=f(a)+b f'(a)ε. This identity is exact in the ring; interpreting it as differential geometry requires a stated calculus/tangent-space gate.

**Satisfying stop.** One checked inverse pair and one nonzero zero divisor, with an explanation of why ordinary cancellation is unavailable.

**Prior use.** No current Week 1-10 equivalent. AD-13 supplies quotient normal forms, but this family investigates invertibility and nilpotent information rather than monomial counting.

**Sources.**

- [J. S. Milne, Algebraic Geometry](https://www.jmilne.org/math/CourseNotes/AG.pdf), Chapter 2, discussion of nilpotents/reduced quotients preceding Theorem 2.16 and Aside 2.24. Inspection: full relevant nilpotent/radical discussion; dual-number computations proved directly.

<a id="ad-15"></a>
## AD-15 - Find every rational point by aiming a line

Primary field: 14. Related: 11, 51. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** When does a geometric projection give a rational parametrization, and how must exceptional points be handled?

**Anchor.** For the circle x^2+y^2=1, a line of rational slope t through (-1,0) meets it again at ((1-t^2)/(1+t^2),2t/(1+t^2)). Conversely every rational point except (-1,0) yields rational t=y/(x+1). This is an exact parametrization with one explicitly handled exception.

**Bridge (exact-special-case).** The drawn circle, rational-slope line, and coordinate calculation are an actual rational map and its inverse on the specified punctured circle. Limits: A drawing alone cannot certify rational coordinates. Not every algebraic curve admits such a parametrization, and the missing point must not be concealed.

**Prerequisite gates.**

- **Entry:** V: draw a circle and lines through one marked point; independent arithmetic can initially be deferred.
- **Explore:** F and A: understand rational slopes and solve a quadratic after substituting a line equation.
- **Explain:** A and P: factor out the already known intersection and account for the exceptional point.
- **Prove:** A and P: derive both formulas and show each rational point in the claimed domain is recovered.
- **Reading:** A coordinate diagram and equations; orally supported derivation is possible.
- **Arithmetic:** Fractions, squares, polynomial factoring, and signed coordinates.
- **Reasoning:** Switch between geometric point and parameter without forgetting which domain excludes a point.
- **Hard Stop:** A complete rational parametrization needs symbolic algebra. Projective or scheme language is a later continuation, not required decoration.

**Materials and preparation (10 minutes).** Unit-circle template with (-1,0) marked, ruler, coordinate grid, and a slope table. A calculator can check arithmetic but not replace exact fractions.

**Launch.** Aim a line from (-1,0) across the unit circle. Choose a rational slope and find the second intersection exactly. Can this method find every point on the circle whose coordinates are fractions? Find any point it misses and explain why.

**Learner choices.** Choose slopes, search for small denominators, invent a way to recover the slope from a point, and decide how to represent the exceptional case.

**Hour menu.** 0-10 draw and compare secants; 10-15 state the rational-coordinate question; 15-35 derive or use the formula and exchange slope challenges; 35-40 move along a large circle while tracing lines from the fixed point; 40-55 prove the converse and connect to triples; 55-60 show an exact point and its recovery rule.

**Explore.**

- Why is one quadratic root already known before calculating?
- What happens at slope zero?
- How do you recover t from a given point?
- Which line through (-1,0) has no distinct second intersection?

**Hint ladder.**

1. Substitute y=t(x+1) into x^2+y^2=1.
2. The result has factor x+1 because (-1,0) lies on both curves.

**Checked instance.** Use slope t=1/2 and prove the general formula covers every rational point other than (-1,0).

**Reasoning.** Substitution gives (x+1)((1+t^2)x+t^2-1)=0. The second root is x=(1-t^2)/(1+t^2); y=t(x+1)=2t/(1+t^2). At t=1/2 this gives (3/5,4/5), and 9/25+16/25=1. Conversely, for a rational circle point with x≠-1, t=y/(x+1) is rational and its line recovers the point. The sole circle point with x=-1 is (-1,0), excluded from the finite-slope formula.

**Boundary.** A line tangent at (-1,0) is vertical and has no finite slope; its intersection is the known point counted twice. Omitting this exception would make the 'every point' claim false.

**Extensions.**

- Take t=p/q with integers p,q and obtain the triple (q^2-p^2,2pq,q^2+p^2). State the further coprimality/parity conditions before claiming primitive triples.
- Try a different conic with a known rational point. A general cubic does not inherit this parametrization merely because a line can be drawn through it.

**Satisfying stop.** One exact fractional point and a reversible slope construction, including the missing-point explanation.

**Prior use.** Week 9 uses rational slopes for billiards; this family uses them to parametrize solutions of an algebraic equation. The geometric language is related, the mathematical question is new.

**Sources.**

- [Ravi Vakil, The Rising Sea, January 29, 2015 draft](https://math.stanford.edu/~vakil/216blog/FOAGjan2915public.pdf), §6.5, printed pp.191-193, rational circle parametrization. Inspection: full relevant passage; source uses (1,0), while this reflected version is rederived below.

<a id="ad-16"></a>
## AD-16 - A curve made of seven finite-field points

Primary field: 14. Related: 11, 12. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How does the choice of ground field change the solutions of a polynomial equation, and what structure remains when a continuous-looking curve becomes a finite set?

**Anchor.** Over F5, the affine equation y^2=x^3-x has seven solutions. Its projective completion Y^2Z=X^3-XZ^2 has one point with Z=0, giving eight projective F5-points. The short Weierstrass discriminant is nonzero modulo five, so this is a nonsingular elliptic curve with its marked point at infinity.

**Bridge (exact-special-case).** Coordinates are residues with arithmetic modulo five; placed tokens are exactly the rational points of the displayed affine curve over that field. Limits: The grid is not a sampled real curve and adjacent dots should not be joined as if continuity were present. Point enumeration alone does not establish the elliptic-curve group law or cryptographic security.

**Prerequisite gates.**

- **Entry:** M and V: use a five-by-five coordinate grid and supplied residue/square tables.
- **Explore:** M: cube, subtract, and compare residues, with a calculator or lookup table if needed.
- **Explain:** P: exhaust all five x-values while using the complete square-residue table.
- **Prove:** A and X: projective coordinates for the extra point; algebraic nonsingularity or elliptic group-law proof is a separate gate.
- **Reading:** Coordinates and one equation; partner can record values.
- **Arithmetic:** Modulo-five addition/multiplication; supplied tables lower calculation demand without changing the mathematical question.
- **Reasoning:** Distinguish the number of y-solutions from the number of square residues, and affine from projective counting.
- **Hard Stop:** Finish with the seven affine points when projective coordinates are unavailable; do not quietly add an unexplained eighth point.

**Materials and preparation (10 minutes).** Five-by-five grids labeled 0 through 4, counters, a square table, and a separate ordinary real-coordinate sketch for comparison. Prepare an infinity card only for the projective stage.

**Launch.** Place a counter at (x,y) exactly when y times y and x cubed minus x have the same remainder after division by five. Find every permitted point without testing all twenty-five pairs separately. What symmetry can shorten the search?

**Learner choices.** Choose whether to search by columns or square residues, predict partners of known points, organize a completeness certificate, and compare a changed modulus or polynomial.

**Hour menu.** 0-10 explore residue multiplication; 10-15 place two sample points and reject one; 15-35 complete the curve and explain missing columns; 35-40 stand in residue positions paired by negation; 40-55 change the equation or introduce projective infinity at its real gate; 55-60 report exactly which point set was counted.

**Explore.**

- Which remainders can a square have?
- Why does a nonzero y normally have a partner?
- When do y and -y coincide?
- Does a smooth real-looking drawing determine the number of points modulo five?

**Hint ladder.**

1. Compute the squares of 0,1,2,3,4 once and reuse that table.
2. For each x, compare x^3-x with 0,1,4, the possible square residues.

**Checked instance.** Find every affine F5-point of y^2=x^3-x and, if projective coordinates are understood, the additional point at infinity.

**Reasoning.** For x=0,1,2,3,4 the right sides are 0,0,1,4,0. Square roots give (0,0),(1,0),(2,1),(2,4),(3,2),(3,3),(4,0), seven points. At Z=0 the homogeneous equation forces X=0; a projective point cannot have all coordinates zero, so Y≠0 and all such triples represent the single point [0:1:0]. The projective total is eight. The discriminant is -16(4(-1)^3)=64, which is 4 modulo 5 and nonzero, as required for nonsingularity.

**Boundary.** Using modulus four would not give a field and changes square-root behavior; formulas requiring division by any nonzero residue would fail. Counting affine points and reporting eight without explaining infinity is also incorrect.

**Extensions.**

- Over F7 the same curve has seven affine points and one point at infinity; verify independently rather than assume the total follows the modulus.
- With field division and the actual group-law formulas, investigate addition of points. Associativity is a theorem, not a consequence of the finite picture; keep it a separately sourced continuation.

**Satisfying stop.** A seven-point picture with a five-column table proving completeness and a visible y↦-y symmetry.

**Prior use.** Week 4 supplies modular arithmetic, but polynomial curves over fields are a new mathematical object. AD-15 contrasts rational parametrization with changing the ground field.

**Sources.**

- [J. S. Milne, Elliptic Curves, second edition](https://www.jmilne.org/math/Books/EC2.pdf), Introduction, printed p.1: projective Weierstrass equation, nonsingularity condition, and distinguished point; I §1 Example 1.15 for the point at infinity. Inspection: full relevant introductory statement and point-at-infinity example; finite enumeration proved below; broader finite-field theory is continuation.

<a id="ad-17"></a>
## AD-17 - The average stays, the disagreement shrinks

Primary field: 15. Related: 37, 39. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How does decomposing a linear transformation into invariant directions explain every iterate without repeated calculation?

**Anchor.** The real linear map T(x,y)=((3x+y)/4,(x+3y)/4) preserves s=x+y and sends d=x-y to d/2. Thus (1,1) and (1,-1) are eigenvectors with eigenvalues 1 and 1/2, and T^n is explicitly determined by these two coordinates.

**Bridge (exact-special-case).** Two marked quantities undergo the actual rational linear transformation, not a numerical analogy. Sum and difference give a change of coordinates that diagonalizes it. Limits: One symmetric two-variable averaging rule does not prove convergence of every averaging network. The midpoint can remain fixed while other linear maps oscillate or expand.

**Prerequisite gates.**

- **Entry:** O and V: move two markers on a number line toward one another by a demonstrated quarter of the gap.
- **Explore:** F: use halves and quarters to record exact positions.
- **Explain:** A and P: calculate sum/difference before and after one move, or use a symmetric geometric argument.
- **Prove:** A and P: induct on iteration number; L for the eigenvector and diagonalization interpretation.
- **Reading:** Number line and one move rule; full matrix notation optional.
- **Arithmetic:** Fractions and signed difference; start with multiples of four to delay awkward denominators.
- **Reasoning:** Both new positions must be computed from the old pair simultaneously, not sequentially.
- **Hard Stop:** Convergence and its error estimate are meaningful without general spectral theory; arbitrary networks require new hypotheses.

**Materials and preparation (5 minutes).** Large number line, two differently colored markers, a midpoint marker, and old/new recording columns. Prepare a quarter-gap strip or folding paper for the geometric move.

**Launch.** Put markers at two chosen numbers. In one round, each moves one quarter of the old gap toward the other. Both move using the old positions. Predict where they will settle and how far apart they will be after several rounds without doing every round.

**Learner choices.** Choose starting pairs, compare pairs with equal midpoint or equal gap, invent a faster prediction, and decide whether exact meeting ever occurs.

**Hour menu.** 0-10 explore marker moves; 10-15 establish simultaneous updating; 15-35 record pairs and seek invariants; 35-40 two participants act out shrinking gaps; 40-55 derive an iteration formula or change the step fraction; 55-60 explain the fixed midpoint and shrinking disagreement. Eigenvector notation is optional.

**Explore.**

- What never changes?
- How much gap is removed in one round?
- Can the markers meet after finitely many rounds?
- What would change if each moved three quarters of the gap?

**Hint ladder.**

1. Add the two positions before and after a move.
2. Instead of tracking both numbers, track their midpoint and signed difference.

**Checked instance.** Start at (0,8). Find the pair after three rounds and describe round n exactly.

**Reasoning.** The midpoint is 4. The gaps are 8,4,2,1, so the pairs are (0,8),(2,6),(3,5),(3.5,4.5). After n rounds the pair is (4-4/2^n,4+4/2^n). Algebra gives x'+y'=x+y and x'-y'=(x-y)/2, proving the formula by induction. For unequal starting positions the gap remains nonzero at every finite n, although it tends to zero.

**Boundary.** If each marker moves the entire old gap, the two positions merely swap: the signed difference changes sign and never shrinks. 'Moving toward the other marker' alone does not guarantee convergence.

**Extensions.**

- For fraction a, the signed difference multiplies by 1-2a. Determine convergence for real a: unequal inputs converge exactly when 0<a<1; a=1/2 meets in one round.
- Explore three connected markers with a specified averaging matrix, checking whether the average is actually conserved. General consensus needs conditions on the update matrix, not a visual impression.

**Satisfying stop.** A prediction for any round from the midpoint and one halving rule, with a reason exact meeting need not occur.

**Prior use.** Week 2 uses linear algebra over F2; this family introduces real scalars, eigen-directions, and convergence. It is not a new toggle-board story.

**Sources.**

- [Sheldon Axler, Linear Algebra Done Right, fourth edition](https://linear.axler.net/LADR4e.pdf), §3A linear maps and chapter 5 eigenvectors; §7B spectral discussion. Inspection: relevant definitions inspected; this map and iteration formula are proved directly.

<a id="ad-18"></a>
## AD-18 - Stretch, shear, flatten: what happens to area?

Primary field: 15. Related: 51, 52. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How does the determinant encode signed area change, and why does nonzero determinant distinguish invertibility from flattening?

**Anchor.** A real two-by-two matrix [[a,b],[c,d]] sends the unit square to the parallelogram spanned by (a,c),(b,d), with signed area ad-bc. Its ordinary area scale is |ad-bc|. Determinant zero means the two image directions are dependent.

**Bridge (exact-special-case).** Moving the square's two basis directions and completing the parallelogram is the exact action of a linear map. Cut-and-rearrange area arguments can precede matrices. Limits: Preserving area does not imply preserving angles, distances, or the whole shape. Signed area records orientation and can be negative; physical area cannot.

**Prerequisite gates.**

- **Entry:** O and V: construct parallelograms on a grid and compare areas by cutting or counting.
- **Explore:** F and V: use signed coordinates and triangle areas where needed.
- **Explain:** P: justify the shear's area preservation and distinguish reflection from collapse.
- **Prove:** A and P: derive ad-bc from coordinate geometry; L for the equivalence with invertibility and composition law.
- **Reading:** Arrow diagrams suffice initially; two-by-two matrices optional.
- **Arithmetic:** Whole-number coordinates and halves for triangle areas; signed multiplication for determinants.
- **Reasoning:** Map both basis vectors from the same origin, and preserve the order of those vectors when discussing orientation.
- **Hard Stop:** General volume scaling in higher dimension or change of variables requires additional algebra/analysis, not merely many drawings.

**Materials and preparation (10 minutes).** Squared paper, two colored arrow strips, transparent unit squares, scissors, and transformation cards for shear, reflection, and projection. A drawing alternative avoids cutting demands.

**Launch.** A linear machine sends the horizontal unit arrow to u and the vertical unit arrow to v. Its full rule is T(x,y)=x u+y v: combine the chosen arrows using the same coefficients as the input. Their parallelogram is the transformed unit square. Find a machine that changes shape without changing area, one that reverses orientation, and one that flattens the square completely.

**Learner choices.** Choose image arrows, decide how to measure area, find examples with the same area but different shapes, and challenge a proposed inverse.

**Hour menu.** 0-10 build parallelograms; 10-15 explain how the two arrows determine every grid-point image; 15-35 compare the three machines; 35-40 walk around images in vertex order; 40-55 derive or test determinant rules and compose maps; 55-60 show one distinction that area alone misses.

**Explore.**

- Can a slanted parallelogram have area one?
- What changes when the two image arrows are exchanged?
- How can area reveal information loss?
- Can two different shapes have determinant one?

**Hint ladder.**

1. For a shear, cut a triangle from one side and move it to the other.
2. A reflection reverses the clockwise/counterclockwise vertex order even though its ordinary area stays the same.

**Checked instance.** Compare S(x,y)=(x+y,y), R(x,y)=(y,x), and P(x,y)=(x,0).

**Reasoning.** S maps the square to vertices (0,0),(1,0),(2,1),(1,1). Base and height are both one, so area remains one; its determinant is 1. R exchanges the basis arrows, retaining area one but changing signed area to -1. P sends both (0,0) and (0,1) to (0,0), collapses the square to a segment, and has determinant zero. The inverse shear is (u,v)↦(u-v,v), whereas P cannot be inverted because distinct inputs coincide.

**Boundary.** S preserves area but sends the vertical unit edge to a diagonal of length √2. It therefore does not preserve lengths or make a rigid motion.

**Extensions.**

- Compose two shears and compare the resulting parallelogram with determinant multiplication. For S followed by (x,y)↦(x,x+y), the matrix is [[1,1],[1,2]] and determinant remains one.
- Use integer image arrows to investigate lattice-point counts and fundamental parallelograms; introduce any connection to Pick's theorem separately with its polygon hypotheses.

**Satisfying stop.** Three machines distinguished by area, orientation, and recoverability, with a concrete example showing area preservation is weaker than rigidity.

**Prior use.** Week 1 shape work can supply manipulatives, but this family studies linear transformations and signed area rather than tiling reachability. It complements AD-17's spectral view.

**Sources.**

- [Sheldon Axler, Linear Algebra Done Right, fourth edition](https://linear.axler.net/LADR4e.pdf), §7F volume discussion, especially 7.108-7.111; linear-map framework in §3A. Inspection: relevant volume discussion inspected; the two-dimensional examples use direct area arguments.

<a id="ad-19"></a>
## AD-19 - Take one linear arrow apart

Primary field: 16. Related: 15, 18. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can a representation of a directed graph split into indecomposable pieces, and what information survives a change of bases?

**Anchor.** A finite-dimensional representation of the one-arrow quiver is a linear map T:V→W over a field. Up to independent changes of bases, it decomposes into dim(kernel T) copies of k→0, rank(T) copies of the identity k→k, and dim(W)-rank(T) copies of 0→k. These are the three indecomposable representations.

**Bridge (exact-special-case).** The two spaces, their bases, and the specified linear map are an actual quiver representation, equivalently a module for the associated path algebra. Limits: Dots and arrows without vector spaces would omit the mechanism. Rank classifies this single-arrow problem, not arbitrary quivers or linear operators under similarity.

**Prerequisite gates.**

- **Entry:** L: understand vectors, a linear map, and how images of a basis determine it.
- **Explore:** L and A: solve a small homogeneous linear system and choose independent vectors.
- **Explain:** P: separate killed directions, transmitted directions, and unreachable target directions.
- **Prove:** L and P: choose complements to kernel and image and verify direct-sum decomposition and indecomposability of one-dimensional blocks.
- **Reading:** Symbolic equations and small matrices are essential.
- **Arithmetic:** Signed rational arithmetic and elementary linear systems.
- **Reasoning:** Distinguish a basis change in the domain from one in the target; the two may be chosen independently.
- **Hard Stop:** Keep a genuine linear-algebra gate. A token-routing analogy is only motivation until linear combinations and basis changes are present.

**Materials and preparation (5 minutes).** Graph paper, two labeled vector-space boxes, vector cards, and a matrix worksheet with space to record chosen bases. No specialized manipulative or software is required.

**Launch.** Study T(x,y,z)=(x+y,y+z) from Q^3 to Q^2. Choose new coordinate directions so the machine becomes a collection of simple parts: directions killed, directions passed across unchanged, and target directions no input can reach. Show your new bases explicitly.

**Learner choices.** Choose convenient kernel and complement vectors, decide how to depict the blocks, compare different decompositions, and create another map with the same or a different block inventory.

**Hour menu.** 0-10 test images of selected vectors; 10-15 define the three proposed simple blocks; 15-35 find bases and verify a decomposition; 35-40 reset with domain/target direction cards; 40-55 compare matrices and justify the classification; 55-60 report the block counts and which choices were nonunique. Do not require a general quiver theorem.

**Explore.**

- Which input changes are completely invisible?
- Can every target vector be reached?
- Do different chosen complements change the numbers of blocks?
- Why is this classification different from diagonalizing an operator?

**Hint ladder.**

1. Solve x+y=0 and y+z=0 first.
2. Choose two input vectors whose images form the standard target basis, then add a kernel basis vector.

**Checked instance.** Decompose T(x,y,z)=(x+y,y+z) into one-arrow indecomposables.

**Reasoning.** The kernel is spanned by k=(1,-1,1). Choose u=(1,0,0) and v=(0,0,1), whose images are (1,0) and (0,1). The vectors u,v,k are independent and form a domain basis. Relative to that basis and the standard target basis, T has matrix [[1,0,0],[0,1,0]]. Thus the representation is two identity blocks Q→Q plus one killed block Q→0, with no unreachable-target block. Complement choices differ, but kernel dimension one and rank two fix the inventory.

**Boundary.** As endomorphisms under the same basis change on both sides, I and 2I are not similar over Q, despite equal rank: P^-1 I P is always I. Independent domain/target bases are an essential hypothesis here.

**Extensions.**

- Try S(x,y,z)=(x+y,2x+2y). Its rank is one, so the block counts are two killed, one transmitted, and one unreachable target direction.
- Add a second arrow V→W→U and track the ranks of both arrows and their composite. More complicated quivers introduce new classification behavior; the one-arrow rank rule is not a universal solution.

**Satisfying stop.** An explicit basis choice makes the given machine visibly two transmitted directions and one killed direction.

**Prior use.** Week 2 contains image/kernel ideas over F2; this advanced revisit changes the question to decomposition up to independent bases and its representation-theoretic meaning.

**Sources.**

- [Pavel Etingof et al., Introduction to Representation Theory, 2011 notes](https://math.mit.edu/~etingof/replect.pdf), §5.2, Example 5.8, printed p.81; §1.8 quiver representations. Inspection: full relevant decomposition text.

<a id="ad-20"></a>
## AD-20 - Measure how matrix moves fail to commute

Primary field: 17. Related: 16, 15. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why does the commutator of an associative algebra become a nonassociative Lie product, and what replaces associativity?

**Anchor.** For rational two-by-two matrices define [A,B]=AB-BA. The bracket is bilinear, alternating, and satisfies [[A,B],C]+[[B,C],A]+[[C,A],B]=0. For E=[[0,1],[0,0]], F=[[0,0],[1,0]], H=[[1,0],[0,-1]], the relations are [E,F]=H, [H,E]=2E, [H,F]=-2F.

**Bridge (exact-special-case).** The new operation is the actual matrix commutator, and the three displayed matrices span the Lie algebra sl2(Q). Calculations investigate its identities directly. Limits: A physical sequence of large rotations is not automatically this bracket. The activity does not establish the Lie-group/Lie-algebra correspondence or classification of Lie algebras.

**Prerequisite gates.**

- **Entry:** L and F: multiply two-by-two matrices and subtract them, with a template if needed.
- **Explore:** L: distinguish matrix product from the newly defined bracket and track nested operations.
- **Explain:** P: give a concrete associativity failure and identify cancelling terms in Jacobi.
- **Prove:** A and P: expand each double commutator using associativity of the original matrix product; L for identifying the span with trace-zero matrices.
- **Reading:** Symbolic matrix and bracket notation is essential.
- **Arithmetic:** Signed integer multiplication/addition; coefficients no larger than two in the main table.
- **Reasoning:** There are two different multiplications in play. Use a color or box around each bracket calculation and keep parenthesization explicit.
- **Hard Stop:** Keep the matrix prerequisite. A story in which order matters would establish only noncommutativity, omitting the nonassociative Lie structure.

**Materials and preparation (8 minutes).** Three matrix cards E=[[0,1],[0,0]], F=[[0,0],[1,0]], H=[[1,0],[0,-1]]; blank product/bracket tables; two colors for positive and negative expansion terms. Provide one worked ordinary matrix product, not a completed commutator table.

**Launch.** Ordinary matrix multiplication is associative but can depend on order. Make a new operation [A,B]=AB-BA. Investigate whether this new operation is associative. If it fails, search for a three-term identity that always cancels, using E,F,H as a small laboratory.

**Learner choices.** Choose pairs to compare, choose a triple likely to reveal failure, organize a multiplication table, and decide whether an identity follows from examples or symbolic cancellation.

**Hour menu.** 0-10 refresh matrix products with chosen vectors; 10-15 introduce the bracket as a second operation; 15-35 build the small relation table; 35-40 reset and swap order cards physically; 40-55 test associativity and expand Jacobi; 55-60 display one failed law and one valid replacement. Calculations can be split between partners.

**Explore.**

- What is [A,A]?
- What happens when A and B are exchanged?
- Do [H,[E,F]] and [[H,E],F] agree?
- Where does each triple product cancel in the Jacobi sum?

**Hint ladder.**

1. Calculate EF and FE separately before subtracting.
2. Write all twelve terms of the three double commutators, then pair identical triple products with opposite signs.

**Checked instance.** Compute the three listed brackets, find an associativity failure, and verify Jacobi on E,F,H.

**Reasoning.** EF=diag(1,0) and FE=diag(0,1), giving [E,F]=H. Direct products give [H,E]=2E and [H,F]=-2F. Thus [[H,E],F]=2H while [H,[E,F]]=[H,H]=0, so the bracket is not associative. For the cyclic Jacobi sum, [[E,F],H]=0, [[F,H],E]=[2F,E]=-2H, and [[H,E],F]=2H; their sum is zero. For arbitrary matrices, expansion pairs and cancels the same ordered triple products.

**Boundary.** A zero commutator does not mean both matrices are zero: every matrix commutes with the identity. Nonzero bracket measures failure to commute, not the size of the matrices.

**Extensions.**

- Prove every rational trace-zero two-by-two matrix is a unique linear combination of E,F,H, so their closed bracket table describes the whole three-dimensional algebra.
- With polynomial differentiation as an explicit new prerequisite, compare D and multiplication by x: [D,M_x]=I. This is an operator-algebra continuation, not needed for the matrix investigation.

**Satisfying stop.** An explicit nonassociativity witness and a checked Jacobi cancellation, with the two products clearly distinguished.

**Prior use.** Week 3 compositions are reversible permutations; this is a substantially different advanced structure involving subtraction and a nonassociative operation. No elementary-equivalence claim is made.

**Sources.**

- [Pavel Etingof et al., Introduction to Representation Theory](https://math.mit.edu/~etingof/replect.pdf), §1.9, Definition 1.39, Example 1.40, and Example 1.46 sl(2) relations. Inspection: full relevant definition and relations.

<a id="ad-21"></a>
## AD-21 - The collection that remembers both choices

Primary field: 18. Related: 03, 68. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** What makes a construction universal rather than merely a convenient list, and how do pullbacks encode compatible choices?

**Anchor.** For functions f:A→C and g:B→C, the pullback is P={(a,b):f(a)=g(b)}, with its two projection maps. Given u:X→A and v:X→B with f∘u=g∘v, there is exactly one map h:X→P whose projections are u and v: h(x)=(u(x),v(x)).

**Bridge (faithful-representation).** Two labeled inventories map to a common color set. Compatible ordered pairs and the unique pairing map realize the full finite-set pullback, including its universal property. Limits: Matching one object per color is not the pullback when labels repeat. The example does not establish all categorical limits or turn every commuting square into a pullback.

**Prerequisite gates.**

- **Entry:** O: match labels and keep two inventory roles distinct.
- **Explore:** C: enumerate every compatible ordered pair without duplicates.
- **Explain:** P: explain why each object carrying two compatible choices has one forced location in the pair collection.
- **Prove:** P and X: functions, composition, and quantification over an arbitrary set X for the universal statement.
- **Reading:** Names and color labels can be replaced by pictures; upper stage uses arrows/functions.
- **Arithmetic:** Small counts; multiplication of fiber sizes is optional.
- **Reasoning:** Preserve both individual identities, not just their shared color. The universal claim asks about all other compatible assignments, which is a genuine abstraction gate.
- **Hard Stop:** Constructing the pair list is a complete lower task; call the universal-property proof complete only when existence and uniqueness are both explained.

**Materials and preparation (10 minutes).** Inventory A: Ada and Bo colored red, Cy colored blue. Inventory B: r red, s and t blue, u green. Draw one space for each compatible pair and keep a common color legend.

**Launch.** Choose one person card and one badge card, but their colors must match. Build a catalog remembering exactly which person and which badge were chosen. Another group will give each of its tokens a person and a compatible badge. Show that every token then has one forced place in your catalog.

**Learner choices.** Choose a layout, decide how to retain repeated-color identities, create an alternative group's assignments, and test whether a smaller catalog loses required information.

**Hour menu.** 0-10 freely match cards; 10-15 specify that both identities must survive; 15-35 create and test catalogs; 35-40 participants enact two projections from pair positions; 40-55 investigate the forced map from another inventory; 55-60 explain why one possible catalog entry per token is both available and unique.

**Explore.**

- Why are Ada-r and Bo-r different?
- What happens to the green badge?
- Can one blue catalog slot remember both Cy-s and Cy-t?
- What must be true before another token can be placed at all?

**Hint ladder.**

1. Make a row for each person and list every badge with the same color.
2. A token's two assigned identities force its ordered pair; there is no further choice.

**Checked instance.** Construct the pullback of the displayed inventories and explain its universal property for an arbitrary compatible assignment.

**Reasoning.** The catalog is {(Ada,r),(Bo,r),(Cy,s),(Cy,t)}. There are four pairs; badge u has no compatible person. If a token x is assigned person u(x) and badge v(x) of the same color, then (u(x),v(x)) is on the list, proving existence. Any catalog placement preserving both assignments must have exactly those two entries, proving uniqueness. This works for every token independently and therefore defines the unique required function.

**Boundary.** A three-entry catalog containing only one pair per color fails: there is no green pair, and red/blue repetitions require multiple distinct pairs. Equal labels do not erase identities.

**Extensions.**

- Change fiber sizes and prove the count is the sum over colors of |A_color|×|B_color|; this counts all compatible pairs, not arbitrary pairings without replacement.
- Compare with an ordinary Cartesian product, obtained when both inventories map to a one-element color set. Then every pair is compatible.

**Satisfying stop.** A four-entry catalog and a concrete explanation that preserving both choices forces a unique placement.

**Prior use.** Week 5 combines constraints but does not study a universal mapping property. This family must retain the uniqueness-of-map question to count as categorical content.

**Sources.**

- [Brendan Fong and David Spivak, Seven Sketches in Compositionality](https://ocw.mit.edu/courses/18-s097-applied-category-theory-january-iap-2019/a4175d61479a35340d6307ae5e48ef5a_18-s097iap19textbook.pdf), §3.5.3, pullbacks of sets and colored-pair example near PDF p.125. Inspection: full relevant construction and explanation.

<a id="ad-22"></a>
## AD-22 - Which loops can face moves erase?

Primary field: 18. Related: 55, 15. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How does taking cycles modulo boundaries distinguish a closed pattern from a genuinely surviving homology class?

**Anchor.** Over F2, a finite simplicial complex has boundary maps C2→C1→C0 with consecutive composite zero. H1 is kernel(∂1)/image(∂2). In a square with diagonal AC, the cycle space has basis T1=AB+BC+AC and T2=AC+CD+DA; filling chosen triangular faces changes the boundary subspace.

**Bridge (faithful-representation).** Marked edges are F2 chains; endpoints with odd incidence form their boundary. Flipping the three edges of an available face adds that face's boundary. Reachability between closed patterns is equality of homology classes. Limits: The legal faces are part of the data. A loop drawn in a plane does not automatically bound an available face, and this one complex does not prove topological invariance in general.

**Prerequisite gates.**

- **Entry:** O and C: flip edge markers and count parity at four vertices.
- **Explore:** C and P: distinguish closed edge patterns from patterns with odd endpoints.
- **Explain:** P: list all four cycles and compare which face flips are legal.
- **Prove:** L and X: interpret vector spaces, boundary maps, image/kernel, and quotient for formal homology; finite parity proofs can precede notation.
- **Reading:** Edge names and short move rules; oral launch suffices.
- **Arithmetic:** Odd/even counts; binary addition means toggling twice cancels.
- **Reasoning:** Track both a marked edge state and which faces are actually filled. An empty drawn triangular region is not automatically a legal face.
- **Hard Stop:** The concrete reachability result is exact. Claims about arbitrary surfaces or homotopy invariance require additional topology.

**Materials and preparation (10 minutes).** Square A,B,C,D with diagonal AC, five edge counters, and removable face cards ABC and ACD. Use a different color for face availability than for marked edges.

**Launch.** Mark any edges so every vertex touches an even number of marked edges. A move flips all three edges around a face whose card is present. Can you erase your pattern? Compare no face cards, only ABC, and both faces. Keep the graph unchanged while changing available faces.

**Learner choices.** Choose closed patterns, choose face moves, choose targets, invent a certificate that a target cannot be reached, and decide how to group mutually reachable patterns.

**Hour menu.** 0-10 explore edge toggling; 10-15 define closed patterns and face moves; 15-35 catalog cycles and test erasing; 35-40 enact boundary cancellation with vertex gestures; 40-55 classify reachability for the three face choices; 55-60 explain one loop that changes status when a face is added.

**Explore.**

- Why does a face move preserve even incidence?
- Does the outer square count as a closed pattern?
- What is T1 plus T2 when the diagonal is toggled twice?
- Can a visible loop be equivalent to zero?

**Hint ladder.**

1. At B, AB and BC must have the same mark; at D, CD and DA must match.
2. Adding both triangle boundaries cancels AC and leaves the outer square.

**Checked instance.** Classify closed patterns and homology classes with only face ABC available.

**Reasoning.** Let a mark AB=BC and c mark CD=DA. Evenness at A forces AC=a+c mod two; the condition at C then follows. The four cycles are 0,T1,T2,T1+T2. The only available face boundary is T1, so classes are {0,T1} and {T2,T1+T2}. Thus H1 has two elements, a one-dimensional F2 space. With no faces all four classes differ; with both faces every cycle can be erased and H1 is zero.

**Boundary.** The marked outer square is a cycle in all three versions, but its class is nonzero with only ABC filled and zero with both faces filled. 'Closed loop' and 'nonzero homology class' are not synonyms.

**Extensions.**

- Remove diagonal AC and all faces: only the empty pattern and outer square remain closed. Compare the surviving one-dimensional cycle space with the one-face version, without asserting they are identical complexes.
- Use signed integer edges to study oriented boundaries. The F2 cancellation picture is exact for its coefficient field and should not silently be used to claim integer homology computations.

**Satisfying stop.** The same outer loop can or cannot be erased depending on available faces, with an exact reachability certificate.

**Prior use.** Week 2 introduces parity and incidence; adding faces and quotienting cycles by face boundaries is the genuinely new question. Coordinate with topology families to avoid counting the identical complex twice.

**Sources.**

- [Stacks Project, Complexes](https://stacks.math.columbia.edu/tag/010V), §12.13, chain-complex definition and homology formula after Lemma 12.13.3. Inspection: full relevant definitions; finite graph/face matrices checked directly.

<a id="ad-23"></a>
## AD-23 - Why two dimensions are better than one count

Primary field: 19. Related: 16, 15. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How does K0 retain the independent ranks of projective modules, and why are formal differences needed even in a completely computable example?

**Anchor.** For R=Q×Q, every finitely generated R-module splits as e1P⊕e2P, where e1=(1,0), e2=(0,1). It is classified by the pair of rational dimensions (a,b), and is projective because it is a sum of the summands e1R,e2R of R. K0(R), the group completion of projective isomorphism classes under direct sum, is Z×Z.

**Bridge (exact-special-case).** Paired vector spaces are genuine modules over Q×Q. Two-color counters faithfully encode their isomorphism classes only after the idempotent decomposition is established. Formal signed pairs compute actual K0 for this ring. Limits: Counter subtraction by itself is only the group-completion mechanism. It does not constitute a lesson on arbitrary projective modules, higher K-groups, or algebraic K-theory generally.

**Prerequisite gates.**

- **Entry:** L and X: vector spaces, direct sums, ring action, and module isomorphism for the genuine K0 investigation. Two-color counting offers a preparatory subtask.
- **Explore:** L: separate e1 and e2 components and compare dimension pairs.
- **Explain:** P: show why total dimension forgets structure and why every pair is projective.
- **Prove:** X and P: use the definition of projective as a direct summand of a free module, then verify the universal group-completion construction.
- **Reading:** Symbolic definitions are essential for the K0 claim; counters can carry the subsequent computations.
- **Arithmetic:** Nonnegative integer dimension pairs and signed subtraction.
- **Reasoning:** Distinguish a module, its isomorphism class, and a formal difference of classes. Negative coordinates need not be actual objects.
- **Hard Stop:** Participants who only manipulate counters finish a preliminary monoid investigation, not the full K0 computation. The algebra gate is deliberate.

**Materials and preparation (12 minutes).** Two-color counters, paired vector-space diagrams, and a one-page definition sheet for R, e1,e2, projective modules, and group completion. No software or large computations.

**Launch.** The ring R has two independent scalar controls: (r,s) scales the first space by r and the second by s. Classify finite pairs of rational vector spaces under maps respecting both controls. Then allow formal differences of classes. What information must survive, and which differences cannot be represented by a single actual module?

**Learner choices.** Choose pairs with equal total dimension, construct distinguishing ring actions, select stable additions, and decide what invariants should classify formal differences.

**Hour menu.** 0-10 explore paired spaces and their two controls; 10-15 define module-respecting comparison; 15-35 derive the two dimensions and projectivity; 35-40 reset with two-color direct sums; 40-55 construct formal differences and the K0 identification; 55-60 state the exact computed ring invariant and the limits of the counter model.

**Explore.**

- Why are (Q,0) and (0,Q) different despite equal total dimension?
- Which pairs are free as R-modules?
- Can adding the same pair erase a dimension mismatch?
- What could a negative coordinate of a class mean?

**Hint ladder.**

1. Apply e1 and e2 separately; they sum to the identity and their product is zero.
2. A free module R^n has dimension pair (n,n); the two one-color modules are direct summands of R.

**Checked instance.** Compute [P]-[Q] for dimension pairs P=(2,1), Q=(1,2), and explain why K0(R)=Z^2.

**Reasoning.** The class difference is (1,-1), so it is not the class of an actual module, whose coordinates are nonnegative. Every module splits into e1P and e2P because e1+e2=1 and e1e2=0; respecting the R action preserves each component. Finite vector-space classification gives the monoid N^2. Conversely every pair is a sum of e1R,e2R and hence projective. Group completion sends formal differences to coordinate differences, which are additive and classify them, giving Z^2.

**Boundary.** The modules (Q,0) and (0,Q) have equal total rational dimension but are not R-isomorphic: e1 acts as identity on the first and zero on the second. One scalar dimension count would lose essential information.

**Extensions.**

- Classify free modules inside this monoid: precisely pairs (n,n). A projective module with dimensions (1,0) is not free, despite being a direct summand of R.
- For a general commutative monoid cancellation may fail: if e+e=e, its image in every group is zero. This warns against assuming every group completion embeds its starting monoid.

**Satisfying stop.** A correct computation K0(Q×Q)=Z^2 with one actual projective nonfree module and one genuinely virtual class.

**Prior use.** No existing week covers this definition. The advanced gate prevents elementary counter bookkeeping from being counted as full K-theory coverage.

**Sources.**

- [Charles Weibel, The K-book, chapter II](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.II.pdf), §1 group completion; §2 definition of K0 and product-ring calculation preceding Example 2.1.4, chapter-PDF p.6. Inspection: full relevant definition and product calculation.

<a id="ad-24"></a>
## AD-24 - Necklaces that resist dividing by four

Primary field: 20. Related: 05. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How do stabilizers explain why dividing labeled configurations by the number of symmetries can fail, and why does averaging fixed configurations work?

**Anchor.** For a finite group G acting on a finite set X, the number of orbits is (1/|G|) times the sum over g of the number of configurations fixed by g. The cyclic group of four rotations acts on sixteen binary colorings of four labeled positions, producing six orbits.

**Bridge (faithful-representation).** Four-bead rings and allowed rotations realize the exact group action. The same-versus-different rule is orbit equivalence, and symmetrical necklaces have nontrivial stabilizers. Limits: Reflections are excluded from the core rule, and color names are fixed. Changing either convention changes the action; a symmetry story without an exact equivalence rule is not a well-defined counting problem.

**Prerequisite gates.**

- **Entry:** O: arrange two colors on four positions and rotate a ring without turning it over.
- **Explore:** C: group all sixteen labeled strings into rotation classes and avoid duplicates.
- **Explain:** P: show why different orbit sizes invalidate division by four.
- **Prove:** P: double-count pairs (rotation, fixed coloring); the general theorem needs finite group actions and orbit-stabilizer reasoning.
- **Reading:** None for rings; binary strings optional for systematic recording.
- **Arithmetic:** Count to sixteen, sum four fixed counts, and divide by four.
- **Reasoning:** Keep rotation separate from reflection and preserve named colors; a marked top position helps compare labeled versus unlabeled states.
- **Hard Stop:** The six-orbit classification is complete without group terminology. General orbit-counting extensions require precise action rules and checked stabilizers.

**Materials and preparation (10 minutes).** Four-position circular mats with a removable top marker, two-color counters, and sixteen small recording cards. Reversible bracelets are inappropriate unless flipping is explicitly discussed as a rule change.

**Launch.** Make four-bead necklaces with two colors. Two count as the same if turning the ring makes them match; do not flip it over and do not exchange color names. Find every different necklace. Someone says there are sixteen strings and four turns, so the answer must be four. Decide whether that argument works.

**Learner choices.** Choose representatives, invent a catalog order, decide how to prove no necklace is missing, and search for the most and least symmetric patterns.

**Hour menu.** 0-10 build and rotate patterns freely; 10-15 fix the equivalence rule; 15-35 catalog necklaces and inspect the divide-by-four claim; 35-40 rotate a four-person pattern; 40-55 count fixed colorings under each turn; 55-60 connect the two correct counts. The orbit catalog can be an earlier stop.

**Explore.**

- How many distinct rotations does 0000 have?
- How many does 0101 have?
- Why does every pattern fixed by a quarter-turn use one color only?
- Can the fixed-pattern average be explained rather than memorized?

**Hint ladder.**

1. Sort first by the number of beads of each color, then distinguish adjacent from opposite pairs.
2. Count colorings fixed by zero, one, two, or three quarter-turns separately.

**Checked instance.** Count binary four-bead necklaces up to rotation and verify Burnside's average.

**Reasoning.** Representatives are 0000,1111,0001,0011,0101,0111. Their orbit sizes are 1,1,4,4,2,4, totaling sixteen strings. The identity fixes sixteen colorings; each quarter-turn fixes only 0000 and 1111; the half-turn fixes four, determined by the first two bits. The average (16+2+4+2)/4=6 agrees. Each orbit contributes exactly four to the total fixed-pair count because its number of positions times its stabilizer size equals four.

**Boundary.** Dividing sixteen by four fails because not every orbit has four elements. For this particular binary length-four example, additionally allowing reflections happens not to reduce the count, but that coincidence must not be generalized.

**Extensions.**

- Use three named colors on three beads. Rotations give (27+3+3)/3=11 classes; including reflections gives (27+3+3+9+9+9)/6=10. All-three-color necklaces expose the difference.
- Explore longer binary necklaces with a fixed bead count. Rotation-cycle lengths determine fixed configurations, but derive the constraints before applying a formula.

**Satisfying stop.** A complete six-necklace catalog and a concrete explanation of why orbit sizes differ.

**Prior use.** Week 3 studies permutation return times; this family studies actions on colorings and unequal stabilizers. Repeated rotations are shared tools, but the counting question and proof are new.

**Sources.**

- [Thomas Judson, Abstract Algebra: Theory and Applications](https://judsonbooks.org/aata-files/aata-html/actions-section-burnsides-counting-theorem.html), §14.3 Burnside's Counting Theorem; supporting orbit-stabilizer discussion in §14.1. Inspection: full relevant theorem discussion; finite fixed counts checked directly.

