
def bfs(x ,y):
    # 1. 출발점 세팅
    Q = []
    D[x][y] = 0
    Q.append((x,y))
    # 2. 반복
    while Q:
        x,y = Q.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 인접하고 방문 안한 정점
            if 0 <= nx < N and 0 <= ny < N:
                diff = 0
                if arr[x][y] < arr[nx][ny]:  # 오르막
                    diff = arr[nx][ny] - arr[x][y]
                # 갱신
                if D[nx][ny] > D[x][y] + 1 + diff:
                    D[nx][ny] = D[x][y] + 1 + diff
                    Q.append((nx,ny))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    INF = 987654321
    N = int(input())
    D = [[INF] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    bfs(0, 0)
    print(f'#{tc} {D[N - 1][N - 1]}')