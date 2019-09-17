import sys
sys.stdin = open("sample_input (14).txt", "r")


def perm(n, k):
    global minV, price, product
    if n == k:
        possiblity.append(product[:])
        for i in range(len(possiblity)):
            hap = 0
            for j in range(N):
                hap += price[j][possiblity[i][j]]
                if minV < hap:
                    break
            else:
                pass
            if minV > hap:
                minV = hap
    else:
        for i in range(n, k):
            product[i], product[n] = product[n], product[i]
            perm(n + 1, k)
            product[i], product[n] = product[n], product[i]


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    price = [list(map(int, input().split())) for i in range(N)]
    product = list(range(N))
    possiblity = []
    minV = 10000000000000000
    perm(0, N)
    print("#{} {}".format(tc, minV))