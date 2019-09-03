def find(day, month, threemonth, year, useplan):
    short = day * sum(useplan)
    monthorday = [0]*12
    for i in range(12):
        if useplan[i]:
            if useplan[i]*day < month:
                monthorday[i] = 1       # 1은 하루씩이 더 싸다
            else:
                monthorday[i] = 2       # 2는 한달씩이 더 싸다

    j = 0
    while j != 12:
        if monthorday[j]:
            dayplusmonth = sum([day * useplan[k] if monthorday[j] <= 1 else month for k in range(j % 12, (j+3) % 12)])
            print(dayplusmonth)
            if dayplusmonth > threemonth:
                print(monthorday)
                monthorday[j % 12: (j+3) % 12] = [3, 3, 3]      # 3은 세달씩이 더 싸다
                j += 2
        j+=1
                # 세달치 요금이 가장 비싼 구간에 넣어야한다.
                # for kk in range(j % 12, (j + 3) % 12):
                #     if monthorday[j]:
                #         monthorday[kk] = 3  # 3은 세달씩이 더 싸다

    res = 0
    for m in range(12):
        if monthorday[m] == 1:
            res += useplan[m]*day
        elif monthorday[m] == 2:
            res += month
        elif monthorday[m] == 3:
            res += threemonth/3

    return int(res)


t = int(input())
for tc in range(1, t+1):
    day, month, threemonth, year = map(int, input().split())
    useplan = list(map(int, input().split()))
    res = find(day, month, threemonth, year, useplan)
    print("#{} {}".format(tc, res))