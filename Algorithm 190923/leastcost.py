def find(N):
    global minV
    queue = [[0, 0]]
    dc = [0, 1, 0, -1]
    dr = [1, 0, -1, 0]
    while queue != []:
        col, row = queue.pop(0)
        for i in range(4):
            nc = col + dc[i]
            nr = row + dr[i]
            if 0 <= nc < N and 0 <= nr < N:
                energy = pair[col][row] + 1
                diff = world[nc][nr] - world[col][row]
                if diff >= 1:
                    energy += diff
                if pair[nc][nr] == 0:
                    pair[nc][nr] = energy
                    queue.append([nc, nr])
                else:
                    if pair[nc][nr] > energy:
                        pair[nc][nr] = energy
                        queue.append([nc, nr])
    return pair[-1][-1]


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    world = [list(map(int, input().split())) for i in range(N)]
    pair = [[0]*N for i in range(N)]
    minV = 1000000000000000000000
    res = find(N)
    # print(pair)
    print("#{} {}".format(tc, res))
