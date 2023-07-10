from collections import deque

Q = deque()

for _ in range(8):
    a = int(input())
    Q.append(a)
A = deque(sorted(Q))
A.popleft()
A.popleft()
A.popleft()
print(sum(A))
T = []
for a in A:
    T.append(Q.index(a)+1)
print(*sorted(T))