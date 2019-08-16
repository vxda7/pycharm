for i in range(10):
    test_case = input()
    table = []
    for j in range(100):
        table.append(list(map(int, input().split())))
    row = [0] * 100
    col = [0] * 100
    rightarrow = 0
    leftarrow = 0

    for i in range(100):
        for j in range(100):
            row[i] += table[i][j]
            col[i] += table[j][i]
            if i == j:
                rightarrow += table[i][j]
            if i + j == 100:
                leftarrow += table[i][j]

    result = max(max(row), max(col), rightarrow, leftarrow)

    print("#{} {}".format(test_case, result))