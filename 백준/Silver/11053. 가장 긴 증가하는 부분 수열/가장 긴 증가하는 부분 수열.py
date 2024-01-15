T = int(input())
arr = list(map(int,input().split()))
cnt = 0 # 수열의 전체 길이
cur_Num = 0 # 현재 수
dp = [1] * T
for i in range(1,T):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j] + 1)
print(max(dp))