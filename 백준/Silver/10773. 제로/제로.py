T = int(input())
arr = []

for tc in range(T):
    K = int(input())
    if K != 0:
        arr.append(K)
    else:
        arr.pop(-1)

if not arr:
    print(0)
else:
    print(sum(arr))
