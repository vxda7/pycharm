t = int(input())
for tc in range(1, t+1):
    N = int(input())
    info = []
    placeinfo = []
    for i in range(N):
        get = list(map(int, input()))
        info.append(get)
        placeinfo.append(get[0:2])


    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    energy = 0
    for time in range(2000):
        for i in range(N):
            this = info[i]
            this[0] = dx[this[2]]
            this[1] = dy[this[2]]
        for i in range(N):
            cnt = 0
            for j in range(N):
                if (info[i][0] == info[j][0] and info[i][1] == info[j][1]) or (info[i][0] == info[j][0] and info[j][1] - info[j][1] == 1) or (info[i][1] == info[j][1] and abs(info[j][0] - info[j][0]) == 1):
                    # info[i][0] == info[j][0] and info[j][1] - info[j][1] == 1
                    energy += info[i][3] + info[j][3]
                    info[i].append(1)
                    info[j].append(1)
