def merge(left,right):
    i, j = 0, 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged += left[i:]
    merged += right[j:]
    return merged

def mergesort(arr):
    global cnt
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])
    if left[-1] > right[-1]:
        cnt += 1
    return merge(left,right)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    K = mergesort(arr)

    print(f'#{tc} {K[N//2]} {cnt}')