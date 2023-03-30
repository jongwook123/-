T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')

    list_n = []
    for n in range(N*N,0,-1):
        list_n.append(n)


    for s in range(N):
        new_list = []
        for k in range(1,N+1):
            new_list.append(chr((list_n[s-N*k]-1)%26+65))
        new_list.reverse()
        for i in range(len(new_list)):
            print(f'{new_list[i]} ',end='')
        print()