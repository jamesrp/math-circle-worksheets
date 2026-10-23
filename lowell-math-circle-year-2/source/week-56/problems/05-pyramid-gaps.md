+++
id = "w56.pyramid-gaps"
title = "The square pyramid: two kinds of corner"
grades = ["shared"]
route = "first"
page = "new"
kernel = 'The pyramid top leaves $120^\circ$ and each base corner $150^\circ$, the bigger gap; together $120^\circ+4\cdot150^\circ=720^\circ$.'
+++

## text
\renewcommand{\band}{Grades K--5}

## prompt
The square pyramid has one square face and four equilateral triangle faces. Which corner leaves the bigger gap, the top or a base corner? Find its total gap.

## text
\begin{center}\pyramid\hspace{1.2cm}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
 \draw[fill=blue!8] (0,0) rectangle (1,1);
 \foreach \x in {1.6,2.95,4.3,5.65}{\draw[fill=blue!8] (\x,0)--++(1,0)--++(-.5,.866)--cycle;}
\end{tikzpicture}\end{center}
\begin{center}\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|m{4.0cm}|>{\centering\arraybackslash}m{3.1cm}|>{\centering\arraybackslash}m{4.1cm}|>{\centering\arraybackslash}m{3.7cm}|}
\hline Vertex type & How many? & Face corners meeting there & Gap at each one\\\hline
Top &&&\\[55pt]\hline
Base corner &&&\\[55pt]\hline
\end{tabular}\end{center}
\blank{.6cm}\workbox{9.3}
