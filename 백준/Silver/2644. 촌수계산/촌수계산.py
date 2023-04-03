def dfs(v):
    for w in arr[v]:
        if not visited[w]:
            visited[w] = visited[v] + 1
            dfs(w)



T = int(input())
a,b = map(int,input().split())
N = int(input())
arr = {i:[] for i in range(T + 1)}
visited = [0] * (T+1)
flag = 0
ss = 0
for tc in range(N):
    s,e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)

dfs(a)

if visited[b] == 0:
    print(-1)
else:
    print(visited[b])