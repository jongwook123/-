
T = int(input())

if 1 <= T <= 10:
    for i in range(1,T+1):
        H, W = map(int,input().split())
        print(f'#{i}')
        if 2 <= H <= 9 and 2 <= W <= 9:
            if H <= W:
                for s in range(1, 10):
                    for y in range(H,W+1):

                        print(f'{y} * {s} = {str(y * s).rjust(2)}',end='   ')
                    print()
            else:
                for q in range(1, 10):
                    for p in range(H,W-1 ,-1):
                        print(f'{p} * {q} = {q * p}', end='   ')
                    print()
                    print()