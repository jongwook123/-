T = int(input())

for tc in range(1,T+1):
    N= int(input())
    L = list(map(int,input().split()))
    max_ = 0
    min_ = 1000000
    for l in range(len(L)):
        if L[l] > max_:
            max_ = L[l]

        if L[l] < min_:
            min_ = L[l]

    print(f'#{tc} {max_ - min_}')