import sys
sys.stdin = open("input (12).txt", "r")


def find(table):
    interval = 100
    rot = list(zip(*table))
    for j in range(99):     # table 에서 한줄 빼오기   0 ~ 99
        for i in range(100):  # 0 ~98
            for start in range(100 - interval + 1):  # 0~101-interval
                row = ''
                col = ''
                row = table[i][start: start + interval]
                col = rot[i][start: start + interval]
                if row == row[::-1] or col == col[::-1]:
                    if len(col) < len(row):
                        return len(row)
                    else:
                        return len(col)
        interval -= 1


for case in range(10):
    test_case = input()
    table = []
    for get in range(100):
        table.append(input())
    print("#{} {}".format(test_case, find(table)))

# a = [[1,2,3], [4,5,6], [7,8,9]]
# print(a)
# print(zip(a[:]))
# print(list(zip(*a)))