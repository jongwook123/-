def dfs(v):
    visited[v] = k
    for w in arr[v]:
        if not visited[w]:
            dfs(w)

T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    tmp = list(map(int,input().split()))
    arr = {i:[] for i in range(N+1)}
    visited = [0] * (N+1)
    for i in range(M):
        s,e = tmp[i*2],tmp[i*2+1]
        arr[s].append(e)
        arr[e].append(s)
    cnt = 0
    for k in range(1,N+1):
        if not visited[k]:
            dfs(k)
            cnt += 1

    print(f'#{tc} {cnt}')