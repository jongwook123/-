from collections import deque

def dfs(s,numbers,target,value):
    if s == len(numbers):
        if value == target:
            return 1
        else:
            return 0
    return dfs(s+1,numbers,target,value+numbers[s]) + dfs(s+1,numbers,target,value-numbers[s])

def solution(numbers, target):
    answer = dfs(0,numbers,target,0)
    return answer