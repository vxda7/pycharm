import sys
sys.stdin = open("input (4).txt", "r")


def find(start, end):
    global gets
    if start <= end:
        find(start * 2, end)
        visit.append(gets[start][1])
        find(start * 2 + 1, end)


for tc in range(1, 11):
    N = int(input())
    gets = [0] + [list(input().split()) for i in range(N)]
    visit = []
    find(1, N)
    print("#{} {}".format(tc, ''.join(visit)))
