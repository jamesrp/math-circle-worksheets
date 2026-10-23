+++
id = "w83.cut-rules"
title = "Cutting rules and a worked cut"
grades = ["2-5"]
route = "first"
kind = "setup"
+++

## text
\begin{sheet}
\textat{232}{177}{Blue removes one blue (B) segment. Red removes one red (R) segment. All segments cut off from the ground disappear. Take turns; change one stalk per turn. If you cannot move, you lose.}
\node[font=\small] at (27,194) {Start};
\node[font=\small] at (89,194) {Red cuts R};
\node[font=\small] at (151,194) {Left on ground};
\ground{8}{119}{40}\stalk{23}{119}{B,R,B}
\node[anchor=north,font=\small] at (28,116) {ground};
\ground{70}{119}{40}\stalk{85}{119}{B}
\draw[RedEdge,dashed,line width=2pt] (85,141)--(85,163);
\node[anchor=west,inner sep=0pt,font=\small] at (88,152) {R};
\draw[line width=1.2pt] (80,148)--(90,158) (80,158)--(90,148);
\draw[BlueEdge,dashed,line width=2pt] (85,163)--(85,185);
\node[anchor=west,inner sep=0pt,font=\small] at (88,174) {B};
\draw[->,line width=1pt] (104,180)--(104,164);
\node[anchor=east,font=\footnotesize] at (109,161) {drops};
\ground{132}{119}{40}\stalk{147}{119}{B}
\draw[->,line width=1pt] (54,151)--(63,151);
\draw[->,line width=1pt] (116,151)--(125,151);
