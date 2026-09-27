# An adult-supported bridge for coprime divisibility

Prepared September 20, 2026, for the optional general proofs in [Week 4](week-04-redesign.md) and [Week 9](week-09-redesign.md). This is a suggested teaching scaffold, not evidence that children have proved the lemma. It uses subtraction and strips instead of assuming prime factorization or quoting Euclid's lemma.

## Readiness and preparation

Begin after a child can explain that a multiple of a positive whole number **a** consists of whole **a**-blocks, and that subtracting one multiple of **a** from another leaves a multiple of **a**. Use squared paper, drawn strips, or the existing counters. No extra printed sheet or cutting is required. Start with the numerical examples; the general proof additionally needs an adult discussion of common divisors and why a repeated subtraction process must finish.

Allow roughly five to ten minutes of the optional proof period. If that discussion is not yet accessible, stop at a proved numerical case and label the wider claim **conjectured** or **given as a theorem**. A correct table alone does not establish the general claim.

## Concrete launch: a 12-place ring with steps of 8

A return after **t** turns means that **8t** is a multiple of 12. Dividing all lengths by four gives the same question: is **2t** a multiple of 3?

Draw three equal strips of length **t**, totaling **3t**. Circle two strips, totaling **2t**. The whole three-strip row is always a multiple of 3. If the circled portion is also a multiple of 3, removing it leaves a multiple of 3. What is left? One strip, of length **t**. Thus **3 divides 2t only if 3 divides t**. Conversely, if t is a multiple of 3, twice t is too. The first positive possible t is 3, and three steps of 8 do return. This proves this numerical case for every t, not just the first few trials.

Have the child point to both the remaining strip and the reason it can still be grouped into threes. For a first concrete model choose t=3: the full row has nine squares, the removed row six, and the remainder three. The argument uses a strip of unspecified length t; the sample drawing illustrates it rather than proving all lengths by itself.

## A second example: 5 divides 3t

Draw two rows of three t-strips. Together they have length **6t**. Remove five t-strips, of length **5t**, leaving one t-strip. If **3t** is a multiple of 5, its double **6t** is too; **5t** always is. Therefore the remainder **t** is a multiple of 5.

Ask how we found the recipe **2×3−5=1**. Start with strips of lengths 5 and 3: remove 3 from 5 to get 2; remove that 2 from 3 to get 1. Reading back gives **1=3−(5−3)=2×3−5**. Repeat those same removals on lengths 5t and 3t. Each surviving piece is a multiple of 5, so the final length t is too.

## The general argument: subtraction keeps common divisors

For positive integers **a,b** with no common divisor greater than 1, suppose **a divides bt**. Work with two parallel pairs of strips:

| Base lengths | Scaled lengths | What the adult asks |
| --- | --- | --- |
| a and b | at and bt | Why are both scaled lengths multiples of a? |
| Replace the larger length by its difference with the smaller | Make the identical subtraction on the scaled pair | Why are both remaining scaled lengths still multiples of a? |
| Repeat until the two positive base lengths agree | Each scaled length stays t times its matching base length | Why must this process finish? What can the final base length be? |

The sum of the two positive base lengths decreases at each unequal step, so the process finishes with two equal positive lengths c. A number divides both x and y exactly when it divides y and x−y (when x>y), because x can be put back by adding. Thus the common divisors never change. At the end c divides both original lengths; as a and b are coprime, c=1. The scaled process therefore ends with length **t**. It has remained a multiple of **a** throughout, proving **a divides t**.

The converse is immediate: if a divides t, a also divides bt. We have established:

> If positive integers a and b are coprime, then a divides bt exactly when a divides t.

This is the coprime cancellation lemma, proved here by the subtraction form of the Euclidean algorithm. We do not cancel arbitrary factors in modular arithmetic: for example, 6 divides 2×3, but 6 does not divide 3.

## Where each week uses the result

**Week 4:** for a nonzero shift k on n places, write d=gcd(n,k), n=da, k=db. The reduced a,b are coprime. Return at t means n divides kt, equivalently a divides bt. The lemma says exactly that a divides t, so the first positive return is **a=n/d**. Every starting position has the same length; disjoint loops partition n positions, giving **d loops**. Handle k=0 separately: every position is fixed and returns after one turn; this also fits gcd(n,0)=n. The finite 12-ring investigation remains a satisfying endpoint if the general subtraction argument is not attempted.

**Week 9:** write width w=ga and height h=gb with coprime a,b. A positive common multiple L of w and h has the form **L=gaq**. Since gb divides L, b divides aq; the lemma gives b divides q. The smallest possible positive q is b, and **L=gab** is indeed a common multiple. This proves the least-common-multiple formula. The earlier-corner argument is a separate useful route: if the whole-room counts m,n at a first corner had a common divisor d>1, distance L/d would already give whole counts m/d,n/d and an earlier corner. It supports reduced parity and bounce arguments before the product formula is proved.

## Teaching-source boundary and recording

The choice to use strips, offer numerical stopping points, and make the general lemma optional is our adaptation. Relevant lessons reread for this revision: *Math Circle by the Bay*, preface viii–x, on manipulatives, varied pace, repeated explanation, and reserve problems; Rozhkovskaya, *Math Circles for Elementary School Students*, Lesson 3, “At the lesson,” item 1 (`OEBPS/part0013.xhtml`), on attempts and explanations before a table, and Lesson 8, item 2 (`part0018.xhtml`), on copying slowing the activity. Neither source is being cited as the source of this divisibility proof.

Record separately whether the child explained the 3-and-2 case, the 5-and-3 case, the general subtraction lemma, and the application. Use **tried**, **conjectured**, **verified these cases**, **proved**, or **given as a theorem**, as appropriate.
