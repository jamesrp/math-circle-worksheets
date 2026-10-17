#!/usr/bin/env python3
"""Build two deterministic student PDFs; Python standard library + pdflatex."""
import argparse, os, pathlib, shutil, subprocess
HERE = pathlib.Path(__file__).resolve().parent
PREAMBLE = r'''\documentclass[12pt,letterpaper]{article}
\usepackage[margin=0.65in,top=0.66in,bottom=0.65in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,tikz,array,fancyhdr,amsmath}
\usetikzlibrary{arrows.meta}
\pdfinfoomitdate=1
\pdftrailerid{}
\pdfsuppressptexinfo=15
\pagestyle{fancy}\fancyhf{}
\setlength{\headheight}{16pt}
\renewcommand{\headrulewidth}{0.3pt}
\renewcommand{\footrulewidth}{0pt}
\fancyhead[L]{\small Week 95 / Count the unseen / Grades BAND}
\fancyfoot[L]{\footnotesize Bellingham Math Circle / Week 95 / W95-ID-v1}
\fancyfoot[R]{\footnotesize\thepage}
\setlength{\parindent}{0pt}\setlength{\parskip}{8pt}
\renewcommand{\arraystretch}{1.6}
\newcommand{\problem}[2]{\textbf{Problem #1:} #2\par}
\newcommand{\work}[1]{\par\vspace{#1}\par}
\newcommand{\card}[4]{\draw[rounded corners=1pt] (#1,#2) rectangle ++(.42,.46);\node[font=\scriptsize] at (#1+.21,#2+.25){#3};\ifnum#4=1\fill (#1+.34,#2+.08) circle (.035);\fi}
\begin{document}
'''
RULES = r'''Use identical-size cards or counters with visible marker dots that cannot be felt. Keep the same objects throughout a series; add, remove or exchange none except for temporary catches. For sampling trials, draw without looking; every group of the chosen size should have the same chance, whether marked or unmarked.

Keep each catch out until it is counted. Mark the first catch, return \emph{all} of it, and mix before the second catch. Marks stay on through both catches. An overlap is a marked object in the second catch. Before a new round, return everything and clear the marks. To show a record is possible, you may arrange catches: use distinct objects in each catch, from the same bag.
'''
DEMO = r'''\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,>=Stealth]
% Six identities persist through the entire operation.
\node[anchor=west,font=\small] at (0,5.55) {Start: six unmarked objects};
\draw[rounded corners] (0,4.25) rectangle (4.95,5.25);
\card{.5}{4.52}{A}{0}\card{1.15}{4.52}{B}{0}\card{1.8}{4.52}{C}{0}\card{2.45}{4.52}{D}{0}\card{3.1}{4.52}{E}{0}\card{3.75}{4.52}{F}{0}
\draw[->,thick] (2.5,4.12)--(2.5,3.57) node[midway,right,font=\scriptsize]{catch 2};
\node[anchor=west,font=\small] at (0,3.28) {First catch: A, C};
\draw[rounded corners] (0,1.5) rectangle (4.95,3);
\node[font=\scriptsize] at (2.5,2.78) {Bag: B, D, E, F};
\card{.45}{2.02}{B}{0}\card{1.5}{2.02}{D}{0}\card{2.55}{2.02}{E}{0}\card{3.6}{2.02}{F}{0}
\card{.6}{.68}{A}{0}\card{1.17}{.68}{C}{0}
\draw[->] (1.85,.91)--(2.65,.91) node[midway,above,font=\scriptsize]{mark};
\card{2.85}{.68}{A}{1}\card{3.42}{.68}{C}{1}
\node[font=\scriptsize] at (2.5,.30) {Same A and C, now marked};
\draw[->,thick] (5.15,2.1)--(5.75,2.1);
\node[anchor=west,font=\small] at (5.95,3.28) {Return all; mix};
\draw[rounded corners] (5.95,.65) rectangle (9.83,3);
\card{6.3}{2.03}{D}{0}\card{7.43}{2.03}{A}{1}\card{8.56}{2.03}{F}{0}
\card{6.3}{1.13}{C}{1}\card{7.43}{1.13}{E}{0}\card{8.56}{1.13}{B}{0}
\node[font=\scriptsize] at (7.9,.30) {Same six objects};
\draw[->,thick] (10.03,2.1)--(10.63,2.1);
\node[anchor=west,font=\small] at (10.83,3.28) {Second catch: C, D, F};
\draw[rounded corners] (10.83,1.5) rectangle (15.85,3);
\node[font=\scriptsize] at (13.35,2.78) {Bag: A, B, E};
\card{11.55}{2.02}{A}{1}\card{12.85}{2.02}{B}{0}\card{14.15}{2.02}{E}{0}
\card{11.55}{.68}{C}{1}\card{12.85}{.68}{D}{0}\card{14.15}{.68}{F}{0}
\draw (11.76,.9) ellipse (.36 and .36);
\node[font=\scriptsize] at (13.35,.22) {Overlap: C (1 object)};
\end{tikzpicture}
\end{center}
'''
def table(headers, rows, widths=None):
    if widths is None: widths=[6.95/len(headers)]*len(headers)
    spec='|'+'|'.join('>{\\centering\\arraybackslash}p{'+str(w)+'in}' for w in widths)+'|'
    return '\\begin{center}\\begin{tabular}{'+spec+'}\\hline\n'+' & '.join(headers)+r'\\\hline'+'\n'+ '\n'.join(' & '.join(map(str,row))+r'\\\hline' for row in rows)+'\n\\end{tabular}\\end{center}\n'
