def solution(sizes):
    A = sizes
    max_w = 0
    max_h = 0

    for i in range(len(A)):
        A[i].sort()
        if A[i][0] >= max_w:
            max_w = A[i][0]
        if A[i][1] >= max_h:
            max_h = A[i][1]
            
            
    return max_w * max_h