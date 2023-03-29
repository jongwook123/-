import sys
sys.setrecursionlimit(100000)
def dfs(x):
    if visited[x] == 1:
        return

    visited[x] = 1
    order_.append(x)

    for i in arr[x]:
        if not visited[i]:
            dfs(i)


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
dfs(1)
if order == order_:
    print(1)
else:
    print(0)