+++
id = "w43.twenty-seven"
title = "Twenty-seven stories, six rows"
grades = ["2-3", "4-5"]
route = "return"
page = "same"
kernel = "27 equally likely stories cannot split equally among 6 rows, since 6 does not divide 27; the counts are 4, 5, 5, 5, 4, 4."
+++

## prompt @20 [2-3]
There are 27 equally likely three-ticket stories. Could this rule give all six rows the same chance?

## prompt @3 [4-5]
Can this rule give all six orders the same chance? Find an exact reason; a short run of random shuffles cannot settle the question.

## figure [2-3]
lines(23, 1)

## figure [4-5]
answer_box(6, 8)

## key [2-3]
No. There are $3 \times 3 \times 3 = 27$ equally likely histories. If all six rows were equally likely, each would need the same whole number of histories. But six equal integer counts cannot sum to 27. The exact distribution below is for the facilitator; enumeration is not required of children.\par
\begin{tabular}{lcccccc}\toprule Final order & ABC & ACB & BAC & BCA & CAB & CBA\\\midrule
History count & 4 & 5 & 5 & 5 & 4 & 4\\\bottomrule\end{tabular}\par
The fact that there are collisions alone does not prove unfairness: all outputs might have had the same number of histories. The unequal allocation forced by 27 versus 6 supplies the proof.

## key [4-5]
No. The 27 equally likely histories cannot be divided into six equal-sized output classes. Exact counts for ABC, ACB, BAC, BCA, CAB, CBA are 4, 5, 5, 5, 4, 4. The argument relies on equiprobable histories; merely knowing a total number of possible histories would not suffice if they had unequal weights.
