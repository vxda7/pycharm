# 태환이꺼
import sys

sys.stdin = open("input (9).txt", "r")

def rep(n):
    while n != leader[n]:
        n = leader[n]
    return n

def dfs():
    while stack:
        i, j = stack.pop()
        for k in range(4):
            ni = i + d[k][0]
            nj = j + d[k][1]
            if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0:
                t = rect[ni][nj] - rect[i][j]
                s1 = i * N + j % N
                s2 = ni * N + nj % N
                if t == 1:
                    leader[rep(s2)] = rep(s1)
                    stack.append([ni, nj])
                    visit[ni][nj] = 1
                elif t == -1:
                    leader[rep(s1)] = rep(s2)
                    stack.append([ni, nj])
                    visit[ni][nj] = 1


d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
T = int(input()) + 1
for tc in range(1, T):
    N = int(input())

rect = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
leader = list(range(N ** 2))
leader_count = [0] * (N ** 2)
stack = []

for i in range(N):
    for j in range(N):
        stack.append([i, j])
        dfs()

min_num = N ** 2
for i in range(N ** 2 - 1, -1, -1):
    leader_count[rep(i)] += 1
i = 0
answer = max(leader_count)
for i in range(N ** 2):
    if leader_count[i] == answer:
        x, y = i // N, i % N
        if rect[x][y] < min_num:
            min_num = rect[x][y]

t = leader_count.index(max(leader_count))
print('#{0} {1} {2}'.format(tc, min_num, answer))