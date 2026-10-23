+++
id = "w54.exchange-twice"
title = "Exchange rows and columns twice"
grades = ["shared"]
route = "first"
page = "same"
kernel = 'Exchanging rows and columns twice returns the original collection: the exchange is its own inverse.'
+++

## prompt @7.45
Exchange rows and columns twice for each collection. Draw the results. What does the second exchange do?

## text
\centerlabel{1.61}{6.7}{Before}
\centerlabel{4.23}{6.7}{Once}
\centerlabel{6.77}{6.7}{Twice}
\foreach \top in {6.38,4.59,2.8}{
 \draw[rulegray,line width=0.5pt] (0.6,\top) rectangle ++(7.3,-1.54);
 \foreach \xx in {2.68,5.3}{\draw[gridgray,line width=0.4pt] (\xx,\top)--++(0,-1.54);}
 \pgfmathsetmacro{\gg}{\top-0.2}
 \tinygrid{3.45}{\gg}
 \tinygrid{6.07}{\gg}
 \draw[-{Stealth[length=4pt]},line width=0.65pt] (2.89,{\top-0.75})--(3.22,{\top-0.75});
 \draw[-{Stealth[length=4pt]},line width=0.65pt] (5.51,{\top-0.75})--(5.84,{\top-0.75});
}
\rows{0.88}{6.09}{0.22}{5,2,1}
\rows{0.88}{4.27}{0.22}{4,4}
\rows{0.88}{2.57}{0.22}{3,3,1,1}
