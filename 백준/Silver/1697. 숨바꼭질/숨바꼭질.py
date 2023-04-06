from collections import deque
def bfs(n):
    Q = deque()
    Q.append(n)
    # visited[n] = 1
    while Q:
        n = Q.popleft()
        if n == K:
            return
        ds = [n + 1, n - 1, 2 * n]
        for s in range(3):
            nx = ds[s]
            if 0 <= nx <= 100000:
                if not visited[nx]:
                    Q.append(nx)
                    visited[nx] = visited[n]+1

N,K = map(int,input().split())
visited = [0]*1000002
bfs(N)
print(visited[K])