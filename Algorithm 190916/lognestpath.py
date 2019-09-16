t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    graph = [[] for i in range(N+1)]
    for i in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    print(graph)


