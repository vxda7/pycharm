test_case = int(input())
for case in range(1, test_case + 1):
    get = input()
    if get == get[::-1]:
        print("#{} 1".format(case))
    else:
        print("#{} 0".format(case))
