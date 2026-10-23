+++
id = "w66.rules"
kind = "setup"
title = "Moves, partner jobs and the R-then-F example"
grades = ["3-5"]
route = ["first", "return"]
+++

## text
One move is \textbf{L}: walk left one place, \textbf{R}: walk right one place, or \textbf{F}: flip the lamp under the walker. $\circ$ is off, $\bullet$ is on, and $\blacktriangledown$ is the walker.

One partner moves the walker. The other flips the lamp, only after pointing to the walker's place. Write one letter per move. Swap jobs between targets.

\begin{center}
\begin{tikzpicture}[x=.74cm,y=.74cm,font=\small]
\foreach \s/\p/\lit in {0/-2/9,5/-1/9,10/-1/-1}{
\begin{scope}[shift={(\s,0)}]
\draw (-2,0)--(0,0);
\foreach \i in {-2,-1,0}{\draw[fill=white] (\i,0) circle (.12);\node[below=5pt] at (\i,0){\i};}
\ifnum\lit<2 \fill (\lit,0) circle (.12);\fi
\fill (\p,.4)--++(-.13,.22)--++(.26,0)--cycle;
\end{scope}}
\draw[-{Latex}] (1,.2)--node[above]{R}(2.7,.2);
\draw[-{Latex}] (6,.2)--node[above]{F}(7.7,.2);
\node at (-1,-1.3){start};\node at (4,-1.3){after R};\node at (9,-1.3){after RF};
\end{tikzpicture}
\end{center}
