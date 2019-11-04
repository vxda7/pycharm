from copy import deepcopy
t = int(input())
for tc in range(1, t+1):
    board = [input().split() for i in range(6)]
    possible = set(range(1, 10))
    solved = 0  # 탈출 조건을 위한 값 몇 개의 칸이 해결되었는지 세줌 36이 되면 탈출
    for i in range(6):
        for j in range(6):
            element = board[i][j]
            if '/' in element:  # 분수면
                if element[0] == '-' and element[-1] == '-':    # 두칸다 모르면
                    board[i][j] = [deepcopy(possible), deepcopy(possible)]
                elif element[0] == '-':     # 앞칸만 모르면
                    board[i][j] = [deepcopy(possible), int(element[-1])]
                elif element[-1] == '-':    # 뒷칸만 모르면
                    board[i][j] = [int(element[0]), deepcopy(possible)]
                else:                       # 둘다 안다면
                    board[i][j] = [int(element[0]), int(element[-1])]
                    solved += 1
            elif element == '-':    # 빈칸이라면
                board[i][j] = deepcopy(possible)
            else:   # 숫자라면
                board[i][j] = int(board[i][j])
                solved += 1
    print(board)

    # 각 칸에 빈곳을 채워보자
    while True:
        for i in range(6):
            for j in range(6):
                element = board[i][j]
                # element 의 타입에 따라 할 일이 정해짐
                element_type = type(element)
                if element_type == int:     # 정해진 숫자면 넘어가고
                    pass
                elif element_type == set:   # 안정해졌으면 다른 가능성을 배제하자
                    board[i][j] -= find(i, j, element)  # 특정위치에서 배제할 값을 찾아내는 함수를 만들자
                elif element_type == list:
                    first, last = element
                    first_type, last_type = type(first), type(last)
                    if first_type == int and last_type == int:  # 정해진 분수면 탈출
                        pass
                    elif first_type == set and last_type == set: # 둘다 안정해 졌으면 각각 배제
                        board[i][j][0] -= find(i, j, element)
                        board[i][j][1] -= find(i, j, element)



