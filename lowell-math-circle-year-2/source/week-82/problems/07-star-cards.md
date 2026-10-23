+++
id = "w82.star-cards"
kind = "setup"
title = "Stars and after-every-kid panels"
grades = ["3-5"]
route = ["first", "return"]
page = "new"
+++

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\foreach \x in {0,4.1,8.2,12.3}{
 \draw[dashed,gray] (\x,0) rectangle ++(3.65,-2.8);
 \node[draw,line width=0.8pt,rounded corners=3pt,minimum width=3.25cm,minimum height=2.4cm,font=\Huge] at (\x+1.825,-1.4) {$\bigstar$};
}
\foreach \y in {-4.2,-7.1,-10.0}{
 \draw[dashed,gray] (-0.1,\y) rectangle ++(16.0,-2.25);
 \node[draw,rounded corners=3pt,align=center,minimum width=15.5cm,minimum height=1.8cm] at (7.9,\y-1.125) {This kid comes after EVERY kid\\in the earlier row.};
}
\foreach \y in {-12.9,-15.8}{
 \draw[dashed,gray] (-0.1,\y) rectangle ++(16.0,-2.25);
 \node[draw,rounded corners=3pt,align=center,minimum width=15.5cm,minimum height=1.8cm] at (7.9,\y-1.125) {This whole row starts after EVERY kid\\in the earlier row.};
}
\end{tikzpicture}
\end{center}
