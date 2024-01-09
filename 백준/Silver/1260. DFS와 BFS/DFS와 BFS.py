from collections import deque


def dfs(d,visited,result):
    result.append(d)
    visited[d] = 1

    for s in arr[d]:
        if not visited[s]:
            dfs(s,visited,result)

    return result

def bfs(b):
    Q = deque()
    Q.append(b)
    Visited[b] = 1
    B = []
    while Q:
        t = Q.popleft()
        B.append(t)
        for s in arr[t]:
            if Visited[s] == 0:
                Q.append(s)
                Visited[s] = 1

    return B
N,M,V = map(int,input().split())
arr = {i : [] for i in range(N + 1)}
Visited = [0] * (N+1)
for s in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for s in range(N+1):
    arr[s].sort()

print(*dfs(V,Visited,[]))
Visited = [0] * (N+1)
print(*bfs(V))

