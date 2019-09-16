def change(N, M):
    global codes
    pattern = [211, 221, 122, 411, 132, 231, 114, 312, 213, 112]
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            temp = ''
            if codes[i][j] != '0':
                temp += bin(int(codes[i][j], 16))[2:]



t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    codes = [input() for i in range(N)]
    change(N, M)