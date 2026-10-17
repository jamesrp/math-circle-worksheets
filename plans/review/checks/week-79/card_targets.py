def reach(B,N=6):
    # exhaustive search over move choices
    def go(d,A,moved):
        if d>N: return moved==set(B)
        A=A|{2*d-1,2*d}
        return any(go(d+1,A-{c},moved|{c}) for c in A if c in B)
    return go(1,frozenset(),set())
for T in [{1,3,5,7,9,11},{2,3,5,7,8,11},{1,4,6,9,11,12},{2,4,6,8,10,12},{7,8,9,10,11,12}]:
    bad=[d for d in range(1,7) if sum(b<=2*d for b in T)<d]
    print(sorted(T),reach(T),'first short day',bad[:1])
