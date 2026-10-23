from pathlib import Path
import os, subprocess, shutil, math
HERE=Path(__file__).resolve().parent
OUT=HERE.parent
QA=OUT/'qa'; QA.mkdir(exist_ok=True)
def esc(s):
    return s.replace('&',r'\&').replace('%',r'\%').replace('#',r'\#').replace('–','--').replace('×',r'$\times$').replace('≥',r'$\geq$').replace('→',r'$\to$')
class Page:
    def __init__(self): self.s=[]
    def add(self,s): self.s.append(s)
    def text(self,x,y,s,w=18.5,size=14,bold=False):
        self.add(r'\node[anchor=north west,inner sep=0pt,align=left,text width='+str(w)+r'cm,font=\fontsize{'+str(size)+'}{'+str(size*1.26)+r'}\selectfont'+(r'\bfseries' if bold else '')+'] at ('+f'{x},{-y}'+') {'+esc(s)+'};')
    def prob(self,n,y,s,size=14):
        self.add(r'\node[anchor=north west,inner sep=0pt,align=left,text width=18.6cm,font=\fontsize{'+str(size)+'}{'+str(size*1.27)+r'}\selectfont] at (0,'+str(-y)+') {\\textbf{Problem '+str(n)+':} '+esc(s)+'};')
    def line(self,x,y,X,Y,style='black,line width=.6pt'):
        self.add(r'\draw['+style+'] ('+f'{x},{-y}'+') -- ('+f'{X},{-Y}'+');')
    def rect(self,x,y,w,h,style='black,line width=.65pt'):
        self.add(r'\draw['+style+'] ('+f'{x},{-y}'+') rectangle ('+f'{x+w},{-y-h}'+');')
    def node(self,x,y,s,size=12):
        self.add(r'\node[font=\fontsize{'+str(size)+'}{'+str(size+2)+r'}\selectfont,inner sep=1pt] at ('+f'{x},{-y}'+') {'+esc(str(s))+'};')
    def strip(self,x,y,n,label=True,fill=None,unit=1):
        self.rect(x,y,n*unit,1,('fill='+fill+',' if fill else '')+'line width=.7pt')
        for i in range(1,n): self.line(x+i*unit,y,x+i*unit,y+1,'gray!60,line width=.3pt')
        if label: self.node(x+n*unit+.4,y+.5,n)
    def targets(self,vals,y,cols=8):
        for i,v in enumerate(vals):
            x=(i%cols)*2.2; yy=y+(i//cols)*1.6
            self.rect(x,yy,1.8,1.2); self.node(x+.9,yy+.6,v,16)
    def ruled(self,y,rows=3,gap=1.15):
        for j in range(rows): self.line(0,y+j*gap,18.5,y+j*gap,'gray!45,line width=.35pt')
    def rodkey(self,vals,y):
        x=0
        for n in vals:
            self.strip(x,y,n,label=False,fill='gray!12'); self.node(x+n/2,y+.5,n,14); x+=n+.9
    def gridrect(self,x,y,w,h,unit=1,lab=True):
        self.rect(x,y,w*unit,h*unit)
        for i in range(1,w): self.line(x+i*unit,y,x+i*unit,y+h*unit,'gray!50,line width=.3pt')
        for i in range(1,h): self.line(x,y+i*unit,x+w*unit,y+i*unit,'gray!50,line width=.3pt')
        if lab:
            self.node(x+w*unit/2,y-.35,w)
            self.node(x-.35,y+h*unit/2,h)
    def dots(self,x,y,n=6,unit=2,lines=[],rings=[],labels=True):
        for a,b in lines:
            self.line(x,y+n*unit,x+a*unit,y+(n-b)*unit,'black,line width=.55pt')
        for a in range(n+1):
            for b in range(n+1):
                self.add(r'\fill ('+f'{x+a*unit},{-(y+(n-b)*unit)}'+') circle (1.3pt);')
        for a,b in rings:
            self.add(r'\draw[line width=.8pt] ('+f'{x+a*unit},{-(y+(n-b)*unit)}'+') circle (3.7pt);')
        if labels:
            for a in range(n+1): self.node(x+a*unit,y+n*unit+.48,a,10)
            for b in range(1,n+1): self.node(x-.5,y+(n-b)*unit,b,10)
        self.node(x-.45,y+n*unit+.05,'O',12)
    def pan(self,x,y,target=None,left=[],right=[],scale=1):
        self.rect(x,y,7.9*scale,3.1*scale,'rounded corners=9pt,line width=.7pt')
        self.rect(x+9.1*scale,y,7.9*scale,3.1*scale,'rounded corners=9pt,line width=.7pt')
        if target is not None:
            self.rect(x+.25*scale,y+.3*scale,2.2*scale,2.5*scale,'fill=gray!12,line width=.7pt')
            self.node(x+1.35*scale,y+.95*scale,'target',10*scale)
            self.node(x+1.35*scale,y+1.9*scale,target,16*scale)
        for side,vals,base in [(0,left,x+2.65*scale),(1,right,x+9.8*scale)]:
            for i,v in enumerate(vals):
                xx=base+i*2.1*scale
                self.add(r'\draw ('+f'{xx+0.85*scale},{-(y+1.55*scale)}'+') circle ('+str(.8*scale)+'cm);')
                self.node(xx+.85*scale,y+1.55*scale,v,14*scale)
        self.node(x+8.5*scale,y+1.55*scale,'=',18*scale)
    def ring(self,x,y,n,word=None,r=2.9,start=0,bead=.38,labels=False):
        self.add(r'\draw[gray!65,line width=.7pt] ('+f'{x},{-y}'+') circle ('+str(r)+'cm);')
        for i in range(n):
            a=math.pi/2-2*math.pi*i/n
            X=x+r*math.cos(a); Y=y-r*math.sin(a)
            fill='white' if word is None or word[i]=='A' else 'gray!65'
            self.add(r'\draw[fill='+fill+'] ('+f'{X:.4f},{-Y:.4f}'+') circle ('+str(bead)+'cm);')
            if word is not None: self.node(X,Y,word[i],12 if bead>.25 else 8)
            elif labels: self.node(X,Y,i+1,10)
        a=math.pi/2-2*math.pi*start/n
        X=x+(r+.95)*math.cos(a); Y=y-(r+.95)*math.sin(a)
        XX=x+(r+bead+.12)*math.cos(a); YY=y-(r+bead+.12)*math.sin(a)
        self.line(X,Y,XX,YY,'->,line width=.8pt')
        self.node(X if start==0 else X+.5*math.cos(a),Y-.2 if start==0 else Y-.5*math.sin(a),'start',9)
        # Keep the direction arrow outside bead positions and moved start labels.
        ar=r+bead+.2
        ax=x+ar*math.cos(math.radians(150))
        ay=y-ar*math.sin(math.radians(150))
        self.add(r'\draw[->,line width=.7pt] ('+f'{ax:.4f},{-ay:.4f}'+') arc[start angle=150,end angle=110,radius='+str(ar)+'cm];')


def build(week,topic,band,slug,pages):
    pk={'K--1':'K','Grades 2--3':'23','Grades 4--5':'45'}[band]
    pre=r'''\documentclass[letterpaper,12pt]{article}
\usepackage[margin=.5in]{geometry}
\usepackage{tikz}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\pagestyle{empty}
\pdfmapfile{+cm.map}
\pdfmapfile{+ps2pk35.map}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\begin{document}
'''
    text=pre
    for i,p in enumerate(pages,1):
        text+=r'\null\begin{tikzpicture}[remember picture,overlay,x=1cm,y=1cm]'+ '\n'
        text+=r'\begin{scope}[shift={(current page.north west)}]'+ '\n'
        text+=r'\node[anchor=north west,inner sep=0pt,font=\fontsize{11.5}{13}\selectfont] at (1.4,-.72) {Week '+str(week)+' / '+topic+' / '+band+'};\n'
        text+=r'\node[anchor=south west,inner sep=0pt,font=\fontsize{9}{11}\selectfont] at (1.4,-27.2) {Bellingham Math Circle / Week '+str(week)+' / F'+str(week)+'-'+pk+'-v2};\n'
        text+=r'\node[anchor=south east,inner sep=0pt,font=\fontsize{9}{11}\selectfont] at (20.15,-27.2) {'+str(i)+'};\n'
        text+=r'\begin{scope}[shift={(1.4,-1.65)}]'+'\n'+'\n'.join(p.s)+r'\end{scope}\end{scope}\end{tikzpicture}'+'\n'
        if i<len(pages): text+='\\newpage\n'
    text+='\\end{document}\n'
    fn=HERE/(slug+'.tex'); fn.write_text(text)
    env=os.environ.copy()
    for pass_no in (1,2):
        result=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(QA),str(fn)],cwd=HERE,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        (QA/(slug+'-build-'+str(pass_no)+'.log')).write_text(result.stdout)
        if result.returncode: raise RuntimeError(result.stdout[-3000:])
    shutil.copy(QA/(slug+'.pdf'),OUT/(slug+'.pdf'))
    subprocess.run(['pdftoppm','-r','60','-png',str(OUT/(slug+'.pdf')),str(QA/slug)],check=True)
    print(week,slug,len(pages))
