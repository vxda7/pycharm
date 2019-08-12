T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    howmany = int(input())
    gets = input()
    result={}
    for get in gets:
        if get in result:
            result[get] += 1
        else:
            result[get]=1
    best_key=-1
    best_value=-1
    for key, value in result.items():
        if value == best_value:
            if int(best_key) < int(key):
                best_key = key
        elif int(value) > int(best_value):
            best_value = value
            best_key = key
    print("#{0} {1} {2}".format(test_case, best_key, best_value))

