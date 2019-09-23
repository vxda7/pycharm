def rep(n):
    while p[n] != n:
        n = p[n]
    return n


t = int(input())
V, E = map(int, input().split())
nodes = [list(map(int, input().split())) for i in range(E)]
p = list(range(V+1))
for i in range(E):
    a, b = nodes[i][0], nodes[i][1]
    p[rep(a)] = rep(b)
