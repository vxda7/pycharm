def find(col, row, state):
    global N
    # 0 가로      1 세로        2 대각선
    if col < 0 or row < 0 or col > N - 1 or row > N - 1 or rooms[col][row] == 1 or (
            state == 2 and rooms[col - 1][row] == 1) or (state == 2 and rooms[col][row - 1] == 1):
        return 0
    elif col == N - 1 and row == N - 1:
        return 1
    if state == 0:
        return find(col, row + 1, 0) + find(col + 1, row + 1, 2)
    elif state == 1:
        return find(col + 1, row, 1) + find(col + 1, row + 1, 2)
    elif state == 2:
        return find(col, row + 1, 0) + find(col + 1, row, 1) + find(col + 1, row + 1, 2)
    return 0


N = int(input())
for i in range(N):
    rooms = [list(map(int, input().split())) for i in range(N)]
    print(find(0, 1, 0))
