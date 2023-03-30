T = int(input())


for tc in range(1,T+1):
    arr = [[0] * 10 for _ in range(10)]

    N = int(input())
    for n in range(N):
        arr_list = list(map(int,input().split()))
        x1 = arr_list[0]
        y1 = arr_list[1]
        x2 = arr_list[2]
        y2 = arr_list[3]

        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                arr[x][y] += 1
    count = 0

    for arr_1 in arr:
        for arr_2 in arr_1:
            if arr_2 == 2:
                count += 1
            else:
                pass

    print(f'#{tc} {count}')