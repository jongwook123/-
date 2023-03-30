import sys

INF = int(1e9)
def bell(K):
    dist[K] = 0

    for i in range(1,N+1):
        for j in range(M):
            now, nxt, weight = arr[j][0],arr[j][1],arr[j][2]
            if dist[now] != INF and dist[nxt] > dist[now] + weight:
                dist[nxt] = dist[now] + weight

                if i == N:
                    return True
    return False


N,M = map(int,sys.stdin.readline().split())
arr = []

dist = [INF]*(N+1)
for _ in range(M):
    A,B,C = map(int,sys.stdin.readline().split())
    arr.append((A,B,C))


nc = bell(1)

if nc:
    print(-1)
else:
    for i in range(2,N+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])