def find_(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                list_.append([i,j])

    return list_


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]


    # 가로
    flag = 0
    for i in range(N):
        a_1 = 0
        for j in range(N):
            if arr[i][j] == 'o':
                a_1 += 1
                if a_1 >= 5:
                    flag = 1
                    break
            else:
                a_1 = 0

    # 세로

    for j in range(N):
        a_2 = 0
        for i in range(N):
            if arr[i][j] == 'o':
                a_2 += 1
                if a_2 >= 5:
                    flag = 1
                    break
            else:
                a_2 = 0

    list_ = []
    find_(arr)

    # 대각
    for x,y in list_:
        a_3 = 0
        for i,j in zip(range(N),range(N)):
            if 0 <= x + i < N and 0 <= y + j < N:
                if arr[x+i][y+j] == 'o':
                    a_3 += 1
                    if a_3 >=5:
                        flag = 1
                        break
                else:
                    a_3 = 0
    # 역대각
    for x,y in list_:
        a_4 = 0
        for i,j in zip(range(N),range(N)):
            if 0 <= x + i < N and 0 <= y - j < N:
                if arr[x+i][y-j] == 'o':
                    a_4 += 1
                    if a_4 >= 5:
                        flag = 1
                        break
                else:
                    a_4 = 0




    if flag == 1:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')


