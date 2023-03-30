T = int(input())

if 1 <= T <= 10:
    for i in range(1,T+1):
        H, W = map(int,input().split())
        print(f'#{i}')

        if 2 <= H <= 9 and 2 <= W <= 9:
            if H <= W:
                for y in range(H,W+1):
                    for s in range(1,10,3):
                        print(f'{y} * {s} = {str(y * s).rjust(2)}   {y} * {s + 1} = {str(y * (s+1)).rjust(2)}   {y} * {s + 2} = {str(y * (s + 2)).rjust(2)}')
                    print()

            else:
                for p in range(H,W-1 ,-1):
                    for q in range(1, 10 ,3):
                        print(f'{p} * {q} = {str(p * q).rjust(2)}   {p} * {q + 1} = {str(p * (q + 1)).rjust(2)}   {p} * {q + 2} = {str(p * (q + 2)).rjust(2)}')
                    print()
                    print()
