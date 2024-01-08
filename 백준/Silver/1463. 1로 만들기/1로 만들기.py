n = int(input())

d = [0] * 1000001

for s in range(2,n+1):
    d[s] = d[s-1] + 1

    if s % 2 == 0:
        d[s] = min(d[s],d[s//2] + 1)

    if s % 3 == 0:
        d[s] = min(d[s],d[s//3] + 1)



print(d[n])