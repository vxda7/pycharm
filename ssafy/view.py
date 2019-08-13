def mymax(get):
    best=get[0]
    for g in get:
        if g > best:
            best = g
    return best

def which(a,b):
    if a>b:
        return a
    else:
        return b

def howview(row, buildings):
    count = 0
    for i in range(2, row - 2):
        if buildings[i] == max(buildings[i - 2:i + 3]):
            count += buildings[i] - which(mymax(buildings[i - 2:i]), mymax(buildings[i + 1:i + 3]))
    return count

for test_case in range(1,11):
    row = int(input())
    buildings = list(map(int,input().split()))

    view = howview(row,buildings)
    print("#{0} {1}".format(test_case, view))


