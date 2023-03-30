T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = []
    n_arr = []
    for _ in range(N):
        s,e = map(int,input().split())
        arr.append((s,e))
    arr.sort(key=lambda x : (x[1]))

    s = 0
    c = 0
    for i in range(len(arr)):
        if s <= arr[i][0]:
            s = arr[i][1]
            c += 1

    print(f'#{tc} {c}')
