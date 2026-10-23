+++
id = "w62.two-slot-rule"
title = "A rule for two slots"
grades = ["shared"]
route = "return"
page = "new"
kernel = 'A network fits in two slots exactly when it has no cycle of odd length, component by component.'
+++

## text
\gdef\band{Grades 4--5}

## prompt
Make a rule that decides which networks fit in two slots. Use it on these networks. Explain why your rule works for networks of any size.

## figure
center(graph("p5-disconnected",DISCON,DISCONe))
+center(graph("p5-odd-disconnected",ODDDIS,ODDDISe))
+notespace(0.5)
+r"\noindent My rule:\quad\rule{5.7in}{0.4pt}\par\vspace{0.7cm}\hrule\vspace{0.9cm}\hrule"
+"\n"
