from collections import deque

def bfs(v):
    Q = deque()
    Q.append(v)
    visited[v] = 1
    while Q:
        v = Q.popleft()
        if v == G:
            return
        A = [v+U,v-D]
        for s in A:
            nv = s
            if 0 < nv <= F:
                if not visited[nv]:
                    Q.append(nv)
                    visited[nv] = visited[v] + 1

F,S,G,U,D = map(int,input().split())
visited = [0] * (F+1)
# F = 가장 높은 층
# S = 출발 층
# G = 목적지
# U = 위로 U칸
# D = 아래로 D칸


bfs(S)
if visited[G]:
    print(visited[G]-1)
else:
    print('use the stairs')