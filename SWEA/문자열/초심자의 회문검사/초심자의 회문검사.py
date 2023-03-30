T = int(input())

for tc in range(1,T+1):
    pal = list(input())
    a = 0
    for i in range(len(pal)//2):
        if pal[i] == pal[len(pal)-1-i]:
            a = 1
    print(f'#{tc} {a}')