numbers = int(input())
table = []
for number in range(numbers):
    lines = list(map(int, input().split()))
    table.append(lines)

cnt = 0
for i in range(1, numbers-1):
    for j in range(1, numbers-1):
        if table[i][j] > max(table[i + 1][j], table[i - 1][j], table[i][j + 1], table[i][j - 1], table[i + 1][j + 1], table[i - 1][j - 1], table[i + 1][j - 1], table[i - 1][j + 1]):
            cnt += 1
print(cnt)