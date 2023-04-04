import sys
from collections import deque
di = [1,-1,0,0]
dj = [0,0,-1,1]


def bfs(i,j):
    Q = deque()
    Q.append([i,j])
    a = 1
    visited[i][j] = a

    while Q:
        i,j = Q.popleft()
        for s in range(4):
            ni = i + di[s]
            nj = j + dj[s]
            if 0 <= ni < T and 0 <= nj < T:
                if not visited[ni][nj] and arr[ni][nj]==1:
                    a += 1
                    visited[ni][nj] = a
                    Q.append([ni,nj])

    return a






T = int(sys.stdin.readline())
arr = [list(map(int,input())) for _ in range(T)]
visited = [[0] * T for _ in range(T)]
lst = []
for i in range(T):
    for j in range(T):
        if not visited[i][j] and arr[i][j] == 1:
            lst.append(bfs(i, j))

lst.sort()
print(len(lst))
for s in lst:
    print(s)
