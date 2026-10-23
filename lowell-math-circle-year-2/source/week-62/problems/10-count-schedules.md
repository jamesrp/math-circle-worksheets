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
\begin{tikzpicture}[x=1cm,y=1cm,font=\small,card/.style={draw,minimum width=0.55cm,minimum height=0.7cm,fill=white},>=Stealth]
\node at (1,1.9) {conflict};
\draw (0,1) -- (2,1);
\node[draw,circle,fill=white,minimum size=0.65cm] at (0,1) {X};
\node[draw,circle,fill=white,minimum size=0.65cm] at (2,1) {Y};
\draw[->] (2.8,1) -- (3.6,1);
\node at (5.8,1.9) {slots 1, 2, 3};
\node at (4.5,1.3) {slot 1}; \node[card] at (4.5,0.6) {X};
\node at (5.8,1.3) {slot 2}; \node[card] at (5.8,0.6) {Y};
\node at (7.1,1.3) {slot 3}; \node at (7.1,0.6) {empty};
\draw[->] (8,1) -- (8.8,1);
\node at (10.4,1.9) {different schedules};
\node at (10.4,1.2) {X 1, Y 2}; \node at (10.4,0.6) {X 2, Y 1}; \node at (10.4,0) {X 1, Y 3};
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
