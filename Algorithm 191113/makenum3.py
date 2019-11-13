import time, sys
sys.stdin = open("sample_input (5).txt", "r")
start = time.time()

def perp(start, end, this):
    global minV, maxV
    if start == end:
        cal = nums[0]
        # 하나씩 연산
        for one in range(N-1):
            if operators[this[one]] == '+':
                cal += nums[one + 1]
            elif operators[this[one]] == '-':
                cal -= nums[one + 1]
            elif operators[this[one]] == '*':
                cal *= nums[one + 1]
            elif operators[this[one]] == '/':
                cal = int(cal / nums[one + 1])
        if cal < minV:
            minV = cal
        if cal > maxV:
            maxV = cal
    else:
        for i in range(end):
            this[start], this[i] = this[i], this[start]
            if operators[start] != operators[i]:
                perp(start + 1, end, this)
            this[start], this[i] = this[i], this[start]


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    op_count = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    # + - * /
    operators = ['+'] * op_count[0] + ['-'] * op_count[1] + ['*'] * op_count[2] + ['/'] * op_count[3]

    op_poss = []
    temp = list(range(N - 1))
    minV = 100000001
    maxV = -100000001
    perp(0, N - 1, temp)


    # print(maxV, minV)
    print("#{} {}".format(tc, maxV - minV))

    print(time.time() - start)