+++
id = "w81.forever"
title = "Can a game go on forever?"
grades = ["2-5"]
route = "return"
kernel = "Every game ends, from two buckets or three: the rightmost bucket never refills, so it stops changing, and the game left in the other buckets ends too."
+++

## text
\vspace{4pt}

## prompt
Start from each picture. Can you agree on moves that keep the game going forever? If you think every game ends, however big the refills, explain why.

## text
\begin{center}
\begin{tabular}{@{}c@{\hspace{.75in}}c@{}}
\begin{tikzpicture}[x=1cm,y=1cm]
 \dotsbucket{0}{0}{0}{1}\dotsbucket{2}{0}{3}{2}
\end{tikzpicture} & \smallstart{1}{1}{1}
\end{tabular}
\end{center}
\vspace{5pt}
\begin{tikzpicture}
 \draw[black!35] (0,0) rectangle (17.5,2.15);
\end{tikzpicture}
