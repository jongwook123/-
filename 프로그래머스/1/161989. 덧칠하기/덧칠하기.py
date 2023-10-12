def solution(n, m, section):
    count = 1
    # 현재 위치
    s = section[0]
    for length in section:
        
        if s + (m-1) < length:
            s = length
            count += 1
        
    
    return count