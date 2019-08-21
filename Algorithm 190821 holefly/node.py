# import sys
# sys.stdin = open("sample_input (7).txt", 'r')

T = int(input())
for case in range(1, T + 1):
    V, E = map(int, input().split())
    node = {i: [] for i in range(1,V + 1)}
    print(node)
    for i in range(E):
        start, end = map(int, input().split())
        node[start].append(end)
        node[end].append(start)
    print(node)

    S, G = map(int, input().split())
