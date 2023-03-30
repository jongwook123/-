def solve(arr,N,M):
    a = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for s in range(9):
                ni = i + di[s]
                nj = j + dj[s]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[i][j] > arr[ni][nj]:
                        cnt += 1
            if cnt >= 4:
                a += 1
    return a




di = [-1,-1,-1,0,0,0,1,1,1]
dj = [-1,0,1,-1,0,1,-1,0,1]
T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())  # N : 세로 M : 가로
    arr = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{tc} {solve(arr,N,M)}')