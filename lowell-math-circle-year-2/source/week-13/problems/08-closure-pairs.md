+++
id = "w13.closure-pairs"
title = "Every pair of closing arrows on the bowtie"
grades = ["K-1", "2-3"]
route = { "K-1" = "return", "2-3" = "first" }
kernel = "Exactly eight pairs stop all travel: one half of the bowtie must be blocked completely, with one closure on each of its two branches."
+++

## prompt [K-1]
Stop every route with two markers. Find every different pair of arrows that works.

## prompt [2-3]
Find every pair of arrows you can close to stop all travel on this board. Explain how you know your list is complete.

## figure [K-1]
k1_closure_pairs()

## figure [2-3]
closure_pairs_23()

## key
All eight pairs of closing arrows on the bowtie are below. Here brackets mean “choose one from each listed pair of alternatives.” Before C, choose one from \{sA,AC\} and one from \{sB,BC\}. After C, choose one from \{CD,Dt\} and one from \{CE,Et\}.
\begin{center}\begin{tabular}{ll}\toprule Before C & After C\\\midrule
\{sA,sB\} & \{CD,CE\}\\
\{sA,BC\} & \{CD,Et\}\\
\{AC,sB\} & \{Dt,CE\}\\
\{AC,BC\} & \{Dt,Et\}\\\bottomrule\end{tabular}\end{center}
Completeness: if a path from s to C and a path from C to t both survive, concatenate them to get a whole route. So at least one half must be entirely blocked. Each half has two independent branches; blocking it with exactly two arrows requires one closure on each branch. A mixed pair with one arrow on each half cannot block either half.

## key [K-1]
Exactly eight pairs; use the list and completeness proof on page 6. The final page has a large working board and eight small recording copies. Mark a different successful pair on each; a marker rearrangement alone does not preserve the record.

## hints
Hint ladder: cover the right half temporarily; ask what it takes to stop reaching C; then repeat on the other half.

## hints [K-1]
Hint: check that two marked arrows belong to the same pair before comparing records.
