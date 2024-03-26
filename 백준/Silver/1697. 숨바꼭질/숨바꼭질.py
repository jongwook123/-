from collections import deque


def bfs(n):
    Q = deque()
    Q.append(n)

    Visited[n] = 0

    while Q:
        a = Q.popleft()

        if a == M:
            return
        da = [a - 1, a + 1, a * 2]
        for s in range(3):
            na = da[s]
            if not Visited[na] and 0 <= na <= 100000:
                Visited[na] = Visited[a] + 1
                Q.append(na)

N,M = map(int,input().split())
Visited = [0] * 1000000
bfs(N)

print(Visited[M])