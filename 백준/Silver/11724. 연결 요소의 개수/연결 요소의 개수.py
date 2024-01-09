
def dfs(i):
    Visited[i] = 1

    for s in arr[i]:
        if Visited[s] == 0:
            dfs(s)

    return

N,M = map(int,input().split())
arr = {i : [] for i in range(N+1)}
Visited = [0] * (N+1)
cnt = 0
for _ in range(M):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for s in range(1,N+1):
    if Visited[s] == 0:
        dfs(s)
        cnt += 1

print(cnt)