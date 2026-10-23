"""Week 95 figure helpers, carried over unchanged from the old student builder
(archive-before-problem-files-2026-10-23/student/build.py). Problem files call them
from "## figure" sections; each returns LaTeX."""


def table(headers, rows, widths=None, valign='p'):
    # valign 'm' centres each cell vertically in its row (array's m-column); the default 'p' is the old builder's.
    if widths is None: widths=[6.95/len(headers)]*len(headers)
    spec='|'+'|'.join('>{\\centering\\arraybackslash}'+valign+'{'+str(w)+'in}' for w in widths)+'|'
    return '\\begin{center}\\begin{tabular}{'+spec+'}\\hline\n'+' & '.join(headers)+r'\\\hline'+'\n'+ '\n'.join(' & '.join(map(str,row))+r'\\\hline' for row in rows)+'\n\\end{tabular}\\end{center}\n'


def records(first, second):
    def row(label, ids):
        out=r'\node[anchor=west,font=\small] at (0,0.25) {'+label+r'};'
        for i,c in enumerate(ids): out+=rf'\card{{{3+i*.85}}}{{0}}{{{c}}}{{{int(c in first and label=="Second catch")}}}'
        return out
    return r'\begin{center}\begin{tikzpicture}'+row('First catch',first)+r'\begin{scope}[yshift=-.8cm]'+row('Second catch',second)+r'\end{scope}\end{tikzpicture}\end{center}'
