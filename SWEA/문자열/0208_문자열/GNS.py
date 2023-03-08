T = int(input())

for tc in range(1,T+1):
    N, M = input().split()
    Num = input().split()
    M = int(M)
    num_list = {}
    for a in Num:
        list_1 = []
        if a in num_list:
            num_list[a].append(a)
        else:
            num_list[a] = [a]


    print(f'#{tc}')
    print(*num_list['ZRO'],*num_list['ONE'],*num_list['TWO'],*num_list['THR'],*num_list['FOR'],*num_list['FIV'],*num_list['SIX'],*num_list['SVN'],*num_list['EGT'],*num_list['NIN'])