def none(i, N):
    stack = [i]
    while stack != []:
        col = stack.pop()
        for i in range(N+1):
            if people[col][i] == 1:
                stack.append(i)
                people[col][i] = 0


t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    people = [list(range(N+1)) for i in range(N+1)]
    for i in range(M):
        one, two = map(int, input().split())
        people[one][two] = 1
        people[two][one] = 1
    cnt = 0
    for i in range(N+1):
        for j in range(N+1):
            if people[i][j] == 1:
                cnt += 1
                none(i, N)
    print("#{} {}".format(tc, cnt))


