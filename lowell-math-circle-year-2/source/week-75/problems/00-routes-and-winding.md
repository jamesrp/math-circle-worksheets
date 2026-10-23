+++
id = "w75.routes-and-winding"
kind = "setup"
title = "Yarn routes and their winding"
grades = ["4-5"]
route = ["first", "return"]
+++

## text
Keep the cylinder still. Each yarn route goes upward from A to B, with no self-crossings. Except at A and B, keep the yarn strictly between the rims. Leave spare yarn past both marks. Tape it at A and B; feed spare yarn through if needed, keeping the marked endpoints fixed. To build a different route, lift and re-lay the yarn, putting its ends back on the same marks.

Travel from A to B. At the seam, a rightward crossing counts $+1$; a leftward crossing counts $-1$. Add these to get the route's \emph{winding}.
\begin{center}\begin{tikzpicture}[x=.95in,y=.85in,font=\small,>=Stealth]
\draw[thick](0,0)rectangle(3,1);
\draw[dashed](0,0)--(0,1);\draw[dashed](3,0)--(3,1);
\draw[very thick,->](2.3,.2)--(3,.55);
\draw[very thick,->](0,.55)--(.65,.83);
\fill(2.3,.2)circle(2pt)node[below]{P};\fill(.65,.83)circle(2pt)node[above]{Q};
\draw[gray,dotted](0,.55)--(3,.55);
\node[left]at(0,.55){enter};\node[right]at(3,.55){exit};
\node at(1.5,-.4){Example: P to Q crosses rightward once. Count $+1$.};
\node at(1.5,-.72){Exit and entry stay at the same height.};
\end{tikzpicture}\end{center}
