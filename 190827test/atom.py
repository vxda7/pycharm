t = int(input())
for tc in range(1, t+1):
    n = int(input())
    atoms = []
    best = 0
    for i in range(n):
        row, col, dir, energy = map(int, input().split())
        atoms.append([row, col, dir, energy])
        if best < max(abs(row), abs(col)):
            best = max(abs(row), abs(col))

    space = [[0]*best*2 for i in range(best*2)]
    # empty = [[0]*best*2 for i in range(best*2)]

    for i in range(n):
        # empty[atoms[i][0]+best,atoms[i][1]+best] = 1
        space[atoms[i][0]+best, atoms[i][1]+best] = [atoms[i][0]+best, atoms[i][1]+best, atoms[i][2], atoms[i][3]]


    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]
    for time in range(best):
        for i in range(best*2):
            for j in range(best * 2):
                if space[i][j] != 0:
                    mi = i + di[space[i][j][2]]
                    mj = j + dj[space[i][j][2]]





