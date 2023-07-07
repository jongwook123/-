from collections import deque


def bfs(s):
    num = [0] * (N + 1)
    Visited[s] = 1
    Q =deque()
    Q.append(s)

    while Q:
        k = Q.popleft()

        for i in arr[k]:
            if not Visited[i]:
                Q.append(i)
                num[i] = num[k]+1
                Visited[i] = 1
    return sum(num)

N,M = map(int,input().split())
arr = {i:[] for i in range(N+1)}
for _ in range(M):
    a,b= map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
result =[]
for s in range(1,N+1):
    Visited = [0] * (N+1)

    result.append(bfs(s))

for tc in range(len(result)):
    if result[tc] == min(result):
        print(tc+1)
        break
    
