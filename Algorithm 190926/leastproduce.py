def find(i, N):
    global minV
    if i == N:
        res = 0
        for k in range(N):
            res += abs(place[perm[k]][0] - plant[k][0]) + abs(place[perm[k]][1] - plant[k][1])
        if res < minV:
            minV = res
    else:
        for j in range(i, N):
            perm[j], perm[i] = perm[i], perm[j]
            find(i + 1, N)
            perm[j], perm[i] = perm[i], perm[j]


N = int(input())
place = [list(map(int, input().split())) for i in range(N)]
plant = [list(map(int, input().split())) for i in range(N)]
minV = 100000000
perm = list(range(N))
find(0, N)
print(minV)