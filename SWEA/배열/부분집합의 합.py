T = int(input())

for tc in range(1,T+1):
    N = int(input())
    A = list(map(int,input().split()))

    sum_list = []
    for i in range(1<<N):
        new_list = []
        for j in range(N):
            if i & (1<<j):
                new_list.append(A[j])
        sum_list.append(new_list)

    flag = 0
    for i in range(1,len(sum_list)):
        if sum(sum_list[i]) == 0:
            flag = 1
            break
    if flag == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')