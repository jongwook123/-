def solution(answers):
    c_1 = 0
    c_2 = 0
    c_3 = 0
    c1 = [1,2,3,4,5]
    c2 = [2,1,2,3,2,4,2,5]
    c3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == c1[i%5]:
            c_1 += 1
        if answers[i] == c2[i%8]:
            c_2 += 1
        if answers[i] == c3[i%10]:
            c_3 += 1
    A = [c_1,c_2,c_3]
    m_ = max(A)
    list_ = []
    for s in range(len(A)):
        if A[s] == m_:
            list_.append(s+1)
    return list_