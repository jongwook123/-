T = int(input())
sum_ = 0
lst = sorted(list(map(int,input().split())))
for tc in range(T):
    sum_ += sum(lst[:tc+1])
    # print(sum(lst[:tc+1]))
print(sum_)