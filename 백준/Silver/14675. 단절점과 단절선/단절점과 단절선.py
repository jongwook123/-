T = int(input())
arr = {i : [] for i in range(T+1)}
for tc in range(T-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

N = int(input())
for i in range(N):
    t,k = map(int,input().split())
    if t == 1:
        if len(arr[k]) <= 1:
            print('no')
        else:
            print('yes')
    else:
        if arr[k]:
            print('yes')
        else:
            print('no')


