def stars(N, now, all, rules):
    if now == N:
        return
    for i in range(N):

        if all // 2 in threes:
            print(' ', end="")
        else:
            print('*', end="")
        all += 1
    print()
    stars(N, now + 1, all, rules)


threes = list(3 ** i for i in range(1, 9))
rules = [0] * 8
N = int(input())
stars(N, 0, 0, rules)
