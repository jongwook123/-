def f(k,n):
    global cnt
    if n == k:
        sum_ = 0
        for i in range(n):
            if visited[i] == 1:
                sum_ += arr[i]
        if sum_ == K:
            cnt += 1
    else:
        visited[k] = 0
        f(k+1,n)
        visited[k] = 1
        f(k+1,n)




T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    visited = [0] * N
    cnt = 0
    f(0,N)
    print(cnt)


# 교수님 풀이
def dfs(n,sm):
    global ans
    # [1] 종료조건(n에관련): 반드시 정답처리는 이곳
    if n == N:
        if sm==K:
            ans += 1
        return
    # [2] 하부 호출
    dfs(n+1,sm+lst[n])  # 포함
    dfs(n+1,sm)         # 포함 x

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    lst = list(map(int,input().split()))

    ans = 0
    dfs(0,0)
    print(f'#{tc} {ans}')