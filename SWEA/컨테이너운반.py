T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())  # N : 컨테이너 수 M : 트럭 수
    list_N = list(map(int,input().split())) # 화물의 무게
    list_M = list(map(int,input().split())) # 적재용량
    list_N.sort(reverse=True)
    list_M.sort(reverse=True)
    n = 0
    m = 0
    sum_ = 0
    while True:
        if n == len(list_N) or m == len(list_M):
            break
        elif list_N[n] <= list_M[m]:
            sum_ += list_N[n]
            m += 1
            n += 1
        elif list_N[n] > list_M[m]:
            n += 1
    print(f'#{tc} {sum_}')
