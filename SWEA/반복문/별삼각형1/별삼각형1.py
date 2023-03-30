T = int(input())
for i in range(1,T+1):
    N , M = map(int,input().split())
    print(f'#{i}')
    if M == 1:
        for i in range(1,N+1):
            print(i * '*')


    elif M == 2:
        for i in range(N,0,-1):
            print(i * '*')


    elif M == 3:
        for i in range(1,N+1):
            print(' '*(3-i),end='')
            print((2 * i -1)*'*')