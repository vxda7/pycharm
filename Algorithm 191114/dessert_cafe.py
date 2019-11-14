def perp(start, end, temp):
    global N
    if start == end:
        if sum(temp) < N:
            possibles.append(temp[:])
    else:
        for i in range(1, N - 1):
            perp(start + 1, end, temp + [i])
# 특정가로세로와 시작위치가 주어지면 불가능: -2 가능: 디저트갯수 돌려줌
def find(col, row, possible, kind):
    global N
    tcol, trow = col, row
    for k in range(4):
        for i in range(possible[k % 2]):
            col += directions[k][0]
            row += directions[k][1]
            if 0 <= col < N and 0 <= row < N:
                if flowers[col][row] not in kind:   # 종류에 없다면
                    kind += [flowers[col][row]]
                else:
                    if col == tcol and row == trow:
                        pass
                    else:
                        return -2
            else:
                return -2
    return len(kind)


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    flowers = [list(map(int, input().split())) for i in range(N)]

    possibles = []
    perp(0, 2, [])
    # 우하, 좌하, 좌상, 우상
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    # 아래로만 네모 만들기
    maxV = -1
    for possible in possibles:
        for i in range(N):
            for j in range(N):
                tours = 0
                res = find(i, j, possible, [flowers[i][j]])
                if maxV < res:
                    maxV = res
    print("#{} {}".format(tc, maxV))
