t = int(input())
for tc in range(1, t + 1):
    N, num = input().split()
    res = []
    change = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for i in range(int(N)):
        if num[i].isdigit():
            temp = int(num[i])
            res.append(str(bin(temp)))
        else:
            temp = change[num[i]]
            res.append(str(bin(temp)))
    # print(res)
    for j in range(int(N)):
        diff = 4 - len(res[j][2:])
        res[j] = res[j][2:]
        if diff > 0:
            for k in range(diff):
                res[j] = '0' + res[j]
    # print(res)
    print('#{} {}'.format(tc, ''.join(res)))
