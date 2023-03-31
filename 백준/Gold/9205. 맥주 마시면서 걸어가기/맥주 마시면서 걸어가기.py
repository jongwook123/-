

def bfs():
    Q = []
    Q.append([h1,h2])

    while Q:
        a,b = Q.pop(0)
        if abs(a-p1) + abs(b-p2) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                x, y = N[i]
                if abs(a - x) + abs(b - y) <= 1000:
                    Q.append([x, y])
                    visited[i] = 1

    print("sad")
    return



T = int(input())
for tc in range(T):
    n = int(input())
    h1,h2 = map(int,input().split())
    N = []
    visited = [0] * (n + 1)
    for _ in range(n):
        a,b = map(int,input().split())
        N.append([a,b])
    p1,p2 = map(int,input().split())
    bfs()

