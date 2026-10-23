+++
id = "w94.stretch-shift-rule"
title = "Stretch-and-shift machines"
grades = ["4-5"]
route = "first"
kind = "setup"
page = "new"
+++

## text
For Problems 3--4, a stretch-and-shift machine multiplies every input length by the same positive number, then adds the same fixed amount. Fractions are allowed; the added amount may be negative.

\begin{center}\begin{tikzpicture}[x=12mm,y=10mm,font=\small]
\node at(1.5,1.1){input: 3 units};
\foreach\i in{0,1,2}{\draw[fill=gray!15](\i,0)rectangle+(1,.6);}
\draw[->,thick](3.25,.3)--(4,.3);
\node at(6.55,1.1){stretch: $\times 1\frac12$};
\foreach\i in{0,1,2}{\draw[fill=gray!15](4.3+1.5*\i,0)rectangle+(1.5,.6);}
\node[below]at(6.55,0){$4\frac12$ units};
\draw[->,thick](9.05,.3)--(9.8,.3);
\node at(11.85,1.1){shift: subtract 1};
\draw[fill=gray!15](10.1,0)rectangle+(3.5,.6);
\node[below]at(11.85,0){report: $3\frac12$};
\end{tikzpicture}\end{center}
