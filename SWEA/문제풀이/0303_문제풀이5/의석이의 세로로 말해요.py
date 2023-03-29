T = int(input())
for tc in range(1,T+1):
    print(f'#{tc}',end = ' ')
    arr = [list(input()) for _ in range(5)]
    max_ = 0
    for i in range(5):
        if len(arr[i]) > max_:
            max_ = len(arr[i])


    for j in range(max_):
        for i in range(5):
            if 0 <= j < len(arr[i]):
                print(arr[i][j],end='')

    print()
