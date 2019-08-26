T = int(input())
for tc in range(1, T+1):
    n = int(input())
    alist = list(map(int, input().split()))
    special = []
    for i in range(n//2):
        up = max(alist)
        down = min(alist)
        special.append(up)
        special.append(down)
        alist.remove(up)
        alist.remove(down)

    print("#{}".format(tc), end=" ")
    print(*special[:10])
