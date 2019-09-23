def rep(n):
    while n != answers[n]:
        n = answers[n]
    return n


t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    teams = list(map(int, input().split()))
    answers = list(range(N + 1))
    for i in range(0, M+1, 2):
        a, b = teams[i], teams[i + 1]
        answers[rep(a)] = rep(b)
    print(answers)
    print("#{} {}".format(tc, len(set(answers))-1))
