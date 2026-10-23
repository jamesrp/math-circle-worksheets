+++
id = "w55.card-rules"
title = "Choosing cards and placing counters, with a worked example"
kind = "setup"
grades = ["shared"]
route = "first"
+++

## text
\txt{0}{0}{245}{Choose one card from A and one from B. Keep each input fixed while finding all its totals. Put one counter at each different total. Mark occupied cells before reusing counters. No number repeats within an input; A and B may share numbers. Use cards 0--9 unless a problem says otherwise.}
\txt{9}{21}{50}{\small Inputs}
\cards{9}{28}{A}{1,4}
\cards{9}{45}{B}{0,3}
\draw[->] (58,42)--(69,42);
\txt{75}{21}{75}{\small Three tries}
\txt{75}{29}{75}{$1+3=4$\quad\small counter at 4}
\txt{75}{39}{75}{$4+0=4$\quad\small 4 stays occupied}
\txt{75}{49}{75}{$1+0=1$\quad\small counter at 1}
\draw[->] (154,42)--(164,42);
\txt{169}{21}{72}{\small Positions so far}
\foreach \v [count=\i from 0] in {1,4} {
  \draw (170+19*\i,29) rectangle ++(17,27);
  \node at (178.5+19*\i,35) {\v};
  \draw[fill=black!15,line width=.6pt] (178.5+19*\i,47) circle (4.5);
}
