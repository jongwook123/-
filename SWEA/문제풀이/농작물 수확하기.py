T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    sum_1 = 0
    sum_2 = 0

    for i in range(N//2):
        for j in range(-i,i+1):
            sum_1 += arr[i][(N//2)+j] + arr[-i-1][(N//2)+j]

    for s in range(N//2):
        sum_1 += arr[N//2][s] + arr[N//2][-(s+1)]


    sum_1 = sum_1 + arr[N//2][N//2]

    print(f'#{tc} {sum_1}')