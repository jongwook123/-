for tc in range(1, 11):
    N = int(input())
    L = list(map(int, input().split()))
    L_max = 0
    R_max = 0
    max_ = 0
    dif_ = 0
    for i in range(2, N - 2):
        if L[i - 1] >= L[i - 2]:
            L_max = L[i - 1]

        elif L[i - 1] <= L[i - 2]:
            L_max = L[i - 2]

        if L[i + 1] >= L[i + 2]:
            R_max = L[i + 1]

        elif L[i + 1] <= L[i + 2]:
            R_max = L[i + 2]

        if R_max >= L_max:
            max_ = R_max

        elif R_max <= L_max:
            max_ = L_max

        if L[i] >= max_:
            dif_ += L[i] - max_

    print(f'#{tc} {dif_}')