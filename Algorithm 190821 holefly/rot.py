test_case = int(input())
for case in range(1, test_case + 1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    for i in range(M):
        num.append(num.pop(0))
    print("#{} {}".format(case, num[0]))
