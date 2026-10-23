+++
id = "w77.saved-loops-and-gone"
kind = "setup"
title = "Saved loops, filled tiles and the token test"
grades = ["4-5"]
route = ["first", "return"]
+++

## text
\textat{0}{0}{18.2}{Keep track of a loop while you add edges and cover triangles with tiles. When do the filled tiles fill your saved loop?}
\smallat{0}{1.65}{18.2}{A loop follows edges back to its starting dot without repeating an edge. Save its edge list; keep that list unchanged as the board grows. Here the saved loop is the square's outside rim: AB, BC, CD, DA.}
\foreach \x/\stage/\caption in {0/0/{Build the rim},4.7/1/{Add the diagonal},9.4/2/{Fill one half},14.1/3/{Fill both halves}} {
 \begin{scope}[shift={(\x,4.25)}]
 \ifnum\stage>1 \fill[black!20] (0,0)--(3,0)--(3,3)--cycle;\fi
 \ifnum\stage>2 \fill[black!20] (0,0)--(3,3)--(0,3)--cycle;\fi
 \draw[line width=1.5pt] (0,0)--(3,0)--(3,3)--(0,3)--cycle;
 \ifnum\stage>0 \draw[line width=1pt] (0,0)--(3,3);\fi
 \foreach \a/\b/\v/\pos in {0/0/A/above left,3/0/B/above right,3/3/C/below right,0/3/D/below left}{\fill (\a,\b) circle(1.7pt);\node[\pos,inner sep=2pt,font=\small] at (\a,\b){\v};}
 \node[align=center,font=\fontsize{10}{12}\selectfont,text width=3.5cm] at (1.5,4.0){\caption};
 \end{scope}
}
\smallat{0}{9.0}{18.2}{One filled half does not fill the saved square rim. Both filled halves together do: their shared diagonal is inside, leaving the square rim as their outside boundary. We say the saved loop is \textbf{gone} when filled tiles have that loop as their combined boundary. The edges are still there!}
\smallat{0}{11.4}{18.2}{Use only printed edge places. Add pieces and keep them during a build. A partner checks that all three edges are in place before a triangle is filled. Dashed lines show edge places; solid lines are already present. AB and BA name the same edge.}
\smallat{0}{13.65}{18.2}{Here is a token test for a saved triangular loop. Copy its edge tokens, add the three edge tokens of the filled tile, then remove matching pairs. Nothing remains, so this loop is gone. Only test tokens are removed, never board edges or the saved list.}
\begin{scope}[shift={(.4,16.35)}]
 \fill[black!18] (0,1.4)--(1.8,1.4)--(.9,0)--cycle;
 \draw[line width=1pt] (0,1.4)--(1.8,1.4)--(.9,0)--cycle;
 \node[below left,inner sep=3pt] at (0,1.4) {X};\node[above,inner sep=3pt] at (.9,0) {Y};\node[below right,inner sep=3pt] at (1.8,1.4) {Z};
\end{scope}
\token{3.1}{16.9}{XY}{i1}\token{4.1}{16.9}{YZ}{i2}\token{5.1}{16.9}{XZ}{i3}
\smallat{2.7}{18.1}{3.4}{saved loop}
\draw[-{Stealth[length=2mm]},line width=.8pt] (5.8,17.35)--(7.2,17.35);
\token{8.1}{16.9}{XY}{a}\token{9.1}{16.9}{YZ}{b}\token{10.1}{16.9}{XZ}{c}
\token{8.1}{17.7}{XY}{d}\token{9.1}{17.7}{YZ}{e}\token{10.1}{17.7}{XZ}{f}
\foreach \n in {a,b,c,d,e,f}{\draw[line width=.8pt] (\n.south west)--(\n.north east);}
\smallat{7.4}{18.5}{4.5}{add filled XYZ;\newline cancel each pair}
\draw[-{Stealth[length=2mm]},line width=.8pt] (11,17.35)--(12.5,17.35);
\node[draw=black!40,minimum width=3.6cm,minimum height=1.1cm,font=\small] at (14.75,17.35){no tokens left};
\smallat{0}{20.3}{18.2}{For any saved loop, you may use any selection of the currently filled triangles in this test, each at most once. The loop is gone if some selection leaves no tokens; otherwise it survives.}
