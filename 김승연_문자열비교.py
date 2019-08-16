test_case = int(input())

for case in range(1,test_case+1):
    first = input()
    second = input()
    first_long = len(first)
    second_long = len(second)

    count=0
    result = 0
    while count < second_long:
        if second[count] in first:
            if first == second[count:count+first_long]:
                result = 1
                break
        count+=1

    print("#{} {}".format(case, result))