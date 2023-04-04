def dijkstra(s):
    # 출발점 선택
    D[s] = 0
    # 모든 도시 선택
    for i in range(N+1):
        # 방문 안한 정점 and 가중치의 최소값
        min_v = INF
        for v in range(N+1):
            if not visited[v] and D[v] < min_v:
                min_v = D[v]
                u = v
        # 정점 선택 방문체크
        visited[u] = 1
        # 정점의 인접정점 갱신
        for v in range(N+1):
            if adj_mat[u][v] and not visited[v]:
                if D[v] > D[u] + adj_mat[u][v]:
                    D[v] = D[u] + adj_mat[u][v]

T = int(input())
for tc in range(1,T+1):
    INF = 987654321
    N, E = map(int,input().split())
    adj_mat = [[0] * (N+1) for _ in range(N+1)]
    D = [INF] * (N+1)
    visited = [0] * (N+1)
    for i in range(E):
        s,e,d = map(int,input().split())
        adj_mat[s][e]  = d

    dijkstra(0)
    print(f'#{tc} {D[N]}')
