def dfs(x,y):
    global flag
    arr[x][y] = 9

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 인덱스 체크
        if nx < 0 or nx == N:
            continue
        if ny <0 or ny == N:
            continue
        # 방문체크
        if arr[nx][ny] == 9:
            continue
        # 벽체크
        if arr[nx][ny] == 1:
            continue
        if arr[nx][ny] == 3:
            flag = 1
            return
        dfs(nx,ny)


def search(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i,j

T = int(input())

dx = [-1,0,1,0] #상,좌,하,우
dy = [0,-1,0,1]
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    x,y = search(arr)
    flag = 0
    dfs(x,y)
    print(f'#{tc} {flag}')