def rep(n):
    while n != p[n]:
        n = p[n]
    return n


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    edge.sort(key=lambda x: x[2])  # 가중치를 기준으로 오름차순

    p = [i for i in range(V + 1)]  # 대표원소 배열
    cnt = 0
    s = 0
    for x in edge:  # N개의 노드(V+1)가 있는 겨우 N-1개의 간선을 선택(V)
        n0 = rep(x[0])
        n1 = rep(x[1])
        if n0 != n1:  # 두 노드이 대표원소가 다르면 mst에 추가
            p[n1] = n0
            cnt += 1  # 간선을 선택한 경우
            s += x[2]
            if cnt == V:  #
                break
    print("#{} {}".format(tc, s))
