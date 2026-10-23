+++
id = "w98.exposed-sides"
title = "Exposed sides before and after an addition"
grades = ["4-5"]
route = "return"
page = "new"
kernel = "An addition touching k filled squares changes the exposed sides by 4 - 2k, never more than 0."
+++

## prompt
An exposed side is a side of a filled square next to an empty square or the outside of the board. Count the exposed sides before and after filling the circled square in each picture. Can any legal addition increase the number of exposed sides? Explain.

## text
\fill[black!11] (35,90) rectangle ++(20,20);
\fill[black!11] (15,110) rectangle ++(20,20);
\draw[line width=0.65pt] (15,90) rectangle ++(60,60);
\draw[line width=0.45pt] (35,90) -- ++(0,60);
\draw[line width=0.45pt] (55,90) -- ++(0,60);
\draw[line width=0.45pt] (15,110) -- ++(60,0);
\draw[line width=0.45pt] (15,130) -- ++(60,0);
\fill (45.0,100.0) circle[radius=2.7mm];
\fill (25.0,120.0) circle[radius=2.7mm];
\draw[line width=0.9pt] (45.0,120.0) circle[radius=4.4mm];
\node[anchor=north west,inner sep=0pt,text width=60mm,align=left,font=\sffamily\fontsize{11.5}{15}\selectfont] at (15,160) {Before: \rule{16mm}{0.3pt}};
\node[anchor=north west,inner sep=0pt,text width=60mm,align=left,font=\sffamily\fontsize{11.5}{15}\selectfont] at (15,172) {After: \rule{19mm}{0.3pt}};
\fill[black!11] (98,90) rectangle ++(20,20);
\fill[black!11] (78,110) rectangle ++(20,20);
\fill[black!11] (118,110) rectangle ++(20,20);
\draw[line width=0.65pt] (78,90) rectangle ++(60,60);
\draw[line width=0.45pt] (98,90) -- ++(0,60);
\draw[line width=0.45pt] (118,90) -- ++(0,60);
\draw[line width=0.45pt] (78,110) -- ++(60,0);
\draw[line width=0.45pt] (78,130) -- ++(60,0);
\fill (108.0,100.0) circle[radius=2.7mm];
\fill (88.0,120.0) circle[radius=2.7mm];
\fill (128.0,120.0) circle[radius=2.7mm];
\draw[line width=0.9pt] (108.0,120.0) circle[radius=4.4mm];
\node[anchor=north west,inner sep=0pt,text width=60mm,align=left,font=\sffamily\fontsize{11.5}{15}\selectfont] at (78,160) {Before: \rule{16mm}{0.3pt}};
\node[anchor=north west,inner sep=0pt,text width=60mm,align=left,font=\sffamily\fontsize{11.5}{15}\selectfont] at (78,172) {After: \rule{19mm}{0.3pt}};
\fill[black!11] (161,90) rectangle ++(20,20);
\fill[black!11] (141,110) rectangle ++(20,20);
\fill[black!11] (181,110) rectangle ++(20,20);
\fill[black!11] (161,130) rectangle ++(20,20);
\draw[line width=0.65pt] (141,90) rectangle ++(60,60);
\draw[line width=0.45pt] (161,90) -- ++(0,60);
\draw[line width=0.45pt] (181,90) -- ++(0,60);
\draw[line width=0.45pt] (141,110) -- ++(60,0);
\draw[line width=0.45pt] (141,130) -- ++(60,0);
\fill (171.0,100.0) circle[radius=2.7mm];
\fill (151.0,120.0) circle[radius=2.7mm];
\fill (191.0,120.0) circle[radius=2.7mm];
\fill (171.0,140.0) circle[radius=2.7mm];
\draw[line width=0.9pt] (171.0,120.0) circle[radius=4.4mm];
\node[anchor=north west,inner sep=0pt,text width=60mm,align=left,font=\sffamily\fontsize{11.5}{15}\selectfont] at (141,160) {Before: \rule{16mm}{0.3pt}};
\node[anchor=north west,inner sep=0pt,text width=60mm,align=left,font=\sffamily\fontsize{11.5}{15}\selectfont] at (141,172) {After: \rule{19mm}{0.3pt}};
\draw[black!35,line width=0.3pt] (15,200) -- ++(186,0);
\draw[black!35,line width=0.3pt] (15,218) -- ++(186,0);
\draw[black!35,line width=0.3pt] (15,236) -- ++(186,0);
\draw[black!35,line width=0.3pt] (15,254) -- ++(186,0);
