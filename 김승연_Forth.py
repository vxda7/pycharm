test_case = int(input())
for case in range(1, test_case + 1):
    line = input().split()
    stack = []
    sign = []
    result = 0
    for i in line:
        # print(stack)
        if i.isdigit():
            stack.append(int(i))
        else:
            if i == '.':
                if len(stack) != 1:
                    result = "error"
                else:
                    result = stack[0]
            elif len(stack) < 2:
                result = "error"
                break
            else:
                if i == '+':
                    temp = stack[-2] + stack[-1]
                    del stack[-2:]
                    stack.append(temp)
                elif i == '-':
                    temp = stack[-2] - stack[-1]
                    del stack[-2:]
                    stack.append(temp)
                elif i == '*':
                    temp = stack[-2] * stack[-1]
                    del stack[-2:]
                    stack.append(temp)
                elif i == '/':
                    temp = stack[-2] // stack[-1]
                    del stack[-2:]
                    stack.append(temp)
                else:
                    result = 'error'
                    break
    print("#{} {}".format(case, result))

