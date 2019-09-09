import time
import sys
start = time.time()
sys.stdin = open("sample_input (3).txt",'r')


def addtemp(value):
    global temp
    if value not in temp:
        temp.append(value)  # 메모리주소 복사해줌


def check():
    global info
    global N
    global temp
    temp = []
    for i in range(N):
        for j in range(i+1, N):
            x1, x2, y1, y2, d1, d2= info[i][0], info[j][0], info[i][1], info[j][1], info[i][2], info[j][2]
            xdiff = x1 - x2
            ydiff = y1 - y2
            if x1 == x2 and y1 == y2:   # 같은 위치라면
                addtemp(info[i])
                addtemp(info[j])
            elif xdiff == -1 and d1 == 3 and d2 == 2 and y1 == y2:   # 좌우로 0.5칸씩 만나면
                addtemp(info[i])
                addtemp(info[j])
            elif xdiff == 1 and d1 == 2 and d2 == 3 and y1 == y2:   # 좌우로 0.5칸씩 만나면
                addtemp(info[i])
                addtemp(info[j])
            elif ydiff == -1 and d1 == 0 and d2 == 1 and x1 == x2: # 세로로 0.5칸씩 만나면
                addtemp(info[i])
                addtemp(info[j])
            elif ydiff == 1 and d1 == 1 and d2 == 0 and x1 == x2: # 세로로 0.5칸씩 만나면
                addtemp(info[i])
                addtemp(info[j])
            elif info[i][0] < -1000 or info[i][0] > 1000 or -1000 > info[i][1] or info[i][1] > 1000:
                addtemp(info[i]+[0])
    # temp에 들어있는 항목들을 info에서 모두 제거
    energy = 0
    if temp:
        for k in temp:
            if len(k) == 5:
                k.pop()
            else:
                energy += k[3]  # 에너지를 추가
            info.remove(k)
            N -= 1
    return energy


def find(cnt):
    global info
    global power
    # 0상 1하 2좌 3우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    power += check()
    # while cnt < 2001 and info != []:
    #     # 모든 원소 자기 방향으로 이동
    #     # print(info)
    #     for i in range(N):
    #         x, y, direction, energy  = info[i]
    #         x += dx[direction]
    #         y += dy[direction]
    #         info[i] = [x, y, direction, energy]
    #     else:
    #         cnt += 1
    #         power += check()
    # return power

    for _ in range(2001):
        if info == []:
            break
        # 모든 원소 자기 방향으로 이동
        # print(info)
        for i in range(N):
            x, y, direction, energy  = info[i]
            x += dx[direction]
            y += dy[direction]
            info[i] = [x, y, direction, energy]
        else:
            cnt += 1
            power += check()
    return power

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    info = [list(map(int, input().split())) for i in range(N)]
    power = 0
    res = find(0)
    print("#{} {}".format(tc, res))

print(time.time() - start)