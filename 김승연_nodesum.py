import sys
sys.stdin = open("sample_input (9).txt", "r")


def make(start, end):
    global N
    if start <= end:
        make(start * 2, end)
        make(start * 2 + 1, end)
        if visit[start] == 0:
            if start*2 +1 <= N:
                visit[start] = visit[start*2] + visit[start*2+1]
            else:
                visit[start] = visit[start*2]


t = int(input())
for tc in range(1, t + 1):
    N, M, L = map(int, input().split())
    visit = [0] * (N + 1)
    for i in range(M):
        nodenum, num = map(int, input().split())
        visit[nodenum] = num
    save1 = 0
    save2 = 0
    before = 0
    make(1, N)
    if visit[2] and visit[3]:
        visit[1] = visit[2] + visit[3]
    # print(visit)
    print("#{} {}".format(tc, visit[L]))
