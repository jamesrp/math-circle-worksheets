+++
id = "w98.rules"
kind = "setup"
title = "Rules and a worked 2-by-3 example"
grades = ["2-3", "4-5"]
route = ["first", "return"]
+++

## text
\node[anchor=north west,inner sep=0pt,text width=186mm,align=left,font=\sffamily\fontsize{11.5}{14.6}\selectfont] at (15,27) {Seeds are the squares filled at the start. Put counters on them. Add a counter to an empty square when at least two squares sharing its sides are filled. Your partner points to two filled neighbors before each addition. Counters stay put. Stop when no more can be added. Diagonal touches do not count. Opposite edges do not meet; there are no squares outside the board.};
\node[anchor=north west,inner sep=0pt,text width=186mm,align=left,font=\sffamily\fontsize{11.5}{14}\selectfont] at (15,62) {Mark seeds with $\bullet$ and added squares with $+$.};
\fill[black!11] (24,86) rectangle ++(10,10);
\fill[black!11] (34,86) rectangle ++(10,10);
\fill[black!11] (24,76) rectangle ++(10,10);
\draw[line width=0.65pt] (24,76) rectangle ++(30,20);
\draw[line width=0.45pt] (34,76) -- ++(0,20);
\draw[line width=0.45pt] (44,76) -- ++(0,20);
\draw[line width=0.45pt] (24,86) -- ++(30,0);
\fill (29.0,81.0) circle[radius=1.45mm];
\fill (29.0,91.0) circle[radius=1.45mm];
\fill (39.0,91.0) circle[radius=1.45mm];
\fill[black!11] (90,86) rectangle ++(10,10);
\fill[black!11] (100,76) rectangle ++(10,10);
\fill[black!11] (100,86) rectangle ++(10,10);
\fill[black!11] (90,76) rectangle ++(10,10);
\draw[line width=0.65pt] (90,76) rectangle ++(30,20);
\draw[line width=0.45pt] (100,76) -- ++(0,20);
\draw[line width=0.45pt] (110,76) -- ++(0,20);
\draw[line width=0.45pt] (90,86) -- ++(30,0);
\fill (95.0,81.0) circle[radius=1.45mm];
\fill (95.0,91.0) circle[radius=1.45mm];
\fill (105.0,91.0) circle[radius=1.45mm];
\draw[line width=0.9pt] (103.1,81.0) -- (106.9,81.0) (105.0,79.1) -- (105.0,82.9);
\fill[black!11] (156,86) rectangle ++(10,10);
\fill[black!11] (166,76) rectangle ++(10,10);
\fill[black!11] (166,86) rectangle ++(10,10);
\fill[black!11] (156,76) rectangle ++(10,10);
\draw[line width=0.65pt] (156,76) rectangle ++(30,20);
\draw[line width=0.45pt] (166,76) -- ++(0,20);
\draw[line width=0.45pt] (176,76) -- ++(0,20);
\draw[line width=0.45pt] (156,86) -- ++(30,0);
\fill (161.0,81.0) circle[radius=1.45mm];
\fill (161.0,91.0) circle[radius=1.45mm];
\fill (171.0,91.0) circle[radius=1.45mm];
\draw[line width=0.9pt] (169.1,81.0) -- (172.9,81.0) (171.0,79.1) -- (171.0,82.9);
\draw[-{Stealth[length=2mm]},line width=0.6pt] (61,86) -- (81,86);
\draw[-{Stealth[length=2mm]},line width=0.6pt] (127,86) -- (147,86);
\node[anchor=center,inner sep=0pt,font=\sffamily\fontsize{10.5}{12.5}\selectfont] at (39,101) {Start};
\node[anchor=center,inner sep=0pt,font=\sffamily\fontsize{10.5}{12.5}\selectfont] at (105,101) {One square added};
\node[anchor=center,inner sep=0pt,font=\sffamily\fontsize{10.5}{12.5}\selectfont] at (171,101) {Stopped};
