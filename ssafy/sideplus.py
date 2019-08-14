table = [
    [2, 7, 4, 3, 6],
    [8, 5, 8, 3, 2],
    [2, 2, 3, 6, 9],
    [5, 9, 2, 5, 7],
    [3, 6, 2, 9, 4],
    ]

n = len(table)
everything=0
for i in range(n):
    for j in range(n):
        if i != 0:
            everything += abs(table[i][j] - table[i - 1][j])
        if j != 0:
            everything += abs(table[i][j] - table[i][j - 1])
        if i != n-1:
            everything += abs(table[i][j] - table[i + 1][j])
        if j != n-1:
            everything += abs(table[i][j] - table[i][j + 1])
print(everything)

# 모든 칸의 이웃 출력
for i in range(n):
    for j in range(n):
        if i != 0:
            print(table[i - 1][j],end=" ")
        if j != 0:
            print(table[i][j - 1],end=" ")
        if i != n-1:
            print(table[i + 1][j],end=" ")
        if j != n-1:
            print(table[i][j + 1],end=" ")
        print()

#  모든 칸의 이웃 중 짝수만 출력! 인덱스 범위먼저 검사할 것!
for i in range(n):
    for j in range(n):
        if i != 0 and not table[i - 1][j]%2:
            print(table[i - 1][j],end=" ")
        if j != 0 and not table[i][j - 1]%2:
            print(table[i][j - 1],end=" ")
        if i != n-1 and not table[i + 1][j]%2:
            print(table[i + 1][j],end=" ")
        if j != n-1 and not table[i][j + 1]%2:
            print(table[i][j + 1],end=" ")
        print("")


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for i in range(n):
    for j in range(n):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if(ni>=0 and ni<n and nj>=0 and nj<n):
                print(table[ni][nj],end=" ")
            print("")
