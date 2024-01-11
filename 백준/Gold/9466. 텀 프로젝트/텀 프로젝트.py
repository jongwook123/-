import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    number = numbers[x]

    if visited[number]:
        if number in cycle:
            result += cycle[cycle.index(number):]
        return
    else:
        dfs(number)

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    numbers = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [True] + [False]*N
    result = []

    for i in range(1, N+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(N - len(result))