test_case = int(input())
for case in range(1, test_case + 1):
    num = int(input())
    pascal = [[1], [1, 1]]
    print("#{}".format(case))
    for i in range(num):
        if len(pascal) < i+1:
            for k in range(len(pascal[i])):
                print(pascal[i][k], end=" ")
            print()
        else:
            pascal.append([])
            for k in range(i+1):
                if k == 0 or k == i:
                    pascal[i].append(1)
                    print(1, end=" ")
                else:
                    pascal[i].append(pascal[i-1][k-1] + pascal[i-1][k])
                    print(pascal[i-1][k-1] + pascal[i-1][k], end=" ")
            print()



