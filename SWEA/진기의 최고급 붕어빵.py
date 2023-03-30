def solve(arr,N):
    global a,S,B

    if min(arr) < M:
        a = 1
        return
    else:
        for y in range(0, N):
            while arr[y] != S:
                S += 1
                if S % M == 0:
                    B += K

            B -= 1
            if B < 0:
                a = 1
                return
        return


T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split())  # N =len(arr) K = M 시간동안 굽는 붕어빵
    arr = list(map(int,input().split()))         # 사람 시간초
    arr.sort()
    S = 0 # 시간초
    B = 0 # 붕어빵 개수
    a = 0


    solve(arr,N)
    if a == 0 and B >= 0:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')