def make(start, end, temp, w):
    if start == end:
        possibles.append(temp[:])
    else:
        for i in range(w):
            make(start + 1, end, temp + [i], w)


t = int(input())
for tc in range(1, t + 1):
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for i in range(H)]

    possibles = []
    make(0, N, [], W)
    minV = 1000
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    # 경우 하나 뽑기
    for possible in possibles:
        block = [i[:] for i in blocks]  # 깨뜨릴 맵 복사
        for poss in possible:  # 깨뜨릴 위치 지정
            high = 0
            while high != H:
                if block[high][poss] == 0:
                    high += 1
                else:
                    break
            if high != H:
                # 깨기
                queue = [(high, poss)]
                while queue != []:
                    col, row = queue.pop(0)
                    howlong = block[col][row]
                    block[col][row] = 0
                    for direct in directions:
                        for boom in range(1, howlong):
                            nc = col + direct[0] * boom
                            nr = row + direct[1] * boom
                            if 0 <= nc < H and 0 <= nr < W:
                                if block[nc][nr] == 1:
                                    block[nc][nr] = 0
                                elif block[nc][nr] > 1:
                                    queue.append((nc, nr))

            # 내려주기
            for downrow in range(W):
                downidx = H -1
                while downidx != -1:
                    if block[downidx][downrow] != 0:
                        downidx -= 1
                    else:
                        find = downidx - 1
                        while find != -1:
                            if block[find][downrow] == 0:
                                find -= 1
                            else:
                                break
                        if find != -1:
                            block[downidx][downrow], block[find][downrow] = block[find][downrow], 0
                            downidx -= 1
                        else:
                            break

            # 남은 벽돌 수 찾기
            cnt = 0
            for hh in range(H):
                for ww in range(W):
                    if block[hh][ww]:
                        cnt += 1
            if cnt < minV:
                minV = cnt
                if minV == 0:
                    break
        else:
            continue
        break

    print("#{} {}".format(tc, minV))
