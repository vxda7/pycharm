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

    if L == 0:
        return
    for i in range(4):
        ni = R + di[i]
        nj = C + dj[i]
        if 0 <= ni < N and 0 <= nj < M and [ni, nj] not in visited:
            before = underground[R][C]
            after = underground[ni][nj]
            if after:
                if ri[i] in puzzle[before] and rj[i] in puzzle[after]:
                    visited.append([ni, nj])
                    # stack.append([ni, nj])
                    find(N, M, ni, nj, L - 1)

                # if i == 0:  # 위로 붙을 때
                #     if 0 in puzzle[before] and 1 in puzzle[after]:  # 밑에는 위쪽 위에는 아래쪽을 가진다.
                #         visited.append([ni, nj])
                #         find(N, M, ni, nj, L - 1)
                # elif i == 1:  # 아래로 붙을 때
                #     if 1 in puzzle[before] and 0 in puzzle[after]:  # 전에는 아래쪽 후에는 위쪽을 가진다.
                #         visited.append([ni, nj])
                #         find(N, M, ni, nj, L - 1)
                # elif i == 2:  # 왼쪽으로 붙을 때
                #     if 2 in puzzle[before] and 3 in puzzle[after]:  # 전에는 왼쪽 후에는 오른쪽을 가진다.
                #         visited.append([ni, nj])
                #         find(N, M, ni, nj, L - 1)
                # elif i == 3:  # 오른쪽으로 붙을 때
                #     if 3 in puzzle[before] and 2 in puzzle[after]:  # 전에는 오른쪽 후에는 아래쪽을 가진다.
                #         visited.append([ni, nj])
                #         find(N, M, ni, nj, L - 1)


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
    print(visited)
    print("#{} {}".format(tc, res))
