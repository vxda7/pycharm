t = int(input())
for tc in range(1, t+1):
    N, M, K = map(int, input().split())     # 세로, 가로, 배양시간
    board = [list(map(int, input().split())) for i in range(N)]
    # empty = [[0]*650 for i in range(650)]
    # for i in range(650//2 - N//2, 650// + N//2):

