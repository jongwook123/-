import heapq
import math
import sys
def dijkstra(K):
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


V,E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())
arr = [[] for _ in range(V+1)]
dist = [math.inf] * (V+1)
for i in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    arr[u].append((v,w))

dijkstra(K)

for i in range(1,V+1):
    if dist[i] != math.inf:
        print(dist[i])
    else:
        print('INF')