result = []
t = int(input())
for tc in range(1, t+1):
    m, n, k = map(int, input().split())
    ground = [[0]*m for i in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        ground[y][x] = 1

    cnt = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for j in range(n):
        for i in range(m):
            if ground[j][i] == 1:
                cnt += 1
                queue = []
                ground[j][i] = 0
                queue.append([j, i])
                while queue != []:
                    tj, ti = queue.pop(0)
                    ground[tj][ti] = 0
                    for k in range(4):
                        nj = tj + dj[k]
                        ni = ti + di[k]
                        if 0 <= ni < m and 0 <= nj < n:
                            if ground[nj][ni] == 1:
                                queue.append([nj, ni])
    result.append(cnt)

for i in range(t):
    print(result[i])