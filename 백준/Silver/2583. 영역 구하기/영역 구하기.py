import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    Q = deque()
    Q.append((i, j))

    size = 1

    while Q:
        x, y = Q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    Q.append((nx, ny))
                    size += 1
    result.append(size)


M, N, K = map(int, sys.stdin.readline().rstrip().split())
arr = [[0] * N for _ in range(M)]
arr_V = []
result = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    arr_V.append([x1, y1])
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

cnt = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            arr[i][j] = 1
            bfs(i, j)
print(len(result))
print(*sorted(result))

