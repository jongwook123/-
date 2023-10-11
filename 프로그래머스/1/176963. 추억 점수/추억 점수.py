def solution(name, yearning, photo):
    dic = {}
    answer = []
    for s in range(len(name)):
        dic[name[s]] = yearning[s]
    
    for s in range(len(photo)):
        a = 0
        for k in range(len(photo[s])):
            if photo[s][k] in name:
                a +=(dic[photo[s][k]])
        answer.append(a)
    
    return answer