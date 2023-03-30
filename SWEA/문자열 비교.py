T = int(input())

for tc in range(1,T+1):
    str1 = list(input())
    str2 = list(input())
    a = 0
    for s in range(len(str2)):
        if a == 0:
            if str2[s] == str1[0]:
                if len(str2) - s +1 > len(str1):
                    for i in range(len(str1)):
                        if str2[s+i] == str1[i]:
                            a = 1
                        else:
                            a = 0
                            break
        elif a == 1:
            break

    if a == 1:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')