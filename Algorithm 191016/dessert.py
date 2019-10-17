def find(col, row):
    


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    desserts = [list(map(int, input().split())) for i in range(N)]

    maxV = -2

    # 출발점 선택
    for i in range(N):
        for j in range(N):
            one = find(i, j)
            if maxV < one:
                maxV = one

    print("#{} {}".format(tc, maxV))
