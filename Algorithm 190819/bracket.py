def check(line):
    temp = []
    i = 0
    for cnt in range(len(line)):
        if line[i] == '{':
            temp.append('{')
        if line[i] == '(':
            temp.append('(')
        if line[i] == '}':
            if not temp:
                return 0
            if temp[-1] == '(':
                return 0
            else:
                temp.pop()
        if line[i] == ')':
            if not temp:
                return 0
            if temp[-1] == '{':
                return 0
            else:
                temp.pop()
        i += 1
    if temp:
        return 0
    return 1


test_case = int(input())
for case in range(1, test_case + 1):
    get = input()
    print("#{} {}".format(case, check(get)))