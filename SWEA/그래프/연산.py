from collections import deque


def bfs(v):
    Q = deque()
    Q.append(v)
    # visited[v] = 1
    while Q:
        v = Q.popleft()
        if v == M:
            print(f'#{tc} {visited[v]}')
        ss = [v + 1,v-1,v*2,v-10]
        for w in ss:
            if 0 < w <= 1000000:
                if not visited[w]:
                    Q.append(w)
                    visited[w] = visited[v]+1



T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    visited = [0] * 1000001
    bfs(N)