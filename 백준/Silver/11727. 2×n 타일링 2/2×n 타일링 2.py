n = int(input())

d = [0] * 1001
d[1] = 1
d[2] = 3
for s in range(3,n+1):
    d[s] = d[s-1] + d[s-2] * 2 



print(d[n] % 10007)