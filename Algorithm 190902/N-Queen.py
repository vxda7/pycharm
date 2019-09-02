def find(N):
    stack = []
    stack.append([0,0])
    # place.append([0,0])
    cnt = 0
    res = 0
    ok = False
    next = 0
    while stack != []:
        get = stack.pop()
        col, row = get[0], get[1]
        for i in stack:     # 확인하는 곳
            if i[0] != col and i[1] != row and i[0]+i[1] != col+row and i[0]-i[1] != col-row:
                ok = True
                cnt += 1
                if cnt == N:
                    res += 1
                    cnt = 0
        if ok:      # 위치가 관계없다면 추가
            if 0 <= col + 1 < N and 0 <= row + next < N:
                stack.append([col+1, row+2])
    return res


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    print("#{} {}".format(tc, find(N)))