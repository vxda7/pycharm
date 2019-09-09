def find(children, cnt, root):  # root를 부모로 가진 자식의 갯수 반환
    for i in range(len(children)):
        if children[i] == root:
            cnt += find(children, 1, i)
    return cnt


t = int(input())
for tc in range(1, t + 1):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))
    children = [0] * (E+2)
    for i in range(E):
        first = nodes[i * 2]
        last = nodes[i * 2 + 1]
        children[last] = first
    # print(children)
    res = find(children, 1, N)
    print("#{} {}".format(tc, res))