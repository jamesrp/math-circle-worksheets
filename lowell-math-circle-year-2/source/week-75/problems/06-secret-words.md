+++
id = "w75.secret-words"
title = "Secret twist words"
grades = ["4-5"]
route = "return"
kernel = "Each twist adds $+1$ or $-1$ to the winding, so words with the same signed sum have the same effect, and the shortest equal word has the sum's absolute value as its length."
+++

## prompt
Start with winding 0. Choose a secret word of two to four $+$ and $-$ twists. Make its final route. Your partner tries to make a route with the same winding using the fewest twists. Reveal your word and swap jobs. Which words have the same effect?

## text
\begin{center}\begin{tikzpicture}[x=.78in,y=1.2in,font=\footnotesize]
\draw[thick](-4.5,0)rectangle(4.5,1);
\foreach\k in {-3.5,-2.5,...,3.5}{\draw[dashed](\k,0)--(\k,1);}
\foreach\h in {.25,.5,.75}{\draw[black!55,dotted](-4.5,\h)--(4.5,\h);}
\foreach\k/\l in {-4/\textminus4,-3/\textminus3,-2/\textminus2,-1/\textminus1,0/0,1/1,2/2,3/3,4/4}{\fill(\k,1)circle(1.5pt);\node[above]at(\k,1){B, copy \l};}
\fill(0,0)circle(2pt)node[below]{A, start};
\end{tikzpicture}\end{center}
\vspace{.1in}
\par\begin{tabular}{@{}p{.35\linewidth}p{.25\linewidth}p{.28\linewidth}@{}}
Secret word & Ending winding & Shortest word\\\hline
 & & \\[.28in]\hline
 & & \\[.28in]\hline
 & & \\[.28in]\hline
\end{tabular}\par
\vspace{.12in}
