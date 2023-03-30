import heapq
import sys
T = int(sys.stdin.readline())

S = []                  # 푸시해줄 리스트 생성

for _ in range(T):
    arr = map(int,input().split())  

    for ar in arr:
        if len(S) < T:      # 리스트의 길이 제한
            heapq.heappush(S,ar)    # 5개 보다 
        else:
            if S[0] < ar:
                heapq.heappop(S)
                heapq.heappush(S,ar)



print(S[0])