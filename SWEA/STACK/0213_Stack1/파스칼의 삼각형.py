T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print(f'#{tc}')
    for n in range(0,N):
        if n % 2 == 0:
            A = [0]*(n+1)       #i 짝수리스트
            if n == 0:
                A[0] = 1
                A[-1] = 1
            else:
                for s in range(1,(n//2)+1):
                    A[0] = 1
                    A[s] = B[s] + B[s-1]
                    A[-s-1] = A[s]
                    A[-1] = 1

            print(*A)

        elif n % 2 != 0:
            B = [0]*(n+1)       #i 홀수리스트
            if n == 1:
                B[0] = 1
                B[-1] = 1
            else:
                for s in range(1,(n//2)+2):
                    B[0] = 1
                    B[s] = A[s] + A[s-1]
                    B[-s-1] =B[s]
                    B[-1] =1

            print(*B)

