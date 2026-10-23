+++
id = "w82.three-and-three"
title = "Three kids and three kids"
grades = ["3-5"]
route = "first"
kernel = "Three kids and three kids have 3 x 2 x 1 = 6 complete matches, and only R1-B1, R2-B2, R3-B3 keeps order."
+++

## prompt
Find every match between these two class lines. Which matches keep order? Use cards and yarn to test your matches.

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\foreach \x/\n in {2/1,7.2/2,12.4/3}{
 \longcard{\x}{0}{R\n}{queueR}
 \longcard{\x}{-3.0}{B\n}{queueB}
}
\end{tikzpicture}
\end{center}
\vspace{0.6cm}
\ruleline
\vspace{0.8cm}
\ruleline
