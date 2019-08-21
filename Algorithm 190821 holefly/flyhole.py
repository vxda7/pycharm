# 구멍난 파리채
test_case = int(input())
for case in range(1, test_case + 1):
    N, M = map(int, input().split())
    space = []
    for i in range(N):
        space.append(list(map(int, input().split())))
    best = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            catch = 0
            for k in range(M ** 2):  # 0~8
                if k//M == 0 or k//M == M-1 or k%M == 0 or k%M == M-1:
                    catch += space[i + k // M][j + k % M]
            if catch > best:
                best = catch

    print("#{} {}".format(case, best))