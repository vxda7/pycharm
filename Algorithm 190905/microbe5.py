class microbe:
    def __init__(self, col, row, nums, direction):
        self.col = col
        self.row = row
        self.nums = nums
        self.direction = direction


import sys
sys.stdin = open("sample_input (7).txt", "r")

t = int(input())
for tc in range(1, t + 1):
    N, M, K = map(int, input().split())
    info = [list(map(int, input().split())) for i in range(K)]
    # 0을 제외한 이동방향 상하좌우
    dc = [0, -1, 1, 0, 0]
    dr = [0, 0, 0, -1, 1]