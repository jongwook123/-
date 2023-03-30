T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dp = [[0]*N for _ in range(N)]

    # 열 초기화
    dp[0][0] = arr[0][0]
    for i in range(1,N):
        dp[i][0] = arr[i][0] + dp[i-1][0]

    # 행 초기화
    for i in range(1,N):
        dp[0][i] = arr[0][i] + dp[0][i-1]


    for i in range(1,N):
        for j in range(1,N):
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + arr[i][j]


    print(f'#{tc} {dp[N-1][N-1]}')