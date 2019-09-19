t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    worklist = []
    for i in range(N):
        start, end = map(int, input().split())
        worklist.append([start, end])
    worklist.sort(key=lambda x: x[1])
    work = 1
    start, end = worklist.pop(0)
    for i in range(N-1):
        nstart, nend = worklist[i]
        if end <= nstart:
            work += 1
            end = nend
    print("#{} {}".format(tc, work))