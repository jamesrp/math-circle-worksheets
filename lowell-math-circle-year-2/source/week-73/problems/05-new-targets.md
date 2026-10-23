+++
id = "w73.new-targets"
title = "Smallest worst stretch for new target rectangles"
grades = ["4-5"]
route = "return"
page = "new"
kernel = "For a W-by-H target the least worst stretch is max(W/4, H), attained by (Wx/4, Hy) and forced by a pair across the deciding direction."
+++

## prompt
Your partner chooses one of these new rectangles. Move the whole 4-by-1 sheet onto it, keeping the named sides. Find the smallest possible worst stretch. Give a rule for the whole sheet and find a pair that no legal rule can stretch less. Swap jobs for another rectangle.

## text
\begin{center}\begin{tikzpicture}[x=.6in,y=.6in,font=\small,>=Stealth]
\draw[thick](0,0)rectangle(4,1);\node at(2,-.38){4 by 1};\node at(2,1.3){top};\node[rotate=90]at(-.3,.5){left};
\draw[->](4.4,.5)--(5.1,.5);
\draw[thick](5.6,-.5)rectangle(11.6,1.5);\node at(8.6,-.88){6 by 2};\node at(8.6,1.8){top};\node[rotate=90]at(5.3,.5){left};
\end{tikzpicture}\end{center}
Smallest worst stretch: \rule{.7in}{.3pt}\quad Rule and unavoidable pair:
\answerline
\begin{center}\begin{tikzpicture}[x=.6in,y=.6in,font=\small,>=Stealth]
\draw[thick](0,0)rectangle(4,1);\node at(2,-.38){4 by 1};\node at(2,1.3){top};\node[rotate=90]at(-.3,.5){left};
\draw[->](4.4,.5)--(5.1,.5);
\draw[thick](6,-1)rectangle(8,2);\node at(7,-1.38){2 by 3};\node at(7,2.3){top};\node[rotate=90]at(5.7,.5){left};
\end{tikzpicture}\end{center}
Smallest worst stretch: \rule{.7in}{.3pt}\quad Rule and unavoidable pair:
\answerline
\vspace{.13in}
