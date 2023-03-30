# def perm(i,k):
#     global min_
#     if i == k:
#         total = 0
#         for n in range(len(p)-1):
#             total += arr[p[n]][p[n+1]]
#         total += arr[p[len(p)-1]][0]
#         if total < min_:
#             min_ = total
#     else:
#         for j in range(i,k):
#             p[i],p[j] = p[j],p[i]
#             perm(i+1,k)
#             p[i],p[j] = p[j],p[i]
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     min_ = float('inf')
#     p = [i for i in range(N)]
#     perm(1,N)
#     print(f"#{tc+1} {min_}")


# 교수님 풀이
def calc(cursum):
    global ans
    # cursum 0 -> 1 -> 2 까지만 포함됨
    cursum += arr[order[N-1]][order[N]]
    # 최소값
    if ans > cursum:
        ans = cursum

def perm(n, k, cursum):
    if cursum > ans:
        return
    if n == k:  # 계산
        calc(cursum)
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                order[k] = i
                perm(n,k+1,cursum + arr[order[k-1]][order[k]])
                visited[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    order = [0] * N + [0]   # 0 1 2 0 으로 저장
    visited = [0] * N
    visited[0] = 1          # 0번은 제외
    ans = 999999999
    perm(N,1,0)               # K = 0 인덱스 제외
    print(f'#{tc} {ans}')

