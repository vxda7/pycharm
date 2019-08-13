def flat(count, floor):
    for i in range(count):
        highest = max(floor)
        lowest = min(floor)
        floor[floor.index(highest)]= highest-1
        floor[floor.index(lowest)] = lowest + 1

    return max(floor) - min(floor)

for test_case in range(1,11):
    count = int(input())
    floor = list(map(int,input().split()))
    print("#{0} {1}".format(test_case, flat(count, floor)))