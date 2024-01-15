from collections import deque

n,w,L = map(int,input().split())
# L = 다리의 최대하중
# w = 다리길이
# n = 트럭 개수
array_ = list(map(int,input().split()))
Q = deque()
for _ in range(w):
    Q.append(0)

time = 0

idx = 0

while idx < n:
    time += 1
    Q.popleft()
    
    if sum(Q) + array_[idx] <= L:
        Q.append(array_[idx])
        idx += 1
    
    else:
        Q.append(0)
        
while Q:
    time += 1
    Q.popleft()
    
print(time)