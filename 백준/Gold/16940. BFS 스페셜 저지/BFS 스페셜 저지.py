import sys
from collections import deque
def bfs(x):
    Q = deque()
    Q.append(x)
    visited[x] = 1

    while Q:
        x = Q.popleft()
        order_.append(x)
        for i in arr[x]:
            if not visited[i]:
                Q.append(i)
                visited[i] = 1


T = int(sys.stdin.readline())
arr = {i : [] for i in range(T+1)}
visited = [0]*(T+1)
for _ in range(T-1):
    s,e = map(int,sys.stdin.readline().split())
    arr[s].append(e)
    arr[e].append(s)
order = list(map(int,sys.stdin.readline().split()))
order_ = []
for i in range(1,T+1):
    arr[i].sort(key=lambda x:order.index(x))
bfs(1)
if order == order_:
    print(1)
else:
    print(0)