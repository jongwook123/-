
def solve(arr,N,T):
    while True:
        if N // 2 == 0:
            return

        else:
            a_1 = arr[0:(N//2)]
            a_2 = arr[(N//2)+1:N]

            if a_1[(N // 2)//2] == a_1[-((N // 2) // 2) - 1] or a_2[(N // 2)//2] == a_2[-((N // 2) // 2) - 1]:
                arr_2[T].append(a_1[(N // 2) // 2])
                arr_2[T].append(a_2[(N // 2) // 2])
            else:
                arr_2[T].append(a_1[(N // 2)//2])
                arr_2[T].append(a_1[-((N // 2) // 2) - 1])
                arr_2[T].append(a_2[(N // 2) // 2])
                arr_2[T].append(a_2[-((N // 2) // 2) - 1])


            N = N // 2
            T += 1
            solve(a_1,N,T)
            solve(a_2,N,T)

        return


import sys



T = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr_2 = [[] for _ in range(T)]
N = len(arr)
arr_2[0].append(arr[N//2])

solve(arr,N,1)

for i in range(T):
    print(*arr_2[i])






