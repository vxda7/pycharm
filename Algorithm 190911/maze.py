def find(i, j):
    global blocks
    stack = [[i, j]]
    dc = [0, 1, 0, -1]
    dr = [1, 0, -1, 0]

    while stack != []:
        col, row = stack.pop()

        for i in range(4):
            nc = col + dc[i]
            nr = row + dr[i]
            if 0 <= nc < 100 and 0 <= nr < 100:
                if blocks[nc][nr] == '3':
                    return 1
                elif blocks[nc][nr] == '0':
                    blocks[nc][nr] = '1'
                    stack.append([nc, nr])
    return 0


for tc in range(10):
    t = int(input())
    blocks = [list(input()) for i in range(100)]
    res = find(1, 1)    # 1 가능 0 불가능
    print("#{} {}".format(t, res))