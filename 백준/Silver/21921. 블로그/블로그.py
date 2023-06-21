import sys

a, b = map(int, sys.stdin.readline().split())
V = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0] * (a + 1)
for i in range(1, a + 1):
    prefix_sum[i] = prefix_sum[i - 1] + V[i - 1]

max_sum = 0
count = 0

for i in range(a - b + 1):
    curr_sum = prefix_sum[i + b] - prefix_sum[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
        count = 1
    elif curr_sum == max_sum:
        count += 1

if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(count)
