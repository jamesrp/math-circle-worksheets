+++
id = "w55.grid-routes"
title = "The addition grid and right/up routes, with a worked example"
kind = "setup"
grades = ["shared"]
route = "first"
page = "new"
+++

## text
\txt{0}{0}{245}{In a grid, A increases from bottom to top and B from left to right. Each dot holds the row card plus the column card. A route starts at the bottom-left dot, ends at the top-right dot, and moves one dot right or one dot up.}
\txt{9}{23}{50}{\small Inputs}
\cards{9}{31}{A}{1,5}\cards{9}{48}{B}{0,2,6}
\draw[->] (67,43)--(76,43);
\txt{82}{25}{61}{\small A row: 1\\B column: 2\\$1+2=3$}
\draw[->] (138,43)--(147,43);
\arraygrid{165}{58}{1,5}{0,2,6}{20}
\draw[->,line width=1.4pt] (169.5,58)--(180.5,58);
\draw[->,line width=1.4pt] (185,53.5)--(185,42.5);
\draw[->,line width=1.4pt] (189.5,38)--(200.5,38);
\txt{151}{73}{91}{\small Route totals: 1, 3, 7, 11}
