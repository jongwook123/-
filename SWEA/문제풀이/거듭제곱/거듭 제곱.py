for tc in range(1,11):
    _ = input()
    N,M = map(int,input().split())
    a = N
    for i in range(M-1):
        a = a * N

    print(f'#{tc} {a}')