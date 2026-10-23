+++
id = "w84.coach-dolls"
title = "Coach three dolls with each deal"
grades = ["2-5"]
route = "first"
kernel = "With the announcement, k blue dolls first prove blue in round k."
+++

## prompt
Coach three dolls with each of these deals. Find their replies in each round until every blue doll can show PROVE BLUE. Start each deal with the eight headband cards, then use the shared announcement.

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
 \foreach \x/\name in {0/1,5.7/2,11.4/3}{
  \draw[rounded corners=3pt] (\x,0) rectangle ++(5.25,-4.0);
  \node[font=\small] at (\x+2.625,-0.45) {Deal \name};
  \foreach \i in {1,2,3}{\node[font=\small] at ({\x+0.7+1.3*(\i-1)},-1.9) {\i};}}
 \hatdisk{0.7}{-1.28}{1}\hatdisk{2}{-1.28}{0}\hatdisk{3.3}{-1.28}{0}
 \hatdisk{6.4}{-1.28}{1}\hatdisk{7.7}{-1.28}{1}\hatdisk{9}{-1.28}{0}
 \hatdisk{12.1}{-1.28}{1}\hatdisk{13.4}{-1.28}{1}\hatdisk{14.7}{-1.28}{1}
\end{tikzpicture}
\end{center}
