T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    howmany = int(input())
    gets = list(map(int, input().split()))
    other = reversed(gets)

    for get in range(len(gets)):
        if get == len(gets)-1:
            break
        elif gets[get] < gets[get + 1]:
            gets[get], gets[get + 1] = gets[get + 1], gets[get]
    smallanswer = gets[-1]

    for get in range(len(gets)):
        if get == len(gets)-1:
            break
        elif gets[get] > gets[get + 1]:
            gets[get], gets[get + 1] = gets[get + 1], gets[get]
    biganswer = gets[-1]
    print("#{0} {1}".format(test_case, biganswer - smallanswer))
