def find(N):
    global ri, ni, pi
    for i in range(N):
        if cmd[i][0] == 1:
            if not nodes:
                nodes[ni] = cmd[i][1]
                ni += 1
            else:
                j = pi
                while nodes[j] != 0:
                    if nodes[j] < cmd[i][1]:
                        nodes.insert(j, cmd[i][1])
                        ni += 1
                        break
                    j += 1
                else:
                    nodes[ni] = cmd[i][1]
                    ni += 1
        elif cmd[i][0] == 2:
            if pi != ni:
                res[ri] = nodes[pi]
                pi += 1
                ri += 1
            else:
                res[ri] = -1
                ri += 1

    return res


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    cmd = [list(map(int, input().split())) for i in range(N)]
    res = [0] * N
    nodes = [0] * N
    ri, ni, pi = 0, 0, 0
    res = find(N)
    print("#{}".format(tc), end=" ")
    # print(res)
    print(*res[:ri])
