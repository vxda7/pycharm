def stars(N, col, row, all):
    global space

    for i in range(9):
        if i != 4:
            dc = i // 3
            dr = i % 3
            # print(col + dc, row + dr)
            space[col + dc][row + dr] = '*'
        all += 1
    if all == N ** 2:
        return
    # elif (row//3) // N != 1 and (col//3) // N != 1:
    if row == N - 3:
        row = 0
        stars(N, col + 3, row, all)
    else:
        if (col//3 == 1)//6 and ((row+3)//3)//6:
            stars(N, col, row + 6, all + 9)
        else:
            stars(N, col, row + 3, all)

threes = list(3 ** i for i in range(1, 9))
rules = [0] * 8
N = int(input())
space = [list(' ' * N) for i in range(N)]
stars(N, 0, 0, 0)
for i in range(N):
    for j in range(N):
        print(space[i][j], end="")
    print()

# 0 6 12 18
# 3 9 15 21
# 1 3 5 7 9