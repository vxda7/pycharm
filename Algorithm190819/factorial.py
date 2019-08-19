# factorial
def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    else:
        return 1


# fibo
def fibo(n):
    global memo
    if n >= 2 and memo[n] == 0:   #아직 fibo(n)이 계산되지 않은경우
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]


N=10
memo = [0]*(N+1)
memo[0] = 0
memo[1] = 1
print(fibo(N))