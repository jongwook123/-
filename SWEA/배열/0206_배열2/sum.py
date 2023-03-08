def max_(number):
    max_2 = 0
    for i in range(len(number)):
        if number[i] > max_2:
            max_2 = number[i]
    return max_2


for tc in range(1,11):
    T = int(input())
    max_1 = []
    arr = [list(map(int,input().split())) for _ in range(100)]

    # 행부터
    hang_list = []
    for x in range(100):
        hang_sum = 0
        for y in range(100):
            hang_sum += arr[x][y]

        hang_list.append(hang_sum)
    max_1.append(max_(hang_list))

    #열

    yell_list = []
    for y in range(100):
        yell_sum = 0
        for x in range(100):
            yell_sum += arr[x][y]

        yell_list.append(yell_sum)
    max_1.append(max_(yell_list))

    #대각선
    dae1_sum = 0
    for x in range(100):
        for y in range(100):
            if x == y:
                dae1_sum += arr[x][y]
            else:
                pass

    max_1.append(dae1_sum)

    #역대각선

    ya1_sum = 0
    for x,y in zip(range(99,-1,-1), range(100)):
        ya1_sum += arr[x][y]
    max_1.append(ya1_sum)

    print(f'#{T} {max_(max_1)}')
