T = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort(reverse=True)
sum = 0
for tc in range(T):
    sum += A[tc]*B[tc]
print(sum)