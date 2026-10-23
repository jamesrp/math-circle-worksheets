+++
id = "w58.cut-and-choose-guarantee"
title = "Why cut-and-choose is fair, and a cut at the colour join"
grades = ["shared"]
route = "first"
kernel = "An exact equal-own-value cut gives both people at least half and no envy; an equal-length cut can fail the cutter."
+++

## text
\newband{Grades 3--5}

## prompt
Two people use a splittable strip. The cutter makes pieces of exactly equal value to the cutter. The chooser takes a piece they value at least as much as the other. Must both people receive at least half of their own total value? Must neither person envy the other? Explain.

## text
\linearea{6}

Both people now use A's strip preferences: a whole red panel is worth 3, and a whole blue panel is worth 1. The cutter cuts at the join between the colors. Does this cut-and-choose trial pass both checks?

\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \strip{0}{2}
  \draw[dashed,line width=1pt] (90,-1) -- (90,29);
  \node[anchor=south,font=\small] at (90,30){cut};
\end{tikzpicture}
\end{center}
\linearea{4}
