from itertools import permutations


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def solution(numbers):
    numbers = list(numbers)
    A = []
    result = 0
    for i in range(1,len(numbers) + 1):
        for s in permutations(numbers,i):
            A.append(int(''.join(s)))
    A = list(set(A))
    for s in A:
        if is_prime(s) == True:
            result += 1
    return result