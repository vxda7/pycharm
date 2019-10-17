from copy import deepcopy


def rot(one):
    temp = [[0] * 5 for i in range(5)]
    for i in range(5):
        for j in range(5):
            temp[j][4 - i] = one[i][j]

    for i in range(5):
        one[i] = temp[i][:]
    return one


def maze(temp):  # 12가 최단거리
    queue = [(0, 0, 0)]
    di = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
    if temp[4][4][4] == 0 or temp[0][0][0] == 0:
        return -1
    while queue != []:
        x, y, z = queue.pop(0)
        for i in di:
            dx = x + i[0]
            dy = y + i[1]
            dz = z + i[2]
            if 0 <= dx < 5 and 0 <= dy < 5 and 0 <= dz < 5:
                if temp[dx][dy][dz] == 1:  # 갈수 있다면
                    temp[dx][dy][dz] = temp[x][y][z] + 1  # 이전값 +1 넣기
                    queue.append((dx, dy, dz))

                    if dx == 4 and dy == 4 and dz == 4:  # 도착했다면
                        return temp[4][4][4]  # 도착거리 출력
    return -1  # 시작과 끝은 갈 수 있지만 도달할 수는 없다면


def find(possible, temp, it):
    for i in it:
        for j in range(possible[i]):
            temp[i] = deepcopy(rot(temp[i]))
    return maze(temp)


def perm(start, end):
    global minV
    if start == end:
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        for m in range(4):
                            temp = deepcopy(boards)
                            res = find([i, j, k, l, m], temp, this)
                            if minV > res and res != -1:
                                minV = res
        if minV == 10000000:
            print(-1)
        else:
            print(minV - 1)
    else:
        for i in range(start, end):
            this[i], this[start] = this[start], this[i]
            perm(start+1, end)
            this[i], this[start] = this[start], this[i]




boards = [[list(map(int, input().split())) for i in range(5)] for j in range(5)]
minV = 10000000
this = [0, 1, 2, 3, 4]
perm(0, 5)


