str = list(input())
for i in str:
    if i.isupper():
        a = i.lower()
        print(a,end="")
    else:
        b = i.upper()
        print(b,end="")
    