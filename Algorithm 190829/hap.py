# import sys
# sys.stdin = open("hap.txt","r")

test_case = int(input())
for case in range(1, test_case + 1):
    numbers = int(input())
    row = list(map(int, input().split()))

    hap = 0
    best = 0
    for i in range(numbers):
        hap += row[i]
        if hap < 0:
            hap = 0
        else:
            if best < hap:
                best = hap

    print("#{} {}".format(case, best))





# def find(row, numbers):
#     result = 0
#     for interval in range(1, numbers + 1):
#         for where in range(numbers):
#             hap = sum(row[where: where + interval])
#             if result < hap:
#                 result = hap
#     return result


# test_case = int(input())
# for case in range(1, test_case + 1):
#     numbers = int(input())
#     row = list(map(int, input().split()))
#     result = find(row, numbers)
#
#     print("#{} {}".format(case, result))