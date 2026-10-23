+++
id = "w97.odd-prime-rule"
title = "A rule for odd primes"
grades = ["3-5"]
route = "return"
page = "new"
kernel = "For an odd prime $p$ there are $(p+1)/2$ outputs counting 0, because $p$ divides $(x-y)(x+y)$ only when $x=y$ or $x+y=p$; 8, 9 and 15 break the rule."
+++

## prompt
Compare bundle sizes 3, 5, 7 and 11. Each time, use inputs from 0 to one less than the bundle size. Find a rule connecting the bundle size to the number of different outputs that occur. Count output 0 too. These bundle sizes are odd primes: their only positive divisors are 1 and themselves. Can you explain why your rule works for every odd prime? Does it also work for 8, 9 or 15?

## text
\begin{center}
\support{0}{0}\quad\support{1}{1}\quad\support{2}{4}\\[8pt]
\support{3}{9}\quad\support{4}{16}\quad\support{5}{25}\\[8pt]
\support{6}{36}\quad\support{7}{49}\quad\support{8}{64}\\[8pt]
\support{9}{81}\quad\support{10}{100}
\end{center}
\blank{10.9}
