N = int(input())  # 계단의 개수 입력

stairs = [0]  # 계단의 점수를 저장할 리스트 초기화
for _ in range(N):
    stairs.append(int(input()))  # 계단의 점수 입력

dp = [0] * (N + 1)  # DP 배열 초기화
if len(stairs)<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(stairs))
else: # 계단이 3개 이상일 때
    dp[1] = stairs[1]  # 첫 번째 계단의 점수로 초기화
    dp[2] = stairs[1] + stairs[2]  # 첫 번째와 두 번째 계단의 점수로 초기화
    
    for i in range(3, N + 1):
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

    print(dp[-1])  # 최댓값 출력
