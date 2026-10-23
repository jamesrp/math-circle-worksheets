+++
id = "w75.twist-rule"
kind = "setup"
title = "What a twist does"
grades = ["4-5"]
route = "return"
page = "new"
+++

## text
A $+$ twist moves points rightward: none at the bottom, a quarter-turn at the first dotted line, a half-turn at the middle, three-quarter-turns at the next line, and one full turn at the top. Between lines, the shift grows evenly. A $-$ twist uses the same shifts leftward.

Every rim point ends where it started. Draw the changed route and re-lay the yarn to match. The paper cylinder stays still.
\begin{center}\begin{tikzpicture}[x=1.35in,y=1in,font=\small,>=Stealth]
\draw[thick](0,0)rectangle(2,1);\draw[dashed](1,0)--(1,1);
\foreach\h in {.25,.5,.75}{\draw[black!55,dotted](0,\h)--(2,\h);}
\draw[gray,very thick](.25,0)--(.25,1);
\draw[very thick](.25,0)--(1.25,1);
\foreach\h in {.25,.5,.75,1}{\draw[->](.25,\h)--(.25+\h,\h);}
\fill(.25,0)circle(2pt)node[below]{P};\fill(.25,1)circle(2pt)node[above]{Q};\fill(1.25,1)circle(2pt)node[above]{Q};
\node at(.5,1.34){copy 0};\node at(1.5,1.34){copy 1};
\node at(1,-.38){Example: one $+$ twist on a straight route from P to Q.};
\end{tikzpicture}\end{center}
