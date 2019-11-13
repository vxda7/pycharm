t = int(input())
for tc in range(1, t+1):
    N = int(input())
    line = list(map(int, input().split())) + [0]
    stem = [0] * N
    sweetpotato = [0] * N
    num = 0
    idx = 0
    for i in range(N):
        if line[i] >= line[i + 1]:
            num += 1
            stem[idx] += 1
            sweetpotato[idx] += line[i]
            idx += 1
        else:
            stem[idx] += 1
            sweetpotato[idx] += line[i]
    # sweetpotato[num] += line[N-1]
    # stem[num] += 1

    # print(sweetpotato)
    # print(stem, num)
    maxV = 0
    place = 0
    cnt = 0
    for i in range(N):
        if stem[i] > maxV:
            maxV = stem[i]
            place = i
        elif stem[i] == maxV:
            if sweetpotato[i] > sweetpotato[place]:
                place = i
        if stem[i] >= 2:
            cnt += 1

    print("#{} {} {}".format(tc, cnt, sweetpotato[place]))