# 출발지점 찾기
def find(park,arr):
    for i in range(len(park)):
        for j in range(len(park)):
            if arr[i][j] == 'S':
                return i,j



def solution(park, routes):
    arr = []
    # 쪼개기
    for i in range(len(park)):
        arr.append(list(park[i]))
    
    
    # 초기 위치
    i,j = find(park,arr)
    # 방향이랑 거리체크
    for s in range(len(routes)):
        # 초기위치 지정
        ni = i
        nj = j
        flag = 0
        
        # S 일때
        if routes[s][0] == "S":
            for _ in range(int(routes[s][2])):
                ni = ni + 1
                if 0 <= ni < len(park) and arr[ni][j] !="X":
                    pass
                else:
                    flag = 1
            if flag == 0:
                i = ni
                
        # N 일때
        elif routes[s][0] == "N":
            for _ in range(int(routes[s][2])):
                ni = ni - 1
                if 0 <= ni < len(park) and arr[ni][j] !="X":
                    pass
                else:
                    flag = 1
            if flag == 0:
                i = ni
            
        # E 일때
        elif routes[s][0] == "E":
            for _ in range(int(routes[s][2])):
                nj = nj + 1
                if 0 <= nj < len(arr[0]) and arr[i][nj] !="X":
                    pass
                else:
                    flag = 1

            if flag == 0:
                j = nj

        # W 일때
        elif routes[s][0] == "W":
            for _ in range(int(routes[s][2])):
                nj = nj - 1
                if 0 <= nj < len(arr[0]) and arr[i][nj] !="X":
                    pass
                else:
                    flag = 1

            if flag == 0:
                j = nj
                
                
    answer = [i,j]
    return answer