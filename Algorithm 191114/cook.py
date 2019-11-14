t = int(input())
for tc in range(1, t+1):
    N = int(input())
    tastes = [list(map(int, input().split())) for i in range(N)]

    possibles = []
    for i in range(1 << (N - 1)):
        temp = []
        for j in range(N):
            if i & (1 << j):
                temp.append(1)
            else:
                temp.append(0)
        if sum(temp) == N//2:
            possibles.append(temp[:])


    minV = 100000
    for poss in possibles:
        food1, food2 = [], []
        for i in range(N):
            if poss[i] == 0:    # 1번사람 음식
                food1.append(i)
            else:
                food2.append(i)

        # 음식 가치 계산
        taste1, taste2 = 0, 0
        for i in range(N // 2):
            for j in range(N // 2):
                taste1 += tastes[food1[i]][food1[j]]
                taste2 += tastes[food2[i]][food2[j]]
        # 가치 차이
        value = abs(taste1 - taste2)
        if minV > value:
            minV = value

    print("#{} {}".format(tc, minV))

