from itertools import permutations

def solution(k, dungeons):
    max_ = 0
    # 던전 탐험 수
    # k = 피로도
    A = k
    dungeons = list(permutations(dungeons,len(dungeons)))
    for i in range(len(dungeons)):
        k = A
        answer = 0
        for s in dungeons[i]:
            if k >= s[0]:
                k -= s[1]
                answer += 1
            else:
                continue
        max_ = max(max_,answer)   
    
    return max_