import sys
import heapq
T = int(sys.stdin.readline())
arr = []

for tc in range(T):

    N = int(sys.stdin.readline())

    heapq.heappush(arr,-N)

    if N == 0:
        print(abs(heapq.heappop(arr)))
