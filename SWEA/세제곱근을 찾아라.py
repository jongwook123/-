T = int(input())
for tc in range(1, T + 1):
    start = 1
    a = -1
    N = int(input())
    end = N
    if N == 1:
        a = 1


    else:
        while start < end:
            mid = (start + end) // 2
            if mid ** 3 == N:
                a = mid
                break
            elif mid ** 3 > N:
                end = mid - 1
            else:
                start = mid + 1

    print(f'{tc} {a}')

# feat. 구미1반(김재욱, 김선영)