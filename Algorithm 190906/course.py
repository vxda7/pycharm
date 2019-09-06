import sys
import time
start = time.time()
sys.stdin = open("input (2).txt", "r")


def find(col, row, visited, n):
    global minV
    global home
    # print("모든 값")
    # print(col, row, visited, n)
    if n > minV or (visited == [] and n >= minV):
        return
    elif visited == [] and n < minV:
        n += abs(col - home[0]) + abs(row - home[1])
        minV = n
        return
    else:
        for i in range(len(visited)):
            temp = [one[:] for one in visited]
            tcol, trow = temp.pop(i)
            distance = n + abs(col - tcol) + abs(row - trow)
            # print("템프")
            # print(temp, n)
            find(tcol, trow, temp, distance)


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    places = list(map(int, input().split()))
    company = places[0:2]
    home = places[2:4]
    clients = places[4:]
    clients = [clients[i:i + 2] for i in range(0, N + N, 2)]
    minV = 100000000000
    for i in range(N):
        n = abs(company[0] - clients[i][0]) + abs(company[1] - clients[i][1])
        find(clients[i][0], clients[i][1], clients[:i] + clients[i+1:], n)
    print("#{} {}".format(tc, minV))

    # 거리 |x1-x2| + |y1-y2|

print(time.time()-start)