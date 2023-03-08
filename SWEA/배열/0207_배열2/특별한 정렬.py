T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    new_list = []
    for i in range(N - 1):  # 0~N
        min_idx = i
        for j in range(i + 1, N):
            if num_list[min_idx] > num_list[j]:
                min_idx = j
        num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]

    num1_list = num_list[:5]
    num2_list = num_list[5:]
    num2_list.reverse()
    for i in range(len(num1_list)):
        new_list.append(num2_list[i])
        new_list.append(num1_list[i])
    print(f'#{tc}', end=' ')
    print(*new_list)

# def selection_sort(a,N):
# 
#     for i in range(N-1):
#         idx = i
#         #짝수일 때, 최대값
#         if i % 2 == 0:
#             for j in range(i+1, N):
#                 if a[idx] > a[j]:
#                     idx = j
# 
#         #홀수일 때, 최소값
#         else:
#             for j in range(i+1, N):
#                 if a[idx] > a[j]:
#                     idx = j
#         # 교환환
#         a[idx], [i] = a[i], a[idx]
# 
# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
# 
#     selection_sort(arr,N)
#     print(f'#{tc}',end =' ')
#     for i in range(10):
#         print(arr[i], end=' ')
#     print()