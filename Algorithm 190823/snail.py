# NxN 달팽이 배열
# 초기값 : 이동거리 K = N, 이동방향 dir = 1

# 모든 칸이 채워질 때까지
# (1) 수평 이동 (+1)
# (1-2) 이동 거리 1 감소
# (2) 수직 이동 (+1) 후 이동 방향 반전
# (1) 반복

t = int(input())
for case in range(1, t+1):
    c = 1   # 값
    N = int(input())
    k = N       # 이동거리
    dir = 1     # 증가량
    arr = [[0]*N for _ in range(N)]
    i = 0   # 시작 칸의 인덱스
    j = -1  # 현재 위치로 부터 k번 이동해야 하므로
    while(1):
        # 수평이동
        for h in range(k):
            j += dir
            arr[i][j] = c
            c += 1
        k -= 1  # 이동 거리 감소
        if k == 0:  # 이동 거리가 0이면 중단
            break
        # 수직이동
        for v in range(k):
            i += dir
            arr[i][j] = c
            c += 1
        dir *= -1   # 수직 -> 수평으로 바뀔 때 인덱스 증감 방향 전환
    print("#{}".format(case))
    for i in range(N):
        for j in range(N):
            print("{}".format(arr[i][j]),end=" ")
        print()








