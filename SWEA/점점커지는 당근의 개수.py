T = int(input())

for i in range(1, T + 1):
    N = int(input())
    arr = list(map(int, str(input()).split()))
    max_count = 0
    count = 1
    for s in range(N - 1):
        if arr[s] < arr[s + 1]:
            count += 1
        else:
            count = 1

        if count > max_count:
            max_count = count

    print(f'#{i} {max_count}')