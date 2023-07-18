import sys
from itertools import permutations
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    arr_p = list(permutations(arr, 6))
    for case in arr_p:
        case = list(case)
        if case != sorted(case):
            continue
        elif case == sorted(case):
            print(*case)
            continue
    print()
    if n == 0:
        break