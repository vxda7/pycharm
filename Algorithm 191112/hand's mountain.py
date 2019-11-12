di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def make(i, j, what, length, visited, H):
    global ans
    # print(i,j)
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            # print(ni,nj)
            if arr[ni][nj] < H:
                visited[ni][nj] = 1
                make(ni, nj, what, length + 1, visited, arr[ni][nj])
                visited[ni][nj] = 0
                # print('끝내고 돌아옴')
            else:
                if what == 1:
                    if length > ans:
                        ans = length
                        # print('더이상 못깎 여기서끝', ans)
                else:
                    if arr[ni][nj] - K < H:
                        visited[ni][nj] = 1
                        # print('여기깎음', ni,nj)
                        make(ni, nj, 1, length + 1, visited, H - 1)
                        visited[ni][nj] = 0
                        # print('끝내고 돌아옴')

for tc in range(int(input())):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    maxH = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > maxH:
                maxH = arr[i][j]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == maxH:
                # print('여기부터 시작', i, j)
                array = [[0] * N for _ in range(N)]
                array[i][j] = 1
                make(i, j, 0, 1, array, maxH)
    print('#'+str(tc+1), ans)