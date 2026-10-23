+++
id = "w39.removal-order"
title = "Does the removal order matter?"
grades = ["2-3", "4-5"]
route = { "2-3" = "first", "4-5" = "return" }
page = { "2-3" = "same", "4-5" = "new" }
kernel = "The final route does not depend on which reversal is removed first, on any road map; a left-to-right stack proves it."
+++

## prompt @189 [2-3]
Remove different first detours from the recorded trip below. Can two removal orders end differently?

## prompt @27 [4-5]
Shorten each recorded trip in different orders. Can the choice of first reversal ever change the final route on any road map? Explain, or give a counterexample.

## figure [2-3]
routes(221, ['ABABCBADCDA']) + blank(16, 243, 180, 13)

## figure [4-5]
graph(54, 68, 38, RING, REDGES) + routes(159, ['ABABCBADCDA', 'ABADCBC', 'ABCDABCBA']) + blank(16, 225, 180, 30)

## key [2-3]
ABABCBADCDA always reduces to A. One order is:\\
ABABCBADCDA $\to$ ABCBADCDA $\to$ ABADCDA $\to$ ADCDA $\to$ ADA $\to$ A.\\
Another begins by removing the B$\to$C$\to$B excursion:\\
ABABCBADCDA $\to$ ABABADCDA $\to$ ABADCDA $\to$ ADCDA $\to$ ADA $\to$ A.\\
Each arrow deletes one adjacent same-road reversal. Different intermediate routes do not imply different final routes.

## key [4-5]
The three printed routes reduce to A, ADC, and ABCDA, respectively. The page 6 proof shows no choice of first reversal can change the final reduced edge path on any graph. Illustrative reductions for the last two:\\
ABADCBC $\to$ ADCBC $\to$ ADC.\\
ABCDABCBA $\to$ ABCDABA $\to$ ABCDA.\\
For the first, see the two distinct deletion orders on page 4. These computations illustrate the theorem; they are not its proof.
