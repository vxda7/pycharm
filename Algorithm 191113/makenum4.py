import time, sys
sys.stdin = open("sample_input (5).txt", "r")
start = time.time()

def find(N, operator, now, idx):
    global minV, maxV
    if idx == N:
        if minV > now:
            minV = now
        if maxV < now:
            maxV = now
    # 연산
    if operator[0] != 0:
        operator[0] -= 1
        find(N, operator[:], now + nums[idx], idx + 1)
        operator[0] += 1
    if operator[1] != 0:
        operator[1] -= 1
        find(N, operator[:], now - nums[idx], idx + 1)
        operator[1] += 1
    if operator[2] != 0:
        operator[2] -= 1
        find(N, operator[:], now * nums[idx], idx + 1)
        operator[2] += 1
    if operator[3] != 0:
        operator[3] -= 1
        find(N, operator[:], int(now / nums[idx]), idx + 1)
        operator[3] += 1

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    op_count = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    # + - * /
    operators = ['+'] * op_count[0] + ['-'] * op_count[1] + ['*'] * op_count[2] + ['/'] * op_count[3]
    minV = 100000001
    maxV = -100000001
    find(N, op_count[:], nums[0], 1)
    print("#{} {}".format(tc, maxV - minV))

print(time.time() - start)