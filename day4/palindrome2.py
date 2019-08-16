import sys
sys.stdin = open("input (12).txt", "r")


# def find(table):
#     for fix in range(100):  # 한줄 뜯어오기
#         count = 100
#         best = 1
#         for m in range(98):    # 간격을 줄여가면서 돌기
#             for where in range(101 - count, 0, -1):    # 100 - count -> 0 간격마다 돌기
#                 row = ""
#                 col = ""
#                 for interval in range(count-1):  # 0 -> count
#                     row += table[fix][where + interval]
#                     col += table[where + interval][fix]
#                 if row == row[::-1] or col == col[::-1]:
#                     if best < len(row):
#                         best = len(row)
#                         return best
#                     if best < len(col):
#                         best = len(col)
#                         return best
#             count -= 1

def find(table):
    best = 0
    for i in range(100):
        for j in range(100):
            interval = 100
            row = ''
            col = ''
            for start in range(100 - interval + 1):
                for k in range(interval):
                    row += table[i][j+k]
                    col += table[j+k][i]

                if row == row[::-1] or col == col[::-1]:
                    if len(col) < len(row):
                        return len(row)
                    else:
                        return len(col)

                interval -=1


for case in range(10):
    test_case = input()
    table = []
    for j in range(100):
        table.append(input())
    print("#{} {}".format(test_case, find(table)))