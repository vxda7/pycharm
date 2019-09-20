def dfs2(n, k, V):
    if n == k:  # 찾는 노드에 도착한 경우
        return 1  # 목적지를 찾아서 중단하는 경우
    else:
        visited[n] = 1  # n번 노드에 방문 표시
        for i in range(1, V + 1):  # 모든 노드 i에 대해
            if adj[n][i] == 1 and visited[i] == 0:  # 인접하고 미방문이면
                if dfs2(i, k, V) == 1:  # i 로 이동, 목적지를 찾은 경우
                    return 1
        return 0  # 현재 노드 이후로 목적지가 없는 경우


V, E = map(int, input().split())
adj = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬 만들기
visited = [0] * (V + 1)  # 방문 표시용
edge = list(map(int, input().split()))
for i in range(E):
    n1, n2 = edge[i * 2], edge[i * 2 + 1]
    adj[n1][n2] = 1
    # adj[n2][n1] = 1       # 방향성 그래프인 경우는 필요없음
res = dfs2(1, 7, V)
print(res)
print(dfs2(4, 3, V))