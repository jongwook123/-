T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    for s in range(1,N+1):
        for n in range(1,N+1):
            print(f'{n*s} ',end='')
        print()
