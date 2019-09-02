# col 이 작은 순서
import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    space = [list(map(int, input().split())) for i in range(N)]
    resultstack = []

    for i in range(N):
        for j in range(N):
            if space[i][j] != 0:    # 만나면 가로세로 길이 추출
                rowcnt = 0
                colcnt = 0
                for k in range(j, N):
                    if space[i][k] == 0:
                        break
                    rowcnt += 1
                for l in range(i, N):
                    if space[l][j] == 0:
                        break
                    colcnt += 1

                resultstack.append([rowcnt, colcnt])

                # 만난 네모 제거
                rstack = []
                rstack.append([i,j])
                di = [0, 1, 0, -1]
                dj = [1, 0, -1, 0]
                while rstack != []:
                    get = rstack.pop()
                    ｋi, ｋj = get[0], get[1]
                    space[ｋi][ｋj] = 0
                    for dir in range(4):
                        ni = ｋi + di[dir]
                        nj = ｋj + dj[dir]

                        if 0 <= ni < N and 0 <= nj < N:
                            if space[ni][nj]:
                                rstack.append([ni, nj])
                # print(space)


    # 출력
    res = sorted(resultstack, key=lambda res: (res[0]*res[1], res[0]))
    print("#{} {}".format(tc, len(res)), end=" ")
    for r in res:
        print(*r, end=" ")
    print()