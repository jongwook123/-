import sys
from collections import Counter

# 입력 받기
N = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

# 산술평균 구하기
mean = round(sum(numbers) / N)

# 중앙값 구하기
numbers.sort()
median = numbers[N // 2]

# 최빈값 구하기
counter = Counter(numbers)
mode = counter.most_common(2)
if len(mode) > 1 and mode[0][1] == mode[1][1]:
    mode = mode[1][0]
else:
    mode = mode[0][0]

# 범위 구하기
range_value = max(numbers) - min(numbers)

# 결과 출력
print(mean)
print(median)
print(mode)
print(range_value)
