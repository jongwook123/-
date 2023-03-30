T = int(input())

for i in range(1,T+1):
    N = int(input())
    arr = list(str(input()))
    count = 0
    num_count = 0
    for ar in arr:
        if ar == '0':
            num_count = 0
        elif ar == '1':
            num_count += 1

        if num_count > count:
            count = num_count

    print(f'#{i} {count}')
