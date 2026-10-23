+++
id = "w81.long-game"
title = "Make the game last"
grades = ["2-5"]
route = "return"
kernel = "From an empty first bucket and one counter in the second, refilling the first with M counters makes a game of exactly M + 1 moves, so no finite number bounds the length."
+++

## prompt
Start with an empty first bucket and one counter in the second. Work together to make a game last at least 10 moves, then 30 moves, then 100 moves. Can you beat any finite number someone names?

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
 \dotsbucket{0}{0}{0}{1}\dotsbucket{2}{0}{1}{2}
\end{tikzpicture}
\end{center}
