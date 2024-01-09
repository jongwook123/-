

n = int(input())

d = [[0] * 10 for _ in range(n+1)]

for s in range(0,10):
    d[1][s] = 1

for i in range(2,n+1):
    for j in range(10):
        temp = 0
        for s in range(0,j+1):
            temp += d[i-1][s]
        d[i][j] = temp



print(sum(d[n]) % 10007)







