def inorder(n, last):
    global cnt
    if n <= last:  # 유효한 노드면...
        inorder(n*2, last)    # 왼쪽 자식으로 이동
        tree[n] = cnt   # visit()
        cnt += 1
        inorder(n*2 + 1, last)    # 오른쪽 자식으로 이동


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 1
    inorder(1, N)
    print(tree)
    print("#{} {} {}".format(tc, tree[1], tree[N//2]))

