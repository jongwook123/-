from collections import deque

a = deque()
Jose = []

N,K = map(int,input().split())
new = K
for i in range(1,N+1):
    a.append(i)

while len(a) != 0:
    if new > 1:
        a.append(a.popleft())
        new -= 1
    else:
        Jose.append(a.popleft())
        new = K
        


print('<',end='')
print(*Jose,sep=', ',end='')
print('>')