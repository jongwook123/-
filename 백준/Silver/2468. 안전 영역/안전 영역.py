from collections import deque
di = [1,-1,0,0]
dj = [0,0,1,-1]

def bfs(i,j):
    Q = deque()
    Q.append((i,j))
    while Q:
        i,j = Q.popleft()
        for s in range(4):
            ni = i + di[s]
            nj = j + dj[s]
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj]:
                    Q.append((ni,nj))
                    visited[ni][nj] = 1


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

max_ = 0
for i in range(101):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for k in range(N):
        for j in range(N):
            if arr[k][j] <= i:
                visited[k][j] = 1

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] =1
                bfs(i,j)
                cnt += 1

    if cnt ==0:
        break
    max_ = max(max_,cnt)

print(max_)