def records(first, second):
    def row(label, ids):
        out=r'\node[anchor=west,font=\small] at (0,0.25) {'+label+r'};'
        for i,c in enumerate(ids): out+=rf'\card{{{3+i*.85}}}{{0}}{{{c}}}{{{int(c in first and label=="Second catch")}}}'
        return out
    return r'\begin{center}\begin{tikzpicture}'+row('First catch',first)+r'\begin{scope}[yshift=-.8cm]'+row('Second catch',second)+r'\end{scope}\end{tikzpicture}\end{center}'
LOWER = RULES+DEMO+r'''
\problem{1}{The keeper hides 8 to 20 objects. Catch 4, mark and return them, then catch 4 again. Play three rounds with the same objects. Choose a guess before the keeper reveals the total.}
'''+table(['Round','Overlap','My guess'],[[1,'',''],[2,'',''],[3,'','']],[1,2.4,2.4])+r'''
Keeper's total: \rule{1.2in}{.4pt}
\newpage
\problem{2}{Build the smallest bag that could give these catches. Build a larger bag that could give exactly the same catches. Which of these totals are possible: 6, 7, 8, 12, 20?}
'''+records('ABCDE','BDEFG')+r'''
\work{1.8in}
\problem{3}{Now the two catches share no objects. Find the smallest possible bag. Is there a largest possible bag if you have as many cards as you want?}
'''+records('ABCDE','FGHIJ')+r'''
\newpage
\problem{4}{These example rounds came from one unchanged bag. It holds either 8 or 16 objects. Every round has a fresh first catch of 4 and a second catch of 4. Which total would you guess from each round alone? Use all six rounds to choose one guess.}
'''+table(['Round','Overlap','Guess: 8 or 16'],[[1,2,''],[2,1,''],[3,3,''],[4,1,''],[5,2,''],[6,0,'']],[1,2.4,2.4])+r'''
My guess from all six rounds: \rule{1.1in}{.4pt}

\problem{5}{Make an 8-object bag and a 16-object bag. Arrange legal catches of 4 from each. Can either bag give both an overlap of 0 and an overlap of 3? Use your objects to settle it.}
\newpage
\problem{6}{Use each bag below. The first catch has 5 objects and the second has 4. Find every overlap that can happen. Arrange catches to show your possibilities.}
'''+table(['Bag total','Possible overlaps'],[[6,r'\rule{0pt}{.8in}'],[8,r'\rule{0pt}{.8in}'],[12,r'\rule{0pt}{.8in}']],[1.5,4.5])+r'''
\problem{7}{Choose a bag of 6, 7 or 8 objects. Make two catch records with first catch 5 and second catch 4: one that your bag could give and one that it could never give. Tell a partner the bag's total and the two records. Can they find the impossible record?}
'''
UPPER = RULES+DEMO+r'''
\problem{1}{The keeper hides 12 to 24 objects. Catch 6, mark and return them, then catch 6 again. Play three rounds with the same objects. Choose a guess before the keeper reveals the total.}
'''+table(['Round','Overlap','My guess'],[[1,'',''],[2,'',''],[3,'','']],[1,2.4,2.4])+r'''
Keeper's total: \rule{1.2in}{.4pt}
\newpage
\problem{2}{Both records have first catch 6 and second catch 6. For each record, build the smallest possible bag. Is there a largest possible bag if you have as many cards as you want?}
'''+table(['Record','Overlap','Smallest total'],[['A',2,''],['B',0,'']],[1,2.4,2.4])+r'''
\work{.55in}
\problem{3}{A proposed guessing rule chooses a total that makes the marked fraction in the bag match the marked fraction in the second catch.}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,>=Stealth]
\node[font=\small,align=center] at (2.1,2.25) {Example: 2 marked in the bag};
\node[font=\small] at (2.1,1.75) {Second catch};
\draw[rounded corners] (.6,.65) rectangle (3.6,1.45);
\card{1}{.82}{A}{1}\card{1.9}{.82}{B}{0}\card{2.8}{.82}{C}{0}
\node[font=\small] at (2.1,.28) {1 marked out of 3};
\draw[->,thick] (4.1,1.1)--(4.9,1.1);
\node[font=\small] at (8.15,2.25) {Matching bag model: 2 equal groups};
\node[font=\scriptsize] at (6.45,1.75) {Same sample};
\node[font=\scriptsize] at (9.85,1.75) {Same marked fraction};
\draw[rounded corners] (4.95,.55) rectangle (11.35,1.5);
\draw[rounded corners] (5.05,.65) rectangle (7.95,1.4);
\draw[rounded corners] (8.35,.65) rectangle (11.25,1.4);
\card{5.4}{.82}{A}{1}\card{6.25}{.82}{B}{0}\card{7.1}{.82}{C}{0}
\card{8.7}{.82}{D}{1}\card{9.55}{.82}{E}{0}\card{10.4}{.82}{F}{0}
\node[font=\small] at (8.15,.12) {1 marked out of 3 in each group};
\draw[->,thick] (11.55,1.1)--(12.2,1.1);
\node[font=\small,align=center] at (14,1.4) {Rule's guess: 6 total};
\node[font=\small] at (14,.65) {$\dfrac{2}{6}=\dfrac{1}{3}$};
\end{tikzpicture}
\end{center}
Find the rule's guess for record A. Does the catch record force that total? Make a different possible bag to test your answer.

\begin{center}
\begin{tikzpicture}
\node[anchor=west] at (0,1.1) {Whole bag after marking};
\node[anchor=west] at (9,1.1) {Second catch};
\draw[rounded corners] (0,-.65) rectangle (6.8,.65);
\foreach \x in {0,...,5}{\draw (0.5+\x*.65,0) circle (.23);\fill (0.5+\x*.65,0) circle (.055);}
\node at (5.25,0) {\Large ?};
\foreach \x in {0,...,5}{\draw (9.3+\x*.65,0) circle (.23);}
\fill (9.3,0) circle (.055);\fill (9.95,0) circle (.055);
\node at (3.4,-1.05) {6 marked; total unknown};
\node at (10.9,-1.05) {2 marked out of 6};
\end{tikzpicture}
\end{center}
\newpage
\problem{4}{These example rounds all use one unchanged bag. Each round begins again with unmarked objects: first catch 6, second catch 6. The fraction-matching rule gives these guesses. Could a bag of 18 objects produce every record? Decide what you would report about the total after seeing all five rounds.}
'''+table(['Round','Overlap',"Rule's guess"],[[1,1,36],[2,2,18],[3,3,12],[4,2,18],[5,0,'No matching total']],[1,2.4,2.4])+r'''
\work{1.1in}
\problem{5}{The last round caught no marked objects. Does that rule out every finite bag? Build two different finite bags that could give this record. What would you change about the next round to get more useful evidence?}
\newpage
\problem{6}{A bag has 24 objects. You may handle 12 objects altogether: first catch size + second catch size = 12. Choose the split with the greatest average overlap over many rounds. Explain why no other split does better.}

The average over all equally likely second catches is
\[
\text{average overlap}=\frac{\text{first catch size}\times\text{second catch size}}{\text{bag total}}.
\]
\work{1.7in}
\problem{7}{Would the best split change with a budget of 13 objects? What about 20? Find a rule for any whole-number budget from 2 to 24 and explain why it works.}
\work{1.1in}
\problem{8}{A keeper says, ``Our overlap was small, so our bag must be large.'' Some marks might have rubbed off. How could that change the guess? Design a way to test whether lost marks, rather than the total, caused the small overlap.}
'''
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',type=pathlib.Path,default=HERE.parent)
    args=parser.parse_args(); out=args.output_dir.resolve(); out.mkdir(parents=True,exist_ok=True)
    tex=shutil.which('pdflatex') or '/Library/TeX/texbin/pdflatex'
    for name, band, ident, body in [('grades-2-3','2--3','23',LOWER),('grades-4-5','4--5','45',UPPER)]:
        source=PREAMBLE.replace('BAND',band).replace('ID',ident)+body+'\n\\end{document}\n'
        (out/(name+'.tex')).write_text(source)
        env=os.environ.copy();env['SOURCE_DATE_EPOCH']='1760572800';env['FORCE_SOURCE_DATE']='1';env['TZ']='UTC'
        p=subprocess.run([tex,'-interaction=nonstopmode','-halt-on-error','-output-directory',str(out),str(out/(name+'.tex'))],capture_output=True,text=True,env=env)
        if p.returncode: raise RuntimeError(p.stdout[-6000:])
        warnings=[line for line in p.stdout.splitlines() if 'Overfull' in line]
        print(name+': '+ ('; '.join(warnings) if warnings else 'built without overfull boxes'))
if __name__=='__main__':main()
