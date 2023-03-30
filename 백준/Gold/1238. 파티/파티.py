import heapq
import math
import sys
def dijkstra(K):
    dist = [math.inf] * (N + 1)
    Q = []
    heapq.heappush(Q,(0,K))
    dist[K] = 0

    while Q:
        v, u = heapq.heappop(Q)

        for s in arr[u]:
            weight = v + s[1]
            if weight < dist[s[0]]:
                dist[s[0]] = weight
                heapq.heappush(Q,(weight,s[0]))
    return dist

N, M, X = map(int,sys.stdin.readline().split())

arr = [[] for _ in range(N+1)]
dist = [math.inf] * (N+1)
for _ in range(M):
    u,v,w = map(int,sys.stdin.readline().split())
    arr[u].append((v,w))

dist = dijkstra(X)
dist[0] = 0

for i in range(1, N+1):
    if i != X:
        dist_1 = dijkstra(i)
        dist[i] += dist_1[X]

print(max(dist))
