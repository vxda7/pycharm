def factorial(N, got):
    res = 1
    for i in range(N, got + 1):
        res *= i
    return res % 1000000007


t = int(input())
for tc in range(1, t + 1):
    M, N = map(int, input().split())
    # (M+N-1)!/(M-1)!
    res = factorial(N, N + M - 1)
    print("#{} {}".format(tc, res))