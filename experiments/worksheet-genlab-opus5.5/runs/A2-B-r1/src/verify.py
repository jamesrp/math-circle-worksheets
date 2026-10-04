from functools import lru_cache
def win1(moves):
    @lru_cache(None)
    def w(n):
        return any(n-m>=0 and not w(n-m) for m in moves)
    return w
def win2(moves):
    @lru_cache(None)
    def w(a,b):
        opts=[(a-m,b) for m in moves if a-m>=0]+[(a,b-m) for m in moves if b-m>=0]
        return any(not w(*o) for o in opts)
    return w
w12=win1((1,2)); w123=win1((1,2,3)); w13=win1((1,3)); w134=win1((1,3,4))
print("K1 P1 {1,2} 1..6 first wins:", [n for n in range(1,7) if w12(n)])
print("K1 P2 winning moves:", {n:[m for m in (1,2) if n-m>=0 and not w12(n-m)] for n in (4,5,7,8,10,11)})
print("K1 P3 first loses 1..15:", [n for n in range(1,16) if not w12(n)])
print("K1 P4 20:", w12(20), [m for m in (1,2) if not w12(20-m)])
print("K1 P5 {1,2,3} 3..8:", {n:('1st' if w123(n) else '2nd') for n in range(3,9)})
print("K1 P6 {1,3} 1..9 first wins:", [n for n in range(1,10) if w13(n)])
W2=win2((1,2))
print("K1 P7:", {p:('1st' if W2(*p) else '2nd') for p in [(2,2),(3,3),(2,3),(4,4)]})
print("23 P1:", ['1st' if w12(n) else '2nd' for n in range(1,21)])
print("23 P2:", {n:('1st' if w12(n) else '2nd', [m for m in (1,2) if not w12(n-m)]) for n in (24,29,31,45)})
print("23 P3 {1,3,4}:", {n:('1st' if w134(n) else '2nd') for n in range(1,21)})
mv=(1,3,4)
def claim_move(n,m): return not w134(n-m)  # taking m from n wins?
print("Mia 5 take4:", claim_move(5,4), "Leo 7 second:", not w134(7), "Zoe 9 first:", w134(9), "Sam 10 take1:", claim_move(10,1))
print("Ana: piles where taking 4 is not winning but some move wins:", [n for n in range(4,30) if w134(n) and w134(n-4)])
print("23 P5:", {n:('1st' if w134(n) else '2nd') for n in (30,50,100)})
print("23 P6:", {p:('1st' if W2(*p) else '2nd') for p in [(4,4),(3,5),(3,6),(1,4)]})
for r in [(1,2,3),(1,3),(1,2,3,4),(1,4)]:
    print("23 P7", r, 35, '1st' if win1(r)(35) else '2nd')
print("45 P2 100:", '1st' if w12(100) else '2nd', '1st' if w123(100) else '2nd')
[w134(i) for i in range(1001)]
print("45 P4:", '1st' if w134(100) else '2nd', '1st' if w134(1000) else '2nd')
for r in [(1,3,5),(1,4),(1,4,5),(1,2,4),(1,2,5),(1,2,6),(1,2,7),(1,2,9),(1,2,10),(1,2,3,5)]:
    w=win1(r); print("rule",r,"second wins 1..24:",[n for n in range(1,25) if not w(n)])
W134=win2((1,3,4))
print("grid a:")
for b in range(8,-1,-1): print(b, ''.join('L' if not W2(a,b) else '.' for a in range(9)))
print("grid b:")
for b in range(10,-1,-1): print(b, ''.join('L' if not W134(a,b) else '.' for a in range(11)))
