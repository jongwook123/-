T = int(input())
wine = [0]
for i in range(T):
    wine.append(int(input()))
dp = [0] * (T+1)
dp[1] = wine[1]
if T > 1:
    dp[2] = wine[1] + wine[2]

for i in range(3,T+1):
    dp[i] = max(dp[i-2]+wine[i],dp[i-1],dp[i-3]+wine[i-1]+wine[i])

print(dp[T])