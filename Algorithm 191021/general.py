def bfs(ai, aj):
    visited = [[-1] * 9 for _ in range(10)]
    queue = [(ai, aj)]
    di = [[0, -1, -1], [-1, -1, -1], [-1, -1, -1], [0, -1, -1], [0, 1, 1], [1, 1, 1], [1, 1, 1], [0, 1, 1]]
    dj = [[-1, -1, -1], [0, -1, -1], [0, 1, 1], [1, 1, 1], [1, 1, 1], [0, 1, 1], [0, -1, -1], [-1, -1, -1]]
    visited[ai][aj] = 0

    while queue:
        i, j = queue.pop(0)
        for k in range(8):
            ni, nj = i, j
            # 직선한칸 대각선 두칸
            for m in range(3):
                ni += di[k][m]
                nj += dj[k][m]
                if 0 <= ni < 10 and 0 <= nj < 9:
                    # 도착지점에서 왕과 만나기전에 경로에 닿으면 넘어가기
                    if ni == ER and nj == EC and m < 2:
                        break
                    # 도착지점에서 왕과 만나면 횟수 반환
                    elif ni == ER and nj == EC and m == 2:
                        return visited[i][j] + 1
                    # 도착지점에서 못만나면 횟수 기록
                    elif (ni != ER or nj != EC) and m == 2:
                        visited[ni][nj] = visited[i][j] + 1
                        queue.append([ni, nj])
    return -1

SR, SC = map(int, input().split())
ER, EC = map(int, input().split())
print(bfs(SR, SC))