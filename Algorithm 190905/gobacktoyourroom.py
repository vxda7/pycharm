t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for i in range(N)]
    corrider = [0]*200
    while rooms != []:
        get = rooms.pop()
        start = get[0]
        end = get[1]
        if start > end:
            start, end = end, start
        for i in range((start-1)//2, (end-1)//2+1):
            corrider[i] += 1
        print(corrider)
    time = max(corrider)
    print("#{} {}".format(tc, time))
