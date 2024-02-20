T = int(input())

num_1 = 666
count = 0

while True:
    if "666" in str(num_1):
        count += 1

    if T == count:
        print(num_1)
        break
    num_1 += 1