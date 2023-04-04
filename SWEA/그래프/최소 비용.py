def dijkstra(i,j):
    D[i][j] = 0
    for i in range(N+1):
        for j in range(N+1):
            min_v = INF
            for v in range(N+1):





T = int(input())
for tc in range(1,T+1):
    INF = 987654321
    N = int(input())
    D = [[INF] * N for _ in range(N)]
    visited = [[0] * (N) for _ in range(N)]
    arr = [list(map(int,input().split())) for _ in range(N)]
    dijkstra(0,0)