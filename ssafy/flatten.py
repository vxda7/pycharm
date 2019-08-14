import sys
sys.stdin = open("input.txt", "r")


def flat(count, floor):
    for i in range(count):
        highest = max(floor)
        lowest = min(floor)
        floor[floor.index(highest)] = highest-1
        floor[floor.index(lowest)] = lowest + 1
    return max(floor) - min(floor)


for test_case in range(1,11):
    count = int(input())
    floor = list(map(int,input().split()))
    print("#{0} {1}".format(test_case, flat(count, floor)))



# for test_case in range(1,11):
#     bubu = int(input())
#     floor = list(map(int,input().split()))
#     count = countflat(floor)
#     print("#{0} {1} {2}".format(test_case, count, flat(count, floor)))
