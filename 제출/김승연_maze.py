import sys
sys.stdin = open("sample_input.txt", "r")


def find(scol, srow):
    global maze
    global N
    dl = [0, 1, 0, -1]
    dr = [1, 0, -1, 0]
    queue = [[scol, srow]]
    visited = [[0] * N for _ in range(N)]
    visited[scol][srow] = 1
    while queue != []:
        n = queue.pop(0)
        for i in range(4):
            ndl = n[0] + dl[i]
            ndr = n[1] + dr[i]
            if ndl >= 0 and ndl < N and ndr >= 0 and ndr < N:   # 미로안에 있는가
                if maze[ndl][ndr] == 3: #   3이면 반환
                    return visited[n[0]][n[1]] - 1
                elif maze[ndl][ndr] != 1 and visited[ndl][ndr] == 0:   #  1이 아니고 방문을 안했다면
                    queue.append([ndl, ndr])
                    visited[ndl][ndr] += 1 + visited[n[0]][n[1]]
    return 0

# def bfs(i, j , N):
#     global maze
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#     # 초기화
#     q=[]    #큐생성
#     visited = [[0]*N for _ in range(N)] #visited 생성
#     q.append([i, j])    # 시작점 인큐
#     visited[i][j] = 1   # 시작점 방문표시
#
#     # 탐색
#     while len(q) != 0:  # 큐가 비어있지 않으면 반복
#         n = q.pop(0)    # 디큐
#         i, j = n[0], n[1]
#         if maze[i][j] == 3: # visit()
#             print(visited)
#             return visited[i][j] - 2
#         # i, j에 인접하고 방문하지 않은 칸을 인큐
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if ni >= 0 and ni < N and nj >= 0 and nj < N:   # 미로를 벗어나지 않고
#                 if maze[ni][nj] != 1 and visited[ni][nj] == 0:  # 벽이아니고, 방문하지 않은 칸이면
#                     q.append([ni, nj])  # 인큐
#                     visited[ni][nj] += 1 + visited[i][j]   # 방문 표시
#
#     return 0



test_case = int(input())
for case in range(1, test_case + 1):
    N = int(input())
    maze = []
    for i in range(N):
        get = list(map(int,list(input())))
        maze.append(get)
        if 2 in get:
            scol = i
            srow = get.index(2)
    result = find(scol, srow)
    # result = bfs(scol, srow, N)
    print("#{} {}".format(case, result))
