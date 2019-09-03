def find(S, G):
    global spider
    for i in range(len(spider[S])):
        if spider[S] == []:
            return 0
        a = spider[S].pop()
        if a == G:
            return 1
        elif G in spider[a]:
            return 1
        else:
            if a != S:
                if find(a, G) == 1:
                    return 1
    return 0


t = int(input())
for tc in range(1, t + 1):
    V, E = map(int, input().split())
    spider = {i: [] for i in range(1, V + 1)}
    for i in range(E):
        start, end = map(int, input().split())
        spider[start].append(end)
    S, G = map(int, input().split())
    res = find(S, G)
    print("#{} {}".format(tc, res))