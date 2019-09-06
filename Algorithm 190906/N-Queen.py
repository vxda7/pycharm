def find(col, row):
    global N
    global board
    global col_data
    global row_data
    global all_data
    truth = True
    if row not in row_data and col not in col_data:
        for data in all_data:
            dcol = data[0]
            drow = data[1]
            if 



def check(col, row):
    global N
    global board
    global col_data
    global row_data
    if col == N-1 and col not in col_data and row not in row_data:
        return 1
    if row == N-1:
        col += 1
        row = 0
    if board[col][row] == 0 and find(col, row):
        board[col][row] = 1
        col_data.add(col)
        row_data.add(row)
        all_data.append([col,row])
    else:
        check(col, row + 1)


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    board = [[0]*N for i in range(N)]
    row_data = set()
    col_data = set()
    all_data = []
    res = check(0, 0)
    print("#{} {}".format(tc, res))