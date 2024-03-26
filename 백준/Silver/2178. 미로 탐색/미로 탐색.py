from collections import deque



di = [0,0,1,-1]
dj = [1,-1,0,0]

def bfs(a,b):

    Q = deque()
    Q.append((a,b))
    Visited[a][b] = 1

    while Q:
        i,j = Q.popleft()
        if i == N - 1 and j == M - 1:
            return
        for s in range(4):
            ni = i + di[s]
            nj = j + dj[s]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1:
                    if not Visited[ni][nj]:
                        Q.append((ni,nj))
                        Visited[ni][nj] = Visited[i][j] + 1




N,M = map(int,input().split())
arr = []
Visited = [[0] * M for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int,input())))
bfs(0,0)


print(Visited[N-1][M-1])