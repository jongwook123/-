T = int(input())

for i in range(1,T+1):
    H, W = map(int,input().split())
    print(f'#{i}')
    for h in range(1,(H+1)):
        for w in range(W):
            a = h + H*w
            print(f'{a} ',end = '')
        print()
