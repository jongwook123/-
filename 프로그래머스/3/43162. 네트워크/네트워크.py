from collections import deque

def bfs(s,Visited,arr):
    Q = deque()
    Q.append(s)
    
    Visited[s] = 1
    
    while Q:
        i = Q.popleft()
        
        for a in arr[i]:
            if not Visited[a]:
                Q.append(a)
                Visited[a] = 1

def solution(n, computers):
    Visited = [0] * (n)
    arr = {i:[] for i in range(n)}   
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                arr[i].append(j)
                
    cnt = 0
    for s in range(n):
        if not Visited[s]:
            bfs(s,Visited,arr)
            cnt += 1
    answer = cnt
    return answer