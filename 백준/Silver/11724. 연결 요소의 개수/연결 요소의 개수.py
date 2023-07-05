import sys




def dfs(k):
    Visited[k] = 1
    for m in arr[k]:
        if not Visited[m]:
            dfs(m)


N,M= map(int,sys.stdin.readline().split())
arr = {i:[] for i in range(N+1)}
Visited=[0]*(N+1)
cnt =0
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

for s in range(1,N+1):
    if not Visited[s]:
        dfs(s)
        cnt+=1

print(cnt)