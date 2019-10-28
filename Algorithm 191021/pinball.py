def find(col, row, direction):
    

t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    board = [list(map(int, input().split())) for i in range(N)]
    maxV = 0
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(N):
        for j in range(N):
            for k in direction:
                temp = find(i,j,k)
                if maxV < temp:
                    maxV = temp

    print("#{} {}".format(tc, maxV))
