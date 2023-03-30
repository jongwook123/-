T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    a_1 = []
    a_2 = []
    flag_1 = 0
    flag_2 = 0
    for i in range(0,len(arr)-1,2):
        a_1.append(arr[i])
        a_2.append(arr[i+1])
        a_1.sort()
        a_2.sort()
        for s in range(len(a_1)-2):
            # triplet
            if a_1[s] == a_1[s+1] and a_1[s] == a_1[s+2]:
                flag_1 = 1
                break
            if a_2[s] == a_2[s+1] and a_2[s] == a_2[s+2]:
                flag_2 = 1
                break

            # run
            if a_1[s] + 1 == a_1[s + 1]:
                for i in range(2,len(a_1)-s):
                    if a_1[s] + 2 == a_1[s + i]:
                        flag_1 = 1
                        break

            if a_2[s] + 1 == a_2[s + 1]:
                for i in range(2,len(a_2)-s):
                    if a_2[s] + 2 == a_2[s + i]:
                        flag_2 = 1
                        break

        if flag_1 ==1:
            print(f'#{tc} 1')
            break
        elif flag_2 ==1:
            print(f'#{tc} 2')
            break

    if flag_1 == 0 and flag_2 == 0:
        print(f'#{tc} 0')


# 교수님 풀이
def baby_test(cnt):
    # triplet
    for i in range(10):
        if cnt[i] >= 3:
            return True
    # run
    for i in range(8):
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
            return True
def game():
    cnt1 = [0] * 10
    cnt2 = [0] * 10
    for i in range(12):
        n = arr[i]
        if i % 2 ==0:
            cnt1[n] += 1
        else:
            cnt2[n] += 1
        # 3장이 되면
        if i > 4:
            if i % 2 ==0:
                if baby_test(cnt1):
                    return 1
            else:
                if baby_test(cnt2):
                    return 2
    return 0



T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    print(f'{tc} {game()}')