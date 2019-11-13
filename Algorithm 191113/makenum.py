def perp(start, end, one, possible):
    if start == end:
        possible.append(one[:])
    else:
        for i in range(end):
            one[start], one[i] = one[i], one[start]
            perp(start + 1, end, one, possible)
            one[start], one[i] = one[i], one[start]


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    op_count = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    # + - * /
    operators = ['+'] * op_count[0] + ['-'] * op_count[1] + ['*'] * op_count[2] + ['//'] * op_count[3]

    # poss = []
    # temp = list(range(N))
    # perp(0, N, temp, poss)

    op_poss = []
    temp = list(range(N - 1))
    perp(0, N - 1, temp, op_poss)
    minV = 100000001
    maxV = -100000001
    for first in nums:
        cal = first
        for num_order in op_poss:
            for op_order in op_poss:
                for one in range(N-1):
                    if operators[op_order[one]] == '+':
                        cal += nums[num_order[one]]
                    elif operators[op_order[one]] == '-':
                        cal -= nums[num_order[one]]
                    elif operators[op_order[one]] == '*':
                        cal *= nums[num_order[one]]
                    elif operators[op_order[one]] == '//':
                        cal //= nums[num_order[one]]
                if cal < minV:
                    minV = cal
                if cal > maxV:
                    maxV = cal
                print(cal)
    print(maxV, minV)
    print("#{} {}".format(tc, maxV - minV))
