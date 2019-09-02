t = int(input())
for tc in range(1, t+1):
    N, M, L = map(int, input().split())
    getlist = list(map(int, input().split()))
    res = 0
    for i in range(M):
        get = input().split()
        if get[0] == 'I':
            getlist.insert(int(get[1]), int(get[2]))
        elif get[0] == 'D':
            del getlist[int(get[1])]
        elif get[0] == 'C':
            getlist[int(get[1])] = int(get[2])

    if len(getlist) > L:
        print("#{} {}".format(tc, getlist[L]))
    else:
        print("#{} -1".format(tc))