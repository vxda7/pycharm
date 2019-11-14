def game(possible):
    global N, M, D, ENEMY
    tboard = [i[:] for i in board]
    directions = [(0, -1), (-1, 0), (0, 1)]

    kill = 0  # 죽인 수 결과값
    damage = 0  # 성에 닿아서 사라진 수
    deadlist = set()  # 동시공격 때문에 생길 공간
    time = 0

    while damage + kill != ENEMY:
        # 궁수 위치 큐에 쌓기
        for one in range(M):
            if possible[one] == 1:
                queue = [(N - 1, one, 1)]
                # 궁수의 공격
                while queue != []:
                    col, row, distance = queue.pop(0)

                    if tboard[col][row] == 1:
                        deadlist.add((col, row))
                        break
                    else:
                        if distance < D:
                            for direct in directions:
                                nc = col + direct[0]
                                nr = row + direct[1]
                                if 0 <= nc < N and 0 <= nr < M:
                                    queue.append((nc, nr, distance + 1))


        # deadlist 지우기
        if deadlist:
            for i in range(len(deadlist)):
                col, row = deadlist.pop()
                tboard[col][row] = 0
                kill += 1

        # 적의 이동
        for i in range(M):
            for j in range(N - 1, -1, -1):
                if tboard[j][i] == 1:
                    if j == N - 1:  # 성에 닿아서 사라짐
                        tboard[j][i] = 0
                        damage += 1
                    else:  # 한칸 내려옴
                        tboard[j + 1][i] = 1
                        tboard[j][i] = 0
        # 시간 증가
        time += 1
    return kill


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
ENEMY = sum(map(sum, board))

possibles = []
for i in range(1 << M):
    temp = []
    for j in range(M):
        if i & (1 << j):
            temp.append(1)
        else:
            temp.append(0)
    if sum(temp) == 3:
        possibles.append(temp[:])
maxV = 0
for poss in possibles:
    res = game(poss)
    if maxV < res:
        maxV = res
print(maxV)
