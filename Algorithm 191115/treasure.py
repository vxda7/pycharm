def change(part):
    i = len(part) - 1
    res = 0
    for one in part:
        if one == 'F':
            res += 15 * 16 ** i
        elif one == 'E':
            res += 14 * 16 ** i
        elif one == 'D':
            res += 13 * 16 ** i
        elif one == 'C':
            res += 12 * 16 ** i
        elif one == 'B':
            res += 11 * 16 ** i
        elif one == 'A':
            res += 10 * 16 ** i
        else:
            res += int(one) * 16 ** i
        i -= 1
    return res


t = int(input())
for tc in range(1, t+1):
    # 숫자길이, 몇번째를 출력할지
    N, K = map(int, input().split())
    num = input()
    parts = []
    for i in range(N//4):
        num = num[1:] + num[0]
        for j in range(0, N + 1, N//4):
            part = num[j:j + N//4]
            parts.append(change(part))
    res = sorted(list(set(parts)), reverse=True)
    # print(res)
    print("#{} {}".format(tc, res[K - 1]))
