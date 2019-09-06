t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    subset = set([0])
    for i in scores:
        temp = set(subset)
        for j in temp:
            subset.add(i+j)
    print(subset)
    print("#{} {}".format(tc, len(subset)))
