def find(N):
    people = set()
    stack = []
    for i in range(N + 1):  # 상원이와 친한 친구 추가
        for j in range(N + 1):
            if relation[1][j] == 1:
                people.add(j)
                stack.append(j)
    while stack != []:
        n = stack.pop()
        for k in range(N + 1):
            if relation[n][k] == 1:
                people.add(k)
    people = people - {1}
    return len(people)


t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    relation = [[0] * (N + 1) for i in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        relation[a][b] = 1
        relation[b][a] = 1
    res = find(N)
    print("#{} {}".format(tc, res))
