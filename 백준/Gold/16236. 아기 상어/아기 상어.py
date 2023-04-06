from collections import deque

def find():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                arr[i][j] = 0
                return i,j

def bfs(i,j):
    ca = []
    visited = [[False]*N for _ in range(N)]
    visited[i][j] = True
    q = deque()
    q.append((0,i,j))
    min_w = float('inf')

    while q:
        w ,i,j = q.popleft()
        for s in range(4):
            ni = i + di[s]
            nj = j + dj[s]
            if ni >= N or ni <0 or nj >= N or nj < 0:
                continue
            if visited[ni][nj] or arr[ni][nj] > size:
                continue
            visited[ni][nj] = True
            dw = w+1

            if 0 < arr[ni][nj] < size:
                if min_w == float('inf'):
                    min_w = dw
                elif dw > min_w:
                    return ca
                ca.append((dw,ni,nj))
            q.append((dw,ni,nj))
    return ca



di = [0,0,1,-1]
dj = [1,-1,0,0]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
size = 2
eat = 0
i,j = find()
ans = 0

while True:
    A = bfs(i,j)
    if not A:
        break

    A.sort()
    w,i,j = A[0]
    ans += w
    arr[i][j] = 0

    eat += 1
    if size == eat:
        size += 1
        eat = 0
print(ans)