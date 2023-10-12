def find_f(j_l,j_r,i_t,i_b,arr):
    for s in range(len(arr)):
        for k in range(len(arr[s])):
            if arr[s][k] == "#":
                j_l = k
                j_r = k 
                i_t = s
                i_b = s 
                print(s,k)
                return j_l,j_r,i_t,i_b

def find(j_l,j_r,i_t,i_b,arr):
    
    # 세로 탐색
    for s in range(len(arr)):
        for k in range(len(arr[s])):
            if arr[s][k] =="#":
                if i_b <= s:
                    i_b = s
        
    # 가로 탐색
    for s in range(len(arr)):
        for k in range(len(arr[s])):
            if arr[s][k] =="#":
                if j_l >= k:
                    j_l = k
                if j_r <= k:
                    j_r = k
    return j_l,j_r,i_t,i_b

def solution(wallpaper):
    arr = []
    
    # 왼쪽,오른쪽,위,아래
    j_l,j_r,i_t,i_b = 0,0,0,0

    for s in range(len(wallpaper)):
        arr.append(list(wallpaper[s]))
        
    x,y,z,q = find_f(j_l,j_r,i_t,i_b,arr)
    print(x,y,z,q)
    a,b,c,d = find(x,y,z,q,arr)
    
    answer = [c,a,d+1,b+1]
    return answer