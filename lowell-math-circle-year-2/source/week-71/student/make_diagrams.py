#!/usr/bin/env python3
"""Generate exact-reflection tracing windows as portable TikZ source."""
from pathlib import Path
from math import sqrt

def reflect(p,a,b):
 e=(b[0]-a[0],b[1]-a[1]);q=(p[0]-a[0],p[1]-a[1]);t=(q[0]*e[0]+q[1]*e[1])/(e[0]**2+e[1]**2)
 return(a[0]+2*t*e[0]-q[0],a[1]+2*t*e[1]-q[1])
def xy(p):return f'({p[0]:.8f},{p[1]:.8f})'
def window(poly,name,scale):
 out=[rf'\newcommand{{\{name}}}{{\begin{{tikzpicture}}[scale={scale}]']
 faces=[poly]
 for j in [0,3,0]:
  old=faces[-1];a,b=old[j],old[(j+1)%4]
  faces.append([reflect(p,a,b)for p in old])
 for k,face in enumerate(faces):
  coords='--'.join(map(xy,face))
  out.append(r'\fill[gray!'+('14' if k==0 else '2')+'] '+coords+'--cycle;')
 for face in faces:
  out.append(r'\draw[thick] '+'--'.join(map(xy,face))+'--cycle;')
 # Label the three shared crossing sides prominently, with white backing.
 for face,j,lab in zip(faces,[0,3,0],['A','B','A']):
  a,b=face[j],face[(j+1)%4];m=((a[0]+b[0])/2,(a[1]+b[1])/2)
  out.append(r'\node[fill=white,inner sep=1.4pt,font=\small]at'+xy(m)+'{'+lab+'};')
 # Put a simple start-room label away from the crossing near the vertex.
 c=(sum(p[0]for p in poly)/4,sum(p[1]for p in poly)/4)
 out.append(r'\node[font=\small]at'+xy(c)+'{start};')
 out.append(r'\end{tikzpicture}}')
 return '\n'.join(out)
text=window([(0,0),(4,0),(4,4),(0,4)],'squareABA',.62)+'\n'+window([(0,0),(4,0),(6,2*sqrt(3)),(2,2*sqrt(3))],'rhombusABA',.53)
Path(__file__).with_name('windows.tex').write_text(text+'\n')
