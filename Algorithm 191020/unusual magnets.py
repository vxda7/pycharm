def rot(o, d, changed, idx):
    if o == 1:
        if magnet1[(idx[0] + 2) % 8] != magnet2[(idx[1] - 2 + 8) % 8] and changed == 0:  # 두 극이 다르고 순수하면
            rot(2, -d, -1, idx)  # 2번자석에 영향주기
        if d == 1:
            idx[0] = (idx[0] - 1 + 8) % 8  # 시계로 한칸
        else:
            idx[0] = (idx[0] + 1) % 8  # 반시계로 한칸

    elif o == 2:
        if changed == 0:  # 순수하면 양쪽에 영향주기
            if magnet1[(idx[0] + 2) % 8] != magnet2[(idx[1] - 2 + 8) % 8]:
                rot(1, -d, 1, idx)  # 1번에 무영향 회전
            if magnet2[(idx[1] + 2) % 8] != magnet3[(idx[2] - 2 + 8) % 8]:
                rot(3, -d, -1, idx)  # 3번에 신호
        elif changed == -1:  # 왼쪽 영향이면
            if magnet2[(idx[1] + 2) % 8] != magnet3[(idx[2] - 2 + 8) % 8]:
                rot(3, -d, -1, idx)  # 3번에 신호
        elif changed == 1:  # 오른쪽 영향이면
            if magnet1[(idx[0] + 2) % 8] != magnet2[(idx[1] - 2 + 8) % 8]:
                rot(1, -d, 1, idx)  # 1번에 신호
        if d == 1:
            idx[1] = (idx[1] - 1 + 8) % 8  # 시계로 한칸
        else:
            idx[1] = (idx[1] + 1) % 8  # 반시계로 한칸

    elif o == 3:
        if changed == 0:  # 순수하면 양쪽에 영향주기
            if magnet2[(idx[1] + 2) % 8] != magnet3[(idx[2] - 2 + 8) % 8]:
                rot(2, -d, 1, idx)  # 2번에 신호
            if magnet3[(idx[2] + 2) % 8] != magnet4[(idx[3] - 2 + 8) % 8]:
                rot(4, -d, -1, idx)  # 4번에 무영향 신호
        elif changed == -1:  # 왼쪽 영향이면
            if magnet3[(idx[2] + 2) % 8] != magnet4[(idx[3] - 2 + 8) % 8]:
                rot(4, -d, -1, idx)  # 4번에 신호
        elif changed == 1:  # 오른쪽 영향이면
            if magnet2[(idx[1] + 2) % 8] != magnet3[(idx[2] - 2 + 8) % 8]:
                rot(2, -d, 1, idx)  # 2번에 신호
        if d == 1:
            idx[2] = (idx[2] - 1 + 8) % 8  # 시계로 한칸
        else:
            idx[2] = (idx[2] + 1) % 8  # 반시계로 한칸

    elif o == 4:
        if magnet3[(idx[2] + 2) % 8] != magnet4[(idx[3] - 2 + 8) % 8] and changed == 0:  # 두 극이 다르고 순수하면
            rot(3, -d, 1, idx)  # 2번자석에 영향주기
        if d == 1:
            idx[3] = (idx[3] - 1 + 8) % 8  # 시계로 한칸
        else:
            idx[3] = (idx[3] + 1) % 8  # 반시계로 한칸

    return idx


def find(k):
    idx = [0] * 4
    idx1, idx2, idx3, idx4 = idx
    for i in range(k):
        idx1, idx2, idx3, idx4 = rot(order[i], direction[i], 0, idx)
    # 계산식 반환
    return magnet1[idx1] + magnet2[idx2] * 2 + magnet3[idx3] * 4 + magnet4[idx4] * 8, idx


t = int(input())
for tc in range(1, t + 1):
    K = int(input())
    magnet1 = list(map(int, input().split()))
    magnet2 = list(map(int, input().split()))
    magnet3 = list(map(int, input().split()))
    magnet4 = list(map(int, input().split()))
    order = []
    direction = []
    for i in range(K):
        o, d = map(int, input().split())
        order.append(o)
        direction.append(d)

    res, idx = find(K)
    # print(idx)
    # for what in range(1, 5):
    #     print(eval("magnet" + str(what)))
    print("#{} {}".format(tc, res))
