
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    r_reserve = [r for r in reserve if r not in lost]
    r_lost = [l for l in lost if l not in reserve]
    
    for i in r_reserve:
        for j in r_lost:
            if i - 1 == j:
                r_lost.remove(j)
            elif i + 1 == j:
                r_lost.remove(j)

    answer = n - len(r_lost)
    return answer