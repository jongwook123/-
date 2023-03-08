def lizin(arr,key):
    mid = (len(arr) // 2)       # 200
    start = arr[0]              # 1
    end = len(arr)              # 400
    count = 0
    while mid != key:
        if mid == key:
            break
        elif arr != key:
            if key > mid:
                start = mid
                mid = int((end + start) // 2)
                count += 1
            elif key < mid:
                end = mid
                mid = int((end + start) // 2)
                count += 1
    return count


T = int(input())
for tc in range(1,T+1):

    page,key1,key2 = map(int,input().split())
    arr = []
    for i in range(1,page+1):
        arr.append(int(i))

    P1 = lizin(arr,key1)
    P2 = lizin(arr,key2)

    if P1 == P2:
        print(f'#{tc} 0')
    elif P1 > P2:
        print(f'#{tc} B')
    else:
        print(f'#{tc} A')
