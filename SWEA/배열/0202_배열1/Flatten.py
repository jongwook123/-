for tc in range(1, 11):
    N = int(input())  # 덤프횟수
    L = list(map(int, input().split()))

    for _ in range(N):
        max_ = L.index(max(L))
        min_ = L.index(min(L))
        L[max_] = L[max_] - 1
        L[min_] = L[min_] + 1

    print(f'#{tc} {max(L) - min(L)}')