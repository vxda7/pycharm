def find(N, M):
    global board
    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            if board[i][j] == '1':
                return ''.join(board[i][j - 55:j+1])


def decoding(code):
    global decodingcode
    tempcode = []
    for i in range(0, 56, 7):
        tempcode.append(decodingcode[code[i:i + 7]])
    value = 0
    # print(tempcode)
    for j in range(8):
        if j % 2 == 0:
            value += tempcode[j] * 3
        else:
            value += tempcode[j]
    # print(value)
    if value % 10 == 0:
        return sum(tempcode)
    else:
        return 0


t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    board = [list(input()) for i in range(N)]
    decodingcode = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6,
                    '0111011': 7, '0110111': 8, '0001011': 9}
    code = find(N, M)
    # print(code)
    res = decoding(code)

    print("#{} {}".format(tc, res))
