def perm(n, k, hap):
    global minV, price, product, N
    if n == k:
        if minV > hap:
            minV = hap
    else:
        for i in range(n, k):
            product[i], product[n] = product[n], product[i]
            temp = hap + price[n][product[n]]
            if temp < minV:
                perm(n + 1, k, temp)
            product[i], product[n] = product[n], product[i]


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    price = [list(map(int, input().split())) for i in range(N)]
    product = list(range(N))
    possiblity = []
    minV = 10000000000000000
    perm(0, N, 0)
    print("#{} {}".format(tc, minV))