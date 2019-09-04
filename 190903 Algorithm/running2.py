import sys
sys.stdin = open("sample_input (2).txt", "r")

def find(N, M, R, C, L):
    global underground
    global visited
    global stack
    puzzle = {1: [0, 1, 2, 3], 2: [0, 1], 3: [2, 3], 4: [0, 3], 5: [1, 3], 6: [1, 2], 7: [0, 2]}
    # 0,1,2,3   상하좌우    0
    #                  2        3
    #                       1       R 세로 C 가로
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    ri = [0, 1, 2, 3]
    rj = [1, 0, 3, 2]
    prewhere = visited[-1]
    queue = [[R, C]]
    while queue != []:
        if L == 0:
            break
        R, C = queue.pop(0)

        for i in range(4):
            ni = R + di[i]
            nj = C + dj[i]
            if 0 <= ni < N and 0 <= nj < M and [ni, nj] not in visited:
                before = underground[R][C]
                after = underground[ni][nj]
                if after:
                    if ri[i] in puzzle[before] and rj[i] in puzzle[after]:
                        queue.append([ni, nj])
                        visited.append([ni, nj])

        if prewhere == [R, C]:
            L -= 1
            if queue != []:
                prewhere = queue[-1]

t = int(input())
for tc in range(1, t + 1):
    N, M, R, C, L = map(int, input().split())   # M 가로크기 row 최대값 N 세로크기 col 최대값
    underground = []
    for i in range(N):
        get = list(map(int, input().split()))
        underground.append(get)

    visited = []
    stack = []
    visited.append([R, C])  # 세로위치 가로위치 순서
    find(N, M, R, C, L - 1)
    res = len(visited)
    # print(visited)
    print("#{} {}".format(tc, res))