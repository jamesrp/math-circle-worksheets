def labels(S, N):
    L=[]
    for n in range(N+1):
        L.append(not any(n-m>=0 and L[n-m] for m in S))
    return L
def audit(S, start, takes):
    L=labels(S,start)
    n=start
    for i,t in enumerate(takes,1):
        mistake = (not L[n]) and (not L[n-t])
        print(f"turn {i}: pile {n} take {t} -> {n-t}  {'MISTAKE' if mistake else ''}")
        n-=t
    print('ends at', n)
audit((1,2),8,[2,1,1,1,2,1])
audit((1,3,4),16,[1,4,1,3,4,3])
L=labels((1,3,4),100); print('2-3 P7', {n:('L' if L[n] else 'W') for n in [23,28,33,50,100]}, '6:',L[6],'8:',L[8],'14:',L[14])
L=labels((1,2),40); print('K1 traps', [n for n in range(1,25) if L[n]], '9 trap?', L[9])
L=labels((1,2,3),12); print('K1 P8 traps', [n for n in range(1,13) if L[n]])
L=labels((1,3,5),20); print('2-3 P8', [n for n in range(1,21) if L[n]])
L=labels((1,6,9),39); print('4-5 P6', ''.join('L' if x else 'W' for x in L))
