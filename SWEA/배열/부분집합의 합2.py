
A = [1,2,3,4,5,6,7,8,9,10,11,12]

n = len(A)
sum_list = []
for i in range(1<<n):
    new_list =[]
    for j in range(n):
        if i & (1<<j):
            new_list.append(A[j])
    sum_list.append(new_list)

# print(sum_list)

T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())
    count = 0
    for list_1 in sum_list:
        if len(list_1) == N:
            if sum(list_1) == K:
                count += 1

    print(f'#{tc} {count}')