from pathlib import Path
import math
ROOT=Path(__file__).resolve().parent

def text(x,y,s,w=180,size=13):
    return rf'\node[anchor=north west,inner sep=0pt,text width={w}mm,font=\fontsize{{{size}}}{{{size+3}}}\selectfont] at ({x},{y}) {{{s}}};'+'\n'
def label(x,y,s,size=11,anchor='center'):
    return rf'\node[anchor={anchor},inner sep=1pt,font=\fontsize{{{size}}}{{{size+2}}}\selectfont] at ({x},{y}) {{{s}}};'+'\n'
def line(x,y,X,Y,opts=''):
    return rf'\draw[{opts}] ({x},{y}) -- ({X},{Y});'+'\n'
def rect(x,y,w,h,opts=''):
    return rf'\draw[{opts}] ({x},{y}) rectangle ++({w},{h});'+'\n'
def circle(x,y,r=2,opts=''):
    return rf'\draw[{opts}] ({x},{y}) circle ({r});'+'\n'
def prob(n,s,y=0,size=13): return text(0,y,rf'\textbf{{Problem {n}:}} '+s,size=size)
def board(x,y,n=7,H=5,clues=None,star=None,dx=22,dy=20):
    clues=clues or {}; s=''
    for h in range(H+1):
        s+=line(x-6,y+(H-h)*dy,x+(n-1)*dx+6,y+(H-h)*dy,'gray!45')
        s+=label(x-12,y+(H-h)*dy,str(h),11)
    for i in range(n):
        s+=line(x+i*dx,y,x+i*dx,y+H*dy,'gray!45')
        for h in range(H+1): s+=circle(x+i*dx,y+(H-h)*dy,.8,'fill=white')
        s+=label(x+i*dx,y+H*dy+9,str(i),11)
        if i in clues:
            h=clues[i]; s+=circle(x+i*dx,y+(H-h)*dy,5,'fill=black')
            s+=label(x+i*dx,y+(H-h)*dy,rf'\color{{white}}{h}',11)
        if i==star: s+=label(x+i*dx,y-8,r'$\star$',16)
    return s

def row(x,y,vals,locked=(),dx=22):
    s=''
    for i,v in enumerate(vals):
        s+=rect(x+i*dx,y,dx-2,12,'rounded corners=1mm'+(',fill=gray!20' if i in locked else ''))
        s+=label(x+i*dx+(dx-2)/2,y+6,'' if v is None else str(v),13)
        s+=label(x+i*dx+(dx-2)/2,y+17,str(i),9)
    return s

def hill(x,y,hs,scale=6):
    s=''
    for i,h in enumerate(hs):
        for j in range(h): s+=rect(x+i*(scale+1),y-(j+1)*scale,scale,scale,'fill=gray!15')
        if h==0:s+=circle(x+i*(scale+1)+scale/2,y-2,1.4)
        s+=label(x+i*(scale+1)+scale/2,y+5,str(h),10)
    return s

def write(name,week,topic,band,pages):
    tag={'K--1':'K','Grades 2--3':'23','Grades 4--5':'45'}[band]
    pre=rf'''\documentclass[letterpaper,12pt]{{article}}
\usepackage[margin=14mm,top=18mm,bottom=17mm,headheight=14pt]{{geometry}}
\pdfmapfile{{+cm.map}}\pdfmapfile{{+cmextra.map}}
\usepackage{{tikz,fancyhdr,amsmath,amssymb}}
\usetikzlibrary{{arrows.meta,patterns}}
\pagestyle{{fancy}}\fancyhf{{}}\renewcommand{{\headrulewidth}}{{0pt}}
\fancyhead[L]{{\small Week {week} / {topic} / {band}}}
\fancyfoot[L]{{\small Bellingham Math Circle / Week {week} / F{week}-{tag}-v3}}
\fancyfoot[R]{{\small\thepage}}
\setlength{{\parindent}}{{0pt}}\setlength{{\parskip}}{{0pt}}
\begin{{document}}
'''
    out=pre
    for i,p in enumerate(pages):
        if i:out+='\\newpage\n'
        out+='\\noindent\\begin{tikzpicture}[x=1mm,y=-1mm,line width=.5pt]\n\\path[use as bounding box] (0,0) rectangle (185,235);\n'+p+'\\end{tikzpicture}\n'
    out+='\\end{document}\n'; (ROOT/(name+'.tex')).write_text(out)

def buildscript():
    (ROOT/'build.sh').write_text('''#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p ../qa
python3 make.py
python3 check_examples.py
for file in k-1 grades-2-3 grades-4-5; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../qa "$file.tex" > "../qa/$file-build.txt"
  cp "../qa/$file.pdf" "../$file.pdf"
  pdftoppm -r 70 -png "../$file.pdf" "../qa/$file" >/dev/null 2>&1
done
''')
