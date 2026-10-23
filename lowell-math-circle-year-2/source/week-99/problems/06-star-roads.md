+++
id = "w99.star-roads"
title = "Moving counters on star roads"
grades = ["2-3", "4-5"]
route = "return"
page = "new"
kernel = "On a star each road's imbalance must cross it, and the sum of those imbalances is the least work."
+++

## text
\portraitpage
\promptstyle{10.0}{7.2in}{12.5}{15.5}

## prompt [2-3]
Move counters along the roads to match each target. One counter crossing one road costs 1. Find the least work for each pair. Then draw a new start and target with three counters each whose least work is 6.

## prompt [4-5]
Move counters along the roads. One counter crossing one road costs 1. Find the least work for both pairs. Find a way to know the least work before moving. Does it work for every start and target with the same number of counters on these roads?

## text [2-3]
\node[anchor=north west,inner sep=0pt,align=center,text width=2.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (1.0,8.79) {start};
\node[anchor=north west,inner sep=0pt,align=center,text width=2.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (4.9,8.79) {target picture};
\draw[black!50,line width=.45pt,] (2.25,7.85) -- (1.3900000000000001,8.299999999999999);
\draw[black!50,line width=.45pt,] (2.25,7.85) -- (3.11,8.299999999999999);
\draw[black!50,line width=.45pt,] (2.25,7.85) -- (2.25,7.069999999999999);
\draw[fill=white,line width=.65pt] (1.3900000000000001,8.299999999999999) circle (.31);
\draw[line width=.7pt,fill=black!80] (1.27,8.299999999999999) circle (0.055);
\draw[line width=.7pt,fill=black!80] (1.5100000000000002,8.299999999999999) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (1.06,8.69) {A};
\draw[fill=white,line width=.65pt] (3.11,8.299999999999999) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (3.2199999999999998,8.69) {B};
\draw[fill=white,line width=.65pt] (2.25,7.069999999999999) circle (.31);
\draw[line width=.7pt,fill=black!80] (2.25,7.069999999999999) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (2.13,6.68) {C};
\draw[fill=white,line width=.65pt] (2.25,7.85) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (2.59,7.77) {O};
\draw[black!50,line width=.45pt,] (6.15,7.85) -- (5.29,8.299999999999999);
\draw[black!50,line width=.45pt,] (6.15,7.85) -- (7.010000000000001,8.299999999999999);
\draw[black!50,line width=.45pt,] (6.15,7.85) -- (6.15,7.069999999999999);
\draw[fill=white,line width=.65pt] (5.29,8.299999999999999) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (4.96,8.69) {A};
\draw[fill=white,line width=.65pt] (7.010000000000001,8.299999999999999) circle (.31);
\draw[line width=.7pt,fill=white] (6.890000000000001,8.299999999999999) circle (0.055);
\draw[line width=.7pt,fill=white] (7.130000000000001,8.299999999999999) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (7.120000000000001,8.69) {B};
\draw[fill=white,line width=.65pt] (6.15,7.069999999999999) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (6.03,6.68) {C};
\draw[fill=white,line width=.65pt] (6.15,7.85) circle (.31);
\draw[line width=.7pt,fill=white] (6.15,7.85) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (6.49,7.77) {O};
\node[anchor=north west,inner sep=0pt,align=left,text width=1.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (0.75,6.44) {work: \rule{.6in}{.4pt}};
\draw[black!35,line width=.45pt,] (2.3,6.34) -- (7.65,6.34);
\node[anchor=north west,inner sep=0pt,align=center,text width=2.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (1.0,6.0) {start};
\node[anchor=north west,inner sep=0pt,align=center,text width=2.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (4.9,6.0) {target picture};
\draw[black!50,line width=.45pt,] (2.25,5.06) -- (1.3900000000000001,5.51);
\draw[black!50,line width=.45pt,] (2.25,5.06) -- (3.11,5.51);
\draw[black!50,line width=.45pt,] (2.25,5.06) -- (2.25,4.279999999999999);
\draw[fill=white,line width=.65pt] (1.3900000000000001,5.51) circle (.31);
\draw[line width=.7pt,fill=black!80] (1.27,5.51) circle (0.055);
\draw[line width=.7pt,fill=black!80] (1.5100000000000002,5.51) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (1.06,5.8999999999999995) {A};
\draw[fill=white,line width=.65pt] (3.11,5.51) circle (.31);
\draw[line width=.7pt,fill=black!80] (3.11,5.51) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (3.2199999999999998,5.8999999999999995) {B};
\draw[fill=white,line width=.65pt] (2.25,4.279999999999999) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (2.13,3.8899999999999992) {C};
\draw[fill=white,line width=.65pt] (2.25,5.06) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (2.59,4.9799999999999995) {O};
\draw[black!50,line width=.45pt,] (6.15,5.06) -- (5.29,5.51);
\draw[black!50,line width=.45pt,] (6.15,5.06) -- (7.010000000000001,5.51);
\draw[black!50,line width=.45pt,] (6.15,5.06) -- (6.15,4.279999999999999);
\draw[fill=white,line width=.65pt] (5.29,5.51) circle (.31);
\draw[line width=.7pt,fill=white] (5.29,5.51) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (4.96,5.8999999999999995) {A};
\draw[fill=white,line width=.65pt] (7.010000000000001,5.51) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (7.120000000000001,5.8999999999999995) {B};
\draw[fill=white,line width=.65pt] (6.15,4.279999999999999) circle (.31);
\draw[line width=.7pt,fill=white] (6.03,4.279999999999999) circle (0.055);
\draw[line width=.7pt,fill=white] (6.2700000000000005,4.279999999999999) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (6.03,3.8899999999999992) {C};
\draw[fill=white,line width=.65pt] (6.15,5.06) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (6.49,4.9799999999999995) {O};
\node[anchor=north west,inner sep=0pt,align=left,text width=1.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (0.75,3.66) {work: \rule{.6in}{.4pt}};
\draw[black!35,line width=.45pt,] (2.3,3.56) -- (7.65,3.56);
\node[anchor=north west,inner sep=0pt,align=center,text width=2.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (1.0,3.1999999999999997) {start};
\node[anchor=north west,inner sep=0pt,align=center,text width=2.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (4.9,3.1999999999999997) {target picture};
\draw[black!50,line width=.45pt,] (2.25,2.26) -- (1.3900000000000001,2.71);
\draw[black!50,line width=.45pt,] (2.25,2.26) -- (3.11,2.71);
\draw[black!50,line width=.45pt,] (2.25,2.26) -- (2.25,1.4799999999999998);
\draw[fill=white,line width=.65pt] (1.3900000000000001,2.71) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (1.06,3.1) {A};
\draw[fill=white,line width=.65pt] (3.11,2.71) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (3.2199999999999998,3.1) {B};
\draw[fill=white,line width=.65pt] (2.25,1.4799999999999998) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (2.13,1.0899999999999999) {C};
\draw[fill=white,line width=.65pt] (2.25,2.26) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (2.59,2.1799999999999997) {O};
\draw[black!50,line width=.45pt,] (6.15,2.26) -- (5.29,2.71);
\draw[black!50,line width=.45pt,] (6.15,2.26) -- (7.010000000000001,2.71);
\draw[black!50,line width=.45pt,] (6.15,2.26) -- (6.15,1.4799999999999998);
\draw[fill=white,line width=.65pt] (5.29,2.71) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (4.96,3.1) {A};
\draw[fill=white,line width=.65pt] (7.010000000000001,2.71) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (7.120000000000001,3.1) {B};
\draw[fill=white,line width=.65pt] (6.15,1.4799999999999998) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (6.03,1.0899999999999999) {C};
\draw[fill=white,line width=.65pt] (6.15,2.26) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (6.49,2.1799999999999997) {O};

## text [4-5]
\node[anchor=north west,inner sep=0pt,align=center,text width=2.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (1.0,8.77) {start};
\node[anchor=north west,inner sep=0pt,align=center,text width=2.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (4.9,8.77) {target picture};
\draw[black!50,line width=.45pt,] (2.25,7.83) -- (1.3900000000000001,8.28);
\draw[black!50,line width=.45pt,] (2.25,7.83) -- (3.11,8.28);
\draw[black!50,line width=.45pt,] (2.25,7.83) -- (2.25,7.05);
\draw[fill=white,line width=.65pt] (1.3900000000000001,8.28) circle (.31);
\draw[line width=.7pt,fill=black!80] (1.27,8.28) circle (0.055);
\draw[line width=.7pt,fill=black!80] (1.5100000000000002,8.28) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (1.06,8.67) {A};
\draw[fill=white,line width=.65pt] (3.11,8.28) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (3.2199999999999998,8.67) {B};
\draw[fill=white,line width=.65pt] (2.25,7.05) circle (.31);
\draw[line width=.7pt,fill=black!80] (2.25,7.05) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (2.13,6.66) {C};
\draw[fill=white,line width=.65pt] (2.25,7.83) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (2.59,7.75) {O};
\draw[black!50,line width=.45pt,] (6.15,7.83) -- (5.29,8.28);
\draw[black!50,line width=.45pt,] (6.15,7.83) -- (7.010000000000001,8.28);
\draw[black!50,line width=.45pt,] (6.15,7.83) -- (6.15,7.05);
\draw[fill=white,line width=.65pt] (5.29,8.28) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (4.96,8.67) {A};
\draw[fill=white,line width=.65pt] (7.010000000000001,8.28) circle (.31);
\draw[line width=.7pt,fill=white] (6.890000000000001,8.28) circle (0.055);
\draw[line width=.7pt,fill=white] (7.130000000000001,8.28) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (7.120000000000001,8.67) {B};
\draw[fill=white,line width=.65pt] (6.15,7.05) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (6.03,6.66) {C};
\draw[fill=white,line width=.65pt] (6.15,7.83) circle (.31);
\draw[line width=.7pt,fill=white] (6.15,7.83) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (6.49,7.75) {O};
\node[anchor=north west,inner sep=0pt,align=left,text width=1.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (0.75,6.42) {work: \rule{.6in}{.4pt}};
\draw[black!35,line width=.45pt,] (2.3,6.32) -- (7.65,6.32);
\node[anchor=north west,inner sep=0pt,align=center,text width=2.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (1.0,5.98) {start};
\node[anchor=north west,inner sep=0pt,align=center,text width=2.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (4.9,5.98) {target picture};
\draw[black!50,line width=.45pt,] (2.25,5.04) -- (1.3900000000000001,5.49);
\draw[black!50,line width=.45pt,] (2.25,5.04) -- (3.11,5.49);
\draw[black!50,line width=.45pt,] (2.25,5.04) -- (2.25,4.26);
\draw[fill=white,line width=.65pt] (1.3900000000000001,5.49) circle (.31);
\draw[line width=.7pt,fill=black!80] (1.27,5.6000000000000005) circle (0.055);
\draw[line width=.7pt,fill=black!80] (1.5100000000000002,5.6000000000000005) circle (0.055);
\draw[line width=.7pt,fill=black!80] (1.3900000000000001,5.38) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (1.06,5.88) {A};
\draw[fill=white,line width=.65pt] (3.11,5.49) circle (.31);
\draw[line width=.7pt,fill=black!80] (3.11,5.49) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (3.2199999999999998,5.88) {B};
\draw[fill=white,line width=.65pt] (2.25,4.26) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (2.13,3.8699999999999997) {C};
\draw[fill=white,line width=.65pt] (2.25,5.04) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (2.59,4.96) {O};
\draw[black!50,line width=.45pt,] (6.15,5.04) -- (5.29,5.49);
\draw[black!50,line width=.45pt,] (6.15,5.04) -- (7.010000000000001,5.49);
\draw[black!50,line width=.45pt,] (6.15,5.04) -- (6.15,4.26);
\draw[fill=white,line width=.65pt] (5.29,5.49) circle (.31);
\draw[line width=.7pt,fill=white] (5.29,5.49) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (4.96,5.88) {A};
\draw[fill=white,line width=.65pt] (7.010000000000001,5.49) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (7.120000000000001,5.88) {B};
\draw[fill=white,line width=.65pt] (6.15,4.26) circle (.31);
\draw[line width=.7pt,fill=white] (6.03,4.26) circle (0.055);
\draw[line width=.7pt,fill=white] (6.2700000000000005,4.26) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (6.03,3.8699999999999997) {C};
\draw[fill=white,line width=.65pt] (6.15,5.04) circle (.31);
\draw[line width=.7pt,fill=white] (6.15,5.04) circle (0.055);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (6.49,4.96) {O};
\node[anchor=north west,inner sep=0pt,align=left,text width=1.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (0.75,3.64) {work: \rule{.6in}{.4pt}};
\draw[black!35,line width=.45pt,] (2.3,3.54) -- (7.65,3.54);
\node[anchor=north west,inner sep=0pt,align=center,text width=2.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (1.0,2.88) {start};
\node[anchor=north west,inner sep=0pt,align=center,text width=2.5in,font=\sffamily\fontsize{11}{13.64}\selectfont] at (4.9,2.88) {target picture};
\draw[black!50,line width=.45pt,] (2.25,1.94) -- (1.3900000000000001,2.39);
\draw[black!50,line width=.45pt,] (2.25,1.94) -- (3.11,2.39);
\draw[black!50,line width=.45pt,] (2.25,1.94) -- (2.25,1.16);
\draw[fill=white,line width=.65pt] (1.3900000000000001,2.39) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (1.06,2.7800000000000002) {A};
\draw[fill=white,line width=.65pt] (3.11,2.39) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (3.2199999999999998,2.7800000000000002) {B};
\draw[fill=white,line width=.65pt] (2.25,1.16) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (2.13,0.7699999999999999) {C};
\draw[fill=white,line width=.65pt] (2.25,1.94) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (2.59,1.8599999999999999) {O};
\draw[black!50,line width=.45pt,] (6.15,1.94) -- (5.29,2.39);
\draw[black!50,line width=.45pt,] (6.15,1.94) -- (7.010000000000001,2.39);
\draw[black!50,line width=.45pt,] (6.15,1.94) -- (6.15,1.16);
\draw[fill=white,line width=.65pt] (5.29,2.39) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (4.96,2.7800000000000002) {A};
\draw[fill=white,line width=.65pt] (7.010000000000001,2.39) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (7.120000000000001,2.7800000000000002) {B};
\draw[fill=white,line width=.65pt] (6.15,1.16) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (6.03,0.7699999999999999) {C};
\draw[fill=white,line width=.65pt] (6.15,1.94) circle (.31);
\node[anchor=north west,inner sep=0pt,align=center,text width=0.24in,font=\sffamily\fontsize{10}{12.4}\selectfont] at (6.49,1.8599999999999999) {O};
