t = int(input())
for tc in range(1, t+1):
    get = list(map(int, input().split()))
    result = set()
    for i in range(1 << 7):
        temp = []
        for j in range(7):
            if i & (1 << j):
                temp.append(get[j])
        if len(temp) == 3:
            result.add(sum(temp))
    result = list(result)
    result.sort()
    print("#{} {}".format(tc, result[-5]))