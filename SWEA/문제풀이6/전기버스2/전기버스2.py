def dfs(n,sm):
    global cnt
    if cnt <= sm:
        return
    if n >= N-1:
        cnt = min(cnt, sm)
    else:
        for i in range(1,arr[n]+1):
            dfs(n+i,sm+1)



T = int(input())
for tc in range(1,T+1):
    N, *arr = map(int,input().split())
    cnt = 999999
    dfs(0,0)
    print(f'{tc} {cnt-1}')