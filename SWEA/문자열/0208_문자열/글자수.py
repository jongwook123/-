T = int(input())

for tc in range(1,T+1):
    str1 = list(input())
    str2 = list(input())
    k = 0
    for i in str1:
        a = 0
        for j in str2:
            if j == i:
                a += 1
        if a > k:
            k = a
    print(f'#{tc} {k}')