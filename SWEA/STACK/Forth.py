def perm(arr):

    for s in arr:
        if s not in giho:
            if s == '.' :
                if len(stack) >1:
                    return 'error'
                else:
                    return stack[0]
            else:
                stack.append(int(s))

        elif s in giho:
            if len(stack) > 1:
                a1 = stack.pop()
                a2 = stack.pop()
                if s == '+':
                    stack.append(a1+a2)

                elif s =='-':
                    stack.append(a2-a1)

                elif s == '*':
                    stack.append(a2*a1)
                elif s == '/':
                    stack.append(a2//a1)

            else:
                return 'error'










giho = ['+','/','*','-']

T = int(input())
for tc in range(1,T+1):
    arr = list(input().split())
    stack = []

    print(f'#{tc} {perm(arr)}')
