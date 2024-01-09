

n = int(input())

d = [[0] * 10 for _ in range(n+1)]

for s in range(1,10):
    d[1][s] = 1

for i in range(2,n+1):
    for j in range(10):
        # 가장 뒤에 오는 숫자가 0일때, 그 앞에는 1만 가능
        if j == 0:
            d[i][j] = d[i-1][1]
        # 가장 뒤에 오는 숫자가 9일때, 그 앞에는 8만 가능
        elif j == 9:
            d[i][j] = d[i-1][8]
        
        # 가장 뒤에 오는 숫자가 1~8일때, 그 앞에 +- 1 가능
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]


print(sum(d[n]) % 1000000000)







