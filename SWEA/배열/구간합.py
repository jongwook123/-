T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    max_ = 0
    min_ = 10000000
    for i in range(N - M + 1):  # 0~8
        sum_ = L[i]
        for j in range(1, M):
            sum_ += L[i + j]

        if max_ < sum_:
            max_ = sum_

        if min_ > sum_:
            min_ = sum_
    print(f'#{tc} {max_ - min_}')

