+++
id = "w54.exchange-rule"
title = "Exchanging rows and columns, with a worked example"
kind = "setup"
grades = ["shared"]
route = "first"
page = "new"
+++

## text
\beginpage{4--5}
\textat{0.6}{9.78}{Put the longest row first, with left edges aligned. To exchange rows and columns, make a new row as long as each column.}
\centerlabel{1.41}{9.02}{Rows}
\centerlabel{4.11}{9.02}{Read columns}
\centerlabel{6.84}{9.02}{New rows}
\rows{1.01}{8.61}{0.15}{5,3,3,1}
\arrowat{2.05}{3.08}{8.27}{exchange}{}
\rows{3.73}{8.61}{0.15}{5,3,3,1}
\foreach \n [count=\c from 0] in {4,3,3,1,1}{
 \pgfmathsetmacro{\xx}{3.73+\c*0.15}
 \draw[ink,line width=0.9pt] (\xx,8.61) rectangle ++(0.15,{-\n*0.15});
 \node[anchor=north,inner sep=0,font=\fontsize{10}{11}\selectfont] at ({\xx+0.075},7.91) {\n};
}
\arrowat{4.76}{5.78}{8.27}{rebuild}{}
\rows{6.55}{8.61}{0.15}{4,3,3,1,1}
