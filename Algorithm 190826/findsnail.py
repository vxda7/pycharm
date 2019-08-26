# 오른쪽부터 시계방향으로 0, 1, 2, 3 방향이라 정함
# 0번 방향으로 설정, 맨 위쪽 윗칸을 탐색 위치로 정함.
# 설정 방향으로 탐색 시작
# 현재 방향의 마지막 칸이거나, 다음 칸에 값이 있으면
# 다음 방향으로 변경
# NxN칸 이내면 3) 반복
# 더이상 남은 칸이 없으면 종료

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    dir = 0
    i = 0   # 현재칸 좌표
    j = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    k = 1   # 칸에 기록할 값
    while k <= N**2:   # 아직 NxN칸 이내면
        arr[i][j] = k   # 현재칸에 값을 쓰고
        # 다음칸을 결정, 배열을 벗어나지 않고 비어있어야 함
        # 현재 방향으로 다음칸을 계산할 지, 다음 방향으로 계산할 지 결정
        k += 1
        ni = i+di[dir]
        nj = j+dj[dir]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            dir = (dir+1) % 4
            i += di[dir]
            j += dj[dir]
    for i in arr:
        print(*i)
        
