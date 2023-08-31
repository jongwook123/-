from collections import deque

def bfs():
    Q = deque()
    Q.append((start_i, start_j))
    visited[start_i][start_j] = True
    while Q:
        i, j = Q.popleft()

        for s in range(4):
            ni = i + di[s]
            nj = j + dj[s]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1 and not visited[ni][nj]:
                    arr_1[ni][nj] = arr_1[i][j] + 1
                    Q.append((ni, nj))
                    visited[ni][nj] = True

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr_1 = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
di = [1, 0, 0, -1]
dj = [0, 1, -1, 0]

start_i, start_j = None, None
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            start_i, start_j = i, j
            break
    if start_i is not None:
        break

bfs()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            arr_1[i][j] = 0
        elif arr[i][j] == 2:
            arr_1[i][j] = 0
        elif arr_1[i][j] == 0:
            arr_1[i][j] = -1
        print(arr_1[i][j], end=" ")
    print()
