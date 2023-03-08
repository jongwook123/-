T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    sum_list = []
    for i in range(N):
        for j in range(N):
            new_list = []
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[i][j]-arr[ni][nj] >= 0:
                        new_list.append(arr[i][j]-arr[ni][nj])
                    elif arr[i][j] - arr[ni][nj] < 0:
                        new_list.append(arr[ni][nj] - arr[i][j])

            sum_list.append(sum(new_list))

    print(f'#{tc} {sum(sum_list)}')