T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())      # N : 판 M : 파리채
    arr = [list(map(int,input().split())) for _ in range(N)]

    di_1 = [-1,0,1,0]       # 가세
    dj_1 = [0,1,0,-1]

    di_2 = [-1,-1,1,1]      # 대각
    dj_2 = [-1,1,-1,1]

    max_ = 0
    for i in range(N):      #가세
        for j in range(N):
            a = 0
            for s in range(1,M):
                for k in range(4):
                    ni = i + di_1[k] * s
                    nj = j + dj_1[k] * s
                    if 0 <= ni < N and 0 <= nj < N:
                        a += arr[ni][nj]
            a += arr[i][j]
            if a > max_:
                max_ = a

    for i in range(N):      #가세
        for j in range(N):
            a = 0
            for s in range(1,M):
                for k in range(4):
                    ni = i + di_2[k] * s
                    nj = j + dj_2[k] * s
                    if 0 <= ni < N and 0 <= nj < N:
                        a += arr[ni][nj]
            a += arr[i][j]
            if a > max_:
                max_ = a


    print(f'#{tc} {max_}')