T = int(input())
for i in range(1, T + 1):
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    while N % 2 == 0:
        N = N / 2
        a += 1
    N1 = N
    while N1 % 3 == 0:
        N1 = N1 / 3
        b += 1
    N2 = N1

    while N2 % 5 == 0:
        N2 = N2 / 5
        c += 1
    N3 = N2

    while N3 % 7 == 0:
        N3 = N3 / 7
        d += 1
    N4 = N3

    while N4 % 11 == 0:
        N4 = N4 / 11
        e += 1
    N5 = N4
    print(f'#{i} {a} {b} {c} {d} {e}')