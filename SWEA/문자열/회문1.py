for tc in range(1,11):
    M = int(input())             # N = 판의 크기, M = 회문의 길이
    pal = [list(input()) for _ in range(8)]

    #가로
    count = 0
    for i in range(8):

        for j in range(8-M+1):
            new_list = []
            for k in range(M):
                new_list.append(pal[i][j+k])
            a = 0
            for s in range(M // 2):
                if new_list[s] == new_list[-(1 + s)]:
                    a = 1
                else:
                    a = 0
                    break

            count = count + a

    # 세로
    count_1 = 0
    for j in range(8):

        for i in range(8 - M + 1):
            new_list = []
            for k in range(M):
                new_list.append(pal[i+k][j])
            b = 0
            for s in range(M // 2):
                if new_list[s] == new_list[-(1 + s)]:
                    b = 1
                else:
                    b = 0
                    break

            count_1 = count_1 + b

    print(f'#{tc} {count+count_1}')