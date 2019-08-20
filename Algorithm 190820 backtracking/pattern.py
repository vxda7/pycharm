test_case = int(input())
for case in range(1, test_case + 1):
    get = input()
    long = len(get)
    for j in range(1,long//2):
        if get[0:j] == get[j:2*j]:
            n = get[0:j]
            how = j
            break
    # print(n, how)

    print("#{} {}".format(case, how))
