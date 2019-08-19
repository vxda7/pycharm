test_case = int(input())

for case in range(1, test_case + 1):
    line = list(input())
    cnt = 0
    temp = []
    for i in line:
        if not temp:
            temp.append(i)
        else:
            if temp[-1] != i:
                temp.append(i)
            else:
                del temp[-1]
    print("#{} {}".format(case, len(temp)))
