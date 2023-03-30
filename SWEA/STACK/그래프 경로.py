def dfs(S):
    # 방문처리
    visited[S] = 1

    for i in range(1,V+1):
        if adj_mat[S][i] == 1 and visited[i] == 0:
            dfs(i)


    if visited[G] == 1:
        return 1
    else:
        return 0



T = int(input())

for tc in range(1,T+1):

    V, E = map(int,input().split())
    adj_mat = [[0]* (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        s, e = map(int,input().split())
        adj_mat[s][e] = 1

    S,G = map(int,input().split())

    print(f'#{tc} {dfs(S)}')