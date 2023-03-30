import sys
from collections import deque


def solve(i):
    global cnt
    Q = deque()
    Q.append(i)
    visited[i] = 1

    while Q:
        s = Q.popleft()
        if len(arr[s]) == 1 and visited[arr[s][0]]:  
            cnt += 1

        for w in arr[s]:
            if not visited[w]:
                Q.append(w)
                visited[w] = 1

    return


T,K = map(int,sys.stdin.readline().split()) # T:노드의 개수   K:물의양
arr = {i : [] for i in range(T+1)}
visited = [0] * (T + 1)
for tc in range(T-1):
    U, V = map(int,sys.stdin.readline().split())
    arr[U].append(V)
    arr[V].append(U)

cnt = 0
solve(1)

print(K/cnt)
