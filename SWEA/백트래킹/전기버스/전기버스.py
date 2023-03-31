def find(cnt,i,v):
    if i + v >= N-1:
        return cnt
    else:
        max_ = 0
        k = 0
        for s in range(1,v+1):
            if max_ < i + M[s+i]:
                max_ = i + M[s+i]
                k = s+i
        cnt += 1
        i = k
        v = v + max_ - k
        return find(cnt, i, v)




T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    N = arr.pop(0)
    M = arr
    cnt = 0 # 충전횟수
    i = 0   # 인덱스
    v = M[i]  # 배터리 용량
    print(f'#{tc} {find(cnt,i,v)}')
