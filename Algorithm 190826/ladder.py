for tc in range(1, 11):
    T = int(input())
    ladder = []
    for i in range(100):
        get = input().split()
        get = ['0'] + get + ['0']   # idx가 1늘어남
        ladder.append(get)

    where = ladder[99].index('2')   # 진짜는 where-=1

    x = 0
    for i in range(98,-1,-1):
        if ladder[i][where+x+1] == '1':
            while ladder[i][where+x+1] != '0':
                x += 1

        elif ladder[i][where+x-1] == '1':
            while ladder[i][where+x-1] != '0':
                x -= 1

    print("#{} {}".format(tc, where+x-1))