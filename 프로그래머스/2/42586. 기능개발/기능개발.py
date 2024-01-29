def solution(progresses, speeds):
    ans = []
    count = 0
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        if progresses[0] >= 100:
            while progresses and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            ans.append(count)
            count = 0
    
    return ans