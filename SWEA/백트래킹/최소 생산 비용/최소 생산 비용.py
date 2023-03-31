def perm(N,x,y):
    global min_
    if min_ < y:
        return
    if N == x:
        if min_ > y:
            min_ = y
    else:
        for i in range(N):

            if visited[i] ==0:
                visited[i] = 1
                perm(N,x+1,y+arr[x][i])
                visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    min_ = 999999999999999999999
    perm(N,0,0)
    print(min_)
