from collections import deque

# 4방향 탐색
di = [0,0,1,-1]
dj = [-1,1,0,0]

def bfs(i,j,arr,Visited):
    Q = deque()
    Q.append((i,j))
    Visited[i][j] = 1 # 방문체크

    while Q:
        i,j = Q.popleft()

        for s in range(4):
            ni = i + di[s]
            nj = j + dj[s]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                if Visited[ni][nj] == 0:
                    Q.append((ni,nj))
                    Visited[ni][nj] = 1




T = int(input()) # 총 테스트 케이스
for _ in range(T):
    M, N, K = map(int,input().split()) # 가로, 세로, 지렁이 갯수
    arr = [[0] * M for _ in range(N)] # 배추가 심어진 전체 땅
    Visited = [[0] * M for _ in range(N)] # 방문표시
    Ji = 0 # 지렁이 갯수

    for _ in range(K): # 지렁이가 있는 땅 
        i,j = map(int,input().split())
        arr[j][i] = 1 # 지렁이 기록 
    
    # -> K 입력이 세로 가로 바껴있어서 인덱스 오류가 났음 문제 잘 읽어볼것.

    for j in range(M):
        for i in range(N):
            if arr[i][j] and Visited[i][j] == 0: # 지렁이가 있고 방문을 하지 않았다면
                bfs(i,j,arr,Visited)
                Ji += 1

    print(Ji)