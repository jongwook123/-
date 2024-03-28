import sys
N = int(sys.stdin.readline())
dp = [0] * (N+1)
schedule = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
profit = 0

for i in range(N):
    profit = max(profit,dp[i])

    if i + schedule[i][0] > N:
        continue

    dp[i+schedule[i][0]] = max(profit+schedule[i][1],dp[i + schedule[i][0]])

print(max(dp))