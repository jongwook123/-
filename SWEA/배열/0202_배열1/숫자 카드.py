T = int(input())
for tc in range(1,T+1):
    N = int(input())
    A = list(map(int,input()))
    C = [0] * 10
    B = [0] * 10

    for i in range(len(A)):
        C[A[i]] += 1



    max_ = 0
    for i in range(len(C)):
        if C[i] >=max_:
            max_ = C[i]
            idx = i


    print(f'#{tc} {idx} {max_}')
