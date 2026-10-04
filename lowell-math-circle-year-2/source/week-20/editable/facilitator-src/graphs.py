"""Manually transcribed final-board data. Values on circles are expected answers.
Coordinates only control adult solution diagrams. No student source is modified.
"""
from fractions import Fraction as F
G={}
def graph(key,nodes,edges,title=''):
    G[key]={'nodes':nodes,'edges':edges,'title':title or key}
    return key
def path(key,vals,fixed=None,title=''):
    fixed=set(fixed if fixed is not None else [0,len(vals)-1])
    return graph(key,[(str(i),i,0,i in fixed,v) for i,v in enumerate(vals)],[(str(i),str(i+1)) for i in range(len(vals)-1)],title)
def star(key,vals,center,title=''):
    xy={2:[(-1,0),(1,0)],3:[(0,1),(-1,-.65),(1,-.65)]}[len(vals)]
    return graph(key,[('u',0,0,False,center)]+[(str(i),x,y,True,v) for i,((x,y),v) in enumerate(zip(xy,vals))],[('u',str(i)) for i in range(len(vals))],title)
def tree(key,a,c,b,u,v,title=''):
    return graph(key,[('a',0,.65,True,a),('c',0,-.65,True,c),('u',1.1,0,False,u),('v',2.2,0,False,v),('b',3.3,0,True,b)],[('a','u'),('c','u'),('u','v'),('v','b')],title)
def diamond(key,a,b,u,v,tie=False,title=''):
    return graph(key,[('a',0,0,True,a),('b',3,0,True,b),('u',1.5,.8,False,u),('v',1.5,-.8,False,v)],[('a','u'),('a','v'),('b','u'),('b','v')]+([('u','v')] if tie else []),title)
for i,(a,b,c) in enumerate([(0,2,1),(2,4,3),(0,4,2),(2,6,4)],1): star(f'K1.{i}',[a,b],c,f'Board {i}')
for i,vals in enumerate([[0,1,2,3],[3,2,1,0],[0,2,4,6],[6,4,2,0]],1):path(f'K2.{i}',vals,title=f'Row {i}')
star('K3',[1,2,3],2,'One of 10 fillings')
path('K4',[0,1,2],title='One of 8 fillings')
path('K5.1',[0,1,2,3],title='Upper board');path('K5.2',[1,2,3,4],title='Lower board')
graph('K6.1',[('a',1,1,True,2),('u',0,0,False,2),('v',2,0,False,2)],[('a','u'),('a','v'),('u','v')],'Triangle')
graph('K6.2',[('a',0,1,True,3),('u',2,1,False,3),('v',2,0,False,3),('w',0,0,False,3)],[('a','u'),('u','v'),('v','w'),('w','a')],'Four-cycle')
graph('K7.1',[('a',1,1,False,'c'),('u',0,0,False,'c'),('v',2,0,False,'c')],[('a','u'),('a','v'),('u','v')],'c = 0, 1, 2, 3, 4 or 5')
path('K7.2',['c']*4,fixed=[],title='c = 0, 1, 2, 3, 4 or 5')
star('M1.1',[1,7],4,'Upper left');star('M1.2',[0,3,9],4,'Upper right');star('M1.3',[2,8],5,'Lower left');star('M1.4',[2,5,8],5,'Lower right')
for i,vals in enumerate([[0,3,6,9],[2,5,8,11],[3,3,3,3]],1):path(f'M2.{i}',vals,title=f'Row {i}')
tree('M2.4',0,6,8,4,6,'Bottom tree')
path('M3.1',[1,3,5,7,9],title='Upper path');diamond('M3.2',2,8,5,5,True,'Lower tied diamond')
path('M4.1',[0,3,6,6,6],fixed=[0,2],title='Upper board');path('M4.2',[0,0,0,3,6],fixed=[2,4],title='Lower board')
path('M5.1',[3,6,9,12],title='Top path');tree('M5.2',1,7,9,5,7,'Middle tree');diamond('M5.3',4,10,7,7,title='Bottom diamond')
graph('M6.1',[('a',0,1,False,'c'),('b',2,1,False,'c'),('c',2,0,False,'c'),('d',0,0,False,'c')],[('a','b'),('b','c'),('c','d'),('d','a')],'c = 0, 1, 2, 3, 4 or 5')
path('M6.2',['c']*3,fixed=[],title='c = 0, 1, 2, 3, 4 or 5')
path('O1.1',[0,5,10,15],title='Top path');tree('O1.2',0,8,9,5,7,'Middle tree');diamond('O1.3',2,14,8,8,True,'Bottom tied diamond')
graph('O2.1',[('a',0,1,True,0),('u',1,1,False,3),('v',2,1,False,6),('b',3,1,True,6),('w',2,-.2,False,7),('z',3.2,-.2,False,8),('c',4,-1.2,True,11)],[('a','u'),('u','v'),('v','b'),('v','w'),('w','z'),('z','v'),('z','c')],'Upper board')
diamond('O2.2',2,10,6,6,True,'Lower board')
graph('O3',[('a',0,0,True,0),('u',1,0,False,4),('v',2,0,False,6),('w',3,0,False,8),('b',4,0,True,12),('c',2,-1,True,6),('t',2,1,False,6)],[('a','u'),('u','v'),('v','w'),('w','b'),('v','c'),('u','t'),('t','w')],'Illustration only; the proof covers every allowed board')
path('O4.1',[0,4,8,8,8],fixed=[0,2],title='Upper board')
graph('O4.2',[('a',0,0,True,0),('u',1,0,False,4),('v',2,0,False,8),('b',3,0,True,12),('w',2,-1,False,8)],[('a','u'),('u','v'),('v','b'),('v','w')],'Lower board')
graph('O5',[('a',0,0,True,0),('u',1,0,False,6),('v',2,.7,False,10),('w',2,-.7,False,8),('b',3,.7,True,16),('c',3,-.7,True,8)],[('a','u'),('u','v'),('u','w'),('v','w'),('v','b'),('w','c')],'Both printed copies have this filling')
graph('O6.1',[('a',1,1,False,'c'),('b',0,0,False,'c'),('c',2,0,False,'c')],[('a','b'),('b','c'),('c','a')],'c = 0, 1, 2, 3 or 4')
graph('O6.2',[('a',0,0,False,'a'),('b',1,0,False,'a'),('c',2.6,0,False,'b'),('d',3.6,0,False,'b')],[('a','b'),('c','d')],'One lower board: a and b are chosen independently')
path('O7.1',[0,F(1,2),1],title='Row 1');path('O7.2',[0,1,2,3],title='Row 2');path('O7.3',[0,1,2],title='Row 3');path('O7.4',[0,F(1,3),F(2,3),1],title='Row 4')
