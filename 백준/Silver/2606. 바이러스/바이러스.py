def dfs(v):
    global cnt
    visited[v] = 1
    cnt += 1
    for w in arr[v]:
        if not visited[w]:
            dfs(w)


T = int(input())
N = int(input())
visited = [0] * (T+1)
cnt = -1
arr = {i:[]for i in range(T+1)}

for i in range(N):
    s,e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)

dfs(1)
print(cnt)