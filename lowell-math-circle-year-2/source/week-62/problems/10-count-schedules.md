+++
id = "w62.count-schedules"
title = "Counting schedules with numbered slots"
grades = ["shared"]
route = "return"
page = "new"
kernel = 'The 4-path has 3x2x2x2 = 24 schedules with three slots and 4x3x3x3 = 108 with four; the diamond has 6 and 48.'
+++

## text
\gdef\band{Grades 4--5}
When counting schedules, switching slot numbers counts as a different schedule. Slots may be empty.
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small,>=Stealth]
\node at (1,1.9) {conflict};
\draw (0,1) -- (2,1);
\node[draw,circle,fill=white,minimum size=0.65cm] at (0,1) {X};
\node[draw,circle,fill=white,minimum size=0.65cm] at (2,1) {Y};
\draw[->] (2.8,1) -- (3.6,1);
\node at (5.1,1.9) {place X in slot 1};
\node at (5.1,1) {X 1, Y \underline{\phantom{3}}};
\draw[->] (6.6,1) -- (7.4,1);
\node at (9.7,1.9) {two different schedules};
\node at (9.7,1.1) {X 1, Y 2}; \node at (9.7,0.3) {X 1, Y 3};
\end{tikzpicture}
\end{center}

## prompt
How many different schedules does each network have using only slots 1, 2 and 3? How many using slots 1, 2, 3 and 4? Explain how you know your count is complete.

## figure
center(graph("p9-path",P4,P4e))
+r"\begin{center}3 slots: \rule{1.1in}{0.4pt}\qquad 4 slots: \rule{1.1in}{0.4pt}\end{center}"
+"\n"
+center(graph("p9-diamond",DIAM,DIAMe))
+r"\begin{center}3 slots: \rule{1.1in}{0.4pt}\qquad 4 slots: \rule{1.1in}{0.4pt}\end{center}"
+notespace(0.7)
