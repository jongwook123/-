K,N = map(int,input().split())
list_N = []
for _ in range(K):
    list_N.append(int(input()))

E = max(list_N)
S = 1


while S <= E:
    sum_ = 0
    M = (S+E) // 2
    for n in list_N:
        sum_ += n // M

    if sum_ >= N:
        S = M + 1
    else:
        E = M -1
        
print(E)