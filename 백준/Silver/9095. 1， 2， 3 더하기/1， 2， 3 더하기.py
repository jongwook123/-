
T = int(input())
for _ in range(T):
    n = int(input())

    d = [0] * 11

    d[1] = 1
    d[2] = 2
    d[3] = 4
    for s in range(4,n+1):
        d[s] = d[s-1] + d[s-2] + d[s-3]

    print(d[n])