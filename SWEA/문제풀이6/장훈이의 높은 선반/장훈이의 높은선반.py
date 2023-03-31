def dfs(n,sm):
    global ans
    # 최소값 구할때 항상 성공하는 가지치기
    # if ans <= sm-B:
    #     return
    if ans == 0:    # 이미 만점!
        return
    if n == N:
        if sm >=B:
            ans = min(ans , sm-B)
        return
    dfs(n+1,sm+arr[n])  # 포함
    dfs(n+1,sm)         # 미포함



T = int(input())
for tc in range(1,T+1):
    N,B = map(int,input().split())
    arr = list(map(int,input().split()))
    ans = N*1000000
    dfs(0,0)
    print(f'#{tc} {ans}')