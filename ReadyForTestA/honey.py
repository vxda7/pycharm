import sys

sys.stdin = open("sample_input (5).txt", "r")


def find(choose, N):
    global honeyhouse
    global C  # 최대 채취 가능 양
    global M  # 꿀통갯수
    best = 0
    for i in range(N - M + 1):
        res = honeyhouse[choose][i:i + M]
        new = catch(res)
        if best < new:
            best = new
    return best


def catch(res):
    global C
    tbest = 0  # 선택한 부분의 경우의 수 중 가장 큰 값 반환
    for possible in range(1 << M):
        temp = []
        for part in range(M):
            if possible & (1 << part):
                temp.append(part)
        hap = 0
        ok = 0
        for one in temp:
            hap += res[one] ** 2
            ok += res[one]
        if hap > tbest and ok <= C:
            tbest = hap
    return tbest


t = int(input())
for tc in range(1, t + 1):
    N, M, C = map(int, input().split())
    honeyhouse = [list(map(int, input().split())) for i in range(N)]

    all = []
    for i in range(1 << N):
        temp = []
        for j in range(N):
            if i & (1 << j):
                temp.append(j)
        if len(temp) == 2:
            all.append(temp)

    # 경우의 수를 하나 선택
    best = 0
    for i in range(len(all)):
        choose1 = all[i][0]
        choose2 = all[i][1]
        value1 = find(choose1, N)
        value2 = find(choose2, N)
        get = value1 + value2
        # print(value1, place1, value2, place2)
        if get > best:
            best = get

    print("#{} {}".format(tc, best))
