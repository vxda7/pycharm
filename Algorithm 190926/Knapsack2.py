import time

start = time.time()


def find(N, K):
    for i in range(N):
        for w in range(1, K + 1):
            if valuelist[i][0] > w:
                table[i][w] = table[i - 1][w]
            else:
                table[i][w] = max(table[i - 1][w - valuelist[i][0]] + valuelist[i][1], table[i - 1][w])
    return table[-1][-1]


t = int(input())
for tc in range(1, t + 1):
    N, K = map(int, input().split())
    valuelist = [list(map(int, input().split())) for i in range(N)]
    maxV = 0
    table = [[0] * (K + 1) for i in range(N)]
    print("#{} {}".format(tc, find(N, K)))
      # 현재 선택한 물건 갯수, 현재 선택한 물건의 가치, 남은 가방의 부피
    # print(table)

print(time.time() - start)
