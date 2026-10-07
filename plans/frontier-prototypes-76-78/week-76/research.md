# Week 76 mathematical design: substitution, hidden seams, and aperiodic order

## Recommendation

Use the Thue–Morse substitution A → AB, B → BA. The mathematical center should be **recovering hidden generations and using that recovery to rule out every repeating-unit length**, rather than copying a decorative strip. Equal-length substitution makes the proof accessible through pairing, odd/even shifts, and repeated halving. Fibonacci substitution is attractive but introduces unequal tile lengths or irrational frequencies into the cleanest nonperiodicity arguments; Thue–Morse gives a stronger elementary route here.

A defensible Grades 3–5 target is the full nonperiodicity proof below, with cropped-strip recognizability as the concrete investigation that makes the proof intelligible. Younger children can genuinely discover the seam invariant and prove the absence of three equal adjacent symbols, without being credited with the infinite argument.

## Definition and verified small data

Start with A; simultaneously replace every old symbol, never a newly produced symbol in the same round. The first rows are:

- A
- AB
- ABBA
- ABBABAAB
- ABBABAABBAABABBA
- ABBABAABBAABABBABAABABBAABBABAAB

Each row is a prefix of the next. Thus they specify an infinite one-sided word T. Its first-of-each-pair subsequence is T again; its second-of-each-pair subsequence is T with A and B exchanged. This is the substitution fixed-point definition, not an assertion inferred from inspecting a long sample. See Allouche–Shallit, §§2–3.3, especially Proposition 3; Shallit's slides 10–11 prove equivalence with the copy-and-complement construction.

A computation on the first 4,096 symbols checked:

- The six length-3 factors are AAB, ABA, ABB, BAA, BAB, BBA.
- The ten length-4 factors are AABA, AABB, ABAA, ABAB, ABBA, BAAB, BABA, BABB, BBAA, BBAB.
- ABA and BAB occur starting in both parities; every length-4 factor occurs in only one parity.
- Alternating runs have maximum length 4 in that sample.

These checks validate examples; the proofs below establish the infinite claims.

## Core proof: no eventual repeating unit

**Exact theorem:** There are no positive integers p and N such that T[n+p] = T[n] for every n ≥ N. This excludes periodicity even after discarding an arbitrary finite beginning.

An independently arranged seam proof, using the elementary identities documented in the references:

1. The true child-pairs are AB or BA, so their two symbols differ. Equal neighbors can occur only *between* child-pairs.
2. Every aligned four-symbol block is ABBA or BAAB, because these are the two second-generation children. Its middle neighbors agree. Therefore equal neighbors occur arbitrarily far along T.
3. If an eventual period p were odd, choose an equal pair far inside its repeating tail. Shifting that pair p places preserves its equal symbols but changes its alignment: it would now be a child-pair. Impossible.
4. If p = 2q is an eventual period, retain the first symbol of every true child-pair. This recovers T itself, and the shift of 2q symbols becomes a shift of q parent symbols. Thus q is an eventual period too.
5. Repeated halving of a positive integer eventually reaches an odd integer. Step 3 rules it out.

For children, this can be enacted with two copies of a strip, marked pair seams, proposed odd and even shifts, and a shrinking record of a hypothetical unit's size. The proof must ultimately address an arbitrary proposed size, rather than only the shifts tested physically.

## Cropped-strip recognizability: a substantial investigation

**Elementary entry theorem:** No AAA or BBB occurs. Every three consecutive positions contain one complete true child-pair, whose symbols differ.

**Five-symbol theorem:** No ABABA or BABAB occurs. Taking the first, third, and fifth symbols would produce three equal consecutive symbols in either T or its complemented copy. Hence every genuine five-symbol crop has equal neighbors. Their intervening gap must be a seam, fixing every other seam in that crop. End pieces may be incomplete pairs. Offner, §3, properties 4–6, explicitly supplies these local facts.

**Sharper result:** Four symbols suffice if children reason about the clipped end-pairs. Any crop with equal neighbors is already synchronized. For ABAB, the possible wrong alignment A | BA | B would require its three parent symbols to be BBB, because the initial A is the last half of BA and the terminal B is the first half of BA. That is forbidden. Similarly, BABA's wrong alignment forces AAA. Three symbols do not always suffice: ABA occurs at zero-indexed positions 3 and 10 in the 16-symbol row, with opposite alignments. Swan, Lemma 2.2(3)–(4), proves precisely this parity distinction.

This supports sustained child-controlled work: reconstruct erased seams, decide which partial parent letters are forced, decode cropped strips repeatedly, justify a smallest sufficient crop length, and compare competing reconstructions. Do not claim that recovering an interior pairing also reveals the absolute original position or the whole missing past.

