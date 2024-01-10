import sys
sys.setrecursionlimit(10**6)
def dfs(start,arr,Visited,sg):
    Visited[start] = sg         # 방문체크

    for s in arr[start]:        # 인접정점
        if not Visited[s]:      # 방문하지 않았을 경우
            result = dfs(s,arr,Visited,-sg) # 방문체크를 -sg로 한다.
            if not result:      # result가 False 일때
                return False
        else:
            if Visited[s] == sg:# 방문했는데 같은 sg라면 이분 그래프가 아님
                return False

    return True                 # 다 끝나면 이분 그래프다.


T = int(sys.stdin.readline())

for _ in range(T):
    V,E = map(int,sys.stdin.readline().split()) # V = 정점의 개수, E = 간선의 개수
    arr = {i:[] for i in range(V+1)} # 정점과 연결된 정점
    Visited = [0] * (V+1) # 방문체크 0,-1,1

    for s in range(E):
        u,v = map(int,sys.stdin.readline().split()) # 두 정점
        arr[u].append(v)
        arr[v].append(u)

    for i in range(1,V+1):
        if not Visited[i]:
            result = dfs(i,arr,Visited,1)
            if not result:
                break
    if result:
        print("YES")
    else:
        print("NO")