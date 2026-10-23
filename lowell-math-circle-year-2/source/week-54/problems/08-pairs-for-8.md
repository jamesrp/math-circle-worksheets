+++
id = "w54.pairs-for-8"
title = "Every connected pair for 8 units"
grades = ["shared"]
route = "first"
page = "new"
kernel = 'Joining and splitting pair the six only-odd collections of 8 with the six all-different ones, one to one.'
+++

## text
\beginpage{2--5}

## prompt @9.78
With 8 units, find every pair of collections connected by joining and splitting. One collection uses only odd sizes; the other uses all different sizes. Record their sizes.

## text
\centerlabel{2.18}{8.73}{Only odd sizes}
\centerlabel{6.32}{8.73}{All sizes different}
\foreach \i in {0,...,7}{
 \pgfmathsetmacro{\top}{8.39-\i*0.91}
 \draw[rulegray,line width=0.5pt] (0.6,\top) rectangle ++(3.16,-0.77);
 \draw[rulegray,line width=0.5pt] (4.74,\top) rectangle ++(3.16,-0.77);
 \draw[{Stealth[length=4pt]}-{Stealth[length=4pt]},line width=0.65pt] (3.95,{\top-0.385})--(4.54,{\top-0.385});
}
