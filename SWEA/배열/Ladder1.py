def search(arr,N):
    for s in range(N):
        if arr[N-1][s] == 2:
            i = N -1
            j = s
            return i,j


def solve(arr,i,j):
    while True:
        if i == 0:
            return j
        for s in range(3):
            ni = i + di[s]
            nj = j + dj[s]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] ==1:
                i = ni
                j = nj
                arr[i][j] = 9
                break






di = [0,0,-1]     #좌,우,상
dj = [-1,1,0]
N = 100
for _ in range(1,11):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    i,j = search(arr,N)

    print(f'#{T} {solve(arr,i,j)}')

