from collections import deque
import sys
def bfs(k):
    global cnt
    Visited = [0] * (N + 1)
    Visited[k] = 1
    Q=deque()
    Q.append(k)

    while Q:
        x = Q.popleft()
        cnt += 1
        for s in arr[x]:
            if not Visited[s]:
                Visited[s] = 1
                Q.append(s)



N,M = map(int,sys.stdin.readline().split())
arr = {i:[] for i in range(N+1)}
lst = {i:0 for i in range(N+1)}

for _ in range(M):
    A,B = map(int,sys.stdin.readline().split())
    arr[B].append(A)

for s in range(1,N+1):
    cnt = 0
    if arr[s]:
        bfs(s)
        lst[s]=cnt

for i in range(1,N+1):
    if lst[i] == max(lst.values()):
        print(i,end=' ')