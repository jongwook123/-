def minSum(n, k, _sum):
    global _min
    if _sum > _min:
        return
    if n == k:

        if _sum < _min:
            _min = _sum
        return

    for i in range(k, n):
        p[k], p[i] = p[i], p[k]
        minSum(n, k + 1, _sum + arr[k][p[k]])
        p[k], p[i] = p[i], p[k]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    p = list(range(N))
    _min = 1000
    minSum(N, 0, 0)
    print(f'#{tc}', _min)