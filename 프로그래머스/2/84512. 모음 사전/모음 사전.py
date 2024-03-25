from itertools import product

def solution(word):
    list_ = ['A','E','I','O','U']
    lis_ = []
    for i in range(1,len(list_)+1):
        for s in product(list_,repeat=i):
            lis_.append(s)
    lis_.sort()
    
    answer = 0
    
    for s in lis_:
        answer += 1
        if word == ''.join(s):
            break
        
    return answer

