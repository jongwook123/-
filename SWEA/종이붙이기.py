T = int(input())

for tc in range(1,T+1):
    N = int(input())
    N = N // 10
    list_ = [0] * (N+1)
    list_[0] = 1
    list_[1] = 3
    for i in range(2,N):
        a = i
        b = i - 1


        if i % 2 == 0:        #홀수
            list_[a] = list_[b]*2 -1
        else:
            list_[a] = (list_[b])*2 +1


    print(f'#{tc} {list_[N-1]}')