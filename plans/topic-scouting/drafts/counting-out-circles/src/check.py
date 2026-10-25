def josephus(n, k=2, start=1):
    """People 1..n in a circle; counting starts at `start`; every k-th sits.
    Returns (survivor, order of sitting)."""
    standing = list(range(1, n+1))
    i = standing.index(start)
    order = []
    while len(standing) > 1:
        i = (i + k - 1) % len(standing)
        order.append(standing.pop(i))
        if i == len(standing):
            i = 0
    return standing[0], order

def J2(n): return josephus(n,2)[0]
def J3(n): return josephus(n,3)[0]

print("J2 1..40:", [J2(n) for n in range(1,41)])
print("J3 1..41:", [J3(n) for n in range(1,42)])
assert [J2(n) for n in range(1,17)] == [1,1,3,1,3,5,7,1,3,5,7,9,11,13,15,1]
assert [J3(n) for n in range(1,17)] == [1,2,2,1,4,1,4,7,1,4,7,10,13,2,5,8]
for n in range(1,1025):
    m = n.bit_length()-1; L = n - 2**m
    assert J2(n) == 2*L+1
    b = bin(n)[2:]; assert J2(n) == int(b[1:]+b[0],2)
for n in range(2,300):
    assert J3(n) == (J3(n-1)+2) % n + 1
print("J2(20,25,32,50,100,1000) =", [J2(n) for n in (20,25,32,50,100,1000)])
print("last two for 41,k=3:", josephus(41,3)[1][-1:], J3(41))
print("n<=100 with J2=9:", [n for n in range(1,101) if J2(n)==9])
print("n<=100 with J2=21:", [n for n in range(1,101) if J2(n)==21])
print("n<=100 with J2=n:", [n for n in range(1,101) if J2(n)==n])
print("n<=40 with J2=1:", [n for n in range(1,41) if J2(n)==1])
print("J3 n<=40 with J3=1:", [n for n in range(1,41) if J3(n)==1])
for n in (3,4,5,6,7,8):
    print(n, "k=2 order", josephus(n)[1], "k=3 order", josephus(n,3)[1], "J3", J3(n))
