def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt +=1
            else:
                if cnt == N:
                    ans +=1
                cnt = 0
    return ans


T = int(input())
for tc in range(1,T+1):
    M, N = map(int,input().split())   # M : 판의 크기 N : 테스트 개수
    pal = [list(map(int,input().split())) + [0] for _ in range(M)] + [[0]*(M+1)]

    pal_t = list(map(list,zip(*pal)))
    ans = count(pal) + count(pal_t)
    print(f'#{tc} {ans}')