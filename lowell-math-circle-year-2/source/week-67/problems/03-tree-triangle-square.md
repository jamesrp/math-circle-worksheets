+++
id = "w67.tree-triangle-square"
title = "A tree, a triangle and a square"
grades = ["3-5"]
route = "return"
page = "new"
kernel = "A tree has exactly one meeting dot, the centre of the three paths; a triangle has none; on the square only home B works."
+++

## prompt
Find every meeting dot that works for A, B, and C on each map. If none works, explain why every possible dot fails. Each line between neighboring dots is one road, even when drawn longer.

## text
\begin{center}
\begin{tikzpicture}[x=1.45cm,y=1.15cm]
\foreach \n/\x/\y in {a/0/0,u/1/0,v/2/0,w/3/0,b/4/1,c/2/2,t/2/1,s/3/-1,r/4/-1,q/0/1}{\coordinate (\n) at (\x,\y);}
\draw[line width=1pt] (a)--(u)--(v)--(w)--(b) (v)--(t)--(c) (w)--(s)--(r) (u)--(q);
\foreach \n in {a,u,v,w,b,c,t,s,r,q}\fill (\n) circle (2.5pt);
\home{0}{0}{A}\home{4}{1}{B}\home{2}{2}{C}
\end{tikzpicture}
\end{center}
\vspace{.2in}
\begin{center}
\begin{tikzpicture}[x=1.25cm,y=1.25cm]
\draw[line width=1pt] (0,0)--(3,0)--(1.5,2.5)--cycle;
\home{0}{0}{A}\home{3}{0}{B}\home{1.5}{2.5}{C}
\end{tikzpicture}\hspace{1.0in}
\begin{tikzpicture}[x=1.2cm,y=1.2cm]
\draw[line width=1pt] (0,0)--(3,0)--(3,3)--(0,3)--cycle;
\fill (0,3) circle (2.5pt);\home{0}{0}{A}\home{3}{0}{B}\home{3}{3}{C}
\end{tikzpicture}
\end{center}
\vspace{.35in}\rule{\linewidth}{.4pt}\par\vspace{.35in}\rule{\linewidth}{.4pt}\par\vspace{.35in}\rule{\linewidth}{.4pt}
