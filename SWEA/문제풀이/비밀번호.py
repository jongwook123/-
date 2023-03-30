
for tc in range(1,11):
    N, M = input().split()
    N = int(N)
    M = list(map(int,M))    #N : 번호 수 M : 비밀번호 리스트
    stack = []
    for i in M:
        if len(stack) == 0:
            stack.append(i)

        elif len(stack) > 0:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    new_stack = []
    for i in stack:
        new_stack.append(str(i))

    print(f'#{tc}',end =' ')
    print(''.join(new_stack))
