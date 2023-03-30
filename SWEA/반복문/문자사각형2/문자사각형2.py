T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')

    list_n = [[0] * N for _ in range(N)]

    count = 0

    for s in range(N):
        for k in range(N):
            count += 1
            if s % 2 == 0:
                list_n[k][s] = chr((count%26) + 64 )
            else:
                list_n[N - k - 1][s] = chr((count%26) + 64)
    for k in range(len(list_n)):
        print(*list_n[k])

