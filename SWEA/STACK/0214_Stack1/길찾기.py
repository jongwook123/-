def dfs(S):
    # 방문처리
    visited[S] = 1

    for i in range(1,100+1):
        if adj_mat[S][i] == 1 and visited[i] == 0:
            dfs(i)

    if visited[G] == 1:
        return 1
    else:
        return 0




for tc in range(1,11):

    V, E = map(int,input().split())
    adj_mat = [[0]* (100+1) for _ in range(100+1)]
    visited = [0] * (100+1)
    temp = list(map(int, input().split()))
    for i in range(E):
        s, e = temp[2*i], temp[2*i+1]
        adj_mat[s][e] = 1

    S,G = 0,99
    print(f'#{tc} {dfs(S)}')