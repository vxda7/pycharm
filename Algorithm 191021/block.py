def perp(start, end):
    if start == end:
        choose.append(line[:])
    else:
        for i in range(start, N):
            line[start], line[i] = line[i], line[start]
            perp(start+1, end)
            line[start], line[i] = line[i], line[start]

t = int(input())
for tc in range(1, t+1):
    N, W, H = map(int, input().split())
    line = list(range(N))
    choose = []
    perp(0, N)

    board = [list(map(int, input().split())) for i in range(H)]