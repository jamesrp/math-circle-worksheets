import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import sys
sys.path.insert(0,HERE)
from voronoi_exact import *
# Data re-read from the delivered PDFs (extract_pdf_geometry.py / extract_crosses.py output)
AB={'A':(-2,0),'B':(2,0)}
TRI={'A':(-2,0),'B':(2,0),'C':(0,2)}
SQ={'A':(-2,2),'B':(2,2),'C':(2,-2),'D':(-2,-2)}
FIVE={**SQ,'E':(0,0)}
kp=[(-2.5,2.3),(-1.4,1.2),(-.55,2.4),(0,2.6),(.7,1.3),(2.4,2.3),(-2.55,-1.2),(-1.3,-2.25),(-.5,-.9),(0,0),(0,-2.5),(.6,-2.05),(1.5,-.8),(2.5,-2.3),(2.65,.75),(-2.55,.75)]
tp=[(-2.5,2.5),(-1.8,1.2),(0,1),(1.8,1.2),(2.5,2.5),(-2.3,-1.5),(-.7,-1.5),(0,-1),(1.3,-1.7),(2.4,-.9),(0,0),(0,-2.4)]
gp=[(-2.4,2.4),(-2,1),(-1,2),(0,0),(1,-1),(2.4,-2.4),(-2.2,-.4),(-.4,-2.2),(-2.1,-2.5),(.2,1.9),(1.7,.2),(2.4,2.5),(2.5,-.6),(-.6,2.5)]
report('K1 P1',AB,kp)
report('K1 P2 / G45 P1',{'A':(-1.5,-1),'B':(1.5,1)})
report('K1 P3',{'A':(-2,0),'B':(0,0),'C':(2,0)})
report('K1 P4 / G23 P2 / G45 P2',TRI,tp)
report('K1 P5 / G23 P4 / G45 P4',SQ)
report('K1 P6 / G23 P6 / G45 P5',FIVE)
report('K1 P7 guide answer',{'A':(-1.8,1.2),'B':(1.8,-1.2),'C':(0,0)})
report('K1 P8 guide answer',{'A':(0,0),'B':(-2,0),'C':(2,0)})
report('G23 P1',{'A':(-1.5,-1.5),'B':(1.5,1.5)},gp)
report('G23 P3',{'A':(-2,0),'B':(-.5,0),'C':(2,0)})
report('G23 P5',{'A':(-2,-2),'B':(2,-2),'C':(2,2),'D':(-2,1)})
report('G23 P7 guide answer',{**TRI,'D':(0,-2.5)})
report('G23 P7 rejected D=(0,-2)',{**TRI,'D':(0,-2)})
report('G23 P8 guide answer',{'A':(0,0),'B':(2,0),'C':(0,2)})
report('G45 P3',{'A':(-2,-1),'B':(2,-1),'C':(0,2),'D':(0,0)})
report('G45 P6 guide answer',{'A':(-2,0),'B':(0,0),'C':(2,0),'D':(0,2),'E':(0,-2)})
report('G45 P7 guide answer',{'A':(0,0),'B':(0,-2),'C':(F(24,13),F(16,13)),'D':(-F(24,13),F(16,13))})
s=report('G45 P8 guide answer',{'A':(0,2),'B':(0,-2.5)},[(-2,0),(2,0),(0,0),(0,-2)])
