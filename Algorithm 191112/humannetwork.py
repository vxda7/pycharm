def find(N):
    for k in range(N):
        for i in range(N):
            if i != k:
                for j in range(N):
                    if j != i and j != k:
                        relation[i][j] = min(relation[i][k] + relation[k][j], relation[i][j])

t = int(input())
for tc in range(1, t+1):
    info = list(map(int, input().split()))
    N = info[0]
    relation = [[0] * N for i in range(N)]
    infoidx = 1
    for i in range(N):
        for j in range(N):
            if info[infoidx] == 0:
                relation[i][j] = 1001
            else:
                relation[i][j] = info[infoidx]
            infoidx += 1

    find(N)
    res = min(map(lambda x: sum(x) - 1001, relation))
    print("#{} {}".format(tc, res))