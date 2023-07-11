from collections import deque

def bfs(k):
    global me

    Q = deque()
    Q.append(k)

    while Q:
        x = Q.popleft()
        me = x
        if x == 100:
            print(Board[100])
            return
        for s in range(1,7):
            next = me + s
            if next <= 100 and not Visited[next]:
                if next in ladder.keys():
                    next = ladder[next]

                if next in snake.keys():
                    next = snake[next]

                if not Visited[next]:
                    Visited[next] = 1
                    Board[next] = Board[me]+1
                    Q.append(next)





N,M = map(int,input().split())
ladder = dict()
snake = dict()
me = 1
Board = [0]*101
Visited = [0]*101
for i in range(N):
    x,y = map(int,input().split())
    ladder[x]=y
for j in range(M):
    u,v = map(int,input().split())
    snake[u]=v
bfs(1)
