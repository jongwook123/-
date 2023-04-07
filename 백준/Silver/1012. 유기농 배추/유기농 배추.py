from collections import deque
def bfs(i,j):
    Q = deque()
    Q.append((i,j))
    visited[0][0] = 1
    while Q:
        i,j = Q.popleft()
        for s in range(4):
            ni = i + di[s]
            nj = j + dj[s]
            if 0 <= ni < N and 0 <=nj < M:
                if arr[ni][nj] == 1 and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    Q.append((ni,nj))

di = [1,-1,0,0]
dj = [0,0,1,-1]

T = int(input())
for tc in range(1,T+1):
    M,N,K = map(int,input().split())    # M : 가로 N : 세로
    A = max(M,N)
    cnt = 0
    arr = [[0] * (M+1) for _ in range(N+1)]
    visited = [[0] * (M+1) for _ in range(N+1)]
    for _ in range(K):
        s,e = map(int,input().split())
        arr[e][s] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                cnt += 1

    print(cnt)