for tc in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    while True:
        cnt = 0
        for i in range(N):
            for j in range(N):
                    if arr[i][j] == 1:
                        if 0 <= i + 1 < N:
                            if arr[i+1][j] == 0:
                                arr[i][j] = 0
                                arr[i+1][j] = 1
                                cnt += 1
                            elif arr[i+1][j] == 1:
                                arr[i][j] = 0
                                cnt += 1

                    if arr[i][j] == 2:
                        if 0 <= i-1 < N:
                            if arr[i - 1][j] == 0:
                                arr[i][j] = 0
                                arr[i - 1][j] = 2
                                cnt += 1

                            elif arr[i - 1][j] == 2:
                                arr[i][j] = 0
                                cnt += 1
        if cnt == 0:
            break
    for j in range(N):
        if arr[0][j] == 2:
            arr[0][j] = 0
        if arr[99][j] == 1:
            arr[99][j] = 0

    cnt_1 = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt_1 += 1
    print(f'#{tc} {cnt_1}')

