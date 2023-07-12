from collections import deque
import sys

def bfs(i,j,arr):
    Q = deque()
    Q.append([i,j])
    arr[i][j] = 0
    cnt = 1
    while Q:

        a,b = Q.popleft()


        for s in range(4):
            na = a + da[s]
            nb = b + db[s]
            if 0 < na <= N and 0 < nb <= M and arr[na][nb] == 1:
                    Q.append([na,nb])
                    arr[na][nb] = 0
                    cnt += 1
    return cnt

da = [0,-1,0,1]
db = [1,0,-1,0]

N,M,K = map(int,sys.stdin.readline().split())
arr = [[0]*(M+1) for _ in range(N+1)]
max_ = 0

for _ in range(K):
    r,c = map(int,sys.stdin.readline().split())
    arr[r][c] = 1

for i in range(1,N+1):
    for j in range(1,M+1):
        if arr[i][j] == 1:
            V = bfs(i,j,arr)
            max_ = max(V,max_)

print(max_)