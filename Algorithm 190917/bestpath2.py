import sys
sys.stdin = open("input (8).txt", "r")

def perm(n, k):
    global minV
    global this
    if n == k:
        one = this
        hap = 0
        hap += abs(where[one[0]] - company[0]) + abs(where[one[0] + 1] - company[1])
        for j in range(N - 1):
            hap += abs(where[one[j]] - where[one[j + 1]]) + abs(where[one[j] + 1] - where[one[j + 1] + 1])
            if minV < hap:
                break
        hap += abs(where[one[-1]] - home[0]) + abs(where[one[-1] + 1] - home[1])
        if minV > hap:
            minV = hap
    else:
        for i in range(n, k):
            this[n], this[i] = this[i], this[n]
            perm(n + 1, k)
            this[n], this[i] = this[i], this[n]


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    where = list(map(int, input().split()))
    company = [where[0], where[1]]
    home = [where[2], where[3]]
    where = where[4:]
    this = list(range(0, N*2, 2))
    possibility = []
    minV = 1000000000000000
    perm(0, N)
    # res = find(N)
    print("#{} {}".format(tc, minV))
