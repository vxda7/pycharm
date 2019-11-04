from copy import deepcopy
t = int(input())
for tc in range(1, t+1):
    board = [input().split() for i in range(6)]
    possible = set(map(str, range(1, 10)))
    solved = 0  # 탈출 조건을 위한 값 몇 개의 칸이 해결되었는지 세줌 36이 되면 탈출
    possible_board_col = [set(possible) for i in range(6)]    # 세로줄 가능성 ▥
    possible_board_row = [set(possible) for i in range(6)]    # 가로줄 가능성 ▤
    possible_board_mass = [[set(possible) for i in range(3)] for j in range(2)]   # 한덩이 가능성\
    print(possible_board_mass)
    print(possible_board_mass[0][2])
    for i in range(6):
        for j in range(6):
            element = board[i][j]
            if '/' in element:  # 분수라면
                if element[0] == '-' and element[-1] == '-':  # 두칸다 모르면
                    pass
                elif element[0] == '-':  # 앞칸만 모르면
                    possible_board_col[i] -= {int(board[i][j][-1])}
                    possible_board_row[j] -= {int(board[i][j][-1])}
                    possible_board_mass[i // 3][j // 2] -= {int(board[i][j][-1])}
                elif element[-1] == '-':  # 뒷칸만 모르면
                    possible_board_col[i] -= {int(board[i][j][0])}
                    possible_board_row[j] -= {int(board[i][j][0])}
                    possible_board_mass[i // 3][j // 2] -= {int(board[i][j][0])}
                else:  # 둘다 안다면
                    # 가능성을 제외
                    possible_board_col[i] -= {int(board[i][j][0]), int(board[i][j][-1])}
                    possible_board_row[j] -= {int(board[i][j][0]), int(board[i][j][-1])}
                    possible_board_mass[i // 3][j // 2] -= {int(board[i][j][0]), int(board[i][j][-1])}
                    solved += 1
            elif element == '-':  # 빈칸이라면
                pass
            else:  # 숫자라면
                possible_board_col[i] -= {int(board[i][j])}
                possible_board_row[j] -= {int(board[i][j])}
                print(i//3, j//2)
                possible_board_mass[i // 3][j // 2] -= {int(board[i][j])}
                solved += 1

    while solved != 36:
        for i in range(6):
            for j in range(6):
                cross = (possible_board_col[i] & possible_board_row[j]) & possible_board_mass[i//1][j//2]
                element = board[i][j]
                if len(cross) == 2 and '/' in element:  # 분수 꼴로 알맞은 값
                    A, B = cross.pop(), cross.pop()
                    if A < B:
                        board[i][j] = A + '/' + B
                    else:
                        board[i][j] = B + '/' + A
                    solved += 1
                elif len(cross) == 1:   # 숫자 꼴로 알맞은 값
                    board[i][j] = cross.pop()
                    solved += 1

    print("#{}".format(tc))
    for i in board:
        print(*i)

