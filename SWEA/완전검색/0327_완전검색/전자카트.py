def perm(i,k):
    global min_
    if i == k:
        total = 0
        for n in range(len(p)-1):
            total += arr[p[n]][p[n+1]]
        total += arr[p[len(p)-1]][0]
        if total < min_:
            min_ = total
    else:
        for j in range(i,k):
            p[i],p[j] = p[j],p[i]
            perm(i+1,k)
            p[i],p[j] = p[j],p[i]

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_ = float('inf')
    p = [i for i in range(N)]
    perm(1,N)
    print(f"#{tc+1} {min_}")


