#!/usr/bin/env python3
"""Independent ideal-linkage checks; finite tests complement the guide's proof."""
from math import cos,sin,pi,hypot,isclose
from fractions import Fraction as F

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(k,a): return tuple(k*x for x in a)
def sub(a,b): return add(a,mul(-1,b))
def area(poly):return abs(sum(x*v-y*u for (x,y),(u,v) in zip(poly,poly[1:]+poly[:1])))/2

def main():
 count=0
 for i in range(36):
  for j in range(36):
   if (i-j)%36 in (0,18):continue
   u=(80*cos(i*pi/18),80*sin(i*pi/18));v=(80*cos(j*pi/18),80*sin(j*pi/18))
   O=(0,0);X=u;Q=mul(2,u);Y=add(Q,v);T=add(u,v);P=add(Y,v)
   for a,b in [(O,X),(X,Q),(Q,Y),(Y,P),(X,T),(T,Y)]:
    assert isclose(hypot(*sub(b,a)),80,abs_tol=1e-8)
   assert all(isclose(a,2*b,abs_tol=1e-8) for a,b in zip(P,T))
   count+=1
 for shape in [[(0,0),(20,0),(20,20),(0,20)],[(0,0),(20,0),(20,10),(10,10),(10,20),(0,20)],[(0,0),(20,0),(0,20)]]:
  assert area([mul(2,p) for p in shape])==4*area(shape)
  assert area([mul(F(1,2),p) for p in shape])==area(shape)/4
 for O in [(40,140),(50,150),(70,140)]:
  for T in [(110,115),(110,165),(160,115),(160,165),(135,140)]:
   P=sub(mul(2,T),O)
   assert add(O,mul(F(1,2),sub(P,O)))==T
   for d in [(30,0),(0,10),(-10,5)]: assert sub(sub(mul(2,T),add(O,d)),P)==mul(-1,d)
 # Independently transcribed task geometry; checks exact paper regions, not thumbnails.
 O=(40,140)
 inputs={'A':[(115,125),(150,125),(150,145)],'B':[(120,120),(150,120),(140,150)],'C':[(115,135),(125,135),(125,150),(145,150),(145,125),(155,125)],'G':[(120,125),(140,125),(140,145),(120,145)],'H':[(120,125),(150,125),(150,135),(130,135),(130,145),(120,145)],'I':[(120,125),(150,125),(120,155)],'M':[(130,125),(150,125),(140,150)]}
 outputs={'D':[(190,110),(220,180),(270,160),(260,100),(210,140)],'E':[(200,110),(260,110),(260,150),(230,175),(200,150)],'J':[(200,110),(260,110),(260,150),(200,150)],'K':[(190,135),(240,135),(240,125),(270,145),(240,165),(240,155),(190,155)]}
 for pts in inputs.values():
  for T in pts:
   P=sub(mul(2,T),O);assert 110<=T[0]<=160 and 115<=T[1]<=165;assert 180<=P[0]<=290 and 90<=P[1]<=190
 for pts in outputs.values():
  for P in pts:
   T=mul(F(1,2),add(P,O));assert 110<=T[0]<=160 and 115<=T[1]<=165
 assert [area(inputs[k])/100 for k in 'GHI']==[4,4,F(9,2)]
 for T in inputs['M']:
  shifted=add(T,(10,0));assert shifted[0]<=160
  assert sub(mul(2,T),O)==sub(mul(2,shifted),(60,140))
 assert [mul(F(1,2),add(P,O)) for P in [(220,125),(260,155)]]==[(130,F(265,2)),(150,F(295,2))]
 print(f'PASS: {count} noncollapsed ideal poses; length, inverse, area, all task coordinates and anchor identities.')
 print('Finite checks do not certify physical hardware, print fit or classroom use.')
if __name__=='__main__':main()