## Useful contrast: recurring patches without a periodic whole

Repeated patches do occur: BB, BABA = BA·BA, and BAABBAAB = BAAB·BAAB are genuine factors. The sequence is therefore not square-free. The published stronger theorem is overlap-freeness, which implies cube-freeness, but neither stronger result is needed for the chosen nonperiodicity proof. A full overlap-free proof would be a separate ambitious extension, not a claim licensed merely by ruling out AAA and ABABA. See Shallit, slides 16–20, and Swan, Theorem 3.1.

Optional elementary recurrence proof: any observed patch lies in some generated row μ^k(A). Both next-generation superletters μ^(k+1)(A) and μ^(k+1)(B) contain that entire row. Consequently every aligned superblock at that scale contains the patch, so it reappears with bounded gaps. This supplies the positive sense of “order”: recurring local material together with a nonperiodic whole. Allouche–Shallit §4, Proposition 4, states uniform recurrence and failure of eventual periodicity.

## A particularly valuable false positive

The periodic strip ABBAABBAABBA… avoids AAA, BBB, ABABA, and BABAB. It even has only genuine Thue–Morse factors through length 7 (verified computationally; do not make this an unproved classroom premise). Thus the short prohibitions alone do not establish aperiodicity or characterize T.

Its claimed generation history exposes the problem:

ABBAABBA… → ABABAB… → AAAA… → impossible to divide into legal child-pairs.

This makes repeated decoding consequential: a strip can look right locally but fail at a higher generation. Inventing and exposing such impostors is a stronger investigation than making additional long strips. Allow a suitable crop or acknowledge the infinite periodic extension; a finite object's undecodable endpoint is not automatically a mathematical contradiction.

## Scope and design cautions

- Use “no finite unit repeats forever,” not “nothing ever repeats.”
- Explain that finite generation rows are certificates for finite examples; the nested rule defines the infinite object.
- Keep true pair alignment visible before erasing it. Arbitrary grouping from the left edge of a cropped strip can be wrong.
- The nonperiodicity proof needs the same self-similar rule at every generation. A single rule application to an arbitrary parent does not guarantee an aperiodic output.
- Distinguish the elementary no-triple theorem from the much stronger no-three-repeated-blocks theorem.
- Avoid implying an aperiodic *tile set*: these are labeled one-dimensional substitution words. The work is about inverse substitution, recognizability, and period obstructions, not geometric tiling or necklace equivalence.
- Physical materials can remain two-color counters, paper strips, pair sleeves, transparent shift overlays, and cropped excerpts. No geometric precision, binary notation, irrational numbers, or programming is required.
- Age feasibility is a curriculum judgment, not an empirical learning-outcomes claim. Grades 3–5 can own the finite lemmas; some groups will need support connecting arbitrary period sizes to the repeated-halving contradiction.

## Primary/author-hosted mathematical references

These are researcher-authored mathematical expositions with proofs, rather than popular summaries. They are not represented as the original 1906/1912 publications.

1. Richard G. Swan, **The Morse Sequence**, University of Chicago, 4 pages. Page 2, Lemma 2.2 and its factor inventory give fixed pairing, no triple, and unique parity from length 4; page 3, Theorem 3.1 gives the stronger overlap-free theorem. https://www.math.uchicago.edu/~swan/expo/Morse.pdf
2. Carl D. Offner, **Repetitions of Words and the Thue-Morse sequence**, University of Massachusetts Boston, 5 pages. §3, pages 2–3, properties 1–6 prove the even/odd subsequence identities, equal-pair parity, no triple, and an equal pair in every five-symbol window; Theorem 1 proves strong cube-freeness. https://www.cs.umb.edu/~offner/files/thue.pdf
3. Jean-Paul Allouche and Jeffrey Shallit, **The ubiquitous Prouhet-Thue-Morse sequence**, author-hosted survey, 16 pages. §§2–3.3 (pages 1–4), definition and substitution fixed point; §4, Proposition 4 (pages 4–5), uniform recurrence without ultimate periodicity. https://cs.uwaterloo.ca/~shallit/Papers/ubiq15.pdf
4. Jeffrey Shallit, **The Ubiquitous Thue-Morse Sequence**, author-hosted lecture, 55 slides. Slides 7–11: construction/equivalence; slides 16–20: complete overlap-free proof. The nonperiodicity proof proposed above avoids requiring that stronger theorem. https://cs.uwaterloo.ca/~shallit/Talks/green3.pdf


## Production status

This record supports an outline. Fresh student writer, independent adversarial and mathematical checks, revision, separate guide production, final page inspection and extracted-source reconstruction remain required. Research-stage computations check finite examples and do not replace independent verification of the eventual packet. Physical preparation and classroom piloting are unperformed.
