T = int(input())
for tc in range(1,T+1):
    stack = []
    data = list(input())

    for i in data:
        if i == '(' or i == '{':
            stack.append(i)

        if len(stack) == 0:
            if i == ')' or i == '}':
                stack.append(i)
                break

        elif i == ')':
            if len(stack) > 0:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    break

        elif i == '}':
            if len(stack) > 0:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    break


    if len(stack) == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')