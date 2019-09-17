def perm(n, k):
    global possibility
    global this
    if n == k:
        possibility.append(this[:])
    else:
        for i in range(n, k):
            this[n], this[i] = this[i], this[n]
            perm(n + 1, k)
            this[n], this[i] = this[i], this[n]


def find(N):
    global where, home, company
    global possibility
    minV = 1000000000000000
    for i in range(len(possibility)):
        one = possibility[i]
        hap = 0
        hap += abs(where[one[0]] - company[0]) + abs(where[one[0]+1] - company[1])
        for j in range(N-1):
            hap += abs(where[one[j]] - where[one[j+1]]) + abs(where[one[j]+1] - where[one[j+1]+1])
            if minV < hap:
                break
        hap += abs(where[one[-1]] - home[0]) + abs(where[one[-1] + 1] - home[1])
        if minV > hap:
            minV = hap
    return minV


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    where = list(map(int, input().split()))
    company = [where[0], where[1]]
    home = [where[2], where[3]]
    where = where[4:]
    this = list(range(0, N*2, 2))
    possibility = []
    perm(0, N)
    res = find(N)
    print("#{} {}".format(tc, res))
