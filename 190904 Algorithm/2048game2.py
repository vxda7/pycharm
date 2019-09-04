def change(i, j, S):
    global board
    global setting
    global N
    di, dj = setting[S]  # 증가값
    stack = [[i, j]]
    while stack != []:
        get = stack.pop()
        i = get[0]
        j = get[1]
        ni, nj = i + di, j + dj  # 변화값



t = int(input())
for tc in range(1, t + 1):
    N, S = input().split()
    N = int(N)
    board = [list(map(int, input().split())) for i in range(N)]
    setting = {'up': [1, 0], 'down': [-1, 0], 'left': [0, 1], 'right': [0, -1]}
    for j in range(N):
        board = list(map(list, zip(*board)))
        change(j, 0, S)
    board = list(map(list, zip(*board)))
    print("#{}".format(tc))
    for line in board:
        print(*line)