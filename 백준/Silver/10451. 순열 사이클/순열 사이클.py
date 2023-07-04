import sys
sys.setrecursionlimit(10**7)

def dfs(k):
    Visited[k] = 1
    next = arr[k-1]
    if Visited[next] == 0:
        dfs(next)




T = int(input())

for _ in range(T):
    cnt = 0
    N = int(input())
    arr = list(map(int,input().split()))

    Visited = [0]*(N+1)
    for s in range(N+1):
        if Visited[s] == 0:
            dfs(s)
            cnt += 1
    print(cnt)