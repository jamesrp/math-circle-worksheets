from pathlib import Path
import subprocess, os, shutil
ROOT=Path(__file__).resolve().parent.parent
class Book:
 def __init__(self,week,topic,band,key):
  self.week,self.topic,self.band,self.key=week,topic,band,key; self.pages=[]; self.items=[]
 def page(self):
  if self.items:self.pages.append(''.join(self.items))
  self.items=[]
 def put(self,s):self.items.append(s+'\n')
 def text(self,y,s,x=0,w=18,size=14):
  self.put(r'\node[anchor=north west,text width='+str(w)+r'cm,inner sep=0pt,font=\fontsize{'+str(size)+'}{'+str(size+3)+r'}\selectfont] at ('+str(x)+','+str(-y)+') {'+s+'};')
 def p(self,n,y,s,size=14):self.text(y,r'\textbf{Problem '+str(n)+':} '+s,size=size)
 def line(self,y,w=18,x=0):self.put(fr'\draw[gray!45] ({x},{-y}) -- ({x+w},{-y});')
 def space(self,y,n=3,gap=1):
  for i in range(n):self.line(y+i*gap)
 def box(self,x,y,w,h,label=''):
  self.put(fr'\draw[gray!65,rounded corners=2pt] ({x},{-y}) rectangle ({x+w},{-y-h});')
  if label:self.text(y+.15,label,x+.2,w-.4,11)
 def token(self,x,y,color,label='',r=.44):
  fill={'R':'red!18','B':'blue!18','':'white'}.get(color,'white')
  self.put(fr'\draw[fill={fill},line width=.7pt] ({x},{-y}) circle ({r});')
  if color:self.put(fr'\node[font=\bfseries\small] at ({x},{-y}) {{{label or color}}};')
 def pair(self,x,y,a,b,labels=None,scale=1):
  self.box(x,y,3.5*scale,1.35*scale)
  self.token(x+.9*scale,y+.67*scale,a,labels[0] if labels else '',.44*scale)
  self.token(x+2.6*scale,y+.67*scale,b,labels[1] if labels else '',.44*scale)
 def bag(self,x,y,colors,label='',ident=False):
  cols=min(4,len(colors)); rows=(len(colors)+cols-1)//cols
  w=max(3,cols*1.1+.45); h=rows*1.1+.55
  self.box(x,y,w,h)
  for i,c in enumerate(colors):self.token(x+.75+(i%cols)*1.05,y+.7+(i//cols)*1.05,c, c+str(i+1) if ident else '')
  if label:self.text(y+h+.18,label,x,w,12)
 def arrow(self,x,y,x2,y2,label=''):
  self.put(fr'\draw[-{{Stealth[length=2mm]}},line width=.8pt] ({x},{-y}) -- ({x2},{-y2}) node[midway,above,font=\small] {{{label}}};')
 def shape(self,x,y,s):
  if s=='square':self.put(fr'\draw[line width=1pt] ({x-.35},{-y-.35}) rectangle ({x+.35},{-y+.35});')
  elif s=='circle':self.put(fr'\draw[line width=1pt] ({x},{-y}) circle (.35);')
  else:self.text(y-.3,'none',x-.5,1.4,11)
 def save(self):
  if self.items:self.pages.append(''.join(self.items));self.items=[]
  pre=r'''\documentclass[letterpaper,12pt]{article}
\usepackage[margin=.65in,top=.72in,bottom=.62in,headheight=16pt,headsep=15pt,footskip=19pt]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,tikz,fancyhdr}\pdfmapfile{+lm.map}
\usetikzlibrary{arrows.meta,shapes.geometric}
\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}\renewcommand{\footrulewidth}{0pt}
\setlength{\parindent}{0pt}\setlength{\parskip}{0pt}
'''
  pre+=r'\fancyhead[L]{\small Week '+str(self.week)+' / '+self.topic+' / '+self.band+'}\n'
  pre+=r'\fancyfoot[L]{\footnotesize Bellingham Math Circle / Week '+str(self.week)+' / W'+str(self.week)+'-'+self.key+'-v2}'+r'\fancyfoot[R]{\footnotesize\thepage}'+'\n'+r'\begin{document}'+'\n'
  body=[]
  for p in self.pages:body.append(r'\noindent\begin{tikzpicture}[x=1cm,y=1cm]\path[use as bounding box] (0,0) rectangle (18.2,-23.6);'+'\n'+p+r'\end{tikzpicture}')
  (ROOT/'src'/f'{self.key}.tex').write_text(pre+('\n'+r'\newpage'+'\n').join(body)+'\n'+r'\end{document}'+'\n')
def build():
 env=os.environ.copy()
 builddir=ROOT/'build'; builddir.mkdir(exist_ok=True)
 for key in ['k-1','grades-2-3','grades-4-5']:
  for pass_number in range(2):
   p=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error',f'-output-directory={builddir}',str(ROOT/'src'/f'{key}.tex')],env=env,text=True,capture_output=True)
   (builddir/f'{key}-console.txt').write_text(p.stdout+p.stderr)
   if p.returncode:raise RuntimeError(p.stdout[-3500:]+p.stderr)
  shutil.copy(builddir/f'{key}.pdf',ROOT/f'{key}.pdf')
  r=ROOT/'render'/key;r.mkdir(parents=True,exist_ok=True)
  subprocess.run(['pdftoppm','-r','75','-png',str(ROOT/f'{key}.pdf'),str(r/'page')],check=True)
if __name__=='__main__':build()
