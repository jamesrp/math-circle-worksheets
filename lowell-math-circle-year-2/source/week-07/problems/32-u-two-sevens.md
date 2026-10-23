+++
id = "w07.u-two-sevens"
title = "Two piles of 7"
grades = ["4-5"]
route = "return"
page = "new"
+++

## prompt
Now there are two piles. On your turn, take 1 or 2 counters from one pile,
whichever you choose. Whoever takes the last counter on the table wins.
Play piles of 7 and 7. Would you rather go first or second? Explain why
your way of playing wins whatever your opponent does.

## text
\vspace{0.35in}
\begin{tikzpicture}[x=1in,y=1in]
  \foreach \k in {1,...,7}{\counter{(\k-1)*0.47+0.25}{0}}
  \foreach \k in {1,...,7}{\counter{(\k-1)*0.47+4.0}{0}}
\end{tikzpicture}
\vspace{1.75in}
\end{problem}
