from collections import deque

def bfs(v):
    Q = deque()
    Q.append(v)
    visited[v] = 1
    while Q:
        v = Q.popleft()

        print(v,end=' ')
        for w in arr[v]:
            degree[w] -= 1
            if visited[w] == 0 and degree[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1









for tc in range(1,11):
    V,E = map(int,input().split())
    arr = {i:[] for i in range(V+1)}
    visited = [0] * (V+1)
    tmp = list(map(int,input().split()))
    degree = [0] * (V + 1)
    lst = []
    for s in range(E):
        arr[tmp[2*s]].append(tmp[2*s+1])

    for s in range(1,V+1):
        for i in range(1,V+1):
            degree[s] += arr[i].count(s)

    for i in range(1,len(degree)):
        if degree[i] == 0:
            lst.append(i)
    print(f'#{tc}',end=' ')
    for s in lst:
        bfs(s)
    print()


