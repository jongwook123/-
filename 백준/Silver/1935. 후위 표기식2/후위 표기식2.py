T = int(input())
N = list(input())
num = [0]*T


for tc in range(T):
    num[tc] = int(input())


Stack = []
giho = ['*','+','/','-']



 
for i in N:
    if i.isalpha():
        Stack.append(num[ord(i) - ord('A')])
    elif i in giho:
        a = Stack.pop()
        b = Stack.pop()
        if i == '*':
            Stack.append(b * a)
        elif i == '+':
            Stack.append(b + a)
        elif i == '/':
            Stack.append(b / a)
        elif i == '-':
            Stack.append(b - a)
print(f'{Stack[0]:.2f}')