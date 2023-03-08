T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())             # N = 판의 크기, M = 회문의 길이
    pal = [list(input()) for _ in range(N)]
    t =[]
    # 가로
    for i in range(N):
        for j in range(N-M+1):
            new_list = []
            for k in range(M):
                new_list.append(pal[i][j+k])

            a = 1
            for s in range(M // 2):
                if new_list[s] == new_list[-(1 + s)]:
                    a = 1
                else:
                    a = 0
                    break
            if a == 1:
                print(f'#{tc}',end=' ')
                print(''.join(new_list))

    # 세로
    for j in range(N):
        for i in range(N - M + 1):
            new_list = []
            for k in range(M):
                new_list.append(pal[i+k][j])


            a = 1
            for s in range(M//2):
                if new_list[s] == new_list[-(1+s)]:
                    a = 1
                else:
                    a = 0
                    break
            if a==1:
                print(f'#{tc}',end=' ')
                print(''.join(new_list))
