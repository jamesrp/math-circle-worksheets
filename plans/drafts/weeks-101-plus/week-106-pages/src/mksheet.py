import sys,glob,os
names=sys.argv[2:] or sorted(os.path.basename(f)[:-4] for f in glob.glob('figs/*.tex'))
o=[r"\documentclass{article}\usepackage[margin=0.3in,paperheight=60in]{geometry}\usepackage{tikz}\pagestyle{empty}\begin{document}\small\noindent"]
for i,n in enumerate(names):
    o.append(r"\begin{minipage}{0.32\textwidth}\resizebox{\linewidth}{!}{\input{figs/%s}}\\\verb|%s|\end{minipage}\hfill"%(n,n))
    if i%3==2: o.append(r"\par\medskip\noindent")
o.append(r"\end{document}")
open(sys.argv[1],'w').write("\n".join(o))
