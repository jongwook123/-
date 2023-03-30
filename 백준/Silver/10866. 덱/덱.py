import sys

T = int(sys.stdin.readline())

a = []
for tc in range(T):
    A,*B = sys.stdin.readline().split()

    if A == 'push_back':
        a.append(B)

    if A == 'push_front':
        a.insert(0,B)

    if A == 'pop_front':
        if len(a) == 0:
            print(-1)
        else:
            b = a[0]
            a.remove(a[0])
            print(*b)

    if A == 'pop_back':
        if len(a) == 0:
            print(-1)
        else:
            c = a.pop()
            print(*c)


    if A== 'size':
        print(len(a))

    if A == 'empty':
        if len(a) == 0:
            print(1)
        else:
            print(0)

    if A == 'front':
        if len(a) == 0:
            print(-1)
        else:
            print(*a[0])

    if A == 'back':
        if len(a) == 0:
            print(-1)
        else:
            print(*a[-1])
