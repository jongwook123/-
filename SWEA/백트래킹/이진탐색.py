def bi(A,i):
    a = 0
    left = 0
    right = N - 1

    while left <= right:
        middle = (right+left)//2

        if i == A[middle]:
            return 0

        elif i > A[middle]:
            if a == 1:
                return -1
            else:
                left = middle + 1
                a = 1

        else:
            if a == 2:
                return -1
            else:
                right = middle - 1
                a = 2

    return -1

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr_1 = list(map(int,input().split()))
    arr_1.sort()
    arr_2 = list(map(int, input().split()))
    cnt = 0
    for i in arr_2:
        t = bi(arr_1,i)
        if t != -1:
            cnt += 1

    print(f'#{tc} {cnt}')


