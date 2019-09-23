def prem(n):
    while p[n] != n:
        n = p[n]
    return n


def prim(start):
    global V, E
    visited = [start]
    for i in range()




T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    p = [i for i in range(V+1)]# 대표원소 배열
    near = [[0]*(V+1) for i in range(V+1)]
    for i in edge:
        a, b = i[0], i[1]
        near[a][b], near[b][a] = i[2], i[2]
    prim(0)
    print(near)


