import heapq
def dijkstra(x ,y):
    # 1. 출발점 세팅
    heap = []
    D[x][y] = 0
    heapq.heappush(heap,(D[x][y],x,y))  # 가중치 ,x,y
    # 2. 반복
    while heap:
        d,x,y = heapq.heappop(heap)



        # 4. 방문체크
        if visited[x][y] : continue
        visited[x][y] = 1
        if x == N- 1 and y == N - 1: return
        # 5. 인접정점 갱신
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 인접하고 방문 안한 정점
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                diff = 0
                if arr[x][y] < arr[nx][ny]:  # 오르막
                    diff = arr[nx][ny] - arr[x][y]
                # 갱신
                if D[nx][ny] > D[x][y] + 1 + diff:
                    D[nx][ny] = D[x][y] + 1 + diff
                    heapq.heappush(heap, (D[nx][ny], nx, ny))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    INF = 987654321
    N = int(input())
    D = [[INF] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    dijkstra(0, 0)
    print(f'#{tc} {D[N - 1][N - 1]}')