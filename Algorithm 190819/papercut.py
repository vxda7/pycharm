test_case = int(input())


def fibo(n):
    global data
    if n >= 2 and data[n] == 0:
       data[n] = fibo(n-2)*2 + fibo(n-1)
    return data[n]


for case in range(1, test_case + 1):
    N = int(input())
    data = [0] * (N + 1)
    data[0] = 1
    data[1] = 3
    result = fibo(int(N//10)-1)
    print("#{} {}".format(case, result))