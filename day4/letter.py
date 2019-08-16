test_case = int(input())

for case in range(1, test_case+1):
    str1 = input()
    str2 = input()
    best = 0
    for i in str1:
        count = 0
        for j in str2:
            if i == j:
                count+=1
        if best < count:
            best = count
    print("#{} {}".format(case, best))