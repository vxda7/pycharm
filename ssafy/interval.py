# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     gets = list(map(int,input().split()))
#     numbers = list(map(int, input().split()))
#     big=1
#     small=10000**2
#     for i in range(gets[0]-gets[1]+1):
#         if big < sum(numbers[i:i+gets[1]]):
#             big = sum(numbers[i:i+gets[1]])
#         if small > sum(numbers[i:i+gets[1]]):
#             small = sum(numbers[i:i+gets[1]])
#
#     print("#{0} {1}".format(test_case, big-small))

# sum을 안쓴것
T = int(input())
for test_case in range(1, T + 1):
    gets = list(map(int,input().split()))
    numbers = list(map(int, input().split()))
    big=1
    small=10000**2
    for i in range(gets[0]-gets[1]+1):
        hap = 0
        for j in range(gets[1]):
            hap += numbers[i+j]
        if big < hap:
            big = hap
        if small > hap:
            small = hap

    print("#{0} {1}".format(test_case, big-small))