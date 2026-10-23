+++
id = "w54.at-most-three"
title = "At most 3 strips, after exchanging"
grades = ["shared"]
route = "first"
page = "new"
kernel = 'Exchanging rows and columns matches collections with at most k strips to collections whose sizes are at most k.'
+++

## text
\beginpage{4--5}

## prompt @9.78
Find all 8-unit collections with at most 3 strips. Exchange rows and columns, and record their sizes. Which collections can result? Explain a rule that works for any \mbox{total}.

## text
\centerlabel{2.28}{8.73}{At most 3 strips}
\centerlabel{6.21}{8.73}{After exchanging}
\foreach \i in {0,...,11}{
 \pgfmathsetmacro{\top}{8.41-\i*0.46}
 \draw[rulegray,line width=0.5pt] (0.6,\top) rectangle ++(3.37,-0.46);
 \draw[rulegray,line width=0.5pt] (4.53,\top) rectangle ++(3.37,-0.46);
 \draw[-{Stealth[length=4pt]},line width=0.65pt] (4.12,{\top-0.23})--(4.39,{\top-0.23});
}
\draw[rulegray,line width=0.5pt] (0.6,2.55) rectangle (7.9,0.9);
