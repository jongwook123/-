# nPr
def perm(n,k):
    global flag
    if n == k:
        if ((order[0] == order[1] == order[2]) or (order[0] + 2 ==order[1] + 1 == order[2])) and ((order[3] == order[4] == order[5]) or (order[3] + 2 ==order[4] + 1 == order[5])):
            flag = 1
    if flag == 1:
        return

    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                order[k] = arr[i]
                perm(n,k+1)
                visited[i] = 0





T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input()))
    N = len(arr)
    flag = 0
    order = [0] * N
    visited = [0] * N
    perm(N, 0)
    print(f'#{tc} {flag}')